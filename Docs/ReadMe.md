#Practical 3 

CSC1034: Practical 3
====================

This package allows analysis and display of proteins from Uniprot.

####-----Prerequisites/Requirements---------  
Flask Module  
PIL Module  
image Module   
PyQt5 Module  
matplotlib Module  
os Module  
Glob Module  
Sys Module  



####-----The Project------
The project contains 4 specifications which can all be run from command line.

The first is a frequency analysis of the most common words and characters in a given file of text    
The second allows you to apply filters to a folder of images or find the most common RGB value in each image   
The third creates a website which displays code behind each other specification  
Finally is a Graphical interface which allows a user to reach all the important website for a computer science student at
newcastle univeristy might want to access


####-----Arguement usage-----

  #####Mandatory Arguments:(one of these must be chosen)

    Frequency           This will analyse the frequency of words in a string of text  
    Imageeditor         THis will edit the images in a given folder  
    website             This creates the website that displays source codes  
    Spec4               This creates a Graphical interface for important newcastle university websites  
    --file FILE         Name file/folder location (Frequency/Imageeditor)

#####Optional Arguments:
  -h, --help            show this help message and exit

  #####Image editor arguments
  --T (T)                 Choose to create thumbnails of all the given files(T/F)    
  --F Filtername          Decide an image filter use "--Fhelp T" to see what is available  
  --Fhelp (T)             Use this to show our suite of filters    
  --RGB (T)               Use custom Red tint    
  --common (T)            Find the most common RGB values in each image  

