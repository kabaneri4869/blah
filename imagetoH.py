from PIL import Image
import numpy as np

img = Image.open('image.jpg')

arr = np.asarray(img)
print(arr.shape)

lst = []
for row in arr:
 tmp = []
 for col in row:
 tmp.append(str(col))
 lst.append(tmp)

with open('my_file.csv', 'w') as f:
 for row in lst:
 f.write(','.join(row) + '\n') 