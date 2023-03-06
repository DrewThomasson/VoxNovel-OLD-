from bs4 import BeautifulSoup

# Open the HTML file and read its contents
with open('/content/Harry_Potter.book.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object from the HTML string
soup = BeautifulSoup(html, 'html.parser')

# Extract all the text from the HTML file
all_text = soup.get_text()

# Write the text to a text file
with open('/content/HTML_output.txt', 'w') as file:
    file.write(all_text)
