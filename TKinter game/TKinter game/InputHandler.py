class InputHandler(object):
    _input_dict = {"w" : False, "a" : False, "s" : False, "d" : False}
    
    def SendInput(self,key):
        self._input_dict[key.char] = True
        print(f"Key {key.char} pressed")
         
    
        
    def ResetInput(self,key):
        self._input_dict[key.char] = False
           
    def GetInput(self, key):
        return self._input_dict[key]
         




