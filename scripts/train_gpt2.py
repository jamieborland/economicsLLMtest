# scripts/train_gpt2.py

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from data_loader import EconomicDataset

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
tokenizer.pad_token = tokenizer.eos_token  # Use eos_token as pad_token
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

# Prepare the dataset
dataset = EconomicDataset(tokenizer=tokenizer, file_path="data/training_data.csv")

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=10
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Fine-tune the model
trainer.train()

# Save the model and tokenizer
model.save_pretrained("results/fine_tuned_gpt2")
tokenizer.save_pretrained("results/fine_tuned_gpt2")

