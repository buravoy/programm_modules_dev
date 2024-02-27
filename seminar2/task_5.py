def get_clean_words(w):
    return [str(i).strip().lower() for i in w]


words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]
clean_words = get_clean_words(words)

print(clean_words)

