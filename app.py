import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

st.set_page_config(page_title="Resume Builder", layout="centered")

st.title("📄 Resume Builder")

with st.form("resume_form"):
    st.header("Personal Information")
    name = st.text_input("Full Name", key="name")
    email = st.text_input("Email", key="email")
    phone = st.text_input("Phone", key="phone")
    summary = st.text_area("Professional Summary", key="summary")

    st.header("Skills")
    skills = st.text_area("List your skills (comma separated)", key="skills")

    st.header("Education")
    edu_degree = st.text_input("Degree", key="edu_degree")
    edu_school = st.text_input("School / College", key="edu_school")
    edu_year = st.text_input("Year of Completion", key="edu_year")

    st.header("Experience")
    exp_title = st.text_input("Job Title", key="exp_title")
    exp_company = st.text_input("Company", key="exp_company")
    exp_years = st.text_input("Years (e.g., 2020–2023)", key="exp_years")
    exp_desc = st.text_area("Work Description", key="exp_desc")

    submitted = st.form_submit_button("Generate Resume PDF")

def create_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    text = p.beginText(40, 800)
    text.setFont("Helvetica-Bold", 20)
    text.textLine(name)

    text.setFont("Helvetica", 12)
    text.textLine(email)
    text.textLine(phone)
    text.textLine(" ")

    text.setFont("Helvetica-Bold", 16)
    text.textLine("Professional Summary")
    text.setFont("Helvetica", 12)
    for line in summary.split("\n"):
        text.textLine(line)
    text.textLine(" ")

    text.setFont("Helvetica-Bold", 16)
    text.textLine("Skills")
    text.setFont("Helvetica", 12)
    for skill in skills.split(","):
        text.textLine(f"• {skill.strip()}")
    text.textLine(" ")

    text.setFont("Helvetica-Bold", 16)
    text.textLine("Education")
    text.setFont("Helvetica", 12)
    text.textLine(f"{edu_degree} - {edu_school} ({edu_year})")
    text.textLine(" ")

    text.setFont("Helvetica-Bold", 16)
    text.textLine("Experience")
    text.setFont("Helvetica", 12)
    text.textLine(f"{exp_title} - {exp_company} ({exp_years})")
    for line in exp_desc.split("\n"):
        text.textLine(f"- {line}")

    p.drawText(text)
    p.save()

    buffer.seek(0)
    return buffer


# Generate PDF
if submitted:
    pdf = create_pdf()
    st.success("🎉 PDF Generated Successfully!")

    st.download_button(
        label="⬇ Download Resume",
        data=pdf,
        file_name="resume.pdf",
        mime="application/pdf"
    )
