from src.caption_generator import generate_captions

def test_generate_captions():
    captions = generate_captions("data/sample.jpg", num_captions=2)
    assert isinstance(captions, list)
    assert len(captions) > 0
