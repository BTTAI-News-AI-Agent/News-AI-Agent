from .t5_model import t5_summarize
from .chunking import chunk_text

def generate_summary(text):
    words = text.split()
    length = len(words)

    # short input
    if length < 50:
        return t5_summarize(
            text,
            max_len=60,
            min_len=10,
            beams=2
        )
    
    # medium input
    if length < 300:
        return t5_summarize(
            text,
            max_len=150,
            min_len=40,
            beams=4
        )

    # Long input --> chunking + summarization + combining
    chunks = chunk_text(text, max_words=200)
    chunk_summaries = [
        t5_summarize(chunk, max_len=120, min_len=30, beams=4)
        for chunk in chunks
    ]

    # Combine summaries using T5
    combined = " ".join(chunk_summaries)
    final = t5_summarize(
        combined,
        max_len=200,
        min_len=50,
        beams=4
    )

    return final