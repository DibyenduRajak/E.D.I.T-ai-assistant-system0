import requests, subprocess

def run_code(task):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "codellama",
        "prompt": f"Give ONLY command: {task}",
        "stream": False
    })

    cmd = res.json()["response"].strip()

    try:
        out = subprocess.check_output(cmd, shell=True).decode()
    except:
        out = "Failed"

    return f"{cmd}\n{out}"
