#this will be used to make it so that theres no repeating names in the output file
#I also removes any "[" or "]" from the input file being the 1char file
with open("Extract_gender_from_name_programs/1char_names.txt", "r") as input_file, open("Extract_gender_from_name_programs/2char_names.txt", "w") as output_file:
    lines_seen = set()
    for line in input_file:
        # Remove "[" and "]" symbols from line
        line = line.replace("[", "").replace("]", "").replace("","")
        # Remove numbers from line
        #line = ''.join([i for i in line if not i.isdigit()])
        # Remove leading and trailing whitespace
        line = line.strip()
        # Check if line is a duplicate
        if line not in lines_seen:
            # If line is not a duplicate, add it to the set of seen lines and write it to output file
            lines_seen.add(line)
            output_file.write(line + "\n")
