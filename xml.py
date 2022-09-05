import sys
#import PIL.Image as Image
import os
#import PIL.ImageDraw as ImageDraw
from PIL import Image, ImageDraw
from bs4 import BeautifulSoup


print(sys.argv)

folder = sys.argv[1]

folder_content = os.listdir(folder)
for filename in folder_content:
    if filename.find(".xml") > 0:
        name = filename.split(".xml")[0]
        print(name)

        with open(filename,"r") as file:
            contents = file.readlines()
            contents = "".join(contents)
            soup = BeautifulSoup(contents,'xml')
            titles = soup.find_all('node')
            im = Image.open(name+".png")
            draw = ImageDraw.Draw(im)
            for title in titles:
                node = str(title)
                if node.count('node') == 1:
                    if node.count('bounds') != 1:
                        continue
                    print(node)
                    bound = node[node.index("bounds=")+9: node.index("]\" checkable=")]
                    print(bound)
                    bound = bound.split("][")
                    print(bound)
                    bl = bound[0].split(",")
                    tr = bound[1].split(",")
                    print(bl, " ", tr)

                    print("\n")
                    draw.rectangle([(int(tr[0]), int(tr[1])), (int(bl[0]), int(bl[1]))], width = 10, fill=None, outline="yellow")


            # write to stdout
        im.save(name + ".highlighted.png", "PNG")
            

