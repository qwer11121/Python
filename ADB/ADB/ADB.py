import subprocess
import shlex
import cv2
import numpy  as np

PIC = r"C:\Users\lukir\Pictures\screenshot.png"

def get_screen():
    pipe = subprocess.Popen("adb shell screencap -p",
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    return image

def show_image(image, scale_ratio=1):
    if scale_ratio != 1:
        image = scale_image(image,scale_ratio)
    cv2.startWindowThread()
    cv2.namedWindow("screen")
    cv2.imshow("screenshot",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def scale_image(image, ratio):
    height, width, channels = image.shape
    height *= ratio
    width *= ratio
    out = cv2.resize(image, (int(width),int(height)))
    return out

def show_image(image):
    cv2.imshow("new",image)
    cv2.waitKey()

def new_image(height, width, channel):
    image = np.zeros((height,width,channel))
    return image
    
if __name__ == "__main__":
    image=cv2.imread(PIC)
    height, width, channels = image.shape

    target = np.zeros(image.shape)

    cv2.waitKey()
    for row in range(rows):
        for column in range(columns):
            for channel in range(channels):
                #image.at<Vec3b>(row,column)[channel] = 9
                pass