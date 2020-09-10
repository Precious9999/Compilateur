# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:49:18 2020

@author: madin
"""

#token = ["Type", "Valeur", "Numéro de ligne"] 
# Si le type est un identificateur alors la valeur sera une chaîne
# Si le type est une constante alors la valeur sera un entier
#while est un mot clef, i est un identificateur, un chiffre est une constante  

Lexique = {}

#Opérateurs arithmétiques
Lexique["+"]= ["Addition", None, None] #
Lexique["-"]= ["Soustraction", None, None]#
Lexique["*"]= ["Multiplication", None, None]#
Lexique["/"]= ["Division", None, None]#
Lexique["%"]= ["Modulo", None, None]#
Lexique["^"]= ["Exposant", None, None]#
Lexique["**"]= ["Exposant", None, None]#
Lexique["="]= ["Affectation", None, None]#

#Opérateurs logiques
Lexique["&&"]= ["And", None, None]#
Lexique["||"]= ["Or", None, None]#
Lexique["!"]= ["Not", None, None]#

#Opérateurs de comparaison ope_comp = [">","<",">=","<=","==","!="]
Lexique[">"]= ["Supérieur à", None, None]#
Lexique["<"]= ["Inférieur à ", None, None]#
Lexique[">="]= ["Supérieur ou égale", None, None]#
Lexique["<="]= ["Inférieur ou égale", None, None]#
Lexique["=="]= ["Egal", None, None]#
Lexique["!="]= ["Est différent de", None, None]#

#Mots-clés
Lexique["const"]= ["Constante", None, None]#
Lexique["ident"]= ["Identificateur", None, None]
Lexique["if"]= ["Si conditionnel", None, None]
Lexique["for"]= ["Boucle for", None, None]
Lexique["while"]= ["Boucle while", None, None]
Lexique["else"]= ["Sinon conditionnel", None, None]

#Délimiteurs
Lexique["("]= ["Début de parenthèse", None, None]
Lexique[")"]= ["Fin de parenthèse",None, None]
Lexique[","]= ["Virgule", None, None]

Lexique[":"]= ["", None, None]
#INDENTATION !! Indent - Dedent... 

Lexique["EOF"]= ["EOF", None, None]#
Lexique["#"]= ["Ligne de commentaire", None, None]
Lexique["ERR"]= ["ERR", None , None]
#tout mettre en majuscule

#Divers
Lexique["_"]= ["Underscore", None, None]




tab_source=[]
i =0
no_ligne = 0

def analyseLex():
    global i
    file = open("IMC_Calcul.txt","r")
    c = file.read() 
    c = c + " "
    file.close()
    token = unitesuivante(c)
    i = i+1
    print(token)
    tab_source.append(token)
    while token[0] != "EOF" and token[0] != "ERR":
        token = unitesuivante(c) #on prend le prochain token
        i = i+1
        tab_source.append(token) #et on le rajoute à tab_source
        print(token)
        
def unitesuivante(c):
    nombre = ""
    mot = ""
    global no_ligne
    global i
    global tab_source
    while i < len(c)-1 and c[i] == " ": #cette boucle sert à ignorer tous les espaces
        i = i+1
    while i < len(c)-1 and c[i] == "\n": #cette boucle sert à incrémenter les retour à la ligne et il les ignores
        i = i+1  
        no_ligne = no_ligne+1
    if i >= len(c)-1:
        return Lexique["EOF"]
    
    # Si c"est un opérateur simple
    if c[i] == "+":
        token = Lexique["+"]
        token[1]=c[i]
        token[2]=no_ligne
        return token
    if c[i] == "-":
        token = Lexique["-"]
        token[1]=c[i]
        token[2]=no_ligne
        return token
    if c[i] == "/":
        token = Lexique["/"]
        token[1]=c[i]
        token[2]=no_ligne
        return token
    if c[i] == "^":
        token = Lexique["^"]
        token[1]=c[i]
        token[2]=no_ligne
        return token
    if c[i] == "%":
        token = Lexique["%"]
        token[1]=c[i]
        token[2]=no_ligne
        return token
    
    # Si c"est un opérateur double composé de deux opérateurs simples
    if c[i] == "*" and c[i+1] != "*" :
        token = Lexique["*"]
        token[1]=c[i]
        token[2]=no_ligne
        return token 
    if c[i] == "*" and c[i+1] == "*" :
        token = Lexique["**"]
        token[1]=c[i]+c[i+1]
        token[2]=no_ligne
        i = i+1 #pour tous les token double j'incrémente i   
        return token 
    
    if c[i] == "=" and c[i+1] != "=" :
        token = Lexique ["="]
        token[1]=c[i]
        token[2]=no_ligne
        return token 
    if c[i] == "=" and c[i+1] == "=" :
        token = Lexique ["=="]
        token[1]=c[i]
        token[2]=no_ligne
        i = i+1 #pour tous les token double jincrémente l"i 
        return token  
    
    if c[i] == "!" and c[i+1] != "=" :
        token = Lexique ["!"]
        token[1]=c[i]
        token[2]=no_ligne
        return token 
    if c[i] == "!" and c[i+1] == "=" :
        token = Lexique ["!="]
        token[1]=c[i]
        token[2]=no_ligne
        i = i+1 #pour tous les token double jincrémente l"i 
        return token 

    if c[i] == ">" and c[i+1] != "=" :
        token = Lexique [">"]
        token[1]=c[i]
        token[2]=no_ligne
        return token 
    if c[i] == "=" and c[i+1] == "=" :
        token = Lexique [">="]
        token[1]=c[i]
        token[2]=no_ligne
        i = i+1 #pour tous les token double jincrémente l"i 
        return token 
    
    if c[i] == "<" and c[i+1] != "=" :
        token = Lexique ["<"]
        token[1]=c[i]
        token[2]=no_ligne
        return token 
    if c[i] == "<" and c[i+1] == "=" :
        token = Lexique ["<="]
        token[1]=c[i]
        token[2]=no_ligne
        i = i+1 #pour tous les token double jincrémente l"i 
        return token    
    
    # Si c'est un opérateur logique double 
    if c[i] == "&" and c[i+1] == "&" : # dans le cas ou il n'y en a cas seul on peut renvoyer un message d'erreur
        token = Lexique ["&&"]
        token[1]=c[i]+c[i+1]
        token[2]=no_ligne
        i = i+1 #pour tous les token double jincrémente l"i 
        return token  
    if c[i] == "|" and c[i+1] == "|" : # dans le cas ou il n'y en a cas seul on peut renvoyer un message d'erreur
        token = Lexique ["||"]
        token[1]=c[i]
        token[2]=no_ligne
        i = i+1 #pour tous les token double jincrémente l"i 
        return token  
    
    # Si c"est un chiffre 
    if c[i].isnumeric():
        while c[i].isnumeric():#si il croise un charactere qui est un nombre c'est que c'est le debut d'une constante numérique
            nombre = nombre + c[i] #on parcours tous les chiffres
            i = i+1
        token = Lexique["const"] #on sort de la boucle qd on croise autre chose qu'un nombre
        token[1]=int(nombre)#on converti nos charactere en nombre(recoit nombre)
        i = i-1 #on décrémente car pour se rendre compte que le charactere d'apres n'était pas un chiffre il a fallu avancé dans l'i, donc on décrémente pour revenir à ce charactere
        token[2]=no_ligne
        return token
    
    # Si c'est un identificateur
    if c[i].isalpha() :
        while c[i].isalpha() or c[i].isnumeric() or c[i]== "_":#si il croise un charactere qui est un nombre c'est que c'est le debut d'un identificateur
            mot = mot + c[i] #on parcours tous les lettres
            i = i+1
        if mot != motclef(c):  
            token = Lexique["ident"] #crée une fonction qui va tester si nombre est un mot clef
            token[1]= mot 
            token[2]=no_ligne
            i = i-1 #on décrémente car pour se rendre compte que le charactere d'apres n'était pas un chiffre/lettre/underscore il a fallu avancé dans l'i, donc on décrémente pour revenir à ce charactere 
            return token
        if mot == motclef(c):  
            token = Lexique[motclef(c)]
            token[1]= motclef(c)
            token[2]=no_ligne
            return token
        
    # Si c'est un délimiteur 
    
    # Si c'est un commentaire
    
    # Si c'est une erreur
    token = Lexique["ERR"]
    token [1]= i #
    token[2] = no_ligne #quand il y a une erreur on sauvegarde le numero de la ligne 
    return token 
    
def motclef(c):
    mot = ""
    global i
    
    while c[i].isalpha() :
        mot = mot + c[i] #on parcours tous les lettres
        i = i+1           
    if mot == "if":
        return "if"
    
    if mot == "for":
        return "for"
    
    if mot == "while":
        return "while"
    
    if c[i] == "else":
        return "else"
        

analyseLex()
     
"""
Interface de l'analyseur syntaxique
"""


#token_courant = tab_source[0]
token_index = 0
token_courant = tab_source[token_index]

def courant():
    #permet de savoir le token courant à analyser syntaxiquement
    #print ("Le token courant est : ")
    #print(token_courant)
    #global token_courant
    return token_courant

def avancer():
    global token_index
    global token_courant
    if token_index < len(tab_source):
        token_index+=1
        token_courant = tab_source[token_index]
        #print("Le token suivant est le :")
        #print(token_courant)


def accepter(_type): #pour les parenthèses 
    token_courant = courant()
    if token_courant[0] != _type:
        print("Erreur fatale! Le type n'est pas le bon !")
    else : 
        #print("C'est le bon type pour ce token")
        avancer()
    no_ligne = token_courant[2]    
    return no_ligne #peut renvoyer le numéro de ligne

def verifier(_type):
    token_courant = courant()
    if token_courant[0]==_type : 
        avancer()
        return True
    return False

courant()
avancer()
accepter("Affectation") 
verifier ("Affectation")    


"""
Analyseur syntaxique
"""

# priorité à droite à [0]
# priorité à gauche à [1]
table_priorite = {}

table_priorite["Exposant"]=[60,60,"Nd_exposant"]
table_priorite["Moins unaire"] = [55,55,"noeud_moins_unaire"]
table_priorite["Not"] = [55,55,"not"]
table_priorite["Multiplication"]=[50,51,"mul"]
table_priorite["Division"]=[50,51,"div"]
table_priorite["Modulo"]=[50,51,"mod"]
table_priorite["Addition"]=[40,41,"add"]
table_priorite["Soustraction"]=[40,41,"sub"]
table_priorite["Supérieur à"]=[30,31,"cmpgt"]
table_priorite["Inférieur à"]=[30,31,"cmplt"]
table_priorite["Inférieur ou égale à"]=[30,31,"cmple"]
table_priorite["Supérieur ou égale à"]=[30,31,"cmpgt"]
table_priorite["Est égale à "]=[30,31,"cmpeq"]
table_priorite["Différent de "]=[30,31,"cmpne"]
table_priorite["And"]=[20,21,"and"]
table_priorite["Or"]=[10,11,"or"]

class newNoeud:     
    def __init__ (self, Type, ligne):         
        self.valeur = Type         
        self.valeur_entiere = 0         
        self.num_ligne = ligne
        self.slot=0
        self.enfants = []
        
    def __repr__(self): # affichage
        s = "Type : " + str(self.valeur) + " , " + "Valeur entière : " + str(self.valeur_entiere) + ", " + "Numéro de ligne  : " + str(self.num_ligne) + ", " + "Enfants :" + str(self.enfants)              
        s = s.replace("None",".") # pour alléger l'affichage
        return s
    
    
    
def addEnfant(parent,enfant): #pushback sur les enfants du noeuds parents    
    parent.enfants.append(enfant)
    return parent   
    




def Expression(PrioMin):
    N= Atome()    
    #A2 = newNoeud() #l'enfant à gauche de l'opérateur arithmétique
    
    tokenCourant = courant()#on stocke dans une variable le token courant 
    
    while (tokenCourant[0] in table_priorite)== True and table_priorite[tokenCourant[0]][1] > PrioMin:
        operateur = table_priorite[tokenCourant[0]] #on stocke dans la variable operateur le type du token courant (c'est donc un string)
        operateur_ligne = tokenCourant[2]
        avancer()
        A1 = N
        A2 = Expression(operateur[0])#la c'est la priorité à droite qu'on récupère
        N = newNoeud(operateur[2],operateur_ligne)        
        addEnfant(N,A1)
        addEnfant(N,A2)
        
    return N    





def Atome(): #Fonction qui crée des noeuds constants
    tokenCourant = courant()
    if verifier("Début de parenthèse")==True : 
        N = Expression(0)
        accepter("Début de parenthèse")
        avancer()
        return N
    elif verifier("Soustraction")==True  : #construction des noeuds moins unaires et not !
        N = newNoeud("Moins Unaire",tokenCourant[2])
        Arg=Expression(55)
        addEnfant(N,Arg)
        avancer() #faut-il le mettre 
        return N
    elif verifier("Not")==True : #construction des noeuds moins unaires et not !
        N = newNoeud("Not",tokenCourant[2])
        Arg=Expression(55)
        addEnfant(N,Arg)
        avancer() #faut-il le mettre 
        return N
    if tokenCourant[0]== "Constante" : 
        N = newNoeud("Nd_Constante",tokenCourant[2])
        N.valeur_entiere = tokenCourant[1]
        avancer()
        return N
    print("Erreur Fatale ! Ligne : " + str(tokenCourant[2]) + "Type envoyé : " + tokenCourant[1])
    #ça retourne quoi en cas d'erreur ? 

Expression(0)  




def gencode(Noeud):
    switch(Noeud.type){
            case "Nd_Constante" :
                print("push ",Noeud.valeur_entiere)
            
            }
        
	switch(Noeud.type){      
            case "Nd_Constante" : 
                print("push ",Noeud.valeur_entiere)

    		case "Addition" : 	gencode(Noeud.enfant[0])
    							gencode(Noeud.enfant[1])
    							print("add")
    		case "Soustraction" : 	
    							gencode(Noeud.enfant[0])
    							gencode(Noeud.enfant[1])
    							print("sub")
    		case "Divison" : 	gencode(Noeud.enfant[0])
    							gencode(Noeud.enfant[1])
    							print("div")
    		case "Multiplication" : 	
    							gencode(Noeud.enfant[0])
    							gencode(Noeud.enfant[1])
    							print("mul")
            default : break; 
    }
    
    
def instruction():
    if verifier("debug")==True:
        #Analyse syntaxique 
        E1 = Expression(0)
        accepter("point_virgule")
        #Création de noeud
        N = newNoeud("Debug")
        addEnfant(N,E1)
        return N
    elif verifier("Accolade_ouvrante")==True:
        N=newNoeud("Block")
        while (!verifier("Accolade_fermante")):
            addEnfant(N,instruction())
    return N
        
        return True
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    