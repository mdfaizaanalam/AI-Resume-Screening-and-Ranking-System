import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text + "\n"
    return text.strip()

# Function to extract top keywords from job description
def extract_keywords(text, num_keywords=10):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_array = np.array(vectorizer.get_feature_names_out())
    tfidf_sorting = np.argsort(tfidf_matrix.toarray()).flatten()[::-1]
    top_keywords = feature_array[tfidf_sorting][:num_keywords]
    return ", ".join(top_keywords)

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    
    return cosine_similarities

# Streamlit App UI
st.set_page_config(page_title="AI Resume Screening", page_icon="📄", layout="wide")

# Custom Header with Links
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>📄 AI Resume Screening & Candidate Ranking System</h1>
    <p style='text-align: center;'>
        Created by <b>Md Faizaan Alam</b> |
        <a href="https://github.com/mdfaizaanalam" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white" height="25">
        </a>  
        <a href="https://www.linkedin.com/in/mdfaizaanalam/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white" height="25">
        </a> 
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# Job description input
st.markdown("## 📌 Job Description")
job_description = st.text_area("Enter the job description here", height=150)

# Show extracted keywords from JD
if job_description:
    top_keywords = extract_keywords(job_description)
    st.markdown(f"**🔍 Key Skills in Job Description:** {top_keywords}")

# File uploader
st.markdown("## 📤 Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.markdown("## 📊 Ranking Resumes")
    
    with st.spinner("Processing resumes... Please wait"):
        resumes = []
        progress_bar = st.progress(0)  # Initialize progress bar

        for i, file in enumerate(uploaded_files):
            text = extract_text_from_pdf(file)
            resumes.append(text)
            progress_bar.progress((i + 1) / len(uploaded_files))  # Update progress

        # Rank resumes
        scores = rank_resumes(job_description, resumes)

        # Create results DataFrame
        results = pd.DataFrame({
            "Resume": [file.name for file in uploaded_files],
            "Score": scores
        })

        # Sort results in descending order
        results = results.sort_values(by="Score", ascending=False).reset_index(drop=True)
        
        # Add ranking column
        results["Rank"] = np.arange(1, len(results) + 1)

        # Display ranking results
        st.markdown("### 🏆 Candidate Ranking")

        # Metrics
        col1, col2 = st.columns(2)
        col1.metric(label="📂 Total Resumes Uploaded", value=len(uploaded_files))
        col2.metric(label="📈 Average Score", value=round(results["Score"].mean(), 2))

        # Visualizing results with bar chart
        fig, ax = plt.subplots()
        ax.barh(results["Resume"], results["Score"], color="#4CAF50")
        ax.set_xlabel("Similarity Score")
        ax.set_ylabel("Resume Name")
        ax.set_title("Resume Similarity Score Chart")
        st.pyplot(fig)

        def highlight_top(val):
            color = "#4CAF50" if val == 1 else "#FFC107" if val == 2 else "#FF5722" if val == 3 else "white"
            return f"background-color: {color}; color: black;"

        st.dataframe(results.style.applymap(highlight_top, subset=["Rank"]))

        # Display top candidate resume content dynamically
        st.markdown("### 🥇 Top Candidate Resume Preview")

        # Get the top-ranked resume filename
        top_resume_name = results.iloc[0]["Resume"]

        # Find the matching uploaded file
        top_resume_file = next(file for file in uploaded_files if file.name == top_resume_name)

        # Extract text from the correct top resume file
        top_resume_text = extract_text_from_pdf(top_resume_file)

        with st.expander(f"📜 View Resume: {top_resume_file.name}"):
            st.write(top_resume_text[:1000] + "...")  # Show only first 1000 characters

        # Download button
        csv_data = results.to_csv(index=False).encode("utf-8")
        st.download_button(label="📥 Download Results", data=csv_data, file_name="resume_ranking_results.csv", mime="text/csv")    

# Footer
st.markdown(
    """
    <p style='text-align: center;'>
        💻 Built with <b>Python & Streamlit</b> </br> 🚀 Connect with me on 
        <a href="https://github.com/mdfaizaanalam" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white" height="25">
        </a>  
        <a href="https://www.linkedin.com/in/mdfaizaanalam/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white" height="25">
        </a>  
    </p>
    """,
    unsafe_allow_html=True
)
