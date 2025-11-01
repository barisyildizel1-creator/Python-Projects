# Morse Code Translator

A simple Python program that can encrypt text to Morse code and decrypt Morse code back to text.

## Features

- **Text to Morse Code**: Convert any text message to Morse code
- **Morse Code to Text**: Decode Morse code back to readable text
- **Support for**: Letters (A-Z), numbers (0-9), and common punctuation marks
- **Error handling**: Warns about unsupported characters

## How to Use

1. Run the program:
   ```bash
   python "Mors Code Translator.py"
   ```

2. Enter your message when prompted

3. Choose your operation:
   - Type `1` to encrypt text to Morse code
   - Type `2` to decrypt Morse code to text

## Supported Characters

- **Letters**: A-Z (case insensitive)
- **Numbers**: 0-9
- **Punctuation**: Comma (,), Period (.), Question mark (?), Slash (/), Hyphen (-), Parentheses ()

## Example Usage

### Encryption (Text to Morse Code)
```
Enter the message: Hello World
Type '1' to encrypt or '2' to decrypt: 1
Encrypted message: .... . .-.. .-.. ---   .-- --- .-. .-.. -.. 
```

### Decryption (Morse Code to Text)
```
Enter the message: .... . .-.. .-.. ---   .-- --- .-. .-.. -.. 
Type '1' to encrypt or '2' to decrypt: 2
Decrypted message: HELLO WORLD
```

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/morse-code-translator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd morse-code-translator
   ```

3. Run the program:
   ```bash
   python "Mors Code Translator.py"
   ```

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the [MIT License](LICENSE).