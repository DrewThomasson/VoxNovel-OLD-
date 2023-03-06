def find_line_and_char_gender(name, file_path):
    # Open the text file for reading
    with open(file_path, "r") as file:
        # Read the entire contents of the file into a list of lines
        lines = file.readlines()
        # Iterate over the lines, searching for the name
        for i in range(1, len(lines)):
            if name in lines[i]:
                # If the name is found, get the line above it
                line_above = lines[i-1]
                #cleaning the line above it
                line_above = line_above.strip()
                print(line_above)
                # Check if the line above contains "he" or "him"
                if line_above == "he":
                    return "male"
                if line_above == "him":
                    return "male"
                if line_above == "her":
                    return "female"
                if line_above == "she":
                    return "female"
                else:
                    return "unknown"
    # If the name is not found, return None
    return "unknown"

print(find_line_and_char_gender("paul" ,"/content/5output.txt" ))