class Crypto:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str, key: str) -> str:
        ciphertext = plaintext
        for round in range(10):
            # Step 1: Substitution
            ciphertext = ''.join([self.substitute(c, round) for c in ciphertext])
            # Step 2: Bit shifting
            ciphertext = self.bit_shift(ciphertext, round)
            # Step 3: XOR with the key
            ciphertext = self.XOR_with_key(ciphertext, key)
            # Step 4: Substitution part 2
            ciphertext = ''.join([self.substitute(c, round) for c in ciphertext])
        return ciphertext

    def decrypt(self, ciphertext: str, key: str) -> str:
        plaintext = ciphertext
        for round in range(9, -1, -1):
            # Step 1: Reverse substitution
            plaintext = ''.join([self.reverse_substitute(c, round) for c in plaintext])
            # Step 2: XOR with the key
            plaintext = self.XOR_with_key(plaintext, key)
            # Step 3: Reverse bit shifting
            plaintext = self.reverse_bit_shift(plaintext, round)
            # Step 4: Reverse substitution part 2
            plaintext = ''.join([self.reverse_substitute(c, round) for c in plaintext])
        return plaintext

    def substitute(self, c: str, round: int) -> str:
        # Simple XOR substitution using round number
        return chr(ord(c) ^ (round + 1))

    def reverse_substitute(self, c: str, round: int) -> str:
        return chr(ord(c) ^ (round + 1))

    def bit_shift(self, input_text: str, round: int) -> str:
        shift = round % 8
        return ''.join([chr((ord(c) << shift) & 0xFF | (ord(c) >> (8 - shift))) for c in input_text])

    def reverse_bit_shift(self, input_text: str, round: int) -> str:
        shift = round % 8
        return ''.join([chr((ord(c) >> shift) | ((ord(c) << (8 - shift)) & 0xFF)) for c in input_text])

    def XOR_with_key(self, text: str, key: str) -> str:
        key_len = len(key)
        return ''.join([chr(ord(text[i]) ^ ord(key[i % key_len])) for i in range(len(text))])
