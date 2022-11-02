import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record():
    img_name = 0
    last_time = time.time()
    while(True):
        printscreen =  np.array(ImageGrab.grab(bbox=(1,80,707,481)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        #cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        cv2.imwrite('images/'+str(img_name)+'.jpg',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        img_name += 1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()