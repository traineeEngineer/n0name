import pymupdf
import sys
import os

def extract_paragraphs(pdf_path):
    doc = pymupdf.open(pdf_path)
    paragraphs = []
    
    for page in doc:
        blocks = page.get_text('blocks')
        for block in blocks:
            if block[6] == 0:
                text = block[4].strip()
                if text:
                    paragraphs.append(text)
    
    doc.close()
    return paragraphs

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    results = extract_paragraphs(pdf_path)
    print(f"Total Paragraphs: {len(results)}")
    for i, para in enumerate(results, 1):
        print(f"\n--- Paragraph {i} ---")
        print(para)
