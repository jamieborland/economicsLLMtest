# Fine-Tuning GPT-2 on Economic Question-Answer Pairs

This project serves as a proof of concept for using AI to predict a person's responses to economic problems.

We fine-tune GPT-2, an open-source language model, on a dataset of economic question-answer pairs. The implementation allows for training on various datasets and generates and evaluates responses based on specific prompts. Evaluation is conducted by comparing the generated answers against a test set of questions and responses.

## Methodology
A training set of 1000 questions was generated using ChatGPT. These cover a range of topics, including supply and demand, the role of Government, taxation and fiscal policy, International Trade, Inflation and Monetary Policy, Labour Markets and Employment, Capital Markets, Globalization, Public Debt, and Economic Incentives.

A test set of 71 questions covering the same topics was also generated.

Responses to the trainng and test questions were generated by asking ChatGPT to write responses under different personas; a "Neoclassical" persona and a "Keynesian" persona. 

These training and test questions/responses are available in the subdirectory:
```
scripts/data
``` 

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jamieborland/economicsLLMtest.git
    cd economicsLLMtest
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
4. **Convert the Data to CSV**

    ```
    python scripts/data/neoclassical.py
   python scripts/data/neoclassical_test.py
    ```
Note, repeat for Keynesian datasets too.   

## Usage

### Training the Model

To fine-tune the model on a dataset, bash scripts have been provided, in
```
/bin
```
The scripts "keynesian.sh" and "neoclassical.sh" fine tune the model, storing the output in `results`

**Arguments**:
- `--train_file`: Path to the training data CSV file.
- `--output_dir`: Directory to save the fine-tuned model.
- `--num_epochs`: Number of training epochs (default: 3).
- `--batch_size`: Training batch size (default: 2).

**Example command**:

```
chmod +x bin/neoclassical.sh #Allows the bash script to be executable
./bin/neoclassical.sh
```

## Evaluating the Model

Bash scripts for evaluation have also been provided in `/bin`

**Example Command**

```
chmod +x bin/neoclassical_evaluation.sh
./bin/neoclassical_evaluation.sh

```
This example command's output would be saved in `results/neoclassical_results.csv`
The CSV contains the test question, the true answer, and the model generated answer for comparison.
