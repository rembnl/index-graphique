# https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-programmer-une-interface-graphique-avec-tkinter-partie-1

# L'importation de l’ensemble des éléments du paquet tkinter :
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image

# défilistion de la liste contenant les éléments
liste_photos = []

# définition des variables contanant les paramètres 
contenu_date = ""
contenu_lieu = ""
contenu_pellicule = ""

# Définition du compteur

i = 0


# définition de la classe IMG

class Img() :
    x, y = 1924, 1365
    #x, y = 1920, 1080
    c = 0
    cc = 0
      
    def __init__(self,pics) :
        self.pics = pics

    # Création du fond blanc (bg)
    def SetBackground() :
        bg = Image.new('RGB', (Img.x, Img.y), (255, 255, 255))
        bg.save("bg.jpg")
        return bg
    
    # Ouverture des images et faire une copie pour le programme
    # Self.pics est la liste contanant les chemins vers les images
    def opening(self,i) :
        print ("contenu de self.pics : ", self.pics)
        print ("index en cours (méthode opening): ", i)
        print ("image en cours (méthode opening): ", self.pics[i])
        with Image.open(self.pics[i]) as im:
            im = im.copy()
        return im

    # Position du curseur sur le fond 
    def SetPosition(i) :
        height = 20 + Img.c*200 #i
        width = (i-Img.cc)*273+ 8  #  
        if width > Img.x - 200 :
            width = 8
            Img.c += 1
            height = 20 + Img.c*200 #i
            Img.cc = i
        print("largeur et hauteur :", width, height)
        return width, height

    # Redimentionner les images 
    def SetSize(self, width, height,i) :
        im = self.opening(i)
        im = im.resize((268,194))
        im = bg.paste(im, (width, height))
        return bg


    # Affichage du résultat 
    def ShowPic(self) :
        bg.show()
        

    # Création du texte de bas de page 
    def Ending_text():
        from PIL import ImageFont
        from PIL import ImageDraw

        contenu_date = date.get()
        contenu_lieu = lieu.get()
        contenu_pellicule = pellicule.get()

        texte = "Date : %s  /  Pellicule : %s  /  Notes : %s"%(contenu_date,contenu_pellicule,contenu_lieu)
        font = ImageFont.truetype("times-ro.ttf", 30)
        img = Image.new('RGB', (1800, 60), color = 'grey')
        draw = ImageDraw.Draw(img)
        draw.text((20, 30), texte ,(0,0,0),font=font)       
            
        img = bg.paste(img, (50, 1270))
        return bg

# Fonctions de vérifications de mise à jour 

def choix_os () :
    print ("""
Quel est votre système d'exploitation ?

+----------------------------------------+
|              1 - Windows               |
|              2 - Linux                 |
+----------------------------------------+       
 
""")
    systeme_user = int(input("Votre choix : "))
    if systeme_user == 1 :
        windows()

    if systeme_user == 2 :
        linux()

    elif systeme_user != 1 :
        print ("Choix impossible  \n")
        choix_os()

def windows() : 
    os.system("python -m ensurepip --default-pip")
    print ("")
    os.system("python -m pip install tk==0.1.0")
    print ("")
    os.system("python -m pip install pillow==10.0.1")
    print ("\n Vérification des mises à jour terminée !")
    os.system("cls")

def linux() :
    os.system("-y sudo apt install python3-pip")
    print ("")
    os.system("-y sudo pip3 install tk==0.1.0")
    print ("")
    os.system("-y sudo pip3 install pillow==10.0.1")
    print ("\n Vérification des mises à jour terminée !")
    os.system("clear")


# définition des fonctions pour tkinter
def valider():
    contenu_date = date.get()
    contenu_lieu = lieu.get()
    contenu_pellicule = pellicule.get()
    print("Contenu de date:", contenu_date)
    print("Contenu de lieu:", contenu_lieu)
    print("Contenu de pellicule:", contenu_pellicule)


    # formules pour créer le bg 
    Img.Ending_text()

    image = Img(liste_photos)
    nb =  100 / (len(image.pics) - 1) 
    print ("liste des images : ", image)
    for i in range(len(image.pics)):
        print ("image en cours de traitement : ", i)
        j = int(i*nb)
        print("Progression : " + str(j) + " %  (" + liste_photos[i] +")") 
        #Définition de la position du curseur 
        width, height = Img.SetPosition(i)
        image.opening(i)
        image.SetSize(width, height, i)    
    image.ShowPic()

