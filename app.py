import gradio as gr
import time
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
)
def test(x):
    time.sleep(4)
    print(x)
    return x
print("x")

gr.Interface(test, "textbox", "textbox").queue().launch()