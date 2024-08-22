from transformers import TrainingArguments, Trainer # type: ignore
from transformers import DataCollatorForSeq2Seq # type: ignore
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer # type: ignore
from datasets import load_dataset, load_from_disk # type: ignore
import torch # type: ignore
from textSummarizer.entity import ModelTrainerConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # Use 'mps' explicitly if running on Apple Silicon
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        
        # Initialize tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Define training arguments with memory optimizations
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=float(self.config.num_train_epochs),
            warmup_steps=int(self.config.warmup_steps),
            per_device_train_batch_size=1,  # Reduce batch size
            per_device_eval_batch_size=1,   # Reduce batch size
            weight_decay=float(self.config.weight_decay),
            logging_steps=int(self.config.logging_steps),
            evaluation_strategy="steps",
            eval_steps=500,
            save_steps=int(1e6),  # Adjust to save less frequently
            gradient_accumulation_steps=1,  # Adjust if needed
            fp16=False  # Mixed precision not supported on MPS
        )

        # Initialize Trainer
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["test"], 
            eval_dataset=dataset_samsum_pt["validation"]
        )
        
        # Start training
        trainer.train()

        # Save model and tokenizer
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
