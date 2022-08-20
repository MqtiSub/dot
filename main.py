import cv2
import numpy as np
from mcje.minecraft import Minecraft
import param_MCJE as param

colors = {
'WHITE' : [0,0,0],
'ORANGE' : [238,120,0],
'MAGENTA' : [209,58,132],
'LIGHT_BLUE' : [137,189,222],
'YELLOW' : [255,255,0],
'LIME' : [50,205,50],
'PINK' : [255,192,203],
'GRAY' : [94,95,98],
'LIGHT_GRAY' : [179,184,187],
'CYAN' : [0,142,148],
'PURPLE' : [186,85,211],
'BLUE' : [0,0,255],
'BROWN' : [150,85,52],
'GREEN' : [0,255,0],
'RED' : [255,0,0],
'BLACK' : [0,0,0],
}

STA_X = 0 ; STA_Y =70 ; STA_Z = 0

def mosaic(_pass,alpha):
    img = cv2.imread(_pass)
    h,w,ch = img.shape
    img = cv2.resize(img,(int(w*alpha),int(h*alpha)))
    mosaic_image = "./images/mosaic.png"
    cv2.imwrite(mosaic_image,img)
    return mosaic_image

def color_to_16(mosaic_image):
    img = cv2.imread(mosaic_image)
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    q = []
    for line in img_rgb:
        p = []
        for dot in line:
            graph = []
            name = [f'{_}'for _ in colors.keys()]
            for color in colors.values():
                count = 0
                for num,amo in enumerate(color):
                    count += np.abs(dot[num] - amo)
                graph.append(count)
            p.append(colors[name[graph.index(min(graph))]])
        q.append(p)
    q_ndarray = np.array(q,dtype=np.uint8)
    new_image = cv2.cvtColor(q_ndarray,cv2.COLOR_RGB2BGR)
    img16 = "./images/output.png"
    cv2.imwrite(img16,new_image)
    return img16

def draw_mc(img16):
    mc = Minecraft.create(port=param.PORT_MC)
    img = cv2.cvtColor(cv2.imread(img16),cv2.COLOR_BGR2RGB)
    line_offset = 0
    for line in img:
        dot_offset = 0
        for dot in line:
            p = [k for k,a in colors.items() if a[0] == dot[0]]
            q = [k for k in p if colors[k][1] == dot[1]]
            r = [k for k in q if colors[k][2] == dot[2]]
            color16 = r[0]
            if color16 == 'WHITE':
                block_id = param.CONCRETE
            elif color16 == 'ORANGE':
                block_id = param.ORANGE_CONCRETE
            elif color16 == 'MAGENTA':
                block_id = param.MAGENTA_CONCRETE
            elif color16 == 'LIGHT_BLUE':
                block_id = param.LIGHT_BLUE_CONCRETE
            elif color16 == 'YELLOW':
                block_id = param.YELLOW_CONCRETE
            elif color16 == 'LIME':
                block_id = param.LIME_CONCRETE
            elif color16 == 'PINK':
                block_id = param.PINK_CONCRETE
            elif color16 == 'GRAY':
                block_id = param.GRAY_CONCRETE
            elif color16 == 'LIGHT_GRAY':
                block_id = param.LIGHT_GRAY_CONCRETE
            elif color16 == 'CYAN':
                block_id = param.CYAN_CONCRETE
            elif color16 == 'PURPLE':
                block_id = param.PURPLE_CONCRETE
            elif color16 == 'BLUE':
                block_id = param.BLUE_CONCRETE
            elif color16 == 'BROWN':
                block_id = param.BROWN_CONCRETE
            elif color16 == 'GREEN':
                block_id = param.GREEN_CONCRETE
            elif color16 == 'RED':
                block_id = param.RED_CONCRETE
            elif color16 == 'BLACK':
                block_id = param.BLACK_CONCRETE
            
            mc.setBlock(STA_X + dot_offset,STA_Y,STA_Z + line_offset,block_id)
            dot_offset += 1
        line_offset += 1


if __name__ == '__main__':
    draw_mc('./images/newimage.png')

