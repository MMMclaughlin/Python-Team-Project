import PIL.Image
import glob
import PIL.ImageFilter
import sys
def init(args):
    print("this worked")
    image_list = []
    print(args.file)

    folder=str(args.file)
    print(glob.iglob((folder)))
    for i in  enumerate(glob.iglob(folder)):  # assuming gif
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


class Imageediting():#this is an instance of every image
    def __init__(self,image,filename):
        self.file=image
        self.name=filename
    def thumbnailmaker(self,i):#function to make a thumbnail of the object
        size=128,128
        self.file.thumbnail(size)
        self.file.save(self.name + ".thumbnail", "JPEG")
    def filter(self,args):#takes a filter name as an argument and applies to the object
        print("this is the start of the function")
        option=(args.F).upper()
        print(option)
        try:
            functionname=getattr(PIL.ImageFilter,option)
        except AttributeError:
            print("bad filter name given exiting")
            sys.exit()
        Filteredimage = self.file.filter(functionname)
        Filteredimage.save(self.name + option, "JPEG")
    def RGBchange(self,args):#creates a change to the R and B based on the amount of pixels in the image
        width, height=self.file.size
        print(self.name)
        for y in range(0,height):
            for x in range(0, width):
                values=x, y
                pixel=self.file.getpixel(values)
                newtuple=(pixel[0]+round(x/100),pixel[1],pixel[2]+round(x/100))
                self.file.putpixel(values,newtuple)
        self.file.save(self.name + "RGB", "JPEG")


