# Resume and Job Description Analyzer

## Introduction

The Resume and Job Description Analyzer is a Python-based desktop application designed to help users analyze the relevance of resumes against job descriptions. Utilizing Natural Language Processing (NLP) techniques, the application extracts keywords and computes a semantic similarity score to determine how well a resume matches a job description.

### Features

- **Upload and Analyze Resumes and Job Descriptions**: Allows users to upload PDF files of resumes and job descriptions.
- **Keyword Extraction**: Extracts technical and relevant keywords from both documents.
- **Semantic Similarity Scoring**: Calculates a score based on the semantic similarities of the extracted keywords.
- **Dynamic Term Matching**: Employs NLP to dynamically find and match related technical terms.

### Limitations

- **PDF Format Dependence**: The accuracy of text extraction can vary significantly with the formatting of the PDF.
- **Scope of Terminology**: The initial set of technical terms and the dynamically identified related terms may not encompass all possible technical skills and terminologies, particularly those that are emerging or niche.

## Setup and Installation

### Prerequisites

- Ensure you have Python 3.6 or later installed on your system.

### Step-by-Step Setup

1. **Clone the Repository**
   Clone the project repository to your local machine using the following command:

   ```bash
   git clone https://github.com/subhash-vadlamani/resume-job-description-analyzer.git
   cd resume-job-description-analyzer

   ```

2. **Setup a Virtual Environment**

   On Windows:
   python -m venv venv
   venv\Scripts\activate
   On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

3. **Install Required Packages**
   pip install -r requirements.txt
   python -m spacy download en_core_web_md

4. **Run the Application**
   python main.py

### Usage

1. **Upload Files**
   Use the buttons in the application to upload your resume and job description PDFs.

2. **Setup a Virtual Environment**
   Click the 'Analyze' button to extract and display keywords from both documents.

3. **Install Required Packages**
   Click the 'Calculate Match Score' button to compute and display the similarity score, indicating how well the resume matches the job description.

### Dependencies

- **tkinter**: For creating the GUI. This package is included with standard Python installations.
- **PyPDF2**: For extracting text from PDF files. Install using `pip install PyPDF2`.
- **nltk**: For natural language processing and text tokenization. Install using `pip install nltk`.
- **spacy**: For advanced NLP tasks, including semantic similarity calculations. Install using `pip install spacy`.
- **en_core_web_md**: SpaCy's medium-sized English language model with word vectors. Install using `python -m spacy download en_core_web_md`.

### Contributing

- Contributions to the project are welcome! Please fork the repository and submit a pull request with your suggested changes.

### License

- This project is released under the MIT License.

### Contact Information

- For questions or feedback, please contact me at vadlamanisubhash1998@gmail.com, or open an issue in the GitHub repository.
