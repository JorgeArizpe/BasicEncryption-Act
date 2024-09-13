### Rundown of the Algorithm

This encryption algorithm is a **symmetric block cipher** with basic cryptographic operations designed for educational purposes. It uses a sequence of transformations (substitution, bit shifting, and XOR) applied over multiple rounds (10 rounds) to achieve security characteristics like **confusion** and **diffusion**. Here's a breakdown:

---

### 1. **Symmetric Encryption**:
   - **Symmetric** means the same key is used for both encryption and decryption.
   - A key (up to 16 characters) is provided by the user and is used throughout the algorithm for encryption and decryption.

---

### 2. **Steps in Each Round**:
   The algorithm works on blocks of text (character by character). It performs three operations in each of the 10 rounds during encryption and then reverses them during decryption.

#### **Encryption**:
1. **Substitution**:
   - Every character in the plaintext is modified using an **XOR** operation combined with the current round number.
   - This step ensures **confusion**, making the relationship between the key and the ciphertext more complex.

   Example:
   ```python
   c = chr(ord(c) ^ (round + 1))
   ```

2. **Bit Shifting**:
   - The algorithm shifts the bits of each character left or right by an amount depending on the round number.
   - This introduces **diffusion**, spreading the influence of each bit across multiple characters in the output.

   Example:
   ```python
   shift = round % 8
   c = (c << shift) | (c >> (8 - shift))
   ```

3. **XOR with Key**:
   - After substitution and bit shifting, the characters are XOR-ed with the key.
   - This step further mixes the input with the key to obscure the original message.

   Example:
   ```python
   output[i] = text[i] ^ key[i % key_len]
   ```

---

#### **Decryption**:
   - The decryption process reverses the encryption step-by-step.
   - It starts by XOR-ing with the key, then reverses the bit shifting, and finally undoes the substitution using the same XOR operation as in encryption.

1. **XOR with Key** (reversed order):
   - XOR the ciphertext with the same key to reverse the XOR operation.

2. **Reverse Bit Shifting**:
   - Shift the bits back in the opposite direction to restore the original order.

3. **Reverse Substitution**:
   - XOR each character with the round number, just like in the encryption phase, to get back the original character.

---

### 3. **Rounds**:
   - The algorithm runs the **encryption operations** for **10 rounds**, which increases its complexity and security.
   - During **decryption**, the rounds are processed in reverse order to ensure the ciphertext is correctly transformed back into plaintext.

---

### 4. **Key Elements**:

- **Confusion**:
   - Achieved by **substitution** and **XOR** operations, making it hard to see how the input relates to the output, especially in combination with the key.

- **Diffusion**:
   - Ensured by **bit shifting** and **transposition**, which spread the impact of a single bit across many bits in the output, so small changes in the plaintext lead to big changes in the ciphertext.
