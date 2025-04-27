Hinglish Voice-AI Fine-Tuning Project
This repository contains a 2-hour mini-project to fine-tune a language model for a Hinglish (Hindi-English code-switched) Voice-AI using the OpenAI API. The project includes a small Hinglish dataset, scripts to fine-tune a gpt-3.5-turbo model, and an inference script to generate responses.

Project Overview
The goal is to adapt a base language model to handle casual Hinglish dialogue, typical of voice assistant interactions. The project includes:

Dataset: 15 Hinglish prompt-response pairs in JSONL format, covering greetings, daily plans, food/drink requests, and entertainment.
Fine-Tuning Script: Uploads the dataset and starts a fine-tuning job using the OpenAI API.
Inference Script: Generates responses from the fine-tuned model for new Hinglish prompts.
Status: The dataset was successfully uploaded (file ID: file-QT2ePqKVmwUbBdJw2uLLJr), but fine-tuning requires resolving an OpenAI quota issue.
Repository Structure
text

Copy
Hinglish-Voice-AI/
├── dataset.jsonl        # Hinglish dataset in chat format for gpt-3.5-turbo
├── fine_tune.py        # Script to start fine-tuning with uploaded file
├── inference.py        # Script to generate responses from fine-tuned model
└── README.md           # Project documentation
Prerequisites
Python 3.7+
OpenAI Python SDK (openai>=1.0.0)
An OpenAI API key with sufficient credits (paid plan, e.g., Tier 1, required for fine-tuning)
Windows, Linux, or macOS environment
Setup Instructions
Clone the Repository:
bash

Copy
git clone https://github.com/your-username/Hinglish-Voice-AI.git
cd Hinglish-Voice-AI
Install Dependencies:
bash

Copy
pip install openai>=1.0.0
Set OpenAI API Key:
Windows (PowerShell):
powershell

Copy
$env:OPENAI_API_KEY = "your-api-key"
Verify:
powershell

Copy
echo $env:OPENAI_API_KEY
To set permanently:
Search for "Environment Variables" in the Start menu.
Add a new user variable: OPENAI_API_KEY with your API key.
Restart your terminal.
Linux/macOS:
bash

Copy
export OPENAI_API_KEY="your-api-key"
Verify Dataset:
Ensure dataset.jsonl is in the project directory and uses the chat format (see dataset.jsonl for details).
The dataset is already uploaded (file ID: file-QT2ePqKVmwUbBdJw2uLLJr).
Usage
Run Fine-Tuning:
Ensure your OpenAI account has sufficient credits (check platform.openai.com).
Run the fine-tuning script:
powershell

Copy
python fine_tune.py
This uses the uploaded file ID to start a fine-tuning job. Note the job ID from the output.
If you need to upload a new dataset, use the alternative fine_tune.py with upload logic (available in the commit history or project documentation).
Run Inference:
Update inference.py with the fine-tuned model ID (from the fine-tuning job output).
Run:
powershell

Copy
python inference.py
Example output:
text

Copy
Prompt: Mujhe ek chai pilao.
Response: Ek min, chai banake laata hoon!

Prompt: Aaj sham ko kya karu?
Response: Sham ko dost ke saath coffee pe jaa!

Prompt: Ek funny joke sunao.
Response: Why did the scarecrow become a motivational speaker? Kyunki woh outstanding tha!
Alternative (No Fine-Tuning):
If fine-tuning is blocked by quota issues, modify inference.py to use the base gpt-3.5-turbo model:
python

Copy
model="gpt-3.5-turbo"
Run inference.py to test Hinglish prompts with the base model (less tailored results).
Troubleshooting
Quota Errors (exceeded_quota):
Check your OpenAI account at platform.openai.com under Billing > Overview.
Add credits (e.g., $5–$10 for a small fine-tuning job) or upgrade to a paid plan (Tier 1 or higher).
Contact OpenAI support via help.openai.com, mentioning file ID file-QT2ePqKVmwUbBdJw2uLLJr.
API Key Issues:
Verify the key:
powershell

Copy
echo $env:OPENAI_API_KEY
Regenerate the key in the OpenAI dashboard if invalid.
File Issues:
Ensure dataset.jsonl is in the project directory and uses the chat format (messages with user and assistant roles).
If uploading a new dataset, use the fine_tune.py version with validation and upload logic with client.files.create().
Other Errors:
Test the API key:
python

Copy
import openai
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print(client.models.list())
Check the OpenAI dashboard for fine-tuning job status.
