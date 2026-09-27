import time
import os
import sys

# Pink color codes
PINK = "\033[95m"
LIGHT_PINK = "\033[35m"
WHITE = "\033[97m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, speed=0.03):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)
    print()

def heart_animation():
    hearts = [
        "        ❤️",
        "      ❤️ ❤️",
        "    ❤️ ❤️ ❤️",
        "  ❤️ ❤️ ❤️ ❤️",
        "❤️ ❤️ ❤️ ❤️ ❤️"
    ]

    for line in hearts:
        print(PINK + line + RESET)
        time.sleep(0.15)

clear_screen()

print(PINK + "╔══════════════════════════════════════╗" + RESET)
print(PINK + "║       💗 A SPECIAL MESSAGE 💗        ║" + RESET)
print(PINK + "╚══════════════════════════════════════╝" + RESET)

time.sleep(1)

name = ("A")

clear_screen()

print(PINK)
heart_animation()

print(RESET)
type_text("I have something important to tell you...", 0.05)
time.sleep(1)

clear_screen()

print(PINK + "💗 " * 15 + RESET)
print()

type_text(f"Dear {name},", 0.06)

print()

type_text(
    "I've been keeping something in my heart for a while.",
    0.04
)

type_text(
    "Whenever I see you, my day somehow becomes brighter.",
    0.04
)

type_text(
    "Your smile makes me happy, and your presence feels special.",
    0.04
)

print()

type_text(
    "I don't know exactly when it happened...",
    0.05
)

time.sleep(1)

type_text(
    "but somewhere along the way...",
    0.05
)

print()

type_text(
    "❤️ I FELL FOR YOU. ❤️",
    0.1
)

print()
time.sleep(1)

type_text(
    f"{name}, will you be mine? 💕",
    0.08
)

print()

print(PINK + "╔══════════════════════╗" + RESET)
print(PINK + "║   1. yes ❤️          ║" + RESET)
print(PINK + "║   2. no  💔          ║" + RESET)
print(PINK + "╚══════════════════════╝" + RESET)

choice = input("\nChoose 1 or 2: ")

clear_screen()

if choice == "1":
    heart_animation()

    print()
    type_text("❤️❤️❤️ YAAAAAY!!! ❤️❤️❤️", 0.08)
    print()

    type_text(
        "You just made my heart incredibly happy! 🥰",
        0.05
    )

    print()
    type_text(
        "I promise to always respect, appreciate, and care about you. 💗",
        0.04
    )

elif choice == "2":
    print()
    type_text("That's okay. 💗", 0.06)
    print()

    type_text(
        "Thank you for being honest with me.",
        0.05
    )

    type_text(
        "Your feelings matter, and I will always respect your answer. ❤️",
        0.04
    )

else:
    print()
    type_text("Hmm... I think you need some time to decide. 😳💕", 0.05)

print()
print(PINK + "💗 Thank you for reading my message. 💗" + RESET)