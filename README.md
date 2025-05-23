# fine_tuning_llama3
Fine-Tuning LLaMA 3.1 with LoRA
This project focuses on fine-tuning the LLaMA 3.1 model using a custom dataset in the Alpaca instruction format. The process applies LoRA (Low-Rank Adaptation) for parameter-efficient tuning and is optimized to run on systems with CUDA-compatible GPUs.

✅ Objective
Adapt the pre-trained LLaMA 3.1 model to classify or generate domain-specific responses by training it with a dataset of structured instructions, inputs, and outputs.

💼 Technologies & Libraries Used
PyTorch – for tensor operations and model training

Transformers – to load and manage LLaMA models

PEFT (Parameter-Efficient Fine-Tuning) – to apply LoRA for training only small adapter layers

TRL (Transformer Reinforcement Learning) – used for the supervised fine-tuning interface (SFTTrainer)

Datasets – for loading and mapping over the JSON training file

Anaconda – for isolated environment and dependency management

🔍 Dataset Format
The training dataset follows the Alpaca JSON structure, including:

instruction: what the model is asked to do

input: the specific content to process

output: the expected response

🧠 Training Strategy
The fine-tuning process:

Loads LLaMA 3.1 in fp16 (float16) mode for GPU acceleration

Applies LoRA adapters to reduce GPU memory requirements

Tokenizes and preprocesses each training sample using the Hugging Face Tokenizer API

Trains using SFTTrainer, a streamlined trainer for supervised instruction tuning

📍 Output
After training, the following files are saved:

Fine-tuned LoRA model and adapter weights

Tokenizer configuration for inference

Logs and progress tracking files


