import tkinter as tk
import random

# List of fortunes
fortunes = [
    "Today will be your lucky day!",
    "You will achieve your dreams soon.",
    "Happiness is just around the corner.",
    "Stay strong — good things are coming.",
    "Believe in yourself and magic will happen.",
    "A big opportunity is coming your way!",
    "Trust your instincts — they are right.",
    "Success is a journey, not a destination."
]

# Function to pick a random fortune
def get_fortune():
    fortune = random.choice(fortunes)
    fortune_label.config(text=fortune)

