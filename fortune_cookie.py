import random

def fortune_cookie():
    fortunes = [
        "You will have a great day!",
        "Something wonderful is about to happen.",
        "Expect good news soon.",
        "A new opportunity is on the horizon.",
        "You will make a valuable connection.",
        "Happiness will find you when you least expect it.",
        "Be patient — good things take time.",
        "You are stronger than you think.",
        "Your hard work will soon pay off.",
        "Adventure is coming your way!"
    ]
    
    print("🥠 You crack open the fortune cookie...")
    print("✨ Your fortune: ", random.choice(fortunes))

if __name__ == "__main__":
    fortune_cookie()
