from transformers import pipeline

def generate_captions(image_path, num_captions=2):
    captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    captions = captioner(image_path)
    base_caption = captions[0]['generated_text']

    # Add humor twists
    funny_captions = [
        f"When you realize {base_caption.lower()}",
        f"POV: {base_caption.lower()}",
    ]
    return funny_captions[:num_captions]
