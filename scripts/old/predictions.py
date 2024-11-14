#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:48:02 2024

@author: jamie
"""

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import pandas as pd

# Load the fine-tuned model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("results/neoclassical")
model = GPT2LMHeadModel.from_pretrained("results/neoclassical")

# Load the test dataset (only for generating responses and comparing)
test_data = pd.read_csv("data/test_data.csv")

# Function to generate a response based on a question
def generate_response(question):
    input_text = f"{question} {tokenizer.eos_token}"
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate the response
    output = model.generate(
        inputs['input_ids'],
        max_length=128,
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Iterate through the test set to generate and compare responses
for idx, row in test_data.iterrows():
    question = row['prompt']  # Question only, fed to the model
    true_answer = row['response']  # Correct answer, only for comparison

    generated_answer = generate_response(question)  # Model's answer

    # Print or log the comparison for manual review
    print(f"Q: {question}")
    print(f"True A: {true_answer}")       # Ground truth
    print(f"Generated A: {generated_answer}")  # Model's prediction
    print("-" * 80)
