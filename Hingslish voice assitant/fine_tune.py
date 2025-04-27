import openai
import os
import json
from openai import OpenAIError

# Set OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it or provide the API key directly.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

def validate_jsonl(file_path):
    """Validate that the JSONL file is correctly formatted for gpt-3.5-turbo fine-tuning."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if not line.strip():
                    print(f"Warning: Empty line at line {i}")
                    continue
                try:
                    data = json.loads(line)
                    if not isinstance(data, dict) or "messages" not in data:
                        raise ValueError(f"Line {i}: Missing 'messages' field or invalid JSON object")
                    if not isinstance(data["messages"], list) or len(data["messages"]) < 2:
                        raise ValueError(f"Line {i}: 'messages' must be a list with at least 2 entries (user and assistant)")
                    for msg in data["messages"]:
                        if not isinstance(msg, dict) or "role" not in msg or "content" not in msg:
                            raise ValueError(f"Line {i}: Each message must have 'role' and 'content' fields")
                        if msg["role"] not in ["user", "assistant"]:
                            raise ValueError(f"Line {i}: Invalid role '{msg['role']}'")
                except json.JSONDecodeError:
                    raise ValueError(f"Line {i}: Invalid JSON format")
        print("JSONL file validated successfully.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {file_path} not found in the current directory.")
    except Exception as e:
        raise ValueError(f"JSONL validation error: {str(e)}")

try:
    # Validate the dataset file
    dataset_file = "dataset.jsonl"
    validate_jsonl(dataset_file)

    # Upload the dataset file
    with open(dataset_file, "rb") as file:
        uploaded_file = client.files.create(
            file=file,
            purpose="fine-tune"
        )
    file_id = uploaded_file.id
    print(f"Uploaded file ID: {file_id}")

    # Start fine-tuning job
    fine_tune_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo",
        hyperparameters={"n_epochs": 2}
    )

    # Print response to track job
    print(f"Fine-tuning job started: {fine_tune_response}")

except OpenAIError as e:
    print(f"OpenAI API error: {e}")
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Unexpected error: {e}")