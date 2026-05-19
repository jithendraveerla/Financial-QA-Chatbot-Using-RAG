import fitz

doc = fitz.open("Sample Financial Statement.pdf")
text = ""
for page in doc:
    text += page.get_text()

print(text)