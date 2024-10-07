import docx

# Step 1: Load Offer Letter DOCX Template
def load_template(docx_template_path):
    return docx.Document(docx_template_path)

# Step 2: Replace Placeholders in Paragraphs and Runs
def replace_placeholders(doc, hr_data):
    for para in doc.paragraphs:
        for run in para.runs:
            # Replace placeholders in each run
            for key, value in hr_data.items():
                if key in run.text:
                    run.text = run.text.replace(key, value)
    
    return doc

# Step 3: Save the customized DOCX
def save_customized_docx(doc, output_path):
    doc.save(output_path)
