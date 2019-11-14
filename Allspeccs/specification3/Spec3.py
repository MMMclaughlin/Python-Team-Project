from flask import Flask
import os
app = Flask(__name__)
def textfileopener(location):
    """This opens the python file, converts it to a .txt file"""
    file=open(location,"r")
    textfile = open(location+".txt","w")#this will be the text version of the python file
    for line in file:#rewrite everyline
        textfile.write(line +"\n")#write them with a \n so that each line is on a new line
    textfile.close()
    textfile=open(location+".txt","r")
    return textfile
@app.route("/")
def home():#
    """This is the function which is returned on the homepage"""
    string = "<h1>This is the code behind the solutions to project 3</h1>"
    link1 = "<a href=/spec1><font color='red'>Spec1</font></a>"
    link1 = "<font size=+2>" +link1 +"</font>"
    link2 = "<a href=/spec2><font color='green'>Spec2</font></a>"
    link3 = "<a href=/spec4><font color='blue'>Spec4</font></a>"
    return string+"<h2>"+link1 + "<br/>" + link2 + "<br/>" + link3+"</h2>"

@app.route("/spec1")
def home1():
    """This is the function which is returned on the spec 1 page"""
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification1\Spec1.py"
    string=r"<font size=+10>This is spec 1, this meets the following objectives:</font><br/>" \
           r"<strong><font color=blue>Read in a .txt file and parse the content.<br/>" \
            r"  -This is done using <font color=red>streamreader = open('text.txt', "r", encoding='utf-8')'</font><br/>" \
           r"Perform a frequency analysis of the characters and words in the text file.<br/>" \
            r"  -This is done using the code within the <font color=red>for line in streamreader:</font><br/>" \
           r"Output the frequency of the most occurring words in the text file to a CSV file.<br/>" \
            r"  -This is done using the code within <font color=red>if character == ' ' or character == '.'':</font><br/>" \
           r"Present your frequency analysis of the characters visually using the Matplotlib plotting library.</br>" \
            r"  -This is done using <font color=red> insert explanation here </font><br/>" \
           r"Produce a Markdown file in your repository directory that combines your findings in " \
           r"one place.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/><br/>" \
            r"</font></strong><br/><br/><br/><br/>"
    return Codewriter((textfileopener(location)),string)

@app.route("/spec2")
def home2():
    """This is the function which is returned on the spec 2 page"""
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification2\Spec2.py"
    string=r"<font size=+10>This is spec 2, this meets the following objectives:</font><br/>" \
           r"<strong><font color=blue>Read in image files and store them in an appropriate collection ready for" \
           r"modification.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/>" \
           r"Convert the images to thumbnails and name the new files appropriately.<br/>" \
            r"  -This is done using  <font color=red> for i in  enumerate(glob.iglob(folder)): </font><br/>" \
           r"Apply various filters to the images using the ImageFilter module.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/>" \
           r"Modify the RGB values of images to produce a new filter.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/>" \
           r"Experiment with the Pillow library and its modules and save what you have produced.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font></br>" \
            r"</font></strong><br/><br/><br/><br/>"

    return Codewriter((textfileopener(location)),string)

@app.route("/spec4")
def home3():
    """This is the function which is returned on the spec 4 page"""
    location=(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"\specification4\Spec4.py"
    string=r"<font size=+10>This is spec 4, this meets the following objectives:</font><br/>" \
           r"<strong><font color=blue>Investigate Python libraries to focus your solution around.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/>" \
           r"Plan your solution before development.</br>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/>" \
    r"Develop your program solution.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/>" \
           r"Test your program.<br/>" \
            r"  -This is done using  <font color=red> insert explanation here </font><br/>" \
           "</strong></font><br/><br/><br/><br/>"
    return Codewriter((textfileopener(location)), string)
def Codewriter(file,string):
    """This writes the code to both the webpage and the terminal."""
    for line in file:
        print(line)
        if '"""' in line:
            line= "<font color='red'>" +line +"</font>"#This colours docstrings red on the webpage
        if "def" in line:#This makes functions purple and bold
            line = "<strong>" +line +"</strong>"
            line = "<font color='purple'>" + line + "</font>"
        string = "<pre>" + string + line + "<br/>" +"</pre>"
    return string
def Spec3():
    print("spec3")
    app.run(debug=True)
