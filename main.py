import streamlit as st
from app import load_template, replace_placeholders, save_customized_docx

# Load the offer letter template (Offer_Letter.docx)
template_path = "Offer_Letter.docx"

st.title("Offer Letter Generator")

# Input fields for HR data
employee_name = st.text_input("Employee Name", value="Ashutosh Barik")
job_title = st.text_input("Job Title", value="Backend Developer")
office_address = st.text_area("Office Address", value="Kanakia Wall Street Chakala, Andheri(E), Mumbai – 400 093")
work_hours = st.text_input("Work Hours", value="40")
salary = st.text_input("Salary", value="40000")
vacation_leave = st.text_input("Vacation Leave", value="21")
sick_leave = st.text_input("Sick Leave", value="10")
offer_expiration = st.text_input("Offer Expiration", value="5 days after release")
contact_number = st.text_input("Contact Number", value="9856747372")
contact_email = st.text_input("Contact Email", value="company@gmail.com")
acceptance_date = st.date_input("Acceptance Date")

# Generate the customized offer letter
if st.button("Generate Offer Letter"):
    hr_data = {
        "{employee_name}": employee_name,
        "{job_title}": job_title,
        "{office_address}": office_address,
        "{work_hours}": work_hours,
        "{salary}": salary,
        "{vacation_leave}": vacation_leave,
        "{sick_leave}": sick_leave,
        "{offer_expiration}": offer_expiration,
        "{contact_number}": contact_number,
        "{contact_email}": contact_email,
        "{acceptance_date}": str(acceptance_date)
    }
    
    # Load the DOCX template
    doc = load_template(template_path)
    
    # Replace placeholders with HR data
    customized_doc = replace_placeholders(doc, hr_data)
    
    # Save the generated offer letter
    output_path = "Customized_Offer_Letter.docx"
    save_customized_docx(customized_doc, output_path)
    
    st.success("Offer letter generated successfully! Download it below.")
    st.download_button("Download Offer Letter", data=open(output_path, "rb"), file_name="Offer_Letter.docx")
