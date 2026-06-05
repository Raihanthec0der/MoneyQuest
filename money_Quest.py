print("=" * 55)
print("💰        MONEY QUEST: SAVE TO SUCCEED        💰")
print("=" * 55)

name = input("\n👤 Enter your name: ")

income = float(input("💵 Monthly pocket money/income (Tk): "))
saved = float(input("🏦 Total savings (Tk): "))

saving_rate = (saved / income) * 100 if income > 0 else 0

# ========================
# LEVEL SYSTEM
# ========================

if saving_rate >= 70:
    level = 5
    title = "💎 Savings Legend"
elif saving_rate >= 50:
    level = 4
    title = "👑 Money Master"
elif saving_rate >= 30:
    level = 3
    title = "🚀 Future Investor"
elif saving_rate >= 15:
    level = 2
    title = "⭐ Smart Saver"
else:
    level = 1
    title = "🌱 Beginner Saver"

# ========================
# PROGRESS BAR
# ========================

progress = min(saving_rate, 100)
filled = int(progress / 5)

bar = "█" * filled + "░" * (20 - filled)

# ========================
# MONEY SCORE
# ========================

score = int(saved / 10) + int(saving_rate * 5)

if score >= 1000:
    rank = "💎 Financial Legend"
elif score >= 600:
    rank = "👑 Money Master"
elif score >= 300:
    rank = "🚀 Investor"
elif score >= 100:
    rank = "⭐ Saver"
else:
    rank = "🌱 Beginner"

# ========================
# BADGES
# ========================

badges = []

if saved > 0:
    badges.append("🌱 First Step")

if saved >= 100:
    badges.append("🥉 First 100 Club")

if saved >= 500:
    badges.append("🥈 First 500 Club")

if saved >= 1000:
    badges.append("🥇 1000 Tk Saver")

if saving_rate >= 20:
    badges.append("⭐ Smart Saver")

if saving_rate >= 40:
    badges.append("🚀 Future Investor")

if saving_rate >= 50:
    badges.append("👑 Money Master")

if saving_rate >= 70:
    badges.append("💎 Savings Legend")

# ========================
# NEXT TARGET
# ========================

targets = [
    (100, "🥉 First 100 Club"),
    (500, "🥈 First 500 Club"),
    (1000, "🥇 1000 Tk Saver"),
    (5000, "🚀 Future Investor"),
    (10000, "👑 Money Master"),
    (20000, "💎 Savings Legend")
]

next_badge = None

for amount, badge in targets:
    if saved < amount:
        next_badge = (amount, badge)
        break

# ========================
# MONEY TREE
# ========================

tree = {
    1: """
       🌱
    """,
    2: """
       🌿
       │
    """,
    3: """
      🌿🌿
        │
    """,
    4: """
     🌿🌳🌿
        │
    """,
    5: """
     💰💰💰
    🌳🌳🌳
      ║║║
    """
}

# ========================
# DASHBOARD
# ========================

print("\n" + "=" * 55)
print(f"🏆 MONEY DASHBOARD FOR {name.upper()}")
print("=" * 55)

print(f"\n🎖️ Level {level} | {title}")
print(f"🏅 Rank: {rank}")
print(f"💯 Money Score: {score}")

print("\n📊 SAVING PROGRESS")
print(f"[{bar}] {saving_rate:.1f}%")

print("\n🌳 MONEY TREE")
print(tree[level])

print("🏅 BADGES UNLOCKED")
if badges:
    for badge in badges:
        print("✓", badge)
else:
    print("No badges yet.")

# ========================
# NEXT BADGE
# ========================

if next_badge:
    target_amount, badge_name = next_badge
    remaining = target_amount - saved
    percent = (saved / target_amount) * 100

    filled = int(percent / 5)
    target_bar = "█" * filled + "░" * (20 - filled)

    print("\n🎯 NEXT BADGE TARGET")
    print(f"Badge: {badge_name}")
    print(f"Need: {remaining:.0f} Tk more")
    print(f"[{target_bar}] {percent:.1f}%")

# ========================
# DREAM GOAL
# ========================

goal = float(input("\n🎯 Enter your dream goal amount (Tk): "))

goal_progress = min((saved / goal) * 100, 100)

filled = int(goal_progress / 5)
goal_bar = "█" * filled + "░" * (20 - filled)

print("\n🏠 DREAM GOAL TRACKER")
print(f"[{goal_bar}] {goal_progress:.1f}%")

if goal > saved:
    print(f"💰 Remaining: {goal - saved:.0f} Tk")
else:
    print("🎉 Goal Achieved!")

# ========================
# MOTIVATION
# ========================

quotes = [
    "Small savings today become big opportunities tomorrow.",
    "Money grows where discipline goes.",
    "Don't work only for money—make money work for you.",
    "Every taka saved is a step toward freedom.",
    "Future millionaires start with small habits."
]

import random
print("\n💡 TODAY'S MOTIVATION")
print("👉", random.choice(quotes))

print("\n🚀 Keep growing your Money Tree and unlock more badges!")
print("=" * 55)
