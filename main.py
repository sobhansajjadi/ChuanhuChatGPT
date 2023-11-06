import os
import subprocess

def get_system_info():
    print(f"Operating System: {os.name}")

def get_python_version():
    print(f"Python Version: {os.popen('python --version').read()}")

def start():
    print("start...")

    subprocess.run(["python", "ChuanhuChatbot.py"])
    print("nice ♥")
    #os.system('python app.py')


if __name__ == "__main__":
    get_system_info()
    get_python_version()
    start()
