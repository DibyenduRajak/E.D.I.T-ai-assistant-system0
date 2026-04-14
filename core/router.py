from models.chat_model import run_chat
from models.code_model import run_code
from models.image_model import generate_image
from models.summarizer import summarize
from tools.web_search import search_web

def route(decision):
    task = decision["task"]

    if decision["target_model"] == "code":
        return run_code(task)

    elif decision["target_model"] == "image":
        return generate_image(task)

    elif decision["target_model"] == "web":
        results = search_web(task)
        combined = "\n".join([r["body"] for r in results])
        return summarize(combined)

    else:
        return run_chat(task)
