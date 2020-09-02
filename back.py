class Background:
    def __init__(self, background_size):
        self.background_size = background_size
        self.tex = None
    
    def loadText(self):
        print("Texture Loaded")
        self.tex = loadImage('back.jpg')

    def display(self, z):
        if self.tex is None:
            self.loadText()
            
        pushMatrix()
        translate(-self.background_size,-self.background_size/2, z)
        # fill(255,255,255)
        beginShape(QUAD)
        texture(self.tex)
        vertex(2*self.background_size, 0, self.tex.width, 0)
        vertex(2*self.background_size, self.background_size, self.tex.width, self.tex.height)
        vertex(0, self.background_size, 0, self.tex.height)
        vertex(0, 0, 0, 0)
        endShape()
        popMatrix()
        
