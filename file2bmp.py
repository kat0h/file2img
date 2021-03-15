from PIL import Image, ImageDraw, ImageOps
import sys

args = sys.argv
if len(sys.argv) != 4:
    print("引数が不正")

ifile, out, imgsize = args[1], args[2], int(args[3])

f = open(ifile, 'rb')
b = f.read()

size = imgsize
img = Image.new("RGB", (size, size), (0, 0, 0))
draw = ImageDraw.Draw(img)

imgbgr = []
c = 0
flg = 1
while True:
    a = []
    try:
        a.append(b[c])
    except IndexError:
        a.append(0)
        break
    try:
        a.append(b[c+1])
    except IndexError:
        a.append(0)
        flg = 0
    try:
        a.append(b[c+2])
    except IndexError:
        a.append(0)
        flg = 0
    imgbgr.append((a[2], a[1], a[0]))
    c += 3
    if flg == 0:
        break

pos = 0
for i in imgbgr:
    x, y = pos % size, pos // size
    draw.point((x, y), i)
    pos += 1
img = ImageOps.flip(img)
img.save(out)
