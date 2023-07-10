# Password-Generator
Password Generator
This is a simple password generator implemented in Python using the tkinter library for creating a graphical user interface (GUI). It allows users to generate random passwords based on their desired length and character conditions.

Installation
To use this password generator, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can run the script directly.

Usage
Run the script password_generator.py using Python.
A GUI window titled "Password Generator" will open.
Enter the desired password length in the "Password Length" field.
Check the character conditions you want for your password:
"lowercase": Include lowercase letters (a-z).
"uppercase": Include uppercase letters (A-Z).
"digits": Include digits (0-9).
"punctuation": Include punctuation marks.
Click the "Generate Password" button.
The generated password will be displayed in the label below.
How It Works
The password generator uses the secrets module from the Python standard library to generate cryptographically strong random numbers. The string module provides sets of characters that can be used to form passwords.

The PasswordGenerator class contains two static methods:

gen_sequence(conditions): This method takes a list of conditions and generates a string sequence based on the selected conditions. Each condition corresponds to a set of characters: lowercase letters, uppercase letters, digits, or punctuation marks. The method concatenates the selected character sets to form the sequence.

gen_password(sequence, passlength=8): This method takes a sequence of characters and an optional password length (default is 8). It generates a password by randomly selecting characters from the sequence and joining them together.

The Interface class handles the GUI part of the application using the tkinter library. It creates a window with the title "Password Generator" and includes the following components:

"Password Length" label: Displays a label to indicate the purpose of the adjacent text entry field.
Length entry field: Allows the user to input the desired length of the password.
"Generate Password" button: Triggers the generation of a new password based on the entered length and selected character conditions.
"Characters" label frame: Contains checkboxes for each character condition (lowercase, uppercase, digits, and punctuation).
Password label: Displays the generated password.
When the user clicks the "Generate Password" button, the generate_password method is called. It retrieves the entered length, validates it, retrieves the selected character conditions, generates a sequence of characters based on the conditions, and finally generates a password using the PasswordGenerator class. The generated password is then displayed in the password label.

