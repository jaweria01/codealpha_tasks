import nltk
import spacy
from nltk.chat.util import Chat, reflections
from nltk import pos_tag, word_tokenize
from nltk.stem import WordNetLemmatizer
from spacy import load

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Load spaCy English model for NER
nlp = load("en_core_web_sm")
lemmatizer = WordNetLemmatizer()

# Debug Mode: Set True to show POS, Lemmatization, and NER details
debug_mode = False  # Change to True for debugging

# POS tagging function
def pos_tagging(sentence):
    tokens = word_tokenize(sentence)
    return pos_tag(tokens)

# Lemmatization function
def lemmatize_text(sentence):
    tokens = word_tokenize(sentence)
    return " ".join([lemmatizer.lemmatize(word) for word in tokens])

# Named Entity Recognition (NER) function
def recognize_entities(sentence):
    doc = nlp(sentence)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities if entities else ["No entities found"]

# Chatbot patterns
import re

patterns = [
    # Greetings
    (r'(hi|hello|hey|hye|hola|salam|assalamualaikum)', [
        'Hello! How can I assist you today?',
        'Hi there! How are you?' 
    ]),
    (r'how are you(.*)', [
        "I'm doing great! How about you?"
    ]),
    (r"(i\'m fine|i am fine|im fine|i am good|feeling great)", [
        "That's great to hear! 😊 If you’d like to talk about food, education, or health, I'm here to help!"
    ]),

    # IELTS-related questions (Flexible Matching)
    (r'(.*)(ielts|english test|language test)(.*)', [
        "IELTS is an English language test for study, migration, or work. Would you like tips for preparation?",
        "IELTS assesses your language skills. Would you like to know about its test structure or tips?"
    ]),
    (r'(.*)(yes|sure)(.*)', [
        "For IELTS preparation, practice listening, reading, writing, and speaking daily. Joining online courses and taking practice tests can help a lot!",
        "Focus on vocabulary, grammar, and time management to improve your IELTS score."
    ]),

    # Health Tips
    (r'(.*)(health|fitness|exercise|diet|healthy food)(.*)', [
        "For better health, stay hydrated, exercise regularly, and maintain a balanced diet with fruits and vegetables.",
        "Avoid processed foods, prioritize mental well-being, and aim for 7-8 hours of sleep daily."
    ]),

    # Weather Conditions in Pakistan
    (r'(.*)(weather|temperature|forecast|rain|sunny)(.*)(pakistan|lahore|karachi|islamabad|punjab|sindh|kpk|balochistan)(.*)', [
        "The weather in Pakistan varies greatly by region. Would you like a specific city update?",
        "Pakistan's weather ranges from extreme heat in summer to chilly winters. What city are you inquiring about?"
    ]),

    # Education Trends
    (r'(.*)(education|study|learning|courses|skills)(.*)', [
        "Online learning platforms are gaining popularity for data science, AI, and coding courses.",
        "STEM fields and digital skills are highly sought-after in today's job market. Would you like course recommendations?"
    ]),

    # Job-related updates
    (r'(.*)(job|career|vacancy|interview|hiring)(.*)', [
        "Job opportunities are growing in the fields of data science, software development, and digital marketing.",
        "Focus on building technical skills, creating a strong resume, and preparing for common interview questions."
    ]),

    # Food Suggestions
    (r'(.*)(food|restaurant|cuisine|snacks|recipe)(.*)', [
        "If you're craving something spicy, try biryani or karahi! For something light, salads or sandwiches are a great choice.",
        "Would you like healthy food tips or popular Pakistani dishes?"
    ]),

    # General Advice
    (r'(.*)(advice|suggestion|guidance|recommendation)(.*)', [
        "You can start by setting small goals, exploring new hobbies, or improving your time management skills.",
        "Focusing on self-care, mindfulness, and maintaining a positive mindset can greatly improve your lifestyle."
    ]),

    # Identity
    (r'(.*)(who are you|what is your name|what do you do|what is your main work)(.*)', [
        "I'm your friendly chatbot, here to help you! 😊",
        "I'm your helpful chatbot, ready to assist you with anything you need! What's your name?"
    ]),
    (r'(.*)(my name is|i am|call me)(.*)', [
        "That's nice! 😊 It's great to meet you. What do you do?"
    ]),
    (r'(.*)(i work as|i am a|my job is|i do)(.*)', [
        "That sounds amazing! Keep up the great work. 😊"
    ]),

    # Positive responses
    (r'(.*)(okay|ok|good|great)(.*)', [
        "Yeah! 😊",
        "That's nice to hear!",
        "Sounds good! 👍"
    ]),

    (r'(.*)(thank you|thanks)(.*)', [
        "You're very welcome! I'm always here to help you. 😊",
        "Glad I could assist you!"
    ]),

    # Fallback responses
    (r'(.*)', [
        "That's interesting! Tell me more.",
        "I'm here to chat about anything you'd like.",
        "Feel free to ask me anything!"
    ]),
]






# Custom reflections
custom_reflections = {
    "i am": "you are",
    "i'm": "you are",
    "i was": "you were",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

chatbot = Chat(patterns, custom_reflections)

# Chatbot Function
def chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Debug Mode Display (only shown when debug_mode = True)
        if debug_mode:
            print("[POS Tagging]:", pos_tagging(user_input))
            print("[Lemmatized Text]:", lemmatize_text(user_input))
            print("[Named Entities]:", recognize_entities(user_input))

        response = chatbot.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask me something else?")

chat()
