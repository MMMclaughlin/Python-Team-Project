from flask import Flask

app = Flask(__name__)
location="H:\csc1034-team-project\practical-3\Allspeccs\specification2\Spec2.py"#these are strings of the location
file = open("H:\csc1034-team-project\practical-3\Allspeccs\specification2\Spec2.py", "r")#this is the python file
textfile = open(location+".txt","w")#this will be the text version of the python file
for line in file:#rewrite everyline
    textfile.write(line +"\n")#write them with a \n so that each line is on a new line
textfile.close()
textfile=open(location+".txt","r")
@app.route("/")
def home():
    return "hello"

@app.route("/spec1")
def home1():
    print("this is spec1")
    string = " "
    for line in textfile:
        print(line)
        if '"""' in line:
            line= "<font color='red'>" +line +"</font>"
        if "def" in line:
            line = "<strong>" +line +"</strong>"
            line = "<font color='purple'>" + line + "</font>"
        string = "<pre>" + string + line + "<br/>" +"</pre>"
    return string

@app.route("/spec2")
def home2():
    string = " "
    for line in file:
        string = "<pre>"+ string + line + "<br/>"+"<pre>"
        print(string)
    return string

@app.route("/spec4")
def home3():
    return "spec4"

if __name__ == "__main__":
    app.run(debug=True)


