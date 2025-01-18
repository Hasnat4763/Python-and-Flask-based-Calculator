from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/calculator", methods = ["POST"])
def calculator():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        if operation == "add":
            result = num1+num2
        elif operation == "substract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "to the power":
            result = num1 ** num2
        elif operation == "divide":
            result = num1 / num2
        else:
            result = "Invalid Operation"
        return render_template("index.html" , result=result)
    except ValueError:
        return render_template("index.html", result = "Invalid Input")
if __name__ == "__main__":
    app.run()
