import os
import subprocess


def start():
    print("start...")

    subprocess.run(["python", "ChuanhuChatbot.py"])
    #subprocess.run(["python", "app.py"])
    print("nice ♥")
    #os.system('python app.py')


if __name__ == "__main__":
    start()
