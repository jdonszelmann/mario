from PIL import Image
import os

files = [os.path.join(dirpath, filename) 	for dirpath, dirnames, filenames in os.walk("./Lib/data") 
											for filename in filenames
											if filename.endswith(".bmp")]
print(files)

for i in files: 
	img = Image.open(i)
	img = img.convert("RGBA")
	datas = img.getdata()

	newData = []
	for item in datas:
		if item[0] == 255 and item[1] == 0 and item[2] == 255:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)
	print(i)
	img.putdata(newData)
	img.save(i, "BMP")