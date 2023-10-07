class GameObject:
    _x_pos = 100
    _y_pos = 100
    _awake = False
    _sprite = object    
    input_handler = object
    
    
    def __init__(self,sprite, input_handler):
        self.sprite = sprite
        self.awake = True
        self.input_handler = input_handler
        
    def EarlyUpdate():
        pass
    def Update(self):
        pass
            
    def LateUpdate():
        pass
    
        
    def get_sprite(self):
        return self.sprite
    def get_x(self):
        return self._x_pos
    def get_y(self):
        return self._y_pos
    

    
    
    
    





