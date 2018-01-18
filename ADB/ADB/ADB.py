import subprocess
import shlex
import cv2
import np

def get_screen():
    pipe = subprocess.Popen("adb shell screencap -p",
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow("", image)
    cv2.waitKey(0)
    cv2.destroyWindow("")
    

get_screen()