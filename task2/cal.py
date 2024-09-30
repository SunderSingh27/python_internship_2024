from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
            else:
                result = 'Invalid operation'
        except Exception as e:
            result = f'Error: {e}'
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Simple Calculator</title>
          </head>
          <body>
            <h1>Simple Calculator</h1>
            <form method="post">
              <label for="num1">Number 1:</label>
              <input type="text" id="num1" name="num1" required><br><br>
              <label for="num2">Number 2:</label>
              <input type="text" id="num2" name="num2" required><br><br>
              <label for="operation">Operation:</label>
              <select id="operation" name="operation" required>
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
              </select><br><br>
              <input type="submit" value="Calculate">
            </form>
            {% if result is not none %}
            <h2>Result: {{ result }}</h2>
            {% endif %}
          </body>
        </html>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)