Hinglish Voice-AI Fine-Tuning Mini-Project
This project implements a fine-tuning workflow for a Hinglish Voice-AI using the OpenAI API (version >=1.0.0). Below are the deliverables, including the dataset, fine-tuning script, inference script, and design rationale.

dataset.jsonl
The dataset contains 15 Hinglish prompt-response pairs in the chat format required for gpt-3.5-turbo fine-tuning. Each line is a JSON object with a messages field containing a user prompt and assistant response, covering casual greetings, daily plans, food/drink requests, and light conversational phrases. The dataset has been successfully uploaded to OpenAI (file ID: file-QT2ePqKVmwUbBdJw2uLLJr).

Note: The dataset.jsonl file is available in the project directory and matches the format provided in previous steps. Ensure it is saved with the .jsonl extension if you need to re-upload.

fine_tune.py
The fine-tuning script starts a fine-tuning job using the already uploaded dataset (file ID: file-QT2ePqKVmwUbBdJw2uLLJr). If you need to upload a new dataset, revert to the version with validation and upload logic (available in prior instructions).

Note: The fine_tune.py script is configured to use the existing file ID to avoid redundant uploads. Ensure your OpenAI account has sufficient credits before running.

inference.py
This script loads the fine-tuned model and generates responses for three new Hinglish prompts. Update the model ID in the script once fine-tuning completes.

Note: Replace "ft:gpt-3.5-turbo:your-org:your-model-id" with the fine-tuned model ID from the fine-tuning job.

README.md
Setup Instructions
Install OpenAI SDK: Ensure you have the latest OpenAI Python SDK:
bash

Copy
pip install openai>=1.0.0
Set OPENAI_API_KEY:
On Windows (PowerShell): Set the API key for the current session:
powershell

Copy
$env:OPENAI_API_KEY = "your-api-key"
Verify it:
powershell

Copy
echo $env:OPENAI_API_KEY
To set it permanently:
Open "Environment Variables" (search in Start menu).
Under "User variables," add a new variable with name OPENAI_API_KEY and your API key as the value.
Restart your terminal or IDE.
On Linux/macOS: Export the key:
bash

Copy
export OPENAI_API_KEY="your-api-key"
Prepare Dataset:
The dataset is already uploaded (file ID: file-QT2ePqKVmwUbBdJw2uLLJr). If you need to update it, save dataset.jsonl in the project directory (e.g., C:\Users\Anubhav\OneDrive\Desktop\Hingslish voice assitant) and use the fine_tune.py version with upload logic.
Ensure dataset.jsonl uses the chat format (messages field with user and assistant roles) and has the .jsonl extension.
Run Fine-Tuning:
Navigate to the project directory:
powershell

Copy
cd C:\Users\Anubhav\OneDrive\Desktop\Hingslish voice assitant
Run the fine-tuning script:
powershell

Copy
python fine_tune.py
This starts a fine-tuning job using the uploaded file. Note the job ID from the response.
Run Inference:
Update inference.py with your fine-tuned model ID (from the fine-tuning job).
Run:
powershell

Copy
python inference.py