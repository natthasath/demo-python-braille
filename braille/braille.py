class BrailleTranslator:
    def __init__(self):
        self.braille_map = {
            'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
            'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
            'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
            'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
            'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
            'z': '⠵', '0': '⠚⠋', '1': '⠁', '2': '⠃', '3': '⠉',
            '4': '⠙', '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓',
            '9': '⠊', ' ': ' '
        }

    def braille_to_text(self, braille):
        text = ''
        for i in range(0, len(braille)):
            if braille[i] in self.braille_map.values():
                text += list(self.braille_map.keys())[list(self.braille_map.values()).index(braille[i])]
            else:
                text += braille[i]
        return text
    
    def text_to_braille(self, text):
        braille = ''
        for c in text:
            if c.lower() in self.braille_map:
                braille += self.braille_map[c.lower()]
            else:
                braille += c
        return braille
