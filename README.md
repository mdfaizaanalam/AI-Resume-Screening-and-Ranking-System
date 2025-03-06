# AI Resume Screening & Candidate Ranking System

## 📌 Problem Statement
In the modern recruitment process, organizations receive an overwhelming number of resumes for each job opening. Screening these resumes to identify the most suitable candidates is a time-consuming and labor-intensive task. Automating this process using machine learning and natural language processing (NLP) techniques can significantly improve the efficiency and effectiveness of recruitment.

## 🚀 Proposed Solution
To address the challenges of automating the resume screening process, we propose a solution that leverages **machine learning** and **natural language processing (NLP)** techniques.

The solution involves developing a **web-based application** that enables recruiters to:
- **Match job descriptions** with candidate resumes using text-based similarity analysis.
- **Rank candidates** based on relevance using **cosine similarity**.
- **Visualize results** in an interactive and user-friendly interface.

## 🏗️ Technologies Used
### 🔹 Frontend:
- **Streamlit**: A Python framework for building interactive web applications.

### 🔹 Backend:
- **Python**: The core programming language for implementation.
- **PyPDF2**: Extracts text from uploaded resumes (PDF format).
- **Scikit-learn (sklearn)**: Used for machine learning tasks, including text feature extraction and similarity scoring.
- **NLTK & SpaCy**: Used for NLP tasks such as tokenization and text processing.
- **Matplotlib**: For visualizing resume similarity scores.
- **Pandas & NumPy**: Handles data processing and manipulation.

### 🔹 Deployment:
- **Streamlit Cloud**: Used for easy deployment and hosting.

## 📦 Installation Guide
Follow these steps to set up and run the AI Resume Screening System on your local machine:

### **1️⃣ Install Python (if not installed)**
Make sure you have **Python 3.8 or later** installed. Download it from [Python.org](https://www.python.org/downloads/).

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/mdfaizaanalam/ai-resume-screening.git
cd ai-resume-screening
```

### **3️⃣ Install Required Dependencies**
Run the following command to install all necessary libraries:
```bash
pip install streamlit pypdf2 scikit-learn nltk spacy pandas numpy matplotlib
```

### **4️⃣ Download SpaCy NLP Model (Optional but Recommended)**
```bash
python -m spacy download en_core_web_sm
```

### **5️⃣ Run the Application**
```bash
streamlit run app.py
```
This will launch the **AI Resume Screening System** in your web browser.

## 🛠️ Features
✅ **Upload multiple resumes** (PDF format).  
✅ **Extract text automatically** from resumes.  
✅ **Enter a job description** and extract key skills.  
✅ **Rank resumes based on relevance** to the job description.  
✅ **Display rankings in a table** with color-coded highlights.  
✅ **Generate a similarity score visualization** (bar chart).  
✅ **Preview the top-ranked resume** dynamically.  
✅ **Download the results as a CSV file**.

## 📊 How It Works
1. **Upload PDF resumes** to the system.
2. **Enter a job description** in the input field.
3. The system extracts text from resumes and computes **cosine similarity** scores.
4. **Resumes are ranked** based on similarity to the job description.
5. The top-ranked resume is displayed for quick access.
6. Results are visualized using a **bar chart** and a ranked table.

## 🚀 Deployment Guide (Streamlit Cloud)
1. **Create a Streamlit account** at [Streamlit Cloud](https://streamlit.io/).
2. **Push your project** to GitHub.
3. **Go to Streamlit Cloud**, select **Deploy an App**, and connect your GitHub repository.
4. **Enter app.py as the entry point** and deploy.

## 📄 Example Job Description
```
Looking for a Full-Stack Developer skilled in Python, React.js, and MongoDB.
Experience with APIs, cloud deployment, and security best practices is required.
```

## 🎯 Future Enhancements
- Add **resume parsing** for structured data extraction.
- Improve **accuracy** using **BERT embeddings**.
- Expand **job role matching** with **deep learning models**.
- Enhance **dashboard UI** for a more interactive experience.

## 👨‍💻 Author
**Md Faizaan Alam**  
💼 [GitHub](https://github.com/mdfaizaanalam)  
💼 [LinkedIn](https://www.linkedin.com/in/mdfaizaanalam/)

---
🎉 **Now, recruiters can efficiently shortlist the best candidates with AI-powered screening!** 🚀

