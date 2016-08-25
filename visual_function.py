"drawing the percentage match visual"
from PIL import Image
import time

def percentvisual(percent,width,height, colors):
    im = Image.new("RGBA", (width,height), (250,250,250,0))

    
    limit = (width) * percent
    count = 0
    incrR = colors[0]/(percent* width)
    incrG = colors[1]/(percent * width)
    incrB = colors[2]/(percent * width)
     
    for x in range(height):
        r = colors[0] - (percent* width)
        if r < 0:
            r = int(colors[0]*0.2)
        g = colors[1] - (percent* width)
        if g < 0:
            g = int(colors[1]*0.2)
        b = colors[2] - (percent* width)
        if b < 0:
            b = int(colors[2]*0.2)
        count=0
        for y in range(width):
            if count <= limit:
                im.putpixel((y, x), (int(r),int(g),int(b),0))
                if r <= 120:
                    r = r + incrR
                if g <=100:
                    g = g + incrG
                if b <= 250:
                    b = b + incrB
                count = count + 1
                
    im.show()

percentvisual(0.75,600,50, (10, 255, 100))


