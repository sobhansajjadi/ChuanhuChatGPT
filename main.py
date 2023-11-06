import os
import subprocess


def start():
    print("start...")

    #subprocess.run(["python", "ChuanhuChatbot.py"])
    #subprocess.run(["python", "app.py"])
    os.system('python3 ChuanhuChatbot.py')
    print("nice ♥")

if __name__ == "__main__":
    start()
