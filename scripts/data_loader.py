# scripts/data_loader.py

import pandas as pd
from torch.utils.data import Dataset

class EconomicDataset(Dataset):
    def __init__(self, tokenizer, file_path, max_length=64):
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
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        return {
            "input_ids": inputs["input_ids"].squeeze(),
            "attention_mask": inputs["attention_mask"].squeeze()
        }

