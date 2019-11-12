from flask import Flask
import os
app = Flask(__name__)
def textfileopener(location):
    file=open(location,"r")
    textfile = open(location+".txt","w")#this will be the text version of the python file
    for line in file:#rewrite everyline
        textfile.write(line +"\n")#write them with a \n so that each line is on a new line
    textfile.close()
    textfile=open(location+".txt","r")
    return textfile
@app.route("/")
def home():#
    string = "<h1>This is the code behind the solutions</h1>"
    link1 = "<a href=/spec1><font color='red'>Spec1</font></a>"
    link1 = "<font size=+2>" +link1 +"</font>"
    link2 = "<a href=/spec2><font color='green'>Spec2</font></a>"
    link3 = "<a href=/spec4><font color='blue'>Spec4</font></a>"
    return string+"<h2>"+link1 + "<br/>" + link2 + "<br/>" + link3+"</h2>"

@app.route("/spec1")
def home1():
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification1\Spec1.py"
    string="this is spec 1 and we will look through the text for the most common words and letters"
    return Codewriter((textfileopener(location)),string)

@app.route("/spec2")
def home2():
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification2\Spec2.py"
    return Codewriter((textfileopener(location)),"test")

@app.route("/spec4")
def home3():
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification4\Spec4.py"
    return Codewriter((textfileopener(location)),"test")
def Codewriter(file,string):
    print("this is spec1")
    for line in file:
        print(line)
        if '"""' in line:
            line= "<font color='red'>" +line +"</font>"
        if "def" in line:
            line = "<strong>" +line +"</strong>"
            line = "<font color='purple'>" + line + "</font>"
        string = "<pre>" + string + line + "<br/>" +"</pre>"
    return string


if __name__ == "__main__":
    app.run(debug=True)
