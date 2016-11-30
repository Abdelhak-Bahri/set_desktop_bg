#This script use the pixabay api to collect photos using tags and set them as slideshow desktop background 
import ctypes
import requests
import json
import shutil
import sys
import os


#base_dir="D:\\workspace\\set_desktop_bg\\" #directory to the main.py , get it by code dynamically is better
base_dir = os.path.dirname(os.path.abspath(__file__))
base_url="https://pixabay.com/api/"
key="3847786-5a338eb8002ec90f2352269a4" #get your api key from here : https://pixabay.com/api/docs/
q=""
image_type="photo" # photo vector illustration all
size = 0 # number of pictures to download
per_page="200"

def set_background(path):
    #print "setting ", path , "as bg"
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path , 2)

#construct the link to fetch for pictures
def get_link(query):
    return base_url+'?key='+key+'&q='+query+'&image_type='+image_type+'&per_page='+per_page

#get images
def get_images(query, size):
    output_dir = base_dir + "\\output\\" + "\\" + query + "\\"
    if not os.path.exists(os.path.dirname(output_dir)):
        os.makedirs(os.path.dirname(output_dir))
    url = get_link(query)
    #print url
    try:
        get_response= requests.get(url=url)
        jsonfile = output_dir + query + ".txt"
        with open(jsonfile, 'w') as json_file:
            json_file.write(get_response.text)            
    except requests.exceptions.Timeout:
        print "timeout or connection error"
    except requests.exceptions.ConnectionError:
        print "timeout or connection error"
    if get_response.status_code ==200:
        json_text = get_response.text
        json_object = json.loads(json_text)
        # if size is unset , get all pictures on json 
        if size == 0 :
            size = json_object['totalHits']
            #print size
        for i in range(size):
            print i
            try:
                image_url = json_object['hits'][i]['webformatURL']
            except IndexError:
                print " index error"
                continue 
            image_url = image_url.replace("_640", "_960")
            #print image_url
            file_name = output_dir + str(json_object['hits'][i]['id']) + ".jpg"
            if not os.path.exists(os.path.abspath(file_name)):
                print file_name
                try:
                    get_image = requests.get(image_url, stream=True)
                except requests.exceptions.Timeout,requests.exceptions.ConnectionError:
                    print "timeout or connection error" 
                if get_image.status_code == 200 :
                    with open(file_name, 'wb') as out_file:
                        shutil.copyfileobj(get_image.raw, out_file)
		#set_background(output_dir)
#main call
get_images(sys.argv[1],int(per_page))