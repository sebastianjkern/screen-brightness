import wmi
import cv2
    
brightness = 80 
c = wmi.WMI(namespace='wmi')
methods = c.WmiMonitorBrightnessMethods()[0]    
methods.WmiSetBrightness(brightness, 0)

import numpy as np
import cv2
import time

# Connect to the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Calculate the average brightness of the frame
    avg_brightness = np.mean(frame)

    # Map the average brightness to a value between 0 and 100
    new_brightness = int(avg_brightness / 255 * 100)

    # Set the screen brightness to the calculated value
    methods.WmiSetBrightness(new_brightness, 0)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(2.0)

# Release the webcam
cap.release()

# Close all open windows
cv2.destroyAllWindows()