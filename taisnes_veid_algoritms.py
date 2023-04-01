# Programmējamais kods
import numpy as np #lai strādātu ar masīviem
import matplotlib.pyplot as plt # zīmējuma atspoguļojumam
# uzdot attēlu kur uzdot līniju
img=np.ones((700, 700,3)) # height, width, 3-RGB
#nodefinēt metodi ar kuru realizēs līnijas veidošanu
def DrawLine(x1,y1,x2,y2):
    #x1,y1 - līnijas sākumpunkts
    #x2,y2 - līnijas galapunkts
    dx=abs(x2-x1) #abs modulis ir delta x, abs ir tas pats kas matemātikā ||
    dy=abs(y2-y1) # delta y 
    if x1<x2:
        xs=1
    else:

        xs=-1
            
    if y1<y2:
        ys=1
    else:
        ys=-1
        
    x=x1 # sākumpunkta deefinēšana
    y=y1 # galapunkta definēšana
    if dx>dy: #horizontālas līnijas
        p=2*dy-dx # p0 - risinošais parametrs tiek definēts vienkārši kā p
        while x!=x2: # kamēr nav galapunkts
            x=x+xs
            if p>0:
                y=y+ys
                p=p+2*dy-2*dx
            else:
                p=p+2*dy
            img[y,x]=0 # raksta pretēji, lai līnija nebūtu citā virzienā
    # ieskaitit nevis 1 bet xs vai ys, kas nozīmē vieninieku
    # =0 nozīmē, ka līnija būs melnā krāsā
    #else: tiks iekopētas līnijas no if dx>dy līdz img[x,y]=0
    if dy>dx: #horizontālas līnijas
        p=2*dx-dy # p0 - risinošais parametrs tiek definēts vienkārši kā p
        while y!=y2: # kamēr nav galapunkts
            y=y+ys
            if p>0:
                x=x+xs
                p=p+2*dx-2*dy
            else:
                p=p+2*dx
            img[y,x]=0
    
plt.rcParams["figure.figsize"]=(5,5)#realizē izvadu / loga izmēra maiņu
plt.rcParams["figure.dpi"]=80 # linijas dpi
DrawLine(200,300,200,500) #vertikala
DrawLine(100,400,200,400) #videja trijnieka linija
DrawLine(100,500,200,500)
DrawLine(100,300,200,300) #trijnieka beigas
DrawLine(400,300,400,500) #vert
DrawLine(300,300,300,500) #vert
DrawLine(300,400,400,400)
DrawLine(300,500,400,500)
DrawLine(300,300,400,300) # 8 beidzas
DrawLine(500,500,600,500)
DrawLine(600,500,600,300)
DrawLine(500,400,600,400)
DrawLine(500,300,600,300)
DrawLine(500,300,500,400)
    #lai uzzīmētu nākamo līniju:
    #DrawLine(100,450,500,5) - tikai maina citas koordinātas, arī tam kas augša
    
plt.imshow(img) # attēla izvads
plt.show() # atspoguļo rezultātu
