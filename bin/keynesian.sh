python scripts/train_gpt2.py \
    --model_name gpt2-medium \
    --train_file data/keynesian_data.csv \
    --output_dir results/keynesian \
    --num_train_epochs 5 \
    --batch_size 2 \
    --save_steps 500 \
    --save_total_limit 2 \
    --logging_steps 10



