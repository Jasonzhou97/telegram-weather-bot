from datetime import datetime
import random

def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello","ello","hi","sup"):
        return random.choice(["hey!","hi","diam"])

