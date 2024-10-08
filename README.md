# CoverMe📃
CoverMe is a tool that helps users create customized cover letters based on their resume, the role they are applying for, the company they want to work for, and the job description. Using OpenAI's GPT-4 technology, this app generates personalized cover letters to enhance job applications with ease.

## Features
- Upload your resume (PDF format only)
- Input job role, company name, and job description
- Automatically generates a tailored cover letter based on the provided details
- Preview uploaded resume within the app

## Tech Stack
- Streamlit: For creating the interactive web interface.
- PyPDF2: To extract text from uploaded PDF resumes.
- OpenAI API: GPT-4 is used to generate custom cover letters.
- streamlit-pdf-viewer: For displaying the uploaded PDF resume in the browser.

## Installation
1. Clone this repository:
```bash
git clone https://github.com/your-repo/coverme.git
cd coverme
```
2. Install the required packages:
```bash
pip install requirements.txt
```
3.Set up your Streamlit secrets with your OpenAI API key. Create a <code>secrets.toml</code> file in the <code>.streamlit</code> folder and add your credentials:
```toml
[secrets]
GITHUB_TOKEN = "your_token"
```
4. Run the streamlit app:
```bash
streamli run main.py
```

## Usage
1. Open the Streamlit app in your browser.
2. In the sidebar, upload your resume (PDF format).
3. Enter the role you're applying for, the company name, and the job description.
4. Click **Generate Cover Letter** to receive your personalized cover letter.
5. View the result within the app.

## Example
1. **Resume Upload**: You can upload your resume in PDF format using the file uploader.
2. **Input Fields**: You can enter the role, company name, and job description.
3. **Cover Letter Generation**: Once you click on "Generate Cover Letter", the tool will create a custom letter based on your input.

## Upcoming Improvements
- Edit your generated response.
- Option to generate into PDF file.
