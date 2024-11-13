# scripts/data_loader.py

import pandas as pd
from torch.utils.data import Dataset

class EconomicDataset(Dataset):
    def __init__(self, tokenizer, file_path, max_length=128):
        self.data = pd.read_csv(file_path)
        self.data.columns = self.data.columns.str.strip()  # Remove any leading/trailing spaces
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
            padding="max_length",
            truncation=True,
            return_tensors="pt",
            return_attention_mask=True  # Ensure attention masks are returned
        )

        labels = inputs["input_ids"].clone()  # Clone input_ids as labels

        return {
            "input_ids": inputs["input_ids"].squeeze(),
            "attention_mask": inputs["attention_mask"].squeeze(),
            "labels": labels.squeeze()  # Add labels for loss calculation
        }
