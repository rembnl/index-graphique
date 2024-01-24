from PIL import Image

class Img() :
    x, y = 1924, 1365
    #x, y = 1920, 1080
    c = 0
    cc = 0
      
    def __init__(self,pics) :
        self.pics = pics

    def SetBackground() :
        bg = Image.new('RGB', (Img.x, Img.y), (255, 255, 255))
        bg.save("bg.jpg")
        return bg
    
    def opening(self) :
        with Image.open(self.pics[i]) as im:
            im = im.copy()
        return im

    def SetPosition() :
        
        height = 20 + Img.c*200 #i
        width = (i-Img.cc)*273+ 8  #  
        if width > Img.x - 200 :
            width = 8
            Img.c += 1
            height = 20 + Img.c*200 #i
            Img.cc = i
        return width, height


    def SetSize(self) :
        im = self.opening()
        im = im.resize((268,194))
        im = bg.paste(im, (width, height))
        return bg

    def ShowPic(self) :
        #bg = self.SetSize()
        bg.show()
        
    def liste_Img():
        from os import walk
        im1 = []
        for (repertoire, sousRepertoires, fichiers) in walk("Photos"):
            im1.extend(fichiers)
        im2 = ["Photos/" + im1[i] for i in range(len(im1))]
        im2.sort()
        return im2
    
    def Ending_text():
        from PIL import ImageFont
        from PIL import ImageDraw

        Date = str(input("Date : "))
        Pellicule = str(input("Pellicule : "))
        Notes = str(input("Notes : "))
        texte = "Date : %s  /  Pellicule : %s  /  Notes : %s"%(Date,Pellicule,Notes)
        font = ImageFont.truetype("times-ro.ttf", 30)
        img = Image.new('RGB', (1800, 60), color = 'grey')
        draw = ImageDraw.Draw(img)
        draw.text((20, 30), texte ,(0,0,0),font=font)       
            
        img = bg.paste(img, (50, 1270))
        return bg
        


bg = Img.SetBackground()
Img.Ending_text()


liste = Img.liste_Img()
image = Img(liste)
nb =  100 / (len(image.pics) - 1) 
for i in range(len(image.pics)):
    j = int(i*nb)
    print("Progression : " + str(j) + " %  (" + liste[i] +")") 
    width, height = Img.SetPosition()
    image.opening()
    image.SetSize()
    image.ShowPic()

    
image.ShowPic()
