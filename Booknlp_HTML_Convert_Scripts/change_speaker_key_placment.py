with open('4new_Wanted_output.txt', 'r') as infile:
    lines = infile.readlines()

for i in range(1, len(lines)):
    if lines[i].startswith('['):
        lines[i], lines[i-1] = lines[i-1], lines[i]

with open('TTS_Input.txt', 'w') as outfile:
    outfile.writelines(lines)
