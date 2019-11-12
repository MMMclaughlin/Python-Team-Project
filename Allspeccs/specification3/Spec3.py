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
    string = "<h1>This is the code behind the solutions to project 3</h1>"
    link1 = "<a href=/spec1><font color='red'>Spec1</font></a>"
    link1 = "<font size=+2>" +link1 +"</font>"
    link2 = "<a href=/spec2><font color='green'>Spec2</font></a>"
    link3 = "<a href=/spec4><font color='blue'>Spec4</font></a>"
    return string+"<h2>"+link1 + "<br/>" + link2 + "<br/>" + link3+"</h2>"

@app.route("/spec1")
def home1():
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification1\Spec1.py"
    string="<font size=+10>This is spec 1, this meets the following objectives:</font><br/>" \
           "<strong><font color=blue>Read in a .txt file and parse the content.<br/>" \
           "Perform a frequency analysis of the characters and words in the text file.<br/>" \
           "Output the frequency of the most occurring words in the text file to a CSV file.</br>" \
           "Present your frequency analysis of the characters visually using the Matplotlib plotting library.</br>" \
           "Produce a Markdown file in your repository directory that combines your findings in one place.</strong></font>" \
            "<br/><br/><br/><br/>"
    return Codewriter((textfileopener(location)),string)

@app.route("/spec2")
def home2():
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification2\Spec2.py"
    string="<font size=+10>This is spec 2, this meets the following objectives:</font><br/>" \
           "<strong><font color=blue>Read in image files and store them in an appropriate collection ready for modification.<br/>" \
           "Convert the images to thumbnails and name the new files appropriately.<br/>" \
           "Apply various filters to the images using the ImageFilter module.<br/>" \
           "Modify the RGB values of images to produce a new filter.<br/>" \
           "Experiment with the Pillow library and its modules and save what you have produced.</strong></font>" \
            "<br/><br/><br/><br/>"

    return Codewriter((textfileopener(location)),string)

@app.route("/spec4")
def home3():
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification4\Spec4.py"
    string="<font size=+10>This is spec 4, this meets the following objectives:</font><br/>" \
           "<strong><font color=blue>Investigate Python libraries to focus your solution around.<br/>" \
           "Plan your solution before development.</br>" \
            "Develop your program solution.<br/>" \
            "Test your program.</strong></font>" \
            "<br/><br/><br/><br/>"
    return Codewriter((textfileopener(location)), string)
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
