import cv2
import os

cam = cv2.VideoCapture('videoplayback.mp4')
try:
 if not os.path.exists('temp'):
 os.mkdir('temp')
except OSError:
 print("Error: Creating Directory")

currentframe = 0
while (True):
 ret, frame = cam.read()
 if ret:
 name = './temp/' + str(currentframe) + '.jpg'
 print('Creating Frame')
 cv2.imwrite(name, frame)
 currentframe += 1
 else:
 break
cam.release()
cv2.destroyAllWindows() 