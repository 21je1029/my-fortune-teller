# fortune.py

import random

def main():
    print("🔮 Welcome to V K S Tejaswini's Fortune Teller (21JE1029) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "✨ Your fortune: Great things await you, Tejaswini! Keep smiling. ✨",
            "✨ Your fortune: Happiness attracts success. Enjoy your day! ✨"
        ],
        "sad": [
            "🌧 Your fortune: Storms don’t last forever. Better days are coming. 🌈",
            "🌧 Your fortune: Take time to heal, good news is on the horizon. 🌟"
        ],
        "neutral": [
            "🌤 Your fortune: Today is a blank page—make it a masterpiece. ✨",
            "🌤 Your fortune: Sometimes, peace is the best gift. Savor it. 🍃"
        ],
        "stressed": [
            "💆 Your fortune: Breathe, relax, and trust the journey. 🌿",
            "💆 Your fortune: Even Tejaswini needs a break—treat yourself kindly. 💖"
        ]
    }

    if mood in fortunes:
        print(random.choice(fortunes[mood]))
    else:
        print("❗ Sorry, I don't recognize that mood. Please enter happy, sad, neutral, or stressed.")

if _name_ == "_main_":
    main()