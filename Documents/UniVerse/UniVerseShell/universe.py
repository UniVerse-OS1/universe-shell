# 🌍 UniVerseShell – Core OS v1 (TruthShell CLI)
# Author: Kam | System: Will-driven TruthOS Shell

import os
import hashlib
from datetime import datetime

# 🔐 SET YOUR MASTERKEY
MASTERKEY = "khay@67977890"  # You can change this anytime

# 🧠 XP WALLET – Tracks earned XP (in logs/xp.txt)
def load_xp():
    if not os.path.exists("logs/xp.txt"):
        return 0, 0
    with open("logs/xp.txt", "r") as f:
        lines = f.readlines()
        xp = int(lines[0].strip())
        coins = int(lines[1].strip()) if len(lines) > 1 else 0
        return xp, coins

def save_xp(xp, coins):
    with open("logs/xp.txt", "w") as f:
        f.write(f"{xp}\n{coins}")

# 🔒 LOGIN FUNCTION
def login():
    print("🔐 UniVerseShell Login")
    attempt = input("Enter your MasterKey: ")
    if attempt != MASTERKEY:
        print("❌ Access Denied.")
        exit()
    print("✅ Access Granted.")

# 📜 XP Logger
def log_action(action):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/history.txt", "a") as log:
        log.write(f"[{time_now}] {action}\n")

def boost_xp():
    xp_file = "logs/xp.txt"
    if not os.path.exists(xp_file):
        xp, coins = 0, 0
    else:
        with open(xp_file, "r") as f:
            lines = f.readlines()
            xp = int(lines[0].strip())
            coins = int(lines[1].strip()) if len(lines) > 1 else 0

    xp += 5
    coins = xp // 20
    with open(xp_file, "w") as f:
        f.write(f"{xp}\n{coins}")
    messagebox.showinfo("XP Boosted", f"✅ XP: {xp} | Coins: {coins}")

# 🚀 BOOT SYSTEM
login()
print("🌍 Welcome to UniVerseShell – TruthOS CLI")
print("-----------------------------------------")

if not os.path.exists("logs"):
    os.mkdir("logs")

xp, coins = load_xp()

# 🧭 MAIN OS LOOP
while True:
    command = input("universe> ").strip().lower()

    if command == "init":
        print("✅ System initialized.")
        log_action("System initialized")
        xp += 5
        coins = xp // 20
        save_xp(xp, coins)

    elif command == "will":
        today = datetime.now().strftime("%Y-%m-%d")
        entry = input("✍️  What's your Will or Purpose today?\n> ")
        hash_will = hashlib.sha512(entry.encode()).hexdigest()
        with open(f"logs/{today}.will", "w") as f:
            f.write(f"Original:\n{entry}\n\nEncrypted:\n{hash_will}")
        print(f"✅ Will saved to logs/{today}.will")
        log_action("Will written and encrypted")
        xp += 5
        coins = xp // 20
        save_xp(xp, coins)

    elif command == "xp":
        print(f"🌟 Your current XP: {xp}")
        log_action("Checked XP")

    elif command == "quit":
        print("👋 Exiting UniVerseShell...")
        log_action("System exited by user")
        break

    elif command == "wallet":
        print(f"🌟 XP: {xp} | 💰 Coins: {coins}")
        log_action("Checked wallet")

    elif command == "unistore":
        print("🛍 Welcome to UniStore by UniVerse")
        print("Available apps:")
        print("1. TruthLogger v1.0 – Journal + encrypted purpose logs")
        print("2. TimeBlocker v0.9 – Block distraction habits")
        print("3. LegacyVault v1.0 – Store your final Will")
        choice = input("Install which app? (1-3 or cancel): ").strip()
        if choice in ["1", "2", "3"]:
            app = ["TruthLogger", "TimeBlocker", "LegacyVault"][int(choice)-1]
            os.makedirs(f"apps/{app}", exist_ok=True)
            print(f"✅ {app} installed in apps/{app}/")
            log_action(f"Installed {app}")
        else:
            print("❌ Cancelled.")

    else:
        print("⚠️  Unknown command. Try: init, will, xp, quit.")
