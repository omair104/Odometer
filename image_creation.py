import os
from PIL import Image, ImageDraw, ImageFont
from PIL._imaging import font



def create_image(displayed_number, unit, counter, images_location):
    img = Image.new('RGBA', (1280, 720), (0,0,0,0))
    img_blue = Image.new('RGB', (150, 30), (51, 153, 255))
    img.paste(img_blue, (1100,600))
    img_blue.close()
    
    font = ImageFont.truetype("font.ttf", 24)
    display_on_image=str(displayed_number)+ ' '+ str(unit)
    d = ImageDraw.Draw(img)
    d.text((1100,600), display_on_image , fill=(255,255,255,128), font=font)
    image_name = images_location + str(counter) +  ".png"
    image_path = os.path.join(images_location, image_name)
    img.save(image_name)
    img.close()
    
def delete_images(images_location):
    a = os.listdir(images_location)
    for x in range(len(a)):
        p = os.path.join(images_location, a[x])
        if os.path.splitext(p)[1] =='.png':
            os.remove(p)
 
    
def create_video(path_of_images):
    os.chdir(path_of_images)
    os.system("ffmpeg -r 25 -i %01d.png -vf scale=1920:1080 -vcodec png -y movie.mov")
    #-vf scale=1920:1080
    #delete_images(path_of_images)
    

def main(entered_length=100, entered_unit='m', entered_time=5):
    images_location = "H:\\eclipse_workspace\\Odometer\\images"
    fps=25

    length_per_frame= entered_length/(entered_time*25)
    
    length_on_image=0
    counter=0
    for x in range(entered_time*25):
        create_image(round(length_on_image,1), entered_unit, counter, images_location)
        length_on_image = length_on_image + length_per_frame
        counter=counter+1

    create_video(images_location)
    
if __name__ == '__main__':
    main()
        

