from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", use_safetensors=True)


image = pipeline("An image of a squirrel in Picasso style").images[0]
