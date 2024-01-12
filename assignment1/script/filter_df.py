import pandas as pd
import argparse
parser = argparse.ArgumentParser(description='Input the paragraph.txt and the output will saved.')
# Add arguments with default values
parser.add_argument('--input', type=str, default="./dataframe.csv", help='An input argument with a default value of ./paragraph.txt, the path argument is for select where the input is.')
parser.add_argument('--output', type=str, default="./filtered.csv", help='An output argument with a default value of ./filtered.csv, the path argument is for select where the output will be saved at.')
parser.add_argument('--filter', type=str, help='An filter argument is the type argument is for select what to filter. ex. NOUN, VERB, ADJ')
# Parse the arguments
args = parser.parse_args()
# Read the CSV file
df = pd.read_csv(args.input)
# Filter the DataFrame to keep only rows where 'POS' is 'NOUN'
filtered_df = df[df['POS'] == args.filter]
# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(args.output, index=False)