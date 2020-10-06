# 1.Play MP4 Video 
# Import Libraries required
import numpy as np
import cv2
# Create a VideoCapture Object
Cap_object = cv2.VideoCapture('C:\\Users\\vanit\Videos\\s.mp4')

while(True):
    ret, frame = Cap_object.read()

    cv2.imshow('Video',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
       break
# Release the video capture
# Closes all windows

Cap_object.release()
cv2.destroyAllWindows()

#******************************************************************************************************************************************************************************

# 2.Play MP4 Video 
# Create a VideoCapture object
Cap_object = cv2.VideoCapture(0)

 

# Check if camera opened successfully

if (Cap_object.isOpened() == False): 

  print("Problem with camera feed")

 

# Default resolutions of the frame 

frame_width = int(Cap_object.get(3))

frame_height = int(Cap_object.get(4))

 

# Define the codec and create VideoWriter object.

out = cv2.VideoWriter('Output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

# Rescale the resulting frame
def rescale_frame(frame, percent =75):
    width = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation =cv2.INTER_AREA)
 
while(True):

  ret, frame = Cap_object.read()
  frame = rescale_frame(frame, percent =160)

  if ret == True:      

    # Write the frame into the file 'Output.avi'

    out.write(frame)

    # Display frame    

    cv2.imshow('frame',frame)

    # Press Q to stop

    if cv2.waitKey(1) & 0xFF == ord('q'):

      break 

  else:

    break 


# Release the video capture and write objects

Cap_object.release()

out.release()

# Closes all the frames

cv2.destroyAllWindows()



#*******************************************************************************************************************************************************************************

# 3. To play Youtube Video 

import webbrowser

url = 'https://youtu.be/RWV5EkZppVI'
webbrowser.open(url)
        
