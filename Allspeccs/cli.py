import argparse
from specification1 import Spec1
from specification2 import Spec2
from specification3 import Spec3
from specification4 import Spec4

#these functions run each of our programs, change the called function to be correct
def spec1(args):
    Spec1.Spec1()
def spec2(args):
    Spec2.init(args)
def spec3(args):
    print("spec3")
    Spec3.Spec3()
def spec4(args):
    Spec4.Spec4()
def CLI():#this sets up the arguments we pass to run different parts
    filterhelp="BLUR\nCONTOUR\nDETAIL\nEDGE_ENHANCE\nEDGE_ENHANCE_MORE\nEMBOSS\nFIND_EDGES\nSHARPEN\nSMOOTH\nSMOOTH_MORE"
    parser = argparse.ArgumentParser(prog="Grouptask")#creates parser
    subparsers = parser.add_subparsers(help="Sub Command Help")
    #these will be arguments we can run to test each spec and keep them seperate
    subparsers.add_parser("Frequency",help="This will analyse the frequency of words in a string of text").set_defaults(func=spec1)
    subparsers.add_parser("Imageeditor",help="THis will edit the images in a given folder").set_defaults(func=spec2)
    subparsers.add_parser("website",help="This creates the website?").set_defaults(func=spec3)
    subparsers.add_parser("Spec4",help="this runs spec 4").set_defaults(func=spec4)
    parser.add_argument("--file", help="Imageeditor:change file location (file location string)", default=r"H:\csc1034-team-project\practical-3\resources\img\spec2-images\*")
    parser.add_argument("--T", help="Imageeditor:Choose to create thumbnails of all the given files",
                        default=False)
    parser.add_argument("--F", help="Imageeditor:Decide an image filter",
                        default=False)
    parser.add_argument("--Fhelp",help="Imageeditor:use this to show our suite of filters",default=False)
    parser.add_argument("--RGB", help="Imageeditor:Use custom Red tint",
                        default=False)
    parser.add_argument("--common", help="Imageeditor:Find the most common RGB values in each image ",
                        default=False)
    args=parser.parse_args()

    args.func(args)
