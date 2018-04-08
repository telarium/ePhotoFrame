import subprocess

class ImageProcessing:
	def __init__(self,filename='nico-sleep.jpg',dither=1,color='red'):
		subprocess.call('wget http://cdn.abclocal.go.com/three/kgo/weather/maps/ebay1_1280.jpg -O /tmp/tmp.jpg')