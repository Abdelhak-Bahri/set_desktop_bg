# set_desktop_bg
this python script looks for pictures on pixabay api then set a slideshow destop backround on windows
</br><b> How to use:</b>
</br>simple call from cmd : python desktop_bg.py "tag_1 [tag_2[[+]tag_i]]"
</br><b> exemple :</b>
</br> > python desktop_bg.py "algerian sahara"
</br><b> exemple :</b>
</br> > python desktop_bg.py "china beauty"


<br> For more infos, check out the pixabay api : https://pixabay.com/api/docs/


<br> <b>Additional configurations: </b>
<br> you can parameter the script on changing variables 

<br> output_dir, dir to images output 
<br> api parameters: 
base_url="https://pixabay.com/api/"
key = ""  #get your api key from here : https://pixabay.com/api/docs/
q="" # tags to look for on pixabay 
image_type="photo" # specify the type of pictures
size = 10 # number of pictures to download , if set to zero , the script download all pictures found
