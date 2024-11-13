# scripts/evaluate_gpt2.py

import argparse
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate fine-tuned GPT-2 on economic data.")
    parser.add_argument(
        "--model_dir",
        type=str,
        required=True,
        help="Directory of the fine-tuned model."
    )
    parser.add_argument(
        "--test_file",
        type=str,
        required=True,
        help="Path to the test data CSV file."
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="generated_responses_evaluation.csv",
        help="Path to save the evaluation results (default: generated_responses_evaluation.csv)."
    )
    parser.add_argument(
        "--max_length",
        type=int,
        default=128,
        help="Maximum length for generated responses (default: 128)."
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Load the fine-tuned model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(args.model_dir)
    model = GPT2LMHeadModel.from_pretrained(args.model_dir)

    # Load the test dataset
    test_data = pd.read_csv(args.test_file)

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

        # Print the comparison
        print(f"Q: {question}")
        print(f"True A: {true_answer}")
        print(f"Generated A: {generated_answer}")
        print("-" * 80)

    # Convert results to DataFrame and save as CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv(args.output_file, index=False)
    print(f"Evaluation results saved to '{args.output_file}'")

if __name__ == "__main__":
    main()
