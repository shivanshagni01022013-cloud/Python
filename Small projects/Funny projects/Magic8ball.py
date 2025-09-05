import random

def question():
    question = input("Enter the question you have (Should be a yes or no): ")

answers = [
    "Yes… but only if you dance first 💃",
    "Nope, not in this universe 🌌",
    "Ask Google, not me 🙄",
    "Definitely… in your dreams 😴",
    "Error 404: Answer not found 🤖",
    "Yes, but don’t tell your mom 🤫",
    "No way, José 🚫",
    "I’d say yes, but I’m just a ball 🎱",
    "Maybe… if you bribe me with pizza 🍕",
    "Of course! Just kidding. Nope 😂",
    "Yes, but only after 3 business days 📅",
    "No, and also… stop bothering me 😡",
    "Absolutely! (but my sources are unreliable 📉)",
    "Yes, but it’s classified 🔒",
    "Why are you even asking me this? 🤷",
    "No, and now I’m judging you silently 👀"
]

for i in range(1, 1000):
    question()
    print(random.choice(answers))

