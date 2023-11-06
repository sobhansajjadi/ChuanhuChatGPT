import os
import platform
import subprocess

def get_system_info():
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"OS Release: {platform.release()}")
    print(f"Machine Type: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def get_python_version():
    python_version = platform.python_version()
    print(f"Python Version: {python_version}")

def get_node_version():
    node_version = subprocess.getoutput('node -v')
    print(f"Node.js Version: {node_version}")

def get_current_directory():
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}")

if __name__ == "__main__":
    get_system_info()
    get_python_version()
    get_node_version()
    get_current_directory()
