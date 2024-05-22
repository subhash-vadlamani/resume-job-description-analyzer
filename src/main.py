import tkinter as tk
from tkinter import filedialog
import PyPDF2
import nltk
import spacy
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_md")


# Define initial tech-related terms
initial_tech_terms = [
    "software engineering", "backend development", "database engineering",
    "web development", "devops", "Python", "Django", "MySQL", "PostgreSQL", "Amazon Web Services", "AWS", "React",
    "communication"
]

# Function to find related terms dynamically


def find_related_terms(terms, top_n=15):
    related_terms = set()
    for term in terms:
        main_doc = nlp(term)
        ms = nlp.vocab.vectors.most_similar(
            main_doc.vector.reshape(1, main_doc.vector.shape[0]), n=top_n)
        for word_id in ms[0][0]:
            related_terms.add(nlp.vocab.strings[word_id])
    related_terms.update(terms)
    return related_terms


# Get a set of tech-related terms dynamically
dynamic_tech_terms = find_related_terms(initial_tech_terms)

# Function to check if a word is tech-related


def is_tech_related(word, threshold=0.5):
    word = nlp(word)[0]
    return any(word.similarity(nlp(tech_term)) > threshold for tech_term in dynamic_tech_terms)


class ResumeAnalyzerApp:
    def __init__(self, root):
        self.root = root
        root.title("Resume and Job Description Analyzer")

        self.resume_path = None
        self.job_description_path = None
        self.resume_keywords = set()
        self.job_description_keywords = set()

        self.upload_resume_button = tk.Button(
            root, text="Upload Resume", command=self.upload_resume)
        self.upload_resume_button.pack()

        self.upload_job_description_button = tk.Button(
            root, text="Upload Job Description", command=self.upload_job_description)
        self.upload_job_description_button.pack()

        tk.Button(root, text="Analyze", command=self.analyze_keywords).pack()
        tk.Button(root, text="Calculate Match Score",
                  command=self.calculate_score).pack()

        self.text_area = tk.Text(root, height=15, width=75)
        self.text_area.pack()

    def upload_resume(self):
        self.resume_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")])
        if self.resume_path:
            self.upload_resume_button.config(
                text="Resume Uploaded", state=tk.DISABLED)

    def upload_job_description(self):
        self.job_description_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")])
        if self.job_description_path:
            self.upload_job_description_button.config(
                text="Job Description Uploaded", state=tk.DISABLED)

    def extract_keywords(self, file_path, threshold=0.5):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() if page.extract_text() else ''
        tokens = word_tokenize(text)
        filtered_keywords = {word.lower() for word in tokens if word.isalpha(
        ) and word.lower() not in stopwords.words('english') and len(word) > 2 and word.lower() in words.words()}
        tech_keywords = {
            word for word in filtered_keywords if is_tech_related(word, threshold=threshold)}
        return tech_keywords

    def analyze_keywords(self):
        if not self.resume_path or not self.job_description_path:
            self.text_area.insert(tk.END, "Please upload both files.\n")
            return
        self.resume_keywords = self.extract_keywords(self.resume_path)
        self.job_description_keywords = self.extract_keywords(
            self.job_description_path, threshold=0.5)
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, "Resume Keywords:\n" +
                              ", ".join(self.resume_keywords) + "\n")
        self.text_area.insert(tk.END, "Job Description Keywords:\n" +
                              ", ".join(self.job_description_keywords) + "\n")

    # def calculate_score(self):
    #     self.text_area.delete('1.0', tk.END)
    #     if not self.resume_keywords or not self.job_description_keywords:
    #         self.text_area.insert(tk.END, "Please analyze the files first.\n")
    #         return
    #     intersection = self.resume_keywords.intersection(
    #         self.job_description_keywords)
    #     if len(self.job_description_keywords) == 0:
    #         score = 0
    #     else:
    #         score = len(intersection) / \
    #             len(self.job_description_keywords) * 100

    #     self.text_area.insert(tk.END, f"\nMatch Score: {score:.2f}%\n")

    def calculate_score(self):
        self.text_area.delete('1.0', tk.END)
        if not self.resume_keywords or not self.job_description_keywords:
            self.text_area.insert(tk.END, "Please analyze the files first.\n")
            return

        total_similarity = 0.0
        for jd_keyword in self.job_description_keywords:
            jd_doc = nlp(jd_keyword)
            max_similarity = 0.0
            for resume_keyword in self.resume_keywords:
                resume_doc = nlp(resume_keyword)
                similarity = jd_doc.similarity(resume_doc)
                if similarity > max_similarity:
                    max_similarity = similarity
            total_similarity += max_similarity

        if len(self.job_description_keywords) == 0:
            score = 0
        else:
            score = (total_similarity /
                     len(self.job_description_keywords)) * 100

        self.text_area.insert(tk.END, f"\nMatch Score: {score:.2f}%\n")


# Set up the main application window
root = tk.Tk()
app = ResumeAnalyzerApp(root)
root.mainloop()
