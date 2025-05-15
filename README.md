# AI Resume Screening & Candidate Ranking System
### Internship Project | TechSaksham (Microsoft + SAP) | AICTE (Feb 2025)

## 🚀 Introduction

In the modern recruitment process, organizations receive an overwhelming number of resumes for each job opening. Manually screening these resumes to identify the most suitable candidates is time-consuming and labor-intensive.

This project leverages Machine Learning (ML) and Natural Language Processing (NLP) to automate the resume screening and ranking process. The system extracts important keywords, computes similarity scores, and ranks candidates based on their relevance to the job description.


## 📌 Problem Statement
Recruiters face challenges in manually screening hundreds of resumes, leading to:

- ⏳ Time-consuming hiring process
- 📉 Human errors and biases in shortlisting
- 🛑 Overlooking potential candidates due to inefficiency

## 🚀 Proposed Solution
We propose an AI-powered Resume Screening & Ranking System that automates resume filtering using:

- 🔎 Job Description Matching: Extracts important keywords and skills from the job description.
- 📊 Candidate Ranking: Computes similarity scores between resumes and job descriptions using NLP.
- ⚡ Streamlined Recruitment: Provides recruiters with an intuitive web interface for automated screening.

Using TF-IDF Vectorization and Cosine Similarity, this system accurately matches resumes to job descriptions.

I've formatted the tables with a **short description** for each technology while keeping frontend and backend separate. Here’s your refined section:  

---

## 🛠️ Technologies & Frameworks Used  

### 🌐 Frontend Technologies  

| Technology  | Description | Purpose |  
|------------|------------|---------|  
| **Streamlit**  | Open-source Python framework | Builds an interactive web UI |  
| **Matplotlib** | Visualization library | Displays graphs and similarity scores |  

### 🏗️ Backend Technologies  

| Technology    | Description | Purpose |  
|--------------|------------|---------|  
| **Python**   | High-level programming language | Core development language |  
| **PyPDF2**   | PDF parsing library | Extracts text from resumes (PDF) |  
| **Scikit-learn** | Machine learning library | TF-IDF vectorization & similarity calculations |  
| **NLTK & SpaCy** | NLP libraries | Tokenization, text processing & entity recognition |  
| **NumPy**    | Numerical computing library | Matrix operations & mathematical computations |  
| **Pandas**   | Data manipulation library | Handles structured data for resume processing |  

---

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


### **3️⃣ Install Required Packages & Dependencies**

```sh
$ pip install streamlit
$ pip install PyPDF2
$ pip install scikit-learn
$ pip install numpy
$ pip install pandas
$ pip install matplotlib
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
1. **Create a Streamlit account** at [Streamlit Cloud](https://ai-resumeranker.streamlit.app/).
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
---

🤝 Contributing

Contributions are welcome! Feel free to submit Pull Requests for improvements.

1️⃣ Fork the repository
2️⃣ Create a new branch (feature-xyz)
3️⃣ Commit changes and push (git push origin feature-xyz)
4️⃣ Create a Pull Request

## 👨‍💻 Author
**Md Faizaan Alam**  
💼 [GitHub](https://github.com/mdfaizaanalam)  
💼 [LinkedIn](https://www.linkedin.com/in/mdfaizaanalam/)

---

📜 License

This project is licensed under the GNU General Public License v3.0 – feel free to modify and distribute under the terms of this license. 🚀
---

🎉 **Now, recruiters can efficiently shortlist the best candidates with AI-powered screening!** 🚀

