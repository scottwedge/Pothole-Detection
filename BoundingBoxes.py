from PIL import Image, ImageDraw
import os

def  BoundingBoxes(img, pos, boundedFolder, counter):
    print(counter)


    try:
        im = Image.open(img)
        print("Image Opened")
        key = True
    except:
        key = False

    if key == True:
        draw = ImageDraw.Draw(im)
        for j in range(len(pos)):
            draw.rectangle((int(pos[j][0]),int(pos[j][1]),int(pos[j][2])+int(pos[j][0]),int(pos[j][3])+int(pos[j][1])), outline="black")
            print("Box Drawn")
        #im.show()
        try:
            #print(boundedFolder[0])
            im.save(boundedFolder[0]+str(counter)+".jpg")
            print("Image Saved")
        except:
            #print(boundedFolder[0])
            os.makedirs(boundedFolder[0])
            im.save(boundedFolder[0]+str(counter)+".jpg")
    else:
        print("Image Not Found: Skipped")

if __name__ == '__main__': BoundingBoxes("C:/CNN/G0010033.JPG",[[1990, 1406, 66, 14], [1464, 1442, 92, 16], [1108, 1450, 54, 16], [558, 1434, 102, 16], [338, 1450, 72, 18], [262, 1450, 58, 22]], "./Test/", 1)
