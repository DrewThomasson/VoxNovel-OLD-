#this will make it so that all the names in the txt file being used to store the names are in a list
names = []

with open("/content/2char_names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
# iterate through the string list and replace "." with ". "
for i in range(len(names)):
    names[i] = names[i].replace(".", ". ")


print(names)

#this will run thorugh the HTML txt file and replace any spaces in known names wiht "_"

#names = ["the bob", "bob", "Sarah", "the super Sarah"]

with open("/content/HTML_output.txt", "r") as file:
    content = file.read()
    for name in names:
        content = content.replace(name, name.replace(" ", "_"))
        #content = content.replace(name, name.replace(".", "._"))
    with open("/content/1output.txt", "w") as output_file:
        output_file.write(content)