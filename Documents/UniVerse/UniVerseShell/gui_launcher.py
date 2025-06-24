# 💠 UniVerseShell GUI Desktop v2
# Author: Kam & GPT | GUI for TruthOS System

import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import zipfile
from datetime import datetime

MASTERKEY = "khay@67977890"

def show_welcome():
    messagebox.showinfo("Welcome", "🌍 Welcome to UniVerse GUI.\nRun your life with purpose.")

def open_wallet():
    try:
        with open("logs/xp.txt", "r") as f:
            lines = f.readlines()
            xp = lines[0].strip()
            coins = lines[1].strip() if len(lines) > 1 else "0"
        messagebox.showinfo("XP Wallet", f"XP: {xp}\nCoins: {coins}")
    except:
        messagebox.showerror("Error", "XP file not found. Run CLI at least once.")

def open_will_log():
    def save_will():
        entry = entry_box.get("1.0", tk.END).strip()
        if entry:
            today = datetime.now().strftime("%Y-%m-%d")
            hash_will = __import__('hashlib').sha512(entry.encode()).hexdigest()
            with open(f"logs/{today}.will", "w") as f:
                f.write(f"Original:\n{entry}\n\nEncrypted:\n{hash_will}")
            messagebox.showinfo("Saved", "✅ Will saved and encrypted.")
            top.destroy()
        else:
            messagebox.showwarning("Empty", "Please write your Will.")

    top = tk.Toplevel(root)
    top.title("Write Your Will")
    entry_box = tk.Text(top, height=10, width=40)
    entry_box.pack(padx=10, pady=10)
    tk.Button(top, text="Save Will", command=save_will).pack(pady=5)

def open_unistore():
    messagebox.showinfo("UniStore", "🛍 App Install: Open CLI and run 'unistore' to install truth apps.")

def open_logs():
    logs_path = os.path.abspath("logs")
    os.startfile(logs_path)

def backup_logs():
    backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(backup_name, 'w') as zipf:
        for file in os.listdir("logs"):
            zipf.write(os.path.join("logs", file))
    messagebox.showinfo("Backup Done", f"✅ Backup created: {backup_name}")

def lock_screen():
    lock = tk.Toplevel(root)
    lock.title("🔐 UniVerse Lock Screen")
    lock.geometry("300x120")

    def check_key():
        attempt = key_input.get()
        if attempt == MASTERKEY:
            lock.destroy()
            messagebox.showinfo("Unlocked", "✅ Welcome back.")
        else:
            messagebox.showerror("Wrong", "❌ Access Denied.")

    tk.Label(lock, text="Enter MasterKey to unlock:").pack(pady=5)
    key_input = tk.Entry(lock, show="*", width=25)
    key_input.pack(pady=5)
    tk.Button(lock, text="Unlock", command=check_key).pack(pady=5)

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
    messagebox.showinfo("XP Boosted", f"✅ XP: {xp}\nCoins: {coins}")

def open_unibot():
    try:
        subprocess.run(["python", "unibot.py"])
    except:
        messagebox.showerror("Error", "❌ UniBot file not found.")

# 🌟 BUILD GUI
root = tk.Tk()
root.title("UniVerseShell GUI")
root.geometry("330x460")

tk.Label(root, text="💠 UniVerse GUI Desktop", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="👁‍🗨 Show Welcome", width=25, command=show_welcome).pack(pady=5)
tk.Button(root, text="📖 Log Your Will", width=25, command=open_will_log).pack(pady=5)
tk.Button(root, text="💰 Open Wallet", width=25, command=open_wallet).pack(pady=5)
tk.Button(root, text="🛍 Go to UniStore", width=25, command=open_unistore).pack(pady=5)
tk.Button(root, text="🤖 Launch UniBot", width=25, command=open_unibot).pack(pady=5)
tk.Button(root, text="🕓 Boost XP", width=25, command=boost_xp).pack(pady=5)
tk.Button(root, text="📂 Open Logs Folder", width=25, command=open_logs).pack(pady=5)
tk.Button(root, text="💾 Backup Logs", width=25, command=backup_logs).pack(pady=5)
tk.Button(root, text="🔒 Lock Screen", width=25, command=lock_screen).pack(pady=5)
tk.Button(root, text="❌ Quit", width=25, command=root.destroy).pack(pady=20)

root.mainloop()
