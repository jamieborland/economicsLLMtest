# Fine-Tuning GPT-2 on Economic Question-Answer Pairs

This project fine-tunes GPT-2, an open-source language model, on a dataset of economic question-answer pairs. It allows for training on various datasets and generates and evaluates responses based on specific prompts. Evaluation is conducted by comparing the generated answers against a test set of questions and responses.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/economic-gpt2-finetune.git
    cd economic-gpt2-finetune
    ```
    
2. **Create a virtual environment and activate it**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
    
3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

To train the model on a dataset, use the `train_gpt2.py` script. This script fine-tunes GPT-2 on the specified training dataset, storing the trained model in the `results` directory.

**Arguments**:
- `--train_file`: Path to the training data CSV file.
- `--output_dir`: Directory to save the fine-tuned model.
- `--num_epochs`: Number of training epochs (default: 3).
- `--batch_size`: Training batch size (default: 2).

**Example command**:
```bash
python scripts/train_gpt2.py --train_file data/training_data.csv --output_dir results/fine_tuned_gpt2 --num_epochs 3 --batch_size 2

