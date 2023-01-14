import cv2,os
import numpy as np
from django.conf import settings
import torch
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image




model = torch.hub.load('ultralytics/yolov5', 'custom', path=   os.path.join(
			settings.BASE_DIR,'yolo_weights/weights2/best.pt'), force_reload=True)

####### YOLO TEST IMLEMENTATION
class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		ret, frame = self.video.read()		
		results = model(frame)
		img = np.squeeze(results.render())
		# print(f"\nThe image is :\n\t{img}\n")
		# print(f"\nThe image type  is :\n\t{type(img)}\n")

		# print(f"\nThe image shape  is :\n\t{img.shape}\n")

		# frame_flip = cv2.flip(img,1)
		ret, jpeg = cv2.imencode('.jpg', img)
		return jpeg.tobytes()
		


#########  IN JUPYTER NOTEBOOK
# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
    
#     # Make detections 
#     results = model(frame)
    
#     cv2.imshow('YOLO', np.squeeze(results.render()))
    
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()