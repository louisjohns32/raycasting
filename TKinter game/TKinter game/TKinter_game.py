from tkinter import *
from tkinter import ttk
import random

import math
from turtle import color
from PIL import Image, ImageTk
import PIL
import numpy as np
import GameObject
import PlayerObj
from InputHandler import InputHandler

x = 10
y = 10
angle = 0

BLOCKSIZE = 32


#MAP_ARRAY = [[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
 #            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  #           [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
   #          [1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1],
    #         [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
     #        [1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1],
      #       [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
       #      [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
        #     [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
         #    [1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1],
          #   [1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1],
           #  [1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
            # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
MAP_ARRAY = [[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
             [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1],
             [1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



def StartGame():
    
    print("Game obj created")
    test_obj = GameObject.GameObject(PIL.Image.open("testObj.png"), input_handler)
    main_canvas.create_image(100,100,image=ImageTk.PhotoImage(PIL.Image.open("testObj.png")))
    game_objects.append(test_obj)
    
    GameLoop()


def EarlyUpdate():
    pass

def Update():
    global y
    global x
    global angle
    for obj in game_objects:
        obj.Update()
    
    if input_handler.GetInput("w"):
        
        x += math.cos(angle) *3
        y+= math.sin(angle) *3
    if input_handler.GetInput("s"):
        x -= math.cos(angle) *3
        y-= math.sin(angle) *3
    if input_handler.GetInput("a"):
        angle -= 0.05
        if math.degrees(angle) < 0:
            angle += math.radians(360)
    if input_handler.GetInput("d"):
        angle += 0.05
        if math.degrees(angle) > 360:
            angle -= math.radians(360)
    map_canvas.delete("delete")
    map_canvas.create_rectangle(x/2-5,y/2-5,x/2+5,y/2+5,fill="white",tags="delete")
    
     
        
    

def LateUpdate():
    pass

    
def Render():
    main_canvas.delete("all") # later change to specific tag for objs that have moved on screen
    
    
    
    for i in range(-30,30):
        
        
        ray_ang = angle + math.radians(i)/2
        if ray_ang > math.radians(360):
            ray_ang -= math.radians(360)
        elif ray_ang < 0:
            ray_ang += math.radians(360)
        ray_tuple = RayCast(x,y,ray_ang)
        height = 2048/ray_tuple[0]
            
            
        x0 = (i+30)*(WIDTH/60)
        x1 = x0
        y0 = (HEIGHT/2) + (height/2)
        y1 = (HEIGHT/2) - (height/2)
        if ray_tuple[1]:
            color = "red"
        else:
            color = "darkred"
            
        main_canvas.create_line(x0,y0,x1,y1,width=WIDTH/60,fill = color)
        
        for obj in game_objects:
            distance = (x - obj.get_x())**2 + (y-obj.get_y())**2
            rotatedImg = obj.get_sprite().resize((2,2))
            main_canvas.create_image(obj.get_x(),obj.get_y(),image=ImageTk.PhotoImage(rotatedImg))
            
       
           # main_canvas.create_line(i+30,0,i+30,height*100,width=10)
        

def GameLoop():
    #Game loop
    while True:
        
        EarlyUpdate()
    
        Update()
    
        LateUpdate()
    
        Render()
        
       
        root.update_idletasks()
        root.update()
        

def RayCast(x_pos,y_pos,ang): #The main issue is there needs to be smaller steps to stop the blocky look, but the height becomes too small with small steps
    
    if math.tan(ang) == 0:
        ang+= 0.001
   
    # i = 0
    # hit = False
    
    # ray_x = x_pos
    # ray_y = y_pos

    # while not hit:
    #     ray_x += math.cos(ang) *0.02
    #     ray_y += math.sin(ang) * 0.02
    #     i
        
    #     try:
            
           
    #         if map_array[int(ray_x//64)][int(ray_y//64)] == 1:
    #             distance = (ray_x - x_pos)**2 + (ray_y - y_pos)**2
    #             is the ray closer to a horizontal line or vertical line? 
    #             if ray_x%64 > ray_y%64:
    #                 vertical = true
    #             else:
    #                 vertical = false
    #             return math.sqrt((ray_x - x_pos)**2 + (ray_y - y_pos)**2), vertical
    horizontal_dist = 1000000
    vertical_dist = 10000000
        


    #CHECK HORIZONTAL
             #if looking down:
                 #ray_y = y - y%blocksize
                 #step = -blocksize
            #ray_y = blocksize - y%blocksize + y
            #ray_x = yn/tan(angle)
            #check if block at x_first,y_first is a wall
            #if it is, move to vertical, else:
                #While not hit:
                    #ray_y += blocksize
                    #ray_x += blocksize/tan(angle)
                    #if block at ray_x,ray_y is a wall, hit = true
    step = -BLOCKSIZE
    ray_y = 0
    if ang > 0 and ang < math.radians(180): #looking up
        
        ray_y = BLOCKSIZE - y_pos%BLOCKSIZE + y_pos #nearest y grid above
        
        step = BLOCKSIZE
        
        
    else:
        
        ray_y = y_pos - y_pos%BLOCKSIZE        #nearest y grid below
        
    
    ray_x = (ray_y-y_pos)/(math.tan(ang)) + x_pos
    
    try:
        
        while MAP_ARRAY[(int)(ray_y/BLOCKSIZE)][(int)(ray_x/BLOCKSIZE)] == 0 and MAP_ARRAY[(int)(ray_y/BLOCKSIZE)-1][(int)(ray_x/BLOCKSIZE)] == 0:
            
            ray_y += step
            ray_x += step/math.tan(ang)
            print(f"MAP ARRAY INDEXES: [{(int)(ray_y/BLOCKSIZE)}],[{(int)(ray_x/BLOCKSIZE)}]. Value = {MAP_ARRAY[(int)(ray_y/BLOCKSIZE)][(int)(ray_x/BLOCKSIZE)]}")
        horizontal_dist = math.sqrt((ray_x - x_pos)**2 + (ray_y - y_pos)**2)
        #print(f"HORIZONTAL HIT at y: {ray_y}")
    except Exception as e:
        
        horizontal_dist = 100000
            
       
    #CHECK VERTICALLY
    step = -BLOCKSIZE
    
    if ang > math.radians(270) or ang < math.radians(90): #looking right
        ray_x = BLOCKSIZE - x_pos%BLOCKSIZE + x_pos #nearest x grid to right
        step = BLOCKSIZE
        
    else:
        
        ray_x = x_pos - x_pos%BLOCKSIZE  #nearest x grid to left
        
    ray_y = (ray_x-x_pos)*(math.tan(ang)) +y_pos
    
    
        
    
    try:
        
        while MAP_ARRAY[(int)(ray_y/BLOCKSIZE)][(int)(ray_x/BLOCKSIZE)-1] == 0 and MAP_ARRAY[(int)(ray_y/BLOCKSIZE)][(int)(ray_x/BLOCKSIZE)] == 0:
            
            ray_x += step
            ray_y += step*math.tan(ang)
        vertical_dist = math.sqrt((ray_x - x_pos)**2 + (ray_y - y_pos)**2)
    except Exception as e:
        
        vertical_dist = 100000
    if vertical_dist > horizontal_dist:
        #map_canvas.create_line(x_pos,y_pos,ray_x,ray_y,width=5,fill="green",tags="delete")
        return horizontal_dist ,False
    
    else:
        #map_canvas.create_line(x_pos,y_pos,ray_x,ray_y,width=5,fill="blue",tags="delete")
        return vertical_dist , True
    
            
        
    

       
            
                

    
                
           
           
            
            
            
        

        
        
        
    
    

root = Tk()


#root.geometry(f"{width}x{height}")
root.attributes("-fullscreen",True)
root.resizable(width=False,height=False)
WIDTH = 1024
HEIGHT = 1024

main_frame = ttk.Frame(root)


main_canvas = Canvas(root,width=WIDTH,height=HEIGHT,bg="blue")
main_canvas.pack(side="right")

map_canvas = Canvas(root, width = 256,height=256,bg="black")
map_canvas.pack(side="left")

for i,row in enumerate(MAP_ARRAY):
    for j,block in enumerate(row):
        if block == 1:
            print(i,j,sep=" : ")
            map_canvas.create_rectangle(j*16,i*16,j*16+16,i*16+16,fill="red")
        else:
            map_canvas.create_rectangle(j*16,i*16,j*16+16,i*16+16,fill="pink")
    


game_objects = []

root.update_idletasks()
root.update()

input_handler = InputHandler()

root.bind("<KeyPress>",input_handler.SendInput)
root.bind("<KeyRelease>", input_handler.ResetInput)







StartGame()



    

