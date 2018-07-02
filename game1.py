import pygame
import time
import random


pygame.init()
width=800
height=600
gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption('Game on')
clock=pygame.time.Clock()
pause=False
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
bright_green=(0,255,0)
bright_red=(255,0,0)
blue=(0,0,255)
img=pygame.image.load('racecar.png')
backgrnd_img=pygame.image.load('background.png')
crash_sound = pygame.mixer.Sound("crash.wav")
def score(count):
	font=pygame.font.SysFont(None,45)
	text=font.render("Score:"+str(count),True,white)
	gameDisplay.blit(text,(0,0))
def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def im(x,y):
	gameDisplay.blit(img,(x,y))

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,color):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText,color)
	TextRect.center = ((width/2),(height/2))
	gameDisplay.blit(backgrnd_img,[0,0])
	gameDisplay.blit(TextSurf, TextRect)
	
	pygame.display.update()

	time.sleep(2)
	
def text_objects2(text,count,font):
    textSurface = font.render(text+str(count), True, blue)
    return textSurface, textSurface.get_rect()	
	
def score_display(text,count):
	largetext=pygame.font.Font('freesansbold.ttf',105)
	textsurf,textrect=text_objects2(text,count,largetext)
	textrect.center=((width/2),(height/2))
	gameDisplay.blit(backgrnd_img,[0,0])
	gameDisplay.blit(textsurf,textrect)
	pygame.display.update()
	time.sleep(2)
	
    
def quitgame():
	pygame.quit()
	quit()
def button(msg,x,y,w,h,i,a,action=None):
		mouse=pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()
		if x+w>mouse[0]>x and y+h>mouse[1]>y:
			pygame.draw.rect(gameDisplay,a,(x,y,w,h))
			if click[0]==1 and action!=None:
				action()
		else:
			pygame.draw.rect(gameDisplay,i,(x,y,w,h))
		
		smalltext=pygame.font.Font('freesansbold.ttf',20)
		textSurf,textRect=text_objects(msg,smalltext,black)
		textRect.center=((x+(w/2)),(y+(h/2)))
		gameDisplay.blit(textSurf,textRect)
		#pygame.display.update()
def crash(count):
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)
	message_display('Crashed',bright_red)
	score_display('Your score:',count)
	largetext=pygame.font.Font('freesansbold.ttf',115)
	textsurf,textrect=text_objects('GAME ON',largetext,black)
	textrect.center=((width/2),(height/2))
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		#message_display('GAME ON')
		gameDisplay.blit(backgrnd_img,[0,0])
		gameDisplay.blit(textsurf,textrect)
		button("Play Again",150,450,120,50,green,bright_green,game_loop)
		button("Quit",550,450,120,50,red,bright_red,quitgame)
		
		pygame.display.update()
		clock.tick(60)
def unpause():
	global pause
	pause=False
	pygame.mixer.music.unpause()
  
def paused():
	pygame.mixer.music.pause()
	while pause:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largetext=pygame.font.Font('freesansbold.ttf',115)
		textsurf,textrect=text_objects('PAUSED',largetext,black)
		textrect.center=((width/2),(height/2))
		gameDisplay.blit(textsurf,textrect)
		button('CONTINUE',150,450,120,50,green,bright_green,unpause)
		button('QUIT',550,450,120,50,red,bright_red,quitgame)
		
		
		pygame.display.update()
		clock.tick(60)

def game_loop():
	game_exit=False
	x=width*0.45
	y=height*0.8
	car_width=73
	x_change=0
	thing_w=100
	thing_x=random.randrange(0,width-thing_w)
	thing_y=-600
	count=0
	thing_h=100
	thing_speed=7
	pygame.mixer.music.load('bgm.wav')
	pygame.mixer.music.play(-1)
	while not game_exit:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				game_exit=True
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x_change=-5
				if event.key==pygame.K_RIGHT:
					x_change=5
				if event.key==pygame.K_p:
					global pause
					pause=True
					paused()
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					x_change=0
		x+=x_change
		gameDisplay.fill(white)
		gameDisplay.blit(backgrnd_img,[0,0])
		things(thing_x,thing_y,thing_w,thing_h,black)
		thing_y+=thing_speed
		im(x,y)
		score(count)
		
		
		if x>width-car_width or x<0:
			crash(count)
		if thing_y>height:
			thing_y=-thing_h
			thing_x=random.randrange(0,width-thing_w)
			count=count+1
			if count>=5 and count%5==0:
				thing_speed=thing_speed+1
		if y<thing_y+thing_h:
			if ((x>thing_x and x<thing_x+thing_w) or (x+car_width>thing_x and x+car_width<thing_x+thing_w)):
				crash(count)
		pygame.display.update()
		clock.tick(60)
def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(backgrnd_img,[0,0])
		
		largetext=pygame.font.Font('freesansbold.ttf',115)
		textsurf,textrect=text_objects('GAME ON',largetext,black)
		textrect.center=((width/2),(height/2))
		gameDisplay.blit(textsurf,textrect)
		button("GO!",150,450,100,50,green,bright_green,game_loop)
		button("QUIT",550,450,100,50,red,bright_red,quitgame)
		
		
		pygame.display.update()
		clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
