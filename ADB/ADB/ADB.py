import subprocess
import shlex
import cv2
import numpy  as np

# 点格式: [Blue, Green, Red]
# 行格式: [点, 点, 点, ... , 点]
# 图片格式: [行, 行, 行, ... , 行]
# 取点: image[y,x]=点 或 image[y][x]=点 或 image[y][x][通道]=255  通道: 0:Blue; 1:Green; 2:Red

PIC = r"screenshot.png"

def get_screen():
    pipe = subprocess.Popen("adb shell screencap -p",
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    return image

def show_image(image, scale_ratio=1, title="screenshot"):
    if scale_ratio != 1:
        image = scale_image(image,scale_ratio)
    cv2.startWindowThread()
    cv2.namedWindow(title)
    cv2.imshow(title,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def scale_image(image, ratio):
    height, width, channels = image.shape
    height *= ratio
    width *= ratio
    out = cv2.resize(image, (int(width),int(height)))
    return out

def create_image(height, width, channel):
    image = np.zeros((height,width,channel))
    return image

def test(image):
    height, width, channels = image.shape
    for y in range(int(height)):
        for x in range(int(width)):
            image[y,x]=[255,0,0]    # Blue, Green, Red
    show_image(image)
    return

def init(image, div):
    height, width, channel = image.shape
    for y in range(height):
        for x in range(width):
            for c in range(channel):
                image[y,x,c]=image[y,x,c]//div*div+div//2
    return image

    
if __name__ == "__main__":
    image= scale_image(cv2.imread(PIC),0.5)
    height, width, channels = image.shape
    im=init2(image,32)
    show_image(im,title="im")
    #test(target)
