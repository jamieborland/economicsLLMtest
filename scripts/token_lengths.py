import pandas as pd
from transformers import GPT2Tokenizer


# Load the CSV file
df = pd.read_csv('/Users/jamie/LLMFineTuning/economicsLLMtest/data/training_data.csv')

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")

# List to store the lengths of tokenized sequences
token_lengths = []

# Loop through each question-answer pair
for idx in range(len(df)):
    question = df.loc[idx, 'prompt']
    answer = df.loc[idx, 'response']
    input_text = f"{question} {tokenizer.eos_token} {answer}"
    
    # Tokenize the input text
    tokens = tokenizer.encode(input_text)
    
    # Store the length of the tokenized sequence
    token_lengths.append(len(tokens))

# Calculate and print basic statistics about the lengths
print(f"Average token length: {sum(token_lengths) / len(token_lengths)}")
print(f"Max token length: {max(token_lengths)}")
print(f"Min token length: {min(token_lengths)}")

