class Teseract:
    def __init__(self, total_size, *multiplier):
        self.total_size = total_size
        self.half_size = total_size/2
        self.third_size = total_size/3
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0
        
        if len(multiplier) > 0:
            self.multiplier = multiplier[0]
        else:
            self.multiplier = 1
            
    def display(self, x, y):
        pushMatrix()
        rotateX(-PI/8)
        rotateY(self.y_angle)

        translate(-self.half_size,-self.half_size, -self.half_size)
        noFill()
        teseract = createShape()
        teseract.beginShape(QUAD)
        teseract.vertex(0, 0, 0)
        teseract.vertex(0, self.total_size, 0)
        teseract.vertex(0, self.total_size, self.total_size)
        teseract.vertex(0, 0, self.total_size)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(0, 0, self.total_size)
        teseract.vertex(self.total_size, 0, self.total_size)
        teseract.vertex(self.total_size, self.total_size, self.total_size)
        teseract.vertex(0, self.total_size,self.total_size)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(self.total_size, 0, 0)
        teseract.vertex(self.total_size, self.total_size, 0)
        teseract.vertex(self.total_size, self.total_size, self.total_size)
        teseract.vertex(self.total_size, 0,self.total_size)
        teseract.endShape()
    
        teseract.beginShape(QUAD)
        teseract.vertex(0,0,0)
        teseract.vertex(0,self.total_size,0)
        teseract.vertex(self.total_size,self.total_size,0)
        teseract.vertex(self.total_size,0,0)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(0,0,0)
        teseract.vertex(self.third_size,self.third_size,self.third_size)
        teseract.vertex(self.third_size,2*self.third_size,self.third_size)
        teseract.vertex(0,self.total_size,0)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(0,0,self.total_size)
        teseract.vertex(self.third_size,self.third_size,2*self.third_size)
        teseract.vertex(self.third_size,2*self.third_size,2*self.third_size)
        teseract.vertex(0,self.total_size,self.total_size)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(0,0,self.total_size)
        teseract.vertex(self.third_size,self.third_size,2*self.third_size)
        teseract.vertex(self.third_size,2*self.third_size,2*self.third_size)
        teseract.vertex(0,self.total_size,self.total_size)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(self.total_size,0,self.total_size)
        teseract.vertex(2*self.third_size,self.third_size,2*self.third_size)
        teseract.vertex(2*self.third_size,2*self.third_size,2*self.third_size)
        teseract.vertex(self.total_size,self.total_size,self.total_size)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(self.total_size,self.total_size, 0)
        teseract.vertex(2*self.third_size,2*self.third_size,self.third_size)
        teseract.vertex(2*self.third_size,self.third_size,self.third_size)
        teseract.vertex(self.total_size,0,0)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(self.third_size,self.third_size, self.third_size)
        teseract.vertex(self.third_size,self.third_size, 2*self.third_size)
        teseract.vertex(2*self.third_size,self.third_size, 2*self.third_size)
        teseract.vertex(2*self.third_size,self.third_size, self.third_size)
        teseract.endShape()
        
        teseract.beginShape(QUAD)
        teseract.vertex(self.third_size,2*self.third_size, self.third_size)
        teseract.vertex(self.third_size,2*self.third_size, 2*self.third_size)
        teseract.vertex(2*self.third_size,2*self.third_size, 2*self.third_size)
        teseract.vertex(2*self.third_size,2*self.third_size, self.third_size)
        teseract.endShape()
        
        shape(teseract)
        self.y_angle += 0.05 * self.multiplier
        popMatrix()
