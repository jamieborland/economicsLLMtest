#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:53:37 2024

@author: jamie
"""

# scripts/evaluate_gpt2.py

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import pandas as pd

# Load the fine-tuned model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("results/neoclassical")
model = GPT2LMHeadModel.from_pretrained("results/neoclassical")

# Load the test dataset (only for generating responses and comparing)
test_data = pd.read_csv("data/test_data.csv")
test_data.columns = test_data.columns.str.strip()  # Ensure no leading/trailing spaces

# Function to generate a response based on a question
def generate_response(question):
    input_text = f"{question} {tokenizer.eos_token}"
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=128,
        return_attention_mask=True  # Ensure attention masks are returned
    )

    # Generate the response with attention mask
    output = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],  # Pass the attention mask explicitly
        max_length=128,
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Initialize an empty list to store results
results = []

# Iterate through the test set to generate and compare responses
for idx, row in test_data.iterrows():
    question = row['prompt']  # Question only, fed to the model
    true_answer = row['response']  # Correct answer, only for comparison

    generated_answer = generate_response(question)  # Model's answer

    # Append each result to the list
    results.append({
        "Question": question,
        "True Answer": true_answer,
        "Generated Answer": generated_answer
    })

    # Print the comparison for manual review
    print(f"Q: {question}")
    print(f"True A: {true_answer}")               # Ground truth
    print(f"Generated A: {generated_answer}")     # Model's prediction
    print("-" * 80)

# Optionally, save the results to a CSV file for further analysis
results_df = pd.DataFrame(results)
results_df.to_csv("generated_responses_evaluation.csv", index=False)
print("Evaluation results saved to 'generated_responses_evaluation.csv'")
