class Diamond:
    def __init__(self, base_length, half_height, *multiplier):
        self.base_length = base_length
        self.half_length = base_length/2
        self.center = sin(PI/3)*self.base_length
        self.half_height = half_height
        self.y_angle = 0
        self.x_angle = 0
        self.y_speed = 1
        if len(multiplier) > 0:
            self.multiplier = multiplier[0]
        else:
            self.multiplier = 1
    
    def incrementYSpeed(self):
        self.y_speed += 0.1 * self.multiplier
        
    def decrementYSpeed(self):
        self.y_speed -= 0.1 * self.multiplier
        
    def incrementXAngle(self):
        self.x_angle += 0.1 * self.multiplier
    
    def decrementXAngle(self):
        self.x_angle -= 0.1 * self.multiplier
    
    def display(self, x, y):
        pushMatrix()
        translate(-width/2+x,-height/2+y, 0)
        rotateX(self.x_angle)
        pushMatrix()
        rotateY(self.y_angle)
        
        v = [(0,0,0), 
             (self.half_length, 0, self.center), 
             (self.half_length, -self.half_height, self.center/3), 
             (self.base_length, 0, 0),
             (self.half_length, self.half_height, self.center/3), 
            ]
        
        translate(-self.half_length,0, -self.center/3)

        diamond = createShape()
        diamond.beginShape(TRIANGLE)
        diamond.vertex(v[0][0],v[0][1],v[0][2])
        diamond.vertex(v[1][0],v[1][1],v[1][2])
        diamond.vertex(v[2][0],v[2][1],v[2][2])  
        diamond.endShape()
        diamond.beginShape(TRIANGLE)
        diamond.vertex(v[3][0],v[3][1],v[3][2])
        diamond.vertex(v[1][0],v[1][1],v[1][2])
        diamond.vertex(v[2][0],v[2][1],v[2][2])  
        diamond.endShape()
        diamond.beginShape(TRIANGLE)
        diamond.vertex(v[0][0],v[0][1],v[0][2])
        diamond.vertex(v[2][0],v[2][1],v[2][2])  
        diamond.vertex(v[3][0],v[3][1],v[3][2])
        diamond.endShape()
        
        
        diamond.beginShape(TRIANGLE)
        diamond.vertex(v[0][0],v[0][1],v[0][2])
        diamond.vertex(v[1][0],v[1][1],v[1][2])
        diamond.vertex(v[4][0],v[4][1],v[4][2])  
        diamond.endShape()
        diamond.beginShape(TRIANGLE)
        diamond.vertex(v[3][0],v[3][1],v[3][2])
        diamond.vertex(v[1][0],v[1][1],v[1][2])
        diamond.vertex(v[4][0],v[4][1],v[4][2])  
        diamond.endShape()
        diamond.beginShape(TRIANGLE)
        diamond.vertex(v[0][0],v[0][1],v[0][2])
        diamond.vertex(v[3][0],v[3][1],v[3][2])
        diamond.vertex(v[4][0],v[4][1],v[4][2])  
        diamond.endShape()
        
        shape(diamond)
        self.y_angle += 0.05 * self.y_speed * self.multiplier
        popMatrix()
        popMatrix()
    
