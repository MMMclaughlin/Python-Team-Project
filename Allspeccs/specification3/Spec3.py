from flask import Flask

app = Flask(__name__)
location="H:\Desktop\practical-3\Allspeccs\specification2\Spec2.py"#these are strings of the location
file = open(location, "r")#this is the python file
textfile = open(location+".txt","w")#this will be the text version of the python file
for line in file:#rewrite everyline
    textfile.write(line +"\n")#write them with a \n so that each line is on a new line
textfile.close()
textfile=open(location+".txt","r")
@app.route("/")
def home():
    link1 = "<a href=/spec1><font color='red'>Spec1</font></a>"
    link2 = "<a href=/spec2><font color='green'>Spec2</font></a>"
    link3 = "<a href=/spec4><font color='blue'>Spec4</font></a>"
    return link1 + "<br/>" + link2 + "<br/>" + link3

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
