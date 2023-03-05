from booknlp.booknlp import BookNLP
import pandas as pd
from pprint import pprint
import json
from booknlp.booknlp import BookNLP

model_params={
		"pipeline":"entity,quote,supersense,event,coref", 
		"model":"big"
	}
	
booknlp=BookNLP("en", model_params)

# Input file to process
input_file="input_dir/HarryPotterChapter1.txt"

# Output directory to store resulting files in
output_directory="output_dir/bartleby/"

# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id="bartleby"

booknlp.process(input_file, output_directory, book_id)