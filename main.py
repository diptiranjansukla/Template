import streamlit as st
from app import load_template, replace_placeholders, add_benefits_section, save_customized_docx

# Load the offer letter template (Offer_Letter_Format.docx)
template_path = "offer-letter-format.docx"

st.title("Offer Letter Generator")

# Input fields for HR data
company_name = st.text_input("Company Name", value="ACME Corporation")
address_1 = st.text_input("Address Line 1", value="3147 Patterson Street")
address_2 = st.text_input("Address Line 2", value="")
city = st.text_input("City", value="Houston")
state = st.text_input("State", value="TX")
pin_code = st.text_input("PIN Code", value="77002")
name = st.text_input("Employee Name", value="John Doe")
job_title = st.text_input("Job Title", value="Software Developer")
salary = st.text_input("Salary", value="50000")
annual_ctc = st.text_input("Annual CTC", value="600000")
working_hour = st.text_input("Working Hours", value="9 AM to 5 PM")
starting_weekend_day = st.text_input("Starting Weekend Day", value="Monday")
ending_weekend_day = st.text_input("Ending Weekend Day", value="Friday")
desired_starting_date = st.date_input("Desired Starting Date")
reporting_person = st.text_input("Reporting Person", value="HR Manager")
last_date_of_offer_acceptance = st.date_input("Last Date of Offer Acceptance")
hr_name = st.text_input("HR Name", value="Alice Johnson")

# Optional Benefits Section
benefit_a = st.text_input("Benefit A", value="Health Insurance")
benefit_b = st.text_input("Benefit B", value="")
benefit_c = st.text_input("Benefit C", value="Extra bonus based on performance")

# Generate the customized offer letter
if st.button("Generate Offer Letter"):
    hr_data = {
        "{company_name}": company_name,
        "{address_1}": address_1,
        "{address_2}": address_2,
        "{city}": city,
        "{state}": state,
        "{pin_code}": pin_code,
        "{name}": name,
        "{job_title}": job_title,
        "{salary}": salary,
        "{annual_ctc}": annual_ctc,
        "{working_hour}": working_hour,
        "{starting_weekend_day}": starting_weekend_day,
        "{ending_weekend_day}": ending_weekend_day,
        "{desired_starting_date}": str(desired_starting_date),
        "{reporting_person}": reporting_person,
        "{last_date_of_offer_acceptance}": str(last_date_of_offer_acceptance),
        "{hr_name}": hr_name
    }
    
    # Load the DOCX template
    doc = load_template(template_path)
    
    # Replace placeholders with HR data
    doc = replace_placeholders(doc, hr_data)
    
    # Add benefits section
    doc = add_benefits_section(doc, benefit_a, benefit_b, benefit_c)
    
    # Save the generated offer letter
    output_path = "Customized_Offer_Letter.docx"
    save_customized_docx(doc, output_path)
    
    st.success("Offer letter generated successfully! Download it below.")
    st.download_button("Download Offer Letter", data=open(output_path, "rb"), file_name="Offer_Letter.docx")
