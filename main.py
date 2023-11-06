import os

def get_system_info():
    print(f"Operating System: {os.name}")
    print(f"Current Working Directory: {os.getcwd()}")

def get_python_version():
    print(f"Python Version: {os.popen('python --version').read()}")

def get_node_version():
    print(f"Node.js Version: {os.popen('node -v').read()}")
    os.system('python app.py')
    print("nice♥")
    #os.system('python app.py')


if __name__ == "__main__":
    get_system_info()
    get_python_version()
    get_node_version()
