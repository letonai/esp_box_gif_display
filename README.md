# esp_box_gif_display
ESP_S3_BOX Micropython display for gifs

Use the script git_convert.sh to convert a gif into folder with a sequence of JPGs

```
./gif_convert.sh mygif.gif
mygif         = ['mygif'        ,30,0.010]
```
copy the folder mygif into the root folder of you ESP-S3-BOX and add the script output to the boot.py and the example:

```
    bella         = ['bella'        ,32,0.055]
    mygif         = ['mygif'        ,30,0.010] 
    choices = [bella,mygiff]
```