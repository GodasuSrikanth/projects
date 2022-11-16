from PIL import Image

# def resize_image(sizel, size2) :

image = Image.open('Mphasis_Logo.jpg')

print(f"Current size : {image.size}" )

resized_image = image.resize(( 500, 500 ))            

resized_image.save('Mphasis_Logo4.jpg')




"""
from PIL import Image
 def resize_image(sizel, size2) :
    image = Image.open('Mphasis-logo.jpg')

    print(f"Current size : {image.size}" )

    resized_image = image.resize(( sizel, size2))

    resized_image.save('Mphasis-logo1' + str(size1) + '.jpg')

size1 = int(input( ' Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1, size2) """