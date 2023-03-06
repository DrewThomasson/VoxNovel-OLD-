# Open the text file for reading
with open("/content/2output.txt", "r") as file:
    # Read the entire contents of the file into a string variable
    text = file.read()
    # Replace all "[" and "]" characters with a new line
    text = text.replace("[", "\n").replace("]", "\n")
    # Open the text file for writing
    with open("/content/3output.txt", "w") as output_file:
        # Write the modified text to the output file
        output_file.write(text)
