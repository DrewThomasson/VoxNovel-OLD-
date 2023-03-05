with open("/content/5new_Wanted_output.txt", "r") as input_file, open("1char_names.txt", "w") as output_file:
    for line in input_file:
        if line.startswith("["):
            output_file.write(line)