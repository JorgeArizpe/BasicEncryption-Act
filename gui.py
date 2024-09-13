import tkinter as tk
from tkinter import messagebox
from crypto import Crypto

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.crypto = Crypto()

        # Set up the window
        self.root.title("Symmetric Encryption")
        self.root.geometry("920x600")

        # Text input for plaintext/ciphertext
        self.input_label = tk.Label(root, text="Input Text:")
        self.input_label.pack()

        self.input_text = tk.Text(root, height=5)
        self.input_text.pack()

        # Key input
        self.key_label = tk.Label(root, text="Key:")
        self.key_label.pack()

        self.key_entry = tk.Entry(root)
        self.key_entry.pack()

        # Buttons for Encrypt and Decrypt
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack()

        # Output area for the result
        self.output_label = tk.Label(root, text="Output Text:")
        self.output_label.pack()

        self.output_text = tk.Text(root, height=5)
        self.output_text.pack()

    def encrypt_text(self):
        plaintext = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        if not plaintext or not key:
            messagebox.showwarning("Input Error", "Both text and key are required!")
            return
        elif len(key) > 16:
            messagebox.showwarning("Input Error", "Key cannot be longer than 16!")
            return
        elif len(plaintext) > 100:
            messagebox.showwarning("Input Error", "Text length cannot be over 100!")
            return

        # Encrypt the text
        encrypted_text = self.crypto.encrypt(plaintext, key)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        ciphertext = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        if not ciphertext or not key:
            messagebox.showwarning("Input Error", "Both text and key are required!")
            return
        elif len(key) > 16:
            messagebox.showwarning("Input Error", "Key cannot be longer than 16!")
            return
        elif len(ciphertext) > 100:
            messagebox.showwarning("Input Error", "Text length cannot be over 100!")
            return

        # Decrypt the text
        decrypted_text = self.crypto.decrypt(ciphertext, key)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decrypted_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
