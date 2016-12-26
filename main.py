import arcade
import glob

#0 is idle or something
#1 is walking

class gameObjects:
    def __init__(self,x,y,width,height,path):
        self.state = 0
        self.hitbox = [x,y,x+width,y+height]
        fileList = glob.glob(path+"\*.png")
        self.sprites =[]
        spritesTemp = []
        for i in fileList[:2]:
            spritesTemp.append(arcade.Sprite(i))
        self.sprites.append(spritesTemp)
        spritesTemp = []
        for i in fileList[3:5]:
            spritesTemp.append(arcade.Sprite(i))
        self.sprites.append(spritesTemp)
        spritesTemp = []
        for i in fileList[6:8]:
            spritesTemp.append(arcade.Sprite(i))
        self.sprites.append(spritesTemp)


arcade.open_window("", 600, 600)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.run()
