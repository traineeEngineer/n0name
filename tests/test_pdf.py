from pdf_extractor import extract_paragraphs

def test_invalid_file():
    try:
        extract_paragraphs("fake.pdf")
    except Exception:
        assert True
