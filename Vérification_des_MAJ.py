import os

# Vérification des MAJ

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

def linux() :
    os.system("-y sudo apt install python3-pip")
    print ("")
    os.system("-y sudo pip3 install tk==0.1.0")
    print ("")
    os.system("-y sudo pip3 install pillow==10.0.1")

if __name__ == "__main__" :
    choix_os()
