pronouns = {"[he]","[He]","[HE]","[him]","[Him]","[HIM]","[His]", "[his]","[HIS]", "[her]","[Her]","[HER]", "[hers]","[Hers]","[HERS]", "[she]","[She]","[SHE]"}

#pronouns = ["[he]", "[she]", "[him]", "[her]"]


#this is to try t extract the names from it
# Open the text file for reading
with open("Extract_gender_from_name_programs/1output.txt", "r") as file:
    # Loop through each line in the file
    for line in file:
        # Split the line into individual words
        words = line.split()
        # Loop through each word in the line
        for word in words:
            # Check if the word contains any of the pronouns
            for pronoun in pronouns:
                if pronoun in word:
                    # Print the word if it contains a pronoun
                    print(word)

pronouns = ["[he]", "[she]", "[him]", "[her]"]

# Open the text file for reading
with open("Extract_gender_from_name_programs/1output.txt", "r") as file:
    # Open a new text file for writing
    with open("Extract_gender_from_name_programs/2output.txt", "w") as output_file:
        # Loop through each line in the file
        for line in file:
            # Split the line into individual words
            words = line.split()
            # Loop through each word in the line
            for word in words:
                # Check if the word contains any of the pronouns
                for pronoun in pronouns:
                    if pronoun in word:
                        # Write the word to the output file if it contains a pronoun
                        output_file.write(word + "\n")

#this line will also remove any duplicate liens from it so you dont have multiple lines from each character

# Open the text file for reading
with open("Extract_gender_from_name_programs/2output.txt", "r") as file:
    # Read the entire contents of the file into a list of lines
    lines = file.readlines()
    # Remove duplicate lines from the list
    lines = list(set(lines))
    # Open the text file for writing
    with open("Extract_gender_from_name_programs/2output.txt", "w") as output_file:
        # Write the modified lines to the output file
        output_file.writelines(lines)
