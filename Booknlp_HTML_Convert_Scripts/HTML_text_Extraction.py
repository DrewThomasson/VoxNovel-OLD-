from bs4 import BeautifulSoup

# Load the HTML file
with open('output.html', 'r') as file:
    html = file.read()

# Parse the HTML file with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract all the text from the HTML file
text = soup.get_text()

# Save the text to a file
with open('output.txt', 'w') as file:
    file.write(text)
