import os
import requests


images_dir = 'D:\Datasets\Street2Shop\images'
with open('photos/photos.txt', "r") as f:
	lines = f.readlines()

	for each in lines:
		myfile = requests.get(each.split(",")[1])
		if myfile.status_code == 200:
			open(os.path.join(images_dir, each.split(",")[0] + '.png'), 'wb').write(myfile.content)
			print(each.split(",")[0] + '.png')
