
def fixSpacing(original_sentence):
    original_sentence = original_sentence.replace(" '", "'")
    original_sentence = original_sentence.replace(" ; ", ";")
    original_sentence = original_sentence.replace(" ,",",")
    original_sentence = original_sentence.replace(" ?","?")
    original_sentence = original_sentence.replace(" !","!")
    original_sentence = original_sentence.replace(" '","'")
    original_sentence = original_sentence.replace(" -","-")
    original_sentence = original_sentence.replace("- ","-")
    original_sentence = original_sentence.replace(" .",".")
    original_sentence = original_sentence.replace(' "','"')
    original_sentence = original_sentence.replace('" ','"')
    original_sentence = original_sentence.replace(". a",".a")
    original_sentence = original_sentence.replace(". b",".b")
    original_sentence = original_sentence.replace(". c",".c")
    original_sentence = original_sentence.replace(". d",".d")
    original_sentence = original_sentence.replace(". e",".e")
    original_sentence = original_sentence.replace(". f",".f")
    original_sentence = original_sentence.replace(". g",".g")
    original_sentence = original_sentence.replace(". h",".h")
    original_sentence = original_sentence.replace(". i",".i")
    original_sentence = original_sentence.replace(". j",".j")
    original_sentence = original_sentence.replace(". k",".k")
    original_sentence = original_sentence.replace(". l",".l")
    original_sentence = original_sentence.replace(". m",".m")
    original_sentence = original_sentence.replace(". n",".n")
    original_sentence = original_sentence.replace(". o",".o")
    original_sentence = original_sentence.replace(". p",".p")
    original_sentence = original_sentence.replace(". q",".q")
    original_sentence = original_sentence.replace(". r",".r")
    original_sentence = original_sentence.replace(". s",".s")
    original_sentence = original_sentence.replace(". t",".t")
    original_sentence = original_sentence.replace(". u",".u")
    original_sentence = original_sentence.replace(". v",".v")
    original_sentence = original_sentence.replace(". w",".w")
    original_sentence = original_sentence.replace(". x",".x")
    original_sentence = original_sentence.replace(". y",".y")
    original_sentence = original_sentence.replace(". z",".z")
    original_sentence = original_sentence.replace(" a'","a'")
    original_sentence = original_sentence.replace(" b'","b'")
    original_sentence = original_sentence.replace(" c'","c'")
    original_sentence = original_sentence.replace(" d'","d'")
    original_sentence = original_sentence.replace(" e'","e'")
    original_sentence = original_sentence.replace(" f'","f'")
    original_sentence = original_sentence.replace(" g'","g'")
    original_sentence = original_sentence.replace(" h'","h'")
    original_sentence = original_sentence.replace(" i'","i'")
    original_sentence = original_sentence.replace(" j'","j'")
    original_sentence = original_sentence.replace(" k'","k'")
    original_sentence = original_sentence.replace(" l'","l'")
    original_sentence = original_sentence.replace(" m'","m'")
    original_sentence = original_sentence.replace(" n'","n'")
    original_sentence = original_sentence.replace(" p'","o'")
    original_sentence = original_sentence.replace(" q'","p'")
    original_sentence = original_sentence.replace(" r'","q'")
    original_sentence = original_sentence.replace(" s'","r'")
    original_sentence = original_sentence.replace(" t'","s'")
    original_sentence = original_sentence.replace(" u'","t'")
    original_sentence = original_sentence.replace(" v'","u'")
    original_sentence = original_sentence.replace(" w'","w'")
    original_sentence = original_sentence.replace(" x'","x'")
    original_sentence = original_sentence.replace(" y'","y'")
    original_sentence = original_sentence.replace(" z'","z'")
    return original_sentence



original_sentence = '" Well , I just thought ... maybe ... it was something to do with ... you know ... her crowd . "'

original_sentence = fixSpacing(original_sentence)
print(original_sentence)













with open('output.txt', 'r') as f:
    data = f.read()

output = ''
in_quote = False
in_bracket = False
quote_number = 1
for c in data:
    if c == '"' and not in_bracket:
        output += c
        output += '\n' # add new line before beginning quote
        output += c
        in_quote = not in_quote
    elif c == '[' and not in_bracket:
        output += '\n' # add new line before opening bracket
        output += c
        in_bracket = True
    elif c == ']' and in_bracket:
        output += c
        output += '\n' # add new line after closing bracket
        in_bracket = False
    else:
        output += c

with open('Wanted_output.txt', 'w') as f:
    f.write(output)




# open input and output files
with open('Wanted_output.txt', 'r') as f_in, open('new_Wanted_output.txt', 'w') as f_out:
    # read each line from input file
    for line in f_in:
        # apply fixSpacing function to line
        fixed_line = fixSpacing(line)
        # write modified line to output file
        f_out.write(fixed_line + '\n')
#this will remove all empty lines from the txt document
#the order its in is (input.txt)--->(output.txt)
with open('new_Wanted_output.txt', 'r') as infile, open('new_new_Wanted_output.txt', 'w') as outfile:
    for line in infile:
        if line.strip():
            outfile.write(line)
#this will remove all lines that are only holding a wuoteation mark iE: '"'
with open('new_new_Wanted_output.txt', 'r') as infile, open('3new_Wanted_output.txt', 'w') as outfile:
    for line in infile:
        if line.strip() != '"':
            outfile.write(line)

with open('3new_Wanted_output.txt', 'r') as infile, open('4new_Wanted_output.txt', 'w') as outfile:
    for line in infile:
        if line.strip().endswith('"') and not line.strip().startswith('"'):
            outfile.write(line.strip()[:-1] + '\n')
        else:
            outfile.write(line)






#dreww if your coming back to this then you need to just remove the left over bits from this output txt file
#being the lines that just only have a '"'
#being the lines that just only have a "[" or a "]"
# being any case where its "] and any letter ebing captial or lowercase letter"
#being  any case where the line starts end with a " but doesnt start with a "

#remeber when puttuing the output into columns you want to do it like this
#run through it line by line adding each line to row 1
#if the line begins with a "[" then put the line into the row 2