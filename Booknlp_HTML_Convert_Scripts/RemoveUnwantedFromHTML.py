from bs4 import BeautifulSoup

# Read the HTML file
with open("/content/VoxNovel/Booknlp_HTML_Convert_Scripts/Expected_booknlp_output_Files/alice_in_wonderland/alice_in_wonderland.book.html", "r") as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all elements with the color #FF00FF and remove them
for element in soup.find_all(color = '#FF00FF'):
    print(element)
    element.decompose()

# Find all font elements with color attribute set to "#D0D0D0"
elements_to_remove_text_from = soup.find_all('font', {'color': '#D0D0D0'})

# Remove the text from each element
for element in elements_to_remove_text_from:
    element.string = ""


# Save the modified HTML to a new file
with open("output.html", "w") as f:
    f.write(str(soup))
