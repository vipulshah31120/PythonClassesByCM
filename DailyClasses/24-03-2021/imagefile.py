import os


imageFile = open('E://Vipul shah copy.jpg', 'rb') 	# rb = read binary
#imageFile = open('E://PAN CARD.jpg', 'rb')

if not os.path.exists('me.jpg'):
	createFile = open('me.jpg', 'x')
	createFile.close()

copyFile = open('me.jpg', 'wb') 	# wb = write binary
copyFile.write(imageFile.read())
copyFile.close()

