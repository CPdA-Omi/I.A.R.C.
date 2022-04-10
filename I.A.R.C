from os import system
from time import sleep
import random
#from progressBarLayout import *

mainMenuValue=6
storyKey=0
randomErrorCharacter=['#', '$', 'þ', '¶', '§', '@', '█', '€', '&', 'C', '6']

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def mainMenu():

	sleep(0.1)
	system("clear")
	sleep(1)

	var=random.randint(0,4)

	print("#=====================================================================#", end='')

	if(var==0):

		print('''
|\t ______       ______       _______        ______     
|\t/     /|     /     /\\     /      /\\      /     /\\    
|\t██████/     /██████ /|    ███████  |    /██████ /|   
|\t  ██ |      ██ |__██ |    ██ |__██ |    ██ |  ██/    
|\t  ██ |      ██/   ██ |    ██/   ██ <    ██ |         
|\t  ██ |      ████████ |    ███████ /|    ██ |   __    
|\t _██ |_  __ ██ |  ██ | __ ██ |  ██ | __ ██ |__/ /|__ 
|\t/ ██/ /|/ /|██ |  ██ |/ /|██ |  ██ |/ /|██/   ██// /|
|\t██████/ ██/ ██/   ██/ ██/ ██/   ██/ ██/  ██████/ ██/''')
		#Big Money-sw

	if(var==1):

		print('''
|\t\t
|\t\t██╗    █████╗    ██████╗     ██████╗   
|\t\t██║   ██╔══██╗   ██╔══██╗   ██╔════╝   
|\t\t██║   ███████║   ██████╔╝   ██║        
|\t\t██║   ██╔══██║   ██╔══██╗   ██║        
|\t\t██║██╗██║  ██║██╗██║  ██║██╗╚██████╗██╗
|\t\t╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝''')
		#ANSI Shadow

	if(var==2):
		print('''
|         :::::::::::         :::         :::::::::       ::::::::     
|            :+:           :+: :+:       :+:    :+:     :+:    :+:     
|           +:+          +:+   +:+      +:+    +:+     +:+             
|          +#+         +#++:++#++:     +#++:++#:      +#+              
|         +#+         +#+     +#+     +#+    +#+     +#+               
|        #+#     #+# #+#     #+# #+# #+#    #+# #+# #+#    #+# #+#     
|   ########### ### ###     ### ### ###    ### ###  ########  ###''')
		#Alligator

	if(var==3):
		print('''\n|
|     8 8888          .8.          8 888888888o.      ,o888888o.    
|     8 8888         .888.         8 8888    `88.    8888     `88.  
|     8 8888        :88888.        8 8888     `88 ,8 8888       `8. 
|     8 8888       . `88888.       8 8888     ,88 88 8888           
|     8 8888      .8. `88888.      8 8888.   ,88' 88 8888           
|     8 8888     .8`8. `88888.     8 888888888P'  88 8888           
|     8 8888    .8' `8. `88888.    8 8888`8b      88 8888           
|     8 8888   .8'   `8. `88888.   8 8888 `8b.    `8 8888       .8' 
|     8 8888  .888888888. `88888.  8 8888   `8b.     8888     ,88'  
|     8 8888 .8'       `8. `88888. 8 8888     `88.    `8888888P\'''')
		#Broadway

	if(var==4):
		print('''
|\t    ________________________________________________
|\t    _1001_______101_______1010101_________1001______
|\t    __01______01___10_____01____01______01____01____
|\t    __10_____01_____10____10____10_____01___________
|\t    __01_____101010101____0101010______10___________
|\t    __10_____01_____10____10____10______10____01____
|\t    _1001_01_10_____01_10_01_____10_01____1001___01_
|\t    ________________________________________________''')
		#OS2

	print('''|\n#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\n|
|\t0.\tSortir''')
	if(storyKey==0):
		print("|\t1.\tCommencer\n|\t2.\tCharger une clée de sauvegarde", end='')
	else:
		print("|\t1.\tContinuer\n|\t2.\tChoix du chapitre", end='')
	print('''
|\t3.\tFonctionnement I.A.R.C.
|\t4.\tCopyrights''')
	var=random.randint(1,100)
	if(var==6):
		print("|\t6.\tGlitch call")
	print("|\n#=====================================================================#")

	choice=int(input("\t@¬"))
	while(choice!=0 and choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=6):
		choice=int(input("\tEntrer une valeur valide @¬"))
	
	if(choice==0):
		return 0
#	elif(choice==1):
#		chapter1()
	elif(choice==2 or choice==1):
		trash=input("\tOption invalide pour l'intant ¬")
	elif(choice==3):
		tutorial()
	elif(choice==4):
		copyrights()
	elif(choice==6):
		glitch()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def tutorial():
	sleep(0.1)
	system("clear")
	sleep(0.5)
	print('''/=====================================================================\\
|
|\tBienvenue dans I.A.R.C.
|\n|\tCeci est une histoire interactive dans laquelle vous devrez
|\tfaire des choix.
|\tLorsque vous voudrez quitter le programme, une clé vous est
|\tdonnée en guise de sauvegarde. Notez-les bien.
|\n|\tEnsuite, il y a plusieurs systèmes de saisie :
|\t   ¬ : Attend de vous une validation (entrée par exemple)
|\t  @¬ : Attend de vous d'entrer une valeur numérique
|\t  ß¬ : Attend de vous d'entrer une chaîne de charactères
|\n\\=====================================================================/''')
	trash=input("\t¬")
	var=random.randint(1,10)
	if(var==6):
		glitch()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def copyrights():
	sleep(0.1)
	system("clear")
	sleep(0.5)
	print('''/=====================================================================\\
|
|\t\tCopyright (C) 2022 OMICRO FYTPOWP
|\t\tAuthor        : Omicro Fytpowp
|\t\tCreation date : 2022-04-09
|
|\t\t Progress bar code :
|\t\t bobber205
|\t\t Text in main menu :
|\t\t https://patorjk.com/software/taag/
|\n\\=====================================================================/''')
	trash=input("\t¬")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def glitch():
	for i in range (100):
		for j in range (150):
			var=random.randint(0,len(randomErrorCharacter)-1)
			print(randomErrorCharacter[var], end='')
		print("")

#==========================================================================================================================================================#

print("Chargement I.A.R.C.py...\n")
sleep(2)

#callProgressBar()

print("\nLancement...\n")
sleep(1)

glitch()

while (mainMenuValue!=0):
	mainMenuValue=mainMenu()

print("\tClée de sauvegarde :", storyKey, end='')
trash=input(" ¬")
print("")