def exploreur():
    filename = filedialog.askopenfilenames(initialdir = "~", title = "Select a File", filetypes = (("Images",  "*.png*"), ("all files",  "*.*")))
    for i in filename :
    # Ajouter à la liste
        liste_photos.append(i)
    #Création d'une varioable str quio contiendra la liste des images 
    chaine_photos = ""
    for i in liste_photos :
        chaine_photos += f"fichier sélectioné : {i} \n"
    label_file_explorer.configure(text=chaine_photos )
    print("Liste des fichiers :", liste_photos)
    print("photo selectionnée :", chaine_photos)

# Vérification des mises à jour 
choix_os()      

# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()
fenetre.title("photodex")
#fenetre.iconbitmap("C:\\Users\remi.bonnel\Desktop\indoto\logo.ico")

# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
fenetre.config(bg = "lightgrey")

# Taille de la fenetre
#fenetre.minsize(800,600)
fenetre.resizable(False, False)


police_titre = ("Broadway", 30)
titre = Label (fenetre, text = "Bienvenue dans Photodex !", font = police_titre, pady=20, padx=20, fg="blue", bg="lightgrey")
titre.grid(column=1, row=1)

police_texte = ("Arial", 15)
texte_selection = Label (fenetre, text = " Cliquer pour sélectionner vos photos : ", font = police_texte, pady=5, padx=10, fg="black", bg="lightgrey")
texte_selection.grid(column=1, row=2)

button_explore = Button(fenetre, text = "Rechercher",  command = exploreur, pady=10, padx=20)
button_explore.grid(column = 1, row = 3)

espace = Label (fenetre, text = " ", pady=10, padx=10, bg="lightgrey")
espace.grid(column=1, row=4)

texte_date = Label (fenetre, text = " Indiquer la date de la prise de vue ", font = police_texte, pady=5, padx=10, fg="black", bg="lightgrey")
texte_date.grid(column=1, row=5)

date = Entry(fenetre,  width=70)
date.grid(column = 1, row = 6)

espace2 = Label (fenetre, text = " ", pady=0, padx=10, bg="lightgrey")
espace2.grid(column=1, row=7)

texte_lieu = Label (fenetre, text = " Indiquer le lieu de la prise de vue ", font = police_texte, pady=5, padx=10, fg="black", bg="lightgrey")
texte_lieu.grid(column=1, row=8)

lieu = Entry(fenetre,  width=70)
lieu.grid(column = 1, row = 9)

espace3 = Label (fenetre, text = " ", pady=0, padx=10, bg="lightgrey")
espace3.grid(column=1, row=10)

texte_pellicule = Label (fenetre, text = " Indiquer la pellicule utilisée ", font = police_texte, pady=5, padx=10, fg="black", bg="lightgrey")
texte_pellicule.grid(column=1, row=11)

pellicule = Entry(fenetre,  width=70)
pellicule.grid(column = 1, row = 12)
          
espace4 = Label (fenetre, text = " ", pady=0, padx=10, bg="lightgrey")
espace4.grid(column=1, row=14)

button = Button(fenetre, text="Valider", command=valider,  pady=10, padx=20)
button.grid(column=1, row=15)

espace5 = Label (fenetre, text = " ", pady=0, padx=10, bg="lightgrey")
espace5.grid(column=1, row=16)

label_file_explorer = Label(fenetre,  text = "Merci de sélectionner un fichier",   width = 100, height = 4, fg = "blue")
label_file_explorer.grid(column = 1, row = 20)


# Définition du fond 

bg = Img.SetBackground()



# Affichage de la fenêtre créée :
print("Copyright (C) Yehya Zeaiter & Rémi Bonnel. Tous droits réservés.")
fenetre.mainloop()
print(date.get())
print("A très vite !")

