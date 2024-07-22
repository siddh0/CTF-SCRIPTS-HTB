def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def decrypt(c):
    m = ''
    for i in range(len(c)):
        ch = c[i]
        if not ch.isalpha():
            dch = ch
        else:
            cci = to_identity_map(ch)
            dch = from_identity_map(cci - i)
        m += dch
    return m

# Get the encrypted text as user input
encrypted_text = input("Enter the encrypted text: ").strip()

# Decrypt the text
decrypted_text = decrypt(encrypted_text)

# Print the decrypted text
print("Decrypted text:", decrypted_text)
