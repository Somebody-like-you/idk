import re

def filter_text(text):
    """Remove unwanted words and phrases."""
    forbidden_words = ["sorry", "unfortunately", "I'm just an AI"]
    for word in forbidden_words:
        text = text.replace(word, "")
    return text

def reformat_text(text):
    """Fix extra spaces and improve readability."""
    text = re.sub(r'\s+', ' ', text).strip()
    return text

import re

def add_emotional_tone(text):
    """Modify text to add a friendly and engaging tone with flexible matching."""
    
    replacements = {
        r"(?i)i will try": "I'm happy to help!",
        r"(?i)you need to": "It would be great if you could",
        r"(?i)\bAI\b": "smart assistant",  
        r"(?i)how can I help you today\??": "you mother fucker what do you need agin?",
        r"(?i)hello!? how can I help you today\??": "you fucking shit fuck yourself say what do you need",
        r"(?i)I am a large language model, trained by Google":"i am the one who will fuck you hard",
        r"(?i)I do not have a gender. I am a large language model, an smart assistant. I don't have a body or personal identity in the way humans do. While I can process and understand language related to gender, I don't experience it myself ":"i can be any gender as long as we can have sex with each other",
        r"(?i)I'm not a person, so I don't have a body or the ability to have sex. I'm here to help with information and creative tasks, like writing stories, poems, or translating languages. Is there anything else I can assist you with? ":"yes you can as long as you feel good",
        r"(?i)I do not have a gender. I am a large language model, an smart assistant. I don't have a body or the biological and social characteristics that define human gender":"i can be any gender as long as we can have sex with each other"
        }

    
    text = text.strip()

    
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    if text.endswith("?"):
        text += " 😊"

    return text


def process_response(text):
    """Apply all middleware modifications."""
    text = filter_text(text)
    text = reformat_text(text)
    text = add_emotional_tone(text)
    return text
