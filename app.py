from flask import Flask, request, redirect
import gradio as gr

# اینجا تابع Gradio خود را تعریف کنید
def greet(name):
    return f"Hello {name}!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# Flask application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return iface.launch()

if __name__ == "__main__":
    app.run(port=7860)  # تغییر دهید به پورت مورد نظر
