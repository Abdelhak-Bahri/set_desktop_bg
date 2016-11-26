#This script use the pixabay api to collect photos using tags and set them as slideshow desktop background 
import ctypes
import requests
import json
import shutil
import sys

base_dir="D:\\workspace\\set_desktop_bg\\" #directory to the main.py , get it by code dynamically is better
output_dir= base_dir+"img\\" #
base_url="https://pixabay.com/api/"
key="3847786-5a338eb8002ec90f2352269a4" #get your api key from here : https://pixabay.com/api/docs/
q=""
#image_type="photo"

def set_background(path):
    #print "setting ", path , "as bg"
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path , 0)

#construct the link to fetch for pictures
def get_link(query):
    return base_url+'?key='+key+'&q='+query

#get images
def get_images(query):
    url = get_link(query)
    #print url
    get_response= requests.get(url=url)
    if get_response.status_code ==200:
        json_text = get_response.text
        json_object = json.loads(json_text)
        size = json_object['totalHits']
        for i in range(size):
            image_url = json_object['hits'][i]['webformatURL']
            image_url = image_url.replace("_640", "_960")
            print image_url
            file_name = output_dir + str(json_object['hits'][i]['id']) + ".jpg"
            print file_name
            get_image = requests.get(image_url, stream=True)
            if get_image.status_code == 200 :
                with open(file_name, 'wb') as out_file:
                    shutil.copyfileobj(get_image.raw, out_file)
                del get_image
            #set_background(file_name)
#main call
get_images(sys.argv[1])