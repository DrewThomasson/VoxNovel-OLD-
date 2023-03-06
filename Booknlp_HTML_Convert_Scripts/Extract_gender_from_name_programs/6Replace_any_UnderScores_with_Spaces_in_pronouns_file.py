#this will ru  through the pronoun file and replace any "_" with  " "
# Open the text file for reading
#it also removes any numbers or "-" from the names in the pronouns file

# Open the text file for reading
with open("/content/4output.txt", "r") as file:
    # Read the entire contents of the file into a string variable
    text = file.read()
    # Replace all underscores with spaces
    text = text.replace("_", " ")
    # Remove all numbers and hyphens
    text = ''.join([i for i in text if not i.isdigit() and i != '-'])
    # Open the text file for writing
    with open("/content/5output.txt", "w") as output_file:
        # Write the modified text to the output file
        output_file.write(text)

#itll also run thorugh the char_names file and do the same so then your left with a char fil that doesnt contain any numbers or special characters
# Open the text file for reading
with open("/content/3char_names.txt", "r") as file:
    # Read the entire contents of the file into a string variable
    text = file.read()
    # Replace all underscores with spaces
    text = text.replace("_", " ")
    # Remove all numbers and hyphens
    text = ''.join([i for i in text if not i.isdigit() and i != '-'])
    # Open the text file for writing
    with open("/content/4char_names.txt", "w") as output_file:
        # Write the modified text to the output file
        output_file.write(text)

def find_line_above(name, file_path):
    # Open the text file for reading
    with open(file_path, "r") as file:
        # Read the entire contents of the file into a list of lines
        lines = file.readlines()
        # Iterate over the lines, searching for the name
        for i in range(1, len(lines)):
            if name in lines[i]:
                # If the name is found, return the line above it
                return lines[i-1]
    # If the name is not found, return None
    return None
print()