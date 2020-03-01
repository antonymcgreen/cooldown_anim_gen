from PIL import Image, ImageDraw

FRAMES = 24
SIZE = (100,100)
COLOR1 = (255,255,255,0)
COLOR2 = (255,255,255,128)

def drawCircle(dr, degree):
    dr.pieslice([(0,0), SIZE], 270, degree-90, fill=COLOR1)
    dr.pieslice([(0,0), SIZE], degree-90, 270, fill=COLOR2)

def makePics():
    atlas = Image.new('RGBA', (SIZE[0]*FRAMES, SIZE[1]))
    for i in range(FRAMES):
        pic = Image.new("RGBA", SIZE)
        draw = ImageDraw.Draw(pic)
        drawCircle(draw, 360/FRAMES*i)
        pic.save('output/{}.png'.format(i),'PNG')
        atlas.paste(pic, (SIZE[0]*i, 0, SIZE[0]*(i+1), SIZE[1]))
    atlas.save('output/atlas.png', 'PNG')

makePics()