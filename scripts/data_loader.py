# scripts/data_loader.py

import pandas as pd
from torch.utils.data import Dataset

class EconomicDataset(Dataset):
    def __init__(self, tokenizer, file_path, max_length=128):
        self.data = pd.read_csv(file_path)
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        question = self.data.loc[idx, 'prompt']
        answer = self.data.loc[idx, 'response']
        input_text = f"{question} {self.tokenizer.eos_token} {answer}"

        inputs = self.tokenizer(
            input_text,
            max_length=self.max_length,
            padding="max_length",  # Pads shorter sequences
            truncation=True,  # Truncates longer sequences
            return_tensors="pt"
        )

        # Return both the input_ids and labels
        # GPT-2 uses input_ids as both input and target (labels)
        labels = inputs["input_ids"].clone()  # Clone input_ids as labels

        return {
            "input_ids": inputs["input_ids"].squeeze(),
            "attention_mask": inputs["attention_mask"].squeeze(),
            "labels": labels.squeeze()  # Add labels for loss calculation
        }
