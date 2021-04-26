f = open("Python Classes by me", "w")
f.write("Python is an Easy Language.")
f.write("\n It is used in Machine Learning.")
#print(f.read())


import os 

videoFile = open('E://SampleVideo_1280x720_2mb.mp4', 'rb')

if not os.path.exists('video.mp4') :
	createFile = open('video.mp4', 'x')
	createFile.close()

copyFile = open('video.mp4', 'wb')
copyFile.write(videoFile.read())
copyFile.close()
