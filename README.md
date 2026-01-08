# Natural Language Processing | Model: Translate

NLP is a branch of Artificial Intelligence (AI) that gives computers the ability to understand, interpret, and generate human language.

## What kind of setup is used to build this?

    Dependencies:

    • Sacremoses — The preprocessing text before inserted into NLP model (Helsinki model)
        - pip install sacremoses
    • Sentencepiece — Tokenization, converting the human letter into numbers that computers can read. 
      Based from this log-clip <transformers.pipelines.text2text_generation.TranslationPipeline object at 0x000001CA66902CF0> this is the raw of translation before got translated. I got this log before installed sentencepiece.
        - pip install sentencepiece 
    • hf_xet — A dependency for faster and efficient for downloading huge AI models (like Deepseek, Qwen, Claude, etc.). Not necessary, it's just 7 lines   of code. 
        - pip install hf_xet
    • transformers — The primary module for importing pipeline library.
        - pip install transformers torch
    
    Misc.:
    • Python ver. 3.14.2
    • Model: Helsinki by University of Helsinki 

## Conclusion

    The conclusion of this mini project is, to experimenting and understanding NLP using local dependencies with Huggingface. 
