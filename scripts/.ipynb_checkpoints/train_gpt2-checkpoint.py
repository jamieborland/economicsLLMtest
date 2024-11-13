# scripts/train_gpt2.py

import argparse
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from data_loader import EconomicDataset

def parse_args():
    parser = argparse.ArgumentParser(description="Fine-tune GPT-2 on economic data.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="gpt2-medium",
        help="Pre-trained model name or path (default: gpt2-medium)"
    )
    parser.add_argument(
        "--train_file",
        type=str,
        required=True,
        help="Path to the training data CSV file."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="./results",
        help="Directory to save the fine-tuned model and logs (default: ./results)."
    )
    parser.add_argument(
        "--num_train_epochs",
        type=int,
        default=3,
        help="Number of training epochs (default: 3)."
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=2,
        help="Batch size per device during training (default: 2)."
    )
    parser.add_argument(
        "--save_steps",
        type=int,
        default=500,
        help="Save checkpoint every X steps (default: 500)."
    )
    parser.add_argument(
        "--save_total_limit",
        type=int,
        default=2,
        help="Maximum number of checkpoints to keep (default: 2)."
    )
    parser.add_argument(
        "--logging_steps",
        type=int,
        default=10,
        help="Log training information every X steps (default: 10)."
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Load the tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(args.model_name)
    model = GPT2LMHeadModel.from_pretrained(args.model_name)

    # Add a separate pad token
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})  # Define a unique pad token
    model.resize_token_embeddings(len(tokenizer))         # Resize the model's embeddings to include the new pad token

    # Prepare the dataset
    dataset = EconomicDataset(tokenizer=tokenizer, file_path=args.train_file)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=args.output_dir,             # Directory to save the model and logs
        num_train_epochs=args.num_train_epochs, # Number of training epochs
        per_device_train_batch_size=args.batch_size,  # Batch size per device during training
        save_steps=args.save_steps,             # Save checkpoint every X steps
        save_total_limit=args.save_total_limit, # Keep only the X most recent checkpoints
        logging_dir=f"{args.output_dir}/logs", # Directory for storing logs
        logging_steps=args.logging_steps        # Log training info every X steps
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
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

if __name__ == "__main__":
    main()
