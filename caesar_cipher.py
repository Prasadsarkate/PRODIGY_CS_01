def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.
    
    Args:
        text (str): The input message
        shift (int): The shift value (0-25)
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The resulting encrypted or decrypted text
    """
    if mode == 'decrypt':
        shift = -shift

    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(result)


def get_shift_value():
    """Prompt user for a valid shift value."""
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("⚠  Shift value must be between 0 and 25. Try again.")
        except ValueError:
            print("⚠  Invalid input. Please enter an integer.")


def main():
    print("=" * 45)
    print("        🔐 Caesar Cipher Program")
    print("=" * 45)

    while True:
        print("\nOptions:")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = get_shift_value()
            encrypted = caesar_cipher(message, shift, mode='encrypt')
            print(f"\n✅ Encrypted Message: {encrypted}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = get_shift_value()
            decrypted = caesar_cipher(message, shift, mode='decrypt')
            print(f"\n✅ Decrypted Message: {decrypted}")

        elif choice == '3':
            print("\nGoodbye! 👋")
            break

        else:
            print("⚠  Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
