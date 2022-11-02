import numpy as np
import cv2
import os

def get_values():
    images = []
    for filename in os.listdir('images'):
        image = cv2.imread(os.path.join('images/'+filename))
        throttle = image[342:388, 633:647]
        brake = image[342:388, 618:632]
        right = image[390:397, 633:647]
        left = image[390:397, 618:632]

        green_min = np.array([0, 50, 0], np.uint8)
        green_max = np.array([60, 255, 60], np.uint8)

        dsg = cv2.inRange(throttle, green_min, green_max)
        no_throttle = cv2.countNonZero(dsg)
        print('The number of green pixels is: ' + str(no_throttle))

        red_min = np.array([0, 0, 50], np.uint8)
        red_max = np.array([40, 40, 255], np.uint8)

        dsb = cv2.inRange(brake, red_min, red_max)
        no_brake = cv2.countNonZero(dsb)
        print('The number of red pixels is: ' + str(no_brake))

        blue_min = np.array([60, 0, 0], np.uint8)
        blue_max = np.array([255, 40, 40], np.uint8)

        dst = cv2.inRange(right, blue_min, blue_max)
        no_right = cv2.countNonZero(dst)
        print('The number of right blue pixels is: ' + str(no_right))

        dsl = cv2.inRange(left, blue_min, blue_max)
        no_left = cv2.countNonZero(dsl)
        print('The number of left blue pixels is: ' + str(no_left))

        f = open('labels/'+filename+'.txt', 'w')
        f.write(f'{no_throttle},{no_brake},{no_left},{no_right}')
        f.close()

       # cv2.imshow('window', throttle)
        #if cv2.waitKey(25) & 0xFF == ord('q'):
         #   cv2.destroyAllWindows()
          #  break


get_values()