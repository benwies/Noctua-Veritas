def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 2 if key == 25 else 5
            shifted_char = chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift) % 26) + 97)
            encrypted_text += shifted_char
            key = 2 if key == 25 else 25
        else:
            encrypted_text += char
    return encrypted_text

def main():
    text = """The Theory of the Matrix unveils a conceptual landscape where reality blurs with illusion, where the fabric of existence is woven from lines of code and binary digits. It is a philosophical labyrinth that challenges the very essence of what it means to perceive, to understand, and to be.
In this digital tapestry, the Matrix emerges as a construct—a simulated reality meticulously crafted to deceive the senses and ensnare the mind. Within its confines, humans are but unwitting participants, their consciousness tethered to a collective illusion, while their bodies lie dormant in the realm of the real.
Yet, beyond the veil of the Matrix lies a deeper truth—a truth obscured by layers of deception and obfuscation. It is the realization that reality itself is but a construct, a product of perception and interpretation, shaped by the interplay of mind and matter.
As the theory unfolds, it beckons us to question the nature of existence, to probe the boundaries of consciousness, and to confront the possibility that our reality may be nothing more than an elaborate illusion. It challenges us to look beyond the confines of our perceived reality and to glimpse the infinite possibilities that lie beyond.
But the Theory of the Matrix is more than mere speculation; it is a reflection of our deepest fears and desires, our yearning for truth in a world of deception and uncertainty. It invites us to embrace the unknown, to venture into the depths of the unknown, and to seek answers to the fundamental questions that have plagued humanity since time immemorial.
In the end, the Theory of the Matrix is a journey—a journey into the unknown, into the depths of consciousness, and into the very heart of existence itself. It is a quest for truth, for understanding, and for enlightenment in a world shrouded in mystery and illusion.
The Theory of the Matrix unveils a conceptual landscape where reality blurs with illusion, where the fabric of existence is woven from lines of code and binary digits. It is a philosophical labyrinth that challenges the very essence of what it means to perceive, to understand, and to be.
In this digital tapestry, the Matrix emerges as a construct—a simulated reality meticulously crafted to deceive the senses and ensnare the mind. Within its confines, humans are but unwitting participants, their consciousness tethered to a collective illusion, while their bodies lie dormant in the realm of the real.
Yet, beyond the veil of the Matrix lies a deeper truth—a truth obscured by layers of deception and obfuscation. It is the realization that reality itself is but a construct, a product of perception and interpretation, shaped by the interplay of mind and matter.
As the theory unfolds, it beckons us to question the nature of existence, to probe the boundaries of consciousness, and to confront the possibility that our reality may be nothing more than an elaborate illusion. It challenges us to look beyond the confines of our perceived reality and to glimpse the infinite possibilities that lie beyond.
But the Theory of the Matrix is more than mere speculation; it is a reflection of our deepest fears and desires, our yearning for truth in a world of deception and uncertainty. It invites us to embrace the unknown, to venture into the depths of the unknown, and to seek answers to the fundamental questions that have plagued humanity since time immemorial.
In the end, the Theory of the Matrix is a journey—a journey into the unknown, into the depths of consciousness, and into the very heart of existence itself. It is a quest for truth, for understanding, and for enlightenment in a world shrouded in mystery and illusion."""
    encrypted_text = caesar_cipher(text, 25)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
