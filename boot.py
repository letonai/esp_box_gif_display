'''
Random Gif

    Randomly display an animation on the display
    
    The cat image is from my cat and can be used with no attribution 
    
    It's based on the following Micropython firmware: 
    https://github.com/russhughes/st7789_mpy/tree/master/firmware/ESP32_BOX_LITE

'''

import gc
import random
import time
import tft_config
import machine

gc.enable()
gc.collect()


def main():

    tft = tft_config.config(1)
    tft.init()

    homer         = ['homer'        ,29,0.025]
    pikachu       = ['pikachu'      ,16,0.035]
    win95         = ['win95'        ,20,0.035]
    pika_slap     = ['pika_slap'    ,29,0.030]
    dwight_wig    = ['dwight_wig'   ,33,0.010]
    cuttingcanada = ['cuttingcanada',19,0.035]
    thatsallfolks = ['thatsallfolks',36,0.035]
    bella         = ['bella'        ,32,0.055]
    
    choices = [bella]
    
    current = choices[random.randint(0, len(choices)-1)]
    
    print("Current: "+current[0])
    
    decoded_bitmap = []
    fps = current[2]
    for sprite in range(current[1]):
        frame=current[0]+"/frame_"+str(f'{sprite:05}')+".jpg"
        print("Decoding frame: "+frame)
        decoded_bitmap.append(tft.jpg_decode(frame))
        
        print(len(decoded_bitmap[-1][0]))
        
    print(str(len(decoded_bitmap))+" frames loaded")
    print("Starting gif...")
    
    while True:
        for sprite in range(current[1]):
            tft.rotation(4)
            bm = decoded_bitmap[sprite]
            tft.blit_buffer(bm[0],0,0,bm[1], bm[2])
            time.sleep(fps)
        if random.randint(1,51) == 50:
            machine.reset()
        else:
            continue

main()

