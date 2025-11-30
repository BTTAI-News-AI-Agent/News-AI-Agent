from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

def t5_summarize(
    text,
    max_len=120,
    min_len=30,
    beams=4
):
    input_text = "summarize: " + text
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
        length_penalty=1.2,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)