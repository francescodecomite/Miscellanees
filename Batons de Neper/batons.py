LARGEUR=0.5
HAUTEUR=1
TAILLE=500
xmin=-1
# Les coef de la transfo affine
coefA=-TAILLE/(2*xmin)
coefB=TAILLE/2

def transfo(x):
    return coefA*x+coefB

def ligne(debut,fin,id="\" \"",stroke="\"black\""):
    chaine="<line x1=\""+str(transfo(debut[0]))+"\" y1=\""+str(transfo(debut[1]))+"\"   x2=\""+str(transfo(fin[0]))+"\" y2=\""+str(transfo(fin[1]))+"\"   id="+id+" stroke="+stroke+"  stroke-width=\""+str(LARGEUR)+"\" />"
    return chaine

def ligne_large(debut,fin,coef,id="\" \"",stroke="\"black\""):
    chaine="<line x1=\""+str(transfo(debut[0]))+"\" y1=\""+str(transfo(debut[1]))+"\"   x2=\""+str(transfo(fin[0]))+"\" y2=\""+str(transfo(fin[1]))+"\"   id="+id+" stroke="+stroke+"  stroke-width=\""+str(coef*LARGEUR)+"\" />"
    return chaine

def texte(string,position,police):
    chaine="<text font-family=\"Arial, Helvetica, sans-serif\" font-size=\""+str(police)+"\" x=\""+str(transfo(position[0]))+"\" y=\""+str(transfo(position[1]))+"\" >\n"
    chaine=chaine+string+"</text>"
    return chaine

def rectangle(position,largeur,hauteur):
    chaine=""
    chaine+=ligne((position[0],position[1]+largeur),position)#,stroke="\"red\"")
    chaine+=ligne(position,(position[0]+hauteur,position[1]))#,stroke="\"red\"")
    chaine+=ligne((position[0]+hauteur,position[1]),(position[0]+hauteur,position[1]+largeur))#,stroke="\"red\"")
    chaine+=ligne((position[0]+hauteur,position[1]+largeur),(position[0],position[1]+largeur))#,stroke="\"red\"")
    return chaine

def reglette(position):
    chaine=""
    largeur=HAUTEUR/10
    chaine+=rectangle(position,HAUTEUR,largeur)
    for i in range(10) :
        chaine+=ligne((position[0],position[1]+i*HAUTEUR/10),(position[0]+largeur,position[1]+i*HAUTEUR/10))
        #les diagonales
    for i in range(9):
        chaine+=ligne((position[0]+largeur,position[1]+(i+1)*HAUTEUR/10),(position[0],position[1]+(i+2)*HAUTEUR/10))
    return chaine

def reglettenombre(position,val):
    chaine=reglette(position)
    chaine+=texte(str(val),(position[0]+HAUTEUR/30,position[1]+HAUTEUR/15),16)
    for i in range(1,10):
        dizaine=(val*i)//10
        unite=(val*i)%10
        chaine+=texte(str(dizaine),(position[0]+HAUTEUR/50,position[1]+i*HAUTEUR/10+HAUTEUR/24),10)
        chaine+=texte(str(unite),(position[0]+HAUTEUR/16,position[1]+i*HAUTEUR/10+HAUTEUR/13),10)
    
    return chaine

def quatrefaces(position,v1,v2):
    chaine=""
    liste=[v1,v2,10-v1,10-v2]
    for i in range(4):
        chaine=chaine+reglettenombre((position[0]+i*HAUTEUR/10,position[1]),liste[i])
    return  chaine


def monimage():
    entete="<svg viewBox=\"0 0 "+str(TAILLE)+" "+str(TAILLE)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("neper"+".svg","w")
   
    image.write(entete)
    #for i in range(1,10):
     #image.write(reglettenombre((-1+i*HAUTEUR/9,-1),i))
    image.write(quatrefaces((-1,-1),7,6))
    image.write(quatrefaces((-1+HAUTEUR/10*4,-1),8,5))
    image.write(quatrefaces((-1+HAUTEUR/10*8,-1),9,7))
    image.write(quatrefaces((-1+HAUTEUR/10*12,-1),4,7))
    image.write(pied)
    image.close()
