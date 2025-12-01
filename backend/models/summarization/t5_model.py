from transformers import T5Tokenizer, T5ForConditionalGeneration

# MODEL_NAME = "t5-base"
MODEL_NAME = "google/flan-t5-small"

tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

def t5_summarize(
    text,
    max_len=120,
    min_len=30,
    beams=4
):
    input_text = "summarize:\n" + text
    inputs = tokenizer.encode(
        input_text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    summary_ids = model.generate(
        inputs,
        max_length=max_len,
        min_length=min_len,
        num_beams=beams,
        repetition_penalty=2.5,
        length_penalty=1.2,
        early_stopping=True,
        no_repeat_ngram_size=2
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return clean_summary(summary)
    
def clean_summary(text):
    import re
    # Remove spaces before punctuation
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)
    # Capitalize
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip().capitalize() for s in sentences if s.strip()]
    text = " ".join(sentences)
    return text
