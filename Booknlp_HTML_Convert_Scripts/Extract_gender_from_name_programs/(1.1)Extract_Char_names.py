#this will be sued to extract the character names form the TTS_Input document
with open("Extract_gender_from_name_programs/TTS_Input.txt", "r") as input_file, open("Extract_gender_from_name_programs/1char_names.txt", "w") as output_file:
    for line in input_file:
        if line.startswith("["):
            output_file.write(line)