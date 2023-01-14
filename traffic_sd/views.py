from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from traffic_sd.model_engine import VideoCamera   #, IPWebCam #, MaskDetect, LiveWebCam
# Create your views here.


def index(request):
	return render(request, 'traffic_sd/home.html')


def feed_gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def video_feed(request):
	return StreamingHttpResponse(feed_gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

