from PIL import Image

img = Image.open("ch3llist4_.png")
img = img.convert("RGB")

datas = img.getdata()

new_image_data = []
for item in datas:
    # change all black (also shades of black) pixels to grey
    if item[0] in list(range(0, 20)):
        new_image_data.append((187, 186, 184))
    else:
        #new_image_data.append(item)
        new_image_data.append((97, 75, 77))
        
# update image data
img.putdata(new_image_data)

# save new image
img.save("result.png")

# show image in preview
img.show()