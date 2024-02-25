import random

def build_markov_model(text):
    words = text.split()
    model = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in model:
            model[current_word] = []

        model[current_word].append(next_word)

    return model

def generate_text(markov_model, seed_word, length=50):
    generated_text = []
    current_word = seed_word

    for _ in range(length):
        generated_text.append(current_word)

        if current_word in markov_model:
            next_word = random.choice(markov_model[current_word])
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)
input_text = "The quick brown fox jumps over the lazy dog."
model = build_markov_model(input_text)
generated_text = generate_text(model, seed_word="quick", length=20)
print("Input Text:")
print(input_text)
print("\nGenerated Text:")
print(generated_text)
