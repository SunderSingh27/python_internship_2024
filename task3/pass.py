from flask import Flask, request, render_template_string
import random
import string

app = Flask(__name__)

template = """
<html>
  <body>
    <h1>Password Generator</h1>
    <form action="/" method="post">
      <label for="length">Enter the desired length of the password:</label>
      <input type="number" id="length" name="length"><br><br>
      <input type="submit" value="Generate Password">
    </form>
    {% if password %}
      <p>Generated Password: {{ password }}</p>
    {% endif %}
  </body>
</html>
"""

def password_generator(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = int(request.form["length"])
        password = password_generator(length)
        return render_template_string(template, password=password)
    return render_template_string(template)

if __name__ == "__main__":
    app.run()
