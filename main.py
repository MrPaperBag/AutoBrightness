import screen_brightness_control as sbc
import cv2
  
cam_port = 0

def take_picture():
	try:
		cam = cv2.VideoCapture(cam_port)
		result, image = cam.read()

		if result:
			return image
		else:
			print("Camera Failed")
		cam.release()
	except:
		print("Are you sure the camera is connected?")

def GetBrightness(Image):
	Sum = 0
	grayImage = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

	row = len(grayImage)
	column = len(grayImage[0])
	for i in grayImage:
		for j in i:
			Sum += j
	average = Sum/(len(grayImage)*len(grayImage[0]))
	return average

def SetBrightness(Brightness):
	sbc.fade_brightness(Brightness)

def AutoBright():
	Image = take_picture()
	Bright = GetBrightness(Image)
	print(Bright)
	SetBrightness((Bright*100/255))

if __name__ == '__main__':
	AutoBright()