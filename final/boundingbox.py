
import imutils
import cv2
from time import sleep 
import requests
import json 


def Get_SL(Tag):
    Key = "j2m40Z2Dd2MyPJcsmCSh586VCtvx68ltYwJjZCHujB"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    try:
        value = requests.get(urlValue,headers=headers).text
        data = json.loads(value)
        #print(data)
        result = data.get("value").get("value")
    except Exception as e:
        print(e)
        result = 'failed'
    return result

def Put_SL(Tag, Type, Value):
    Key = "j2m40Z2Dd2MyPJcsmCSh586VCtvx68ltYwJjZCHujB"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    propValue = {"value":{"type":Type,"value":Value}}
    try:
        reply = requests.put(urlValue,headers=headers,json=propValue).text
    except Exception as e:
        print(e)         
        reply = 'failed'
    return reply

Put_SL("stage1", "STRING", "False")
Put_SL("stage2", "STRING", "False")
Put_SL("stage3", "STRING", "False")
Put_SL("start", "STRING", "False")

while Get_SL("start") != "True": 
	print("Waiting for EV3")
	sleep(.25)

x_pos = 0
y_pos = 0
width = 0
height = 0 

vs = cv2.VideoCapture(0)
sleep(2)

if vs.isOpened(): # try to get the first frame
	rval, frame = vs.read()
else:
	rval = False	

## DEFINE CHECKPOINT AREAS 

### 129-647 in the y, 242:1003 in the x

### stage 1 overall box:  310,106 top left 
#  						  438,201 bottom right

### stage 2 overall box:  627,309 top left 
#                         750,421 bottom right

### stage 3 overall box:  387,356 top left
# 						  539,471 bottom right 

#positions    0 0 0 1   1 0 1 1 
stage1box = [[310,106],[438,201]]
stage2box = [[627,309],[750,430]]
stage3box = [[387,356],[539,471]]

#modify to expand the boxes defined above. starting at +- 8px 
latency   = 8

ball_guesses = []

guess_box1 = []
guess_box2 = []
guess_box3 = []
guess_latency = 5

### FOR TESTING PURPOSES:
### IF CENTER BUTTON OF EV3 IS PRESSED, BEGIN IMAGE PROCESSING
### DONE BY SYSTEMLINK STARTER TAG 

### OTHERWISE, BEGIN BY SYSTEMLINK TAG START28 BEING SET TO TRUE
stage1flag = False
stage2flag = False
stage3flag = False 
# initialize the first frame in the video stream
firstFrame = None
# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	if stage1flag and (Get_SL("stage1") == "False"):
		stage1flag = False
	if stage2flag and (Get_SL("stage2") == "False"):
		stage2flag = False
	if stage3flag and (Get_SL("stage3") == "False"):
		stage3flag = False

	ret, frame = vs.read()
	text = "Unoccupied"

	# if ret: 
	# 	print("frame successful")
	frame = cv2.resize(frame, (1280,800),interpolation=cv2.INTER_NEAREST)
	frame = frame[129:647, 242:1003]
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (11, 11), 0)
	if firstFrame is None:
		firstFrame = gray 

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)


	count = 0
	# loop over the contours
	check = True
	for c in cnts:
		if cv2.contourArea(c) < 50 or cv2.contourArea(c) > 150:
			continue
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		#coors = (x, y, w ,h)
		#print("%(x_pos)d %(y_pos)d %(width)d %(height)d" % {"x_pos" : x_pos, "y_pos" : y_pos, "width" : width, "height" : height})
		x_pos = x
		y_pos = y
		width = w
		height = h
		if check:
			if x > stage1box[0][0] and x < stage1box[1][0] and y > stage1box[0][1] and y < stage1box[1][1]:
				if stage1flag: 
					if x <= (guess_box1[0] + guess_latency) and y <= (guess_box1[1] + guess_latency):
						print("Ball tracked in Stage 1.....")
						guess_box1 = [x,y,width,height]
					else: 
						print("Misfire")
				else: 
					#trigger stage 1 firing 
					print("Ball at Stage 1 *FIRED STAGE1*")
					ball_guesses.append([x,y])
					guess_box1 = [x,y,width,height]
					Put_SL("stage1", "STRING", "True")
					#ONCE THE EV3 DOES THE COMMAND, IT WILL TURN THE TAG BACK TO FALSE 
					stage1flag = True
					check = False
			elif x > stage2box[0][0] and x < stage2box[1][0] and y > stage2box[0][1] and y < stage2box[1][1]:
				if stage2flag: 
					if x <= (guess_box2[0] + guess_latency) and y <= (guess_box2[1] + guess_latency):
						print("Ball tracked in Stage 2.....")
						guess_box2 = [x,y,width,height]
					else: 
						print("Misfire")
				else: 
					#trigger stage 1 firing 
					print("Ball at Stage 2 *FIRED STAGE2*")
					ball_guesses.append([x,y])
					guess_box2 = [x,y,width,height]
					Put_SL("stage2", "STRING", "True")
					#ONCE THE EV3 DOES THE COMMAND, IT WILL TURN THE TAG BACK TO FALSE 
					stage2flag = True
					check = False
			elif x > stage3box[0][0] and x < stage3box[1][0] and y > stage3box[0][1] and y < stage3box[1][1]:
				if stage3flag: 
					if x <= (guess_box3[0] + guess_latency) and y <= (guess_box3[1] + guess_latency):
						print("Ball tracked in Stage 3.....")
						guess_box3 = [x,y,width,height]
					else: 
						print("Misfire")
				else: 
					#trigger stage 1 firing 
					print("Ball at Stage 3 *FIRED STAGE3*")
					ball_guesses.append([x,y])
					guess_box3 = [x,y,width,height]
					Put_SL("stage3", "STRING", "True")
					#ONCE THE EV3 DOES THE COMMAND, IT WILL TURN THE TAG BACK TO FALSE 
					stage2flag = True
					check = False
			elif stage3flag and x <= 320:
				print("DONE")
				Put_SL("start", "STRING", "False")
			else: 
				print("Ball at hidden position")
		else: 
			continue
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Activity"

	cv2.putText(frame, "Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

	cv2.imshow("Feed", frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		Put_SL("start", "STRING", "False")
		break
 
	# cv2.imshow("Thresh", thresh)
	# cv2.imshow("Frame Delta", frameDelta)

vs.release()
cv2.destroyAllWindows()