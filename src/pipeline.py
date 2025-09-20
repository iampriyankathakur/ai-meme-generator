import argparse
from caption_generator import generate_captions
from meme_maker import make_meme

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to input image")
    args = parser.parse_args()

    captions = generate_captions(args.image)
    meme_path = make_meme(args.image, captions)

    print(f"✅ Meme created at {meme_path}")
