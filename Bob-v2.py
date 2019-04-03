import pygame
import time
import os, random #to get random file
from pathlib import Path
import RPi.GPIO as GPIO

GPIO.setwarnings(False) #do not display the warnings
GPIO.setmode (GPIO.BCM) #or GPIO.setmode(GPIO.BOARD)

GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor as input"
GPIO.add_event_detect(14, GPIO.RISING)

#FUNCTIONS ----------------------------------------------------------------------------------------------------------------------------------

def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img

def textOutline(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img

def new_cap():
    print("new cap")
    file = open("caps.txt","w") 
    file.write('%d' % (cap + 1)) 
    file.close() 
    play_random_sound()
    #show_random_image()

def get_caps_amount():
    with open("caps.txt") as file: #with statment corresponds to c# using
        return int(file.readline())
            
def play_random_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(base_path+'sounds/' + get_random_file("sounds"))
    pygame.mixer.music.play()

def get_random_file(directory):
    return random.choice(os.listdir(base_path+directory + "/"))
    
def show_random_image():
    random_image = pygame.image.load(base_path+'images/' + get_random_file("images"))
    position_x = 0
    position_y = 0
    height = random_image.get_height()
    width = random_image.get_width()
    if height > width :
        scale = display_height/height
        newheight = display_height
        newwidth = display_width/scale
        position_x = dw_half-(newwidth/2)
    elif height == width :
        newheight = display_height
        newwidth = display_width
    else :
        scale = display_width/width
        newheight = height*scale
        newwidth = display_width
        position_y = dh_half-(newheight/2)
    scaled = pygame.transform.scale(random_image, (int(newwidth), int(newheight)))
    screen.blit(scaled, (position_x, position_y))
    pygame.display.update()
    time.sleep(5) #random pic display time in seconds

def get_new_frame(frame_index, frame_dir) :
    if Path(base_path+"video_backgrounds/"+frame_dir+"/"+str(frame_index)+".jpeg").is_file() :
        frame = pygame.image.load(base_path+"video_backgrounds/"+frame_dir+"/"+str(frame_index)+".jpeg")
        frame_index = frame_index + 1
    else :
        frame_index = 0
        frame = pygame.image.load(base_path+"video_backgrounds/"+frame_dir+"/"+str(0)+".jpeg")
    screen.blit(frame, (0, 0))
    return frame_index
    

#INITIALIZATION ----------------------------------------------------------------------------------------------------------------------------------

pygame.init()

#initiate variables
base_path = "/home/pi/Documents/Bob_Raoul_v2/"
cap = int()
cap = get_caps_amount()
frame_dir = str()
frame_dir = get_random_file("video_backgrounds")
frame_index = 0

display_width = 1280
display_height = 1024
dw_half = display_width/2
dh_half = display_height/2

screen = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)

#colors
black = (0,0,0)
white = (255,255,255)
grey = (100,100,100)

# draw text
font = pygame.font.Font(None, 250)

#clock = pygame.time.Clock()
exit = False
#bg = pygame.image.load("background.png") get single background

#create our fancy text
bigfont = pygame.font.Font(None, 1000)


#MAIN LOOP ----------------------------------------------------------------------------------------------------------------------------------

while not exit:
    if GPIO.event_detected(14):
        new_cap()
        cap = get_caps_amount()
        frame_dir = get_random_file("video_backgrounds")
        #time.sleep(1) #security timer
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit = True
            elif event.key == pygame.K_INSERT:
                new_cap()
                cap = get_caps_amount()
                frame_dir = get_random_file("video_backgrounds")
    
    #text1 = textHollow(bigfont, str(cap), white)
    text2 = textOutline(font, str(cap), grey, white)
    
    #screen.blit(bg, (0, 0)) display single background
    #screen.blit(text1, (dw_half-(text1.get_width()/2), dh_half-(text1.get_height()/2))) #display invisible text with only border
    
    frame_index = get_new_frame(frame_index, frame_dir)
    
    #text = font.render(str(cap), True, black)
    #text_rect = text.get_rect(center=(display_width/2, display_height/2))
    #screen.blit(text, text_rect)
    
    #screen.blit(text2, (dw_half-(text2.get_width()/2), dh_half-(text2.get_height()/2)))
    screen.blit(text2, (display_width-(text2.get_width()), display_height-(text2.get_height())))
    
    pygame.display.update()
    
    #clock.tick(60)

pygame.quit()
quit()