import subprocess

class ImageProcessing:
	def __init__(self,filename='nico-sleep.jpg',dither=1,color='red'):
		clut = color+".clut"

		ditherMethod = "None"
		if dither == 1:
			ditherMethod = 'FloydSteinberg'
		elif dither == 2:
			ditherMethod = 'Riemersma'

		subprocess.call('convert ' + filename + ' -geometry x640 -gravity center -crop 384x640+0+0 -dither ' + ditherMethod + ' -remap txt:' + clut + ' -auto-level output.png',shell=True)

	def replaceColor(self,filename,color1,color2):
		subprocess.call('mogrify -path ' + filename + ' -format png -fill "' + color1 + '" -opaque "' + color2 + '" temp.png',shell=True)

