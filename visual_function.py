"drawing the percentage match visual"
from PIL import Image

def percentvisual(percent,width,height):
    im = Image.new("RGB", (width,height))
    
    limit = (width) * percent
    count = 0
    incrR = int (120 / (percent* width))
    incrG = int (100 / (percent * width))
    incrB = int (250 / (percent * width))
    r = 0
    g = 0
    b = 0

    print limit
    
    for x in range(width):
        for y in range(height):
            if count <= limit:
                im.putpixel((x,y), (r,g,b))
                if r <= 120:
                    r = r + incrR
                    print r
                if g <=100:
                    g = g + incrG
                    print g
                if b <= 250:
                    b = b + incrB
                    print b 
                count = count + 1
                '''

    print incrR
    print incrG
    print incrB
    print r
    print g
    print b
              
'''
    im.show()

percentvisual(.50,500,350)

'''
  
130 130 130

0 -> 130
130 / perscent*widgth = colored pixel

'''
