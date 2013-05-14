from PIL import Image, ImageDraw
import sys

def drawAntennas(pos):
    geo = Image.new("RGB",(640,400))
    draw = ImageDraw.Draw(geo)
    ant1 = (int(pos.pop(0)), int(pos.pop(0)), int(pos.pop(0)))
    ant2 = (int(pos.pop(0)), int(pos.pop(0)), int(pos.pop(0)))
    ant3 = (int(pos.pop(0)), int(pos.pop(0)), int(pos.pop(0)))
    draw.ellipse((ant1[0]-2,ant1[1]-2, ant1[0]+2, ant1[1]+2), fill = 'yellow')
    draw.ellipse((ant1[0]-ant1[2], ant1[1]-ant1[2], ant1[0]+ant1[2], ant1[1]+ant1[2]), outline = 'yellow')

    draw.ellipse((ant2[0]-2,ant2[1]-2, ant2[0]+2, ant2[1]+2), fill = 'blue')
    draw.ellipse((ant2[0]-ant2[2], ant2[1]-ant2[2], ant2[0]+ant2[2], ant2[1]+ant2[2]), outline = 'blue')

    draw.ellipse((ant3[0]-2,ant3[1]-2, ant3[0]+2, ant3[1]+2), fill = 'green')
    draw.ellipse((ant3[0]-ant3[2], ant3[1]-ant3[2], ant3[0]+ant3[2], ant3[1]+ant3[2]), outline = 'green')
    #geo.show()
    return ant1, ant2, ant3, geo

def target(ant1, ant2, ant3, geo):
    x = ( ( ( (ant1[2]**2-ant2[2]**2) + (ant2[0]**2-ant1[0]**2) + (ant2[1]**2-ant1[1]**2) ) * (2*ant3[1]-2*ant2[1]) - ( (ant2[2]**2-ant3[2]**2) + (ant3[0]**2-ant2[0]**2) + (ant3[1]**2-ant2[1]**2) ) * (2*ant2[1]-2*ant1[1]) ) / ( (2*ant2[0]-2*ant3[0]) * (2*ant2[1]-2*ant1[1]) - (2*ant1[0]-2*ant2[0]) * (2*ant3[1]-2*ant2[1] ) ) )
    
    y = ( (ant1[2]**2-ant2[2]**2) + (ant2[0]**2-ant1[0]**2) + (ant2[1]**2-ant1[1]**2) + x*(2*ant1[0]-2*ant2[0])) / (2*ant2[1]-2*ant1[1])
    
    draw = ImageDraw.Draw(geo)
    draw.ellipse((x-2,y-2, x+2, y+2), fill = 'red')
    geo.show()

if __name__ == '__main__':
    '''pos = positions '''
    pos = []
    for i in sys.argv:
        pos.append(i)
    pos.pop(0)
    ant1, ant2, ant3, geo = drawAntennas(pos)
    target(ant1, ant2, ant3, geo)
