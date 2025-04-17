# fortune.py

import random

def main():
    print("🔮 Welcome to V K S Tejaswini's Fortune Teller (21JE1029) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "✨ Your fortune: Great things await you, Tejaswini! Keep smiling. ✨",
            "🌞 Your fortune: Today will bring joy and sunshine!"
        ],
        "sad": [
            "🌧 Your fortune: Storms don’t last forever. Better days are coming. 🌈",
            "🕊 Your fortune: Let yourself feel. Healing is on the way."
        ],
        "neutral": [
            "🌤 Your fortune: A calm day brings clarity. Trust it.",
            "🪞 Your fortune: Even in stillness, growth happens."
        ],
        "stressed": [
            "💆 Your fortune: Even Tejaswini needs a break—treat yourself kindly. 💖",
            "🧘 Your fortune: Breathe deeply. You’re doing better than you think."
        ]
    }

    if mood in fortunes:
        print(random.choice(fortunes[mood]))
    else:
        print("❗ Sorry, I don't recognize that mood. Please enter happy, sad, neutral, or stressed.")

if _name_ == "_main_":
    main()