# resume_pdf.py
from fpdf import FPDF

def create_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, data["name"], ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 7, data["title"], ln=True)
    pdf.ln(5)

    # Contact Info
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Contact Information", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 7,
        f"Email: {data['email']}\n"
        f"Phone: {data['phone']}\n"
        f"Location: {data['location']}\n"
        f"LinkedIn: {data['linkedin']}\n"
        f"GitHub: {data['github']}"
    )
    pdf.ln(3)

    # Summary
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Professional Summary", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 7, data["summary"])
    pdf.ln(3)

    # Skills
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Skills", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 7, ", ".join(data["skills"]))
    pdf.ln(3)

    # Experience
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Experience", ln=True)

    pdf.set_font("Arial", "", 11)
    for exp in data["experience"]:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, f"{exp['role']} - {exp['company']} ({exp['start']} - {exp['end']})", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 7, exp["desc"])
        pdf.ln(2)

    # Education
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Education", ln=True)

    pdf.set_font("Arial", "", 11)
    for edu in data["education"]:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, f"{edu['degree']} - {edu['school']} ({edu['start']} - {edu['end']})", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 7, edu["desc"])
        pdf.ln(2)

    # Certifications
    if data["certifications"]:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Certifications", ln=True)

        pdf.set_font("Arial", "", 11)
        for c in data["certifications"]:
            pdf.multi_cell(0, 7, f"- {c}")

    return pdf.output(dest="S").encode("latin1")
