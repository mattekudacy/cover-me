import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader
from streamlit_pdf_viewer import pdf_viewer

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=st.secrets["GITHUB_TOKEN"]
)

def get_response(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
        temperature=1,
        max_tokens=4096,
        top_p=1
    )
    return response.choices[0].message.content


st.title("CoverMe📃")
st.write("CoverMe is a tool that helps you create a cover letter for your resume. Just upload your resume and we'll take care of the rest!")

with st.sidebar:
    resume = st.file_uploader("Upload your resume:", type=["pdf"])
    role = st.text_input("What role are you applying for:")
    company = st.text_input("Enter the name of the company you are applying to:")
    jd = st.text_area("Paste the job description here:")
    confirm = st.button("Generate Cover Letter")

if resume:
    binary_data = resume.getvalue()
    pdf_viewer(input=binary_data, width=700)

    detect = ""
    reader = PdfReader(resume)
    for page in reader.pages:
        detect = detect + " ".join(page.extract_text().splitlines())

    prompt = "You are a career coach and you will help users in writing their custom cover letters. The user has uploaded their resume and has selected the field of work they are applying for. The user has also entered the name of the company they are applying to and has pasted the job description. Write a cover letter for the user. \
        \n\nRole: " + role + "\nCompany: " + company + "\nJob Description: " + jd + "\n\nResume: " + detect

    if confirm:
        response = get_response(prompt)
        st.write(response)
else:
    st.write("Please upload your resume and fill in the required fields to generate a cover letter.")