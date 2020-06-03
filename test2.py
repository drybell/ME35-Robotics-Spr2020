from tempfile import NamedTemporaryFile
import imutils
import cv2
from time import sleep 

x_pos = 0
y_pos = 0
width = 0
height = 0 

vs = cv2.VideoCapture(0)

# initialize the first frame in the video stream
firstFrame = None
# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	ret, frame = vs.read()
	if ret:
		cv2.imshow("Feed", frame)
	else:
		pass

vs.release()
cv2.destroyAllWindows()