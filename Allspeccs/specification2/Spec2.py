import PIL.Image
import glob
import PIL.ImageFilter
import sys
import time
def init(args):#this selects the correct function in the class to run
    image_list = []
    if args.file:
        folder=str(args.file)+"\*"
    else:
        print("please give a folder location with the --file argument")
        return
    for i in  enumerate(glob.iglob(folder)):#this loop makes a list of all the images in the given folder
        file=PIL.Image.open(i[1])
        instance=Imageediting(file,i[1])
        image_list.append(instance)
    if args.T:
        for i in enumerate(image_list):
            i[1].thumbnailmaker(i)
    if args.F:
        for i in enumerate(image_list):
            i[1].filter(args)
    if args.RGB:
        for i in enumerate(image_list):
            i[1].RGBchange(args)
    if args.common:
        for i in enumerate(image_list):
            i[1].CommonColor(args)
    if args.Fhelp:
        filterhelp = "BLUR\nCONTOUR\nDETAIL\nEDGE_ENHANCE\nEDGE_ENHANCE_MORE\nEMBOSS\nFIND_EDGES\nSHARPEN\nSMOOTH\nSMOOTH_MORE"
        print(filterhelp)

class Imageediting():#this is an instance of every image
    def getname(self):
        return self.__name
    def getfile(self):
        return self.__file
    
    def __init__(self,image,filename):
        self.__file=image
        self.__name=filename


    def thumbnailmaker(self,i):#function to make a thumbnail of the object
        size=128,128#sets to a thumbnail size
        self.getfile().thumbnail(size)
        self.getfile().save(self.getname() + ".thumbnail", "JPEG")


    def filter(self,args):#takes a filter name as an argument and applies to the object
        print("this is the start of the function")
        option=(args.F).upper()#this makes sure that the argument given is in capitals to avoid unnesscary errors
        print(option)
        try:#try is needed incase the give a bad argument
            functionname=getattr(PIL.ImageFilter,option)
        except AttributeError:
            print("bad filter name given exiting")
            sys.exit()
        Filteredimage = self.getfile().filter(functionname)
        Filteredimage.save(self.getname() + option, "JPEG")


    def RGBchange(self,args):#creates a change to the R and B based on the amount of pixels in the image
        width, height=self.getfile().size#this gets the x and y boundaries
        print(self.getname())
        for y in range(0,height):
            for x in range(0, width):
                values=x, y
                pixel=self.getfile().getpixel(values)#gets the rgb tuple of the current pixel at x,y
                newtuple=(pixel[0]+round(x/100),pixel[1],pixel[2]+round(x/100))#fades the rgb value based on our x value
                self.getfile().putpixel(values,newtuple)#changes the rgb value to the newly made tuple ^
        self.getfile().save(self.getname() + "RGB", "JPEG")


    def CommonColor(self,args):#this is a function for finding the most common rgb values in an image
        width, height=self.getfile().size
        dict={}#this will hold a key value pair of each rgb value and the amount of times we find it
        greatestvalue=0
        GvaluePixel=(0,0,0)
        for y in range(0,height):
            for x in range(0, width):
                values=x, y
                pixel=self.getfile().getpixel(values)
                if pixel not in dict:#this checks if the rgb value has been seen before
                    dict[pixel]=1
                else:#increments previously seen rgb values
                    dict[pixel]=dict[pixel]+1
                    if dict.get(pixel)>greatestvalue:
                        greatestvalue=dict[pixel]
                        GvaluePixel=pixel#this keeps track of the greatest values so that i do not need to refind it
        print("the most common RGB value in",self.getname(),"is",GvaluePixel,)

