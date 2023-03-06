#this will make it so that all the names in the txt file being used to store the names are in a list
names = []

with open("/content/2char_names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
# iterate through the string list and replace "." with ". "
for i in range(len(names)):
    names[i] = names[i].replace(".", ". ")


print(names)