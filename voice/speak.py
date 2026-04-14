import subprocess

def speak(text):
    with open("speech.txt","w") as f:
        f.write(text)

    subprocess.run(
        "piper --model en_US-lessac-medium.onnx --output_file out.wav < speech.txt",
        shell=True
    )

    subprocess.run("start out.wav", shell=True)
