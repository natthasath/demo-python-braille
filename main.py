from braille.braille import BrailleTranslator

translator = BrailleTranslator()

# Example usage
text = 'hello world'
braille = translator.text_to_braille(text)
print(braille)
# Output: ⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙

text_back = translator.braille_to_text(braille)
print(text_back)
# Output: hello world