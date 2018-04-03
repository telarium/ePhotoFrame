from imageProcessing import ImageProcessing
import os

class PhotoApp():
	def __init__(self):
		image = ImageProcessing(filename='nico-sleep.jpg',dither=1)
		#os.system('wget https://media.kron.com/nxs-krontv-media-us-east-1/Current_Temps_Bay_Area.jpg -O bay_area_temps.jpg')

		#image.replaceColor('bay_area_temps.jpg','#FFFF33','#FF0000')

photo = PhotoApp()
quit()
