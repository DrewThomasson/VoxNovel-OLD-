#replace spaces in names with input "_"
with open("/content/2char_names.txt", "r") as input_file:
    with open("/content/3char_names.txt", "w") as output_file:
        for line in input_file:
            modified_line = line.replace(" ", "_")
            output_file.write(modified_line)
            print(modified_line)
