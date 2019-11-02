import argparse
from .specification1 import Spec1
from .specification2 import Spec2
from .specification3 import Spec3
from .specification4 import Spec4


def spec1():
    Spec1.test()
def spec2():
    Spec2.test()
def spec3():
    Spec3.test()
def spec4():
    Spec4.test()
def CLI():
    parser = argparse.ArgumentParser(prog="Grouptask")#creates parser
    subparsers = parser.add_subparsers(help="Sub Command Help")
    #these will be arguments we can run to test each spec and keep them seperate
    subparsers.add_parser("Frequency",help="This will analyse the frequency of words in a string of text").set_defaults(func=spec1)
    subparsers.add_parser("Imageeditor",help="THis will edit the images in a given folder").set_defaults(func=spec2)
    subparsers.add_parser("website",help="This creates the website?").set_defaults(func=spec3)#not sure about if we need to run this ?
    subparsers.add_parser("Spec4",help="this runs spec 4").set_defaults(func=spec4)
    args=parser.parse_args()
    args.func()
