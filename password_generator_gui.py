import string as str
import secrets
import random
import tkinter as tk
from tkinter import messagebox


class PasswordGenerator:
    @staticmethod
    def gen_sequence(conditions):
        possible_characters = [
            str.ascii_lowercase,
            str.ascii_uppercase,
            str.digits,
            str.punctuation,
        ]
        sequence = ""
        for x in range(len(conditions)):
            if conditions[x]:
                sequence += possible_characters[x]
        return sequence

    @staticmethod
    def gen_password(sequence, passlength=8):
        password = "".join((secrets.choice(sequence) for i in range(passlength)))
        return password


class Interface:
    def __init__(self, root):
        self.root = root
        self.has_characters = {
            "lowercase": tk.BooleanVar(),
            "uppercase": tk.BooleanVar(),
            "digits": tk.BooleanVar(),
            "punctuation": tk.BooleanVar(),
        }
        self.password_text = tk.StringVar()
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("Password Generator")

        label = tk.Label(self.root, text="Password Length:")
        label.pack()

        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        generate_button = tk.Button(
            self.root, text="Generate Password", command=self.generate_password
        )
        generate_button.pack()

        characters_frame = tk.LabelFrame(self.root, text="Characters")
        characters_frame.pack()

        for key, value in self.has_characters.items():
            checkbox = tk.Checkbutton(
                characters_frame,
                text=key,
                variable=value,
                onvalue=True,
                offvalue=False,
            )
            checkbox.pack(anchor="w")

        password_label = tk.Label(self.root, textvariable=self.password_text)
        password_label.pack()

    def generate_password(self):
        length = self.length_entry.get()
        try:
            length = int(length)
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")
            return

        conditions = [value.get() for value in self.has_characters.values()]
        sequence = PasswordGenerator.gen_sequence(conditions)
        password = PasswordGenerator.gen_password(sequence, length)

        self.password_text.set(password)


if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
