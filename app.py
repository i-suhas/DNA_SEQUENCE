from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)

def create_substitution_map(key):
    """Generates a substitution map for encryption using the provided key."""
    valid_chars = set(string.ascii_uppercase + string.digits + string.punctuation)
    if not all(char in valid_chars for char in key):
        raise ValueError("Invalid key. Key can only contain uppercase letters, digits, and punctuation symbols.")

    shuffled_chars = secrets.choice(key) + ''.join(secrets.choice(key) for _ in range(len(key) - 1))
    substitution_map = {}
    for i in range(len(key)):
        substitution_map[key[i]] = shuffled_chars[i]
    return substitution_map

def encrypt_dna(sequence, key_map):
    """Encrypts DNA sequence using a substitution cipher."""
    encrypted_sequence = ""
    for nucleotide in sequence:
        encrypted_sequence += key_map[nucleotide]
    return encrypted_sequence

def decrypt_dna(sequence, key_map):
    """Decrypts DNA sequence using the inverse substitution map."""
    inverse_map = {v: k for k, v in key_map.items()}
    decrypted_sequence = ""
    for symbol in sequence:
        decrypted_sequence += inverse_map[symbol]
    return decrypted_sequence

def validate_dna_sequence(sequence):
    """Checks if the input sequence contains only valid DNA characters."""
    valid_nucleotides = set("ACGT")
    return all(nucleotide in valid_nucleotides for nucleotide in sequence)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sequence = request.form['sequence'].upper()
        key = request.form['key'].upper()

        if not validate_dna_sequence(sequence):
            return render_template('index.html', error='Invalid DNA sequence. Please enter only A, C, G, or T characters.')

        if len(key) != 4:
            return render_template('index.html', error='Invalid key. Please enter 4 characters.')

        substitution_map = create_substitution_map(key)
        encrypted_sequence = encrypt_dna(sequence, substitution_map)
        decrypted_sequence = decrypt_dna(encrypted_sequence, substitution_map)

        return render_template('index.html', sequence=sequence, key=key,
                               encrypted_sequence=encrypted_sequence, decrypted_sequence=decrypted_sequence)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
