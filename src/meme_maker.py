from PIL import Image, ImageDraw, ImageFont

def make_meme(image_path, captions, output_path="assets/meme_output.jpg"):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Load default font
    font = ImageFont.load_default()

    # Top caption
    draw.text((10, 10), captions[0].upper(), fill="white", font=font, stroke_width=2, stroke_fill="black")

    # Bottom caption (if exists)
    if len(captions) > 1:
        w, h = img.size
        draw.text((10, h-30), captions[1].upper(), fill="white", font=font, stroke_width=2, stroke_fill="black")

    img.save(output_path)
    return output_path
