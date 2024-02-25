# Markov Chain Text Composer 

This project implements a simple Markov Chain Text Composer in Python. The code analyzes a given text and generates new text based on a first-order Markov chain model.

## Usage

1. **Clone the Repository:**

    ```bash
      https://github.com/anushasundark/Python_Mini_Projects/new/main/12.%20Markov%20Chain%20Text%20Composer
    
    ```

2. **Run the Script:**

    Open the Python script (`markov_chain_text.py`) in your preferred editor and replace the `input_text` variable with your own text.

    ```bash
    python markov_chain_text.py
    ```

3. **Adjust Parameters:**

    - Modify the `seed_word` and `length` parameters in the script to control the generated text.
    - Experiment with different input texts for varied results.

## Files

- `markov_chain_text.py`: The main Python script implementing the Markov Chain Text Composer.
- `Readme.md`: Project documentation.

## Example Usage

```python
input_text = "The quick brown fox jumps over the lazy dog."
model = build_markov_model(input_text)
generated_text = generate_text(model, seed_word="quick", length=20)

print("Input Text:")
print(input_text)
print("\nGenerated Text:")
print(generated_text)
