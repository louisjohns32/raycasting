from GameObject import GameObject


class Player(GameObject):
    angle = 0
        
    def Update(self):
        
        if self.input_handler.GetInput("w"):
            self._y_pos -= 0.1
        if self.input_handler.GetInput("s"):
            self._y_pos -= 0.1
        if self.input_handler.GetInput("d"):
            self.angle += 0.1
            if self.angle > 2*3.1415:
                self.angle -= 2*3.1415
        if self.input_handler.GetInput("a"):
            self.angle -= 0.1
            if self.angle < 0:
                self.angle += 2*3.1415
        
    
    
        
        




