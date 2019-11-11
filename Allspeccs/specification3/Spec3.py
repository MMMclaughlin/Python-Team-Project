from flask import Flask

app = Flask(__name__)

file = open("H:\Desktop\practical-3\Allspeccs\specification2\Spec2.txt", "rt")


@app.route("/")
def home():
    return "hello"

@app.route("/spec1")
def home1():
    string = " "
    for line in file:
        string = string+line+"<br/>"
        print(string)
    return string

@app.route("/spec2")
def home2():
    string = " "
    for line in file:
        string = string + line + "<br/>"
        print(string)
    return string

@app.route("/spec4")
def home3():
    return "spec4"

if __name__ == "__main__":
    app.run(debug=True)


