import pandas as pd
import spacy
import argparse
parser = argparse.ArgumentParser(description='Input the paragraph.txt and the output will be saved.')
# Add arguments with default values
parser.add_argument('--input', type=str, default="./paragraph.txt", help='An input argument with a default value of ./paragraph.txt, the path argument is for select where the input is.')
parser.add_argument('--output', type=str, default="./dataframe.csv", help='An output argument with a default value of ./dataframe.csv, the path argument is for select where the output will be saved at.')
# Parse the arguments
args = parser.parse_args()
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")
# read input
f = open(args.input, "r")
text = f.read()
# Process the text with spaCy
doc = nlp(text)
# Initialize an empty list to store the data
data = []
# Iterate over tokens in the doc
for token in doc:
    # Append the token attributes as a tuple to the data list
    data.append((token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                 token.shape_, token.is_alpha, token.is_stop))
# Convert the list of tuples into a DataFrame
df = pd.DataFrame(data, columns=['TEXT', 'LEMMA', 'POS', 'TAG', 'DEP', 'SHAPE', 'ALPHA', 'STOP'])
# Display the DataFrame
print(df)
df.to_csv(args.output, index=False)

