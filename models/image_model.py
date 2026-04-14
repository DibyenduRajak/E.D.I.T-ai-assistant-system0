from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt):
    img = pipe(prompt).images[0]
    path = "generated.png"
    img.save(path)
    return f"generated: {path}"
