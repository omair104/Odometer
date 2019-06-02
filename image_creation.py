import os
from PIL import Image, ImageDraw



def create_image(displayed_number, unit, counter, images_location):
    img = Image.new('RGBA', (1280, 720), (255,255,255,0))
    img_blue = Image.new('RGB', (100, 20), (51, 153, 255))
    img.paste(img_blue, (1100,650))
    img_blue.close()
    
    display_on_image=str(displayed_number)+ ' '+ str(unit)
    d = ImageDraw.Draw(img)
    d.text((1110,655), display_on_image , fill=(255,255,255,128))
    image_name = images_location + str(counter) +  ".png"
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
    os.system("ffmpeg -r 25 -i %01d.png -vcodec mpeg4 -y movie.mp4")
    delete_images(path_of_images)
    

def main(entered_length=100, entered_unit='m', entered_time=5):
    images_location = "H:\\eclipse_workspace\\Odometer\\images\\"
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
        

