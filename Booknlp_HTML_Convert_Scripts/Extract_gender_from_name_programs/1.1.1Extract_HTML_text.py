from bs4 import BeautifulSoup

# Open the HTML file and read its contents
with open('Extract_gender_from_name_programs/output.book.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object from the HTML string
soup = BeautifulSoup(html, 'html.parser')

# Extract all the text from the HTML file
all_text = soup.get_text()

# Write the text to a text file
with open('Extract_gender_from_name_programs/HTML_outputPOOP.txt', 'w') as file:
    file.write(all_text)
