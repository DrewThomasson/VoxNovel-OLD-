#this will make it so that all the names in the txt file being used to store the names are in a list
names = []

with open("Extract_gender_from_name_programs/2char_names.txt", "r") as file:
    for line in file:
        names.append(line.strip())

print(names)