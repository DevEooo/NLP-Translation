from transformers import pipeline

llm_model = "Helsinki-NLP/opus-mt-en-de" # Model: Helsinki, made by University of Helsinki
translatedObject = pipeline("translation_en_to_de", model=llm_model)
result = translatedObject("This is an experiment of NLP - Tranlate model with Huggingface by Herald")

print(result)

# Log Output:
    # Device set to use cpu
    # [{'translation_text': 'Dies ist ein Experiment von NLP - Tranlate Modell mit Huggingface von Herald'}]
