from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def shift_character(char, shift):
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        return chr(start + (ord(char) - start + shift) % 26)
    return char

def encrypt_text(text, shift):
    return ''.join(shift_character(c, shift) for c in text)

def decrypt_text(text, shift):
    return encrypt_text(text, -shift)

def sanitize_text(text):
    return ''.join(c for c in text if c.isalnum() or c.isspace())

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        shift = request.form.get("shift")

        # Validasi input
        if not text or not shift:
            flash("Please provide both text and shift values.")
            return redirect(url_for("index"))

        try:
            shift = int(shift)
        except ValueError:
            flash("Shift must be an integer.")
            return redirect(url_for("index"))

        sanitized_text = sanitize_text(text)
        encrypted_text = encrypt_text(sanitized_text, shift)
        decrypted_text = decrypt_text(encrypted_text, shift)

        return render_template(
            "index.html", 
            original_text=text, 
            sanitized_text=sanitized_text,
            encrypted_text=encrypted_text, 
            decrypted_text=decrypted_text,
            shift=shift
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
