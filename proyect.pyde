from diamond import Diamond
from teseract import Teseract
from back import Background

diamonds = [Diamond(100,100), Diamond(100,100,-1), Diamond(100,100), Diamond(100,100,-1)]
teseract = Teseract(200)
my_back = Background(2000)

s1 = None
s2 = None

def setup():
    global s1, s2
    fullScreen(P3D, 2)
    smooth(8)
    s1 = loadShader('frag.glsl','vert.glsl')
    s2 = loadShader('lightfrag.glsl','lightvert.glsl')
    
    
def draw():
    background(0)
    
    pointLight(255, 255, 255, width/2, height, 600);
    
    translate(width/2, height/2)
    
    shader(s1)
    stroke(255)    
    my_back.display(-300)
    teseract.display(width/2, height/2)
    
    shader(s2)
    fill(0,255,0, 100)
    if mousePressed and mouseX < width/2: fill(255,255,255)
    diamonds[0].display(200,200)
    diamonds[2].display(200,height-200)
    fill(0,255,0, 100)
    if mousePressed and mouseX > width/2: fill(255,255,255)
    diamonds[1].display(width-200,200)
    diamonds[3].display(width-200,height-200)
    
    try:
        if keyPressed and key in 'wW':
            diamonds[0].incrementXAngle()
            diamonds[2].incrementXAngle()
        elif keyPressed and key in 'sS':
            diamonds[0].decrementXAngle()
            diamonds[2].decrementXAngle()
        elif keyPressed and key in 'aA':
            diamonds[0].incrementYSpeed()
            diamonds[2].incrementYSpeed()
        elif keyPressed and key in 'dD':
            diamonds[0].decrementYSpeed()
            diamonds[2].decrementYSpeed()
    except:
        print('Key not found')
    
