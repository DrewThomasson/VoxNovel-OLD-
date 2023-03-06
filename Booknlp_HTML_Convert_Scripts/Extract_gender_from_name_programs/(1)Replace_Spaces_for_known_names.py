#this will make it so that all the names in the txt file being used to store the names are in a list
names = []

with open("Extract_gender_from_name_programs/2char_names.txt", "r") as file:
    for line in file:
        names.append(line.strip())

print(names)

#this will run thorugh the HTML txt file and replace any spaces in known names wiht "_"

#names = ["the bob", "bob", "Sarah", "the super Sarah"]

with open("Extract_gender_from_name_programs/HTML_output.txt", "r") as file:
    content = file.read()
    for name in names:
        content = content.replace(name, name.replace(" ", "_"))
    with open("Extract_gender_from_name_programs/1output.txt", "w") as output_file:
        output_file.write(content)