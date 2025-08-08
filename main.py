import json
from utils.whatsapp import format_response
from puchai_sdk import PuchAssistant

# Load Puch.AI config
with open("puch_config.json") as f:
    assistant_config = json.load(f)

assistant = PuchAssistant.from_config(assistant_config)

# Memory store
MEMORY_PATH = "memory_store.json"

def load_memory():
    try:
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f)

def handle_user_input(user_id, message):
    memory = load_memory()
    user_history = memory.get(user_id, [])

    # Construct conversation context
    full_input = {
        "history": user_history,
        "message": message
    }

    # Get AI response
    response = assistant.chat(full_input)

    # Update memory
    user_history.append({"user": message, "bot": response})
    memory[user_id] = user_history
    save_memory(memory)

    return format_response(response)
