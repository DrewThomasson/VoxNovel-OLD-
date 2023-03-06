# Open the text file for reading
with open("Extract_gender_from_name_programs/3output.txt", "r") as file:
    # Read the entire contents of the file into a list of lines
    lines = file.readlines()
    # Remove all empty lines from the list
    lines = [line for line in lines if line.strip()]
    # Open the text file for writing
    with open("Extract_gender_from_name_programs/4output.txt", "w") as output_file:
        # Write the modified lines to the output file
        output_file.writelines(lines)
