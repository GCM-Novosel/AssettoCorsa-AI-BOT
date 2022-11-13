import numpy as np
import cv2
import os

#we are getting values for each input from the frames by opening each frame and pinpointing the ROI for each value by the coordinates where it is represented on the frame
def get_values():
    images = []
    for filename in os.listdir('images'):
        image = cv2.imread(os.path.join('images/'+filename))
        throttle = image[342:388, 633:647]
        brake = image[342:388, 618:632]
        right = image[390:397, 633:647]
        left = image[390:397, 618:632]
        
# after we defined the ROIs, we need to determine color ranges from which we will count the amounth of pixels in the specific ROI
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

# we create .txt files named the same as the images they are reffering to and writing the obtained values in them       
        f = open('labels/'+filename+'.txt', 'w')
        f.write(f'{no_throttle},{no_brake},{no_left},{no_right}')
        f.close()
        
# NOT FINISHED OR TESTED!!!! create a function for nomralizing values        
def normalize_values():
	max_throttle = 590
	max_brake = 590
	max_left = 270
    max_right = 270

	for filename in os.listdir('labels'):
		f = open(filename)
		values = f.read(filename)
		t, b, l, r = values.split (',')
        nt = t/max_throttle
        nb = b/max_brake
        steering = 0.0
        if l>r :
            steering = l/max_left * -1
        elif r>l :
             steering = r/max_right
        else:
            steering = 0.0
                


get_values()
