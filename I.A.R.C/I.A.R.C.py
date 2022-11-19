# Copyright (C) 2022 CHARLIE PERRON D'ARC
# Author        : Charlie Perron d'Arc
# Creation date : 2022-04-09
# Description	: Main program of the I.A.R.C. interactive story which allows users to continue their story or start a new one

import sys
from os import system
from time import sleep

sys.path.insert(1,'extraLayouts')
from progressBarLayout import *

sys.path.insert(0,'chapters')
from chapter1 import *

mainMenuValue=6
storyKey='0'

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#


def mainMenu(storyKey):

	sleep(0.1)
	system("clear")
	sleep(1)

	var=random.randint(0,4)

	print("#=====================================================================#")

	if(var==0):
		file=open("ASCII_img/I.A.R.C.(Big_Money-sw)0.txt")
	
	elif(var==1):
		file=open("ASCII_img/I.A.R.C.(ANSI_Shadow)1.txt")
	
	elif(var==2):
		file=open("ASCII_img/I.A.R.C.(Alligator)2.txt")
	
	elif(var==3):
		file=open("ASCII_img/I.A.R.C.(Broadway)3.txt")
	
	elif(var==4):
		file=open("ASCII_img/I.A.R.C.(OS2)4.txt")
	
	print(file.read())

	print('''|\n#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#''')
	if(storyKey!='0'):
		print("|                      Clée de sauvegarde :", storyKey)
	print("|\n|\t0.\tSortir")
	if(storyKey=='0'):
		print("|\t1.\tCommencer\n|\t2.\tCharger une clée de sauvegarde")
	else:
		print("|\t1.\tContinuer\n|\t2.\tChoix du chapitre")
	print("|\t3.\tFonctionnement I.A.R.C.\n|\t4.\tCopyrights")
	var=random.randint(1,100)
	if(var==6):
		print("|\t6.\tGlitch call")
	print("|\n#=====================================================================#")

	choice=input("\t@¬ ")
	if(choice=="Galadiel0"):
		storyKey='0'
		print("\n\tClée de sauvegarde chargée à 0.\n\tEntrer la valeur 6 pour recharger le menu.\n")
	try:
	    choice=int(choice)    
	except ValueError:
	    nbCheck=False
	else:
		nbCheck=((choice>=0 and choice<5) or choice==6)
#loop check that choice is int and valid
	while(nbCheck==False):
		choice=input("\tEntrer une valeur valide @¬ ")
		try:
		    choice=int(choice)
		except ValueError:
		    continue
		else:
			nbCheck=((choice>=0 and choice<5) or choice==6)
			continue
	
	if(choice==0):
		return (0, storyKey)

	elif(choice==1):
		if(storyKey=='0'):
			storyKey=chapter_1_1()
		elif (storyKey[1]=='1' and storyKey[2]=='1'):
			trash=input("\n\t/!\\ Attention ! Cette action affectera votre clée de sauvegarde /!\\ ¬")
			storyKey=chapter_1_2(storyKey)
	elif(choice==2):
		if(storyKey=='0'):
			storyKey=input("\tEntrer une clée de sauvegarde ß¬ ")
			if (not((len(storyKey)==7) #and (storyKey[0]==0 or storyKey[0]==1) and (storyKey[1]==0 or storyKey[1]==1) and (storyKey[2]==0 or storyKey[2]==1))
				or (len(storyKey)==1 and storyKey[0]=='0') or (len(storyKey)==1 and storyKey[0]=='6'))):
				trash=input("\tFormat invalide ¬ ")
				storyKey='0'
		else:
			trash=input("\tOption invalide pour le moment ¬ ")

	elif(choice==3):
		tutorial()

	elif(choice==4):
		copyrights()

	elif(choice==6):
		glitch()

	return (1, storyKey)
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def tutorial():
	sleep(0.1)
	system("clear")
	sleep(0.5)
	print('''/=====================================================================\\
|
|\tBienvenue dans I.A.R.C.
|\n|\tCeci est une histoire interactive dans laquelle vous devrez
|\tfaire des choix.
|\tLorsque vous voudrez quitter le programme, une clée vous est
|\tdonnée en guise de sauvegarde. Notez-les bien.
|\n|\tEnsuite, il y a plusieurs systèmes de saisie :
|\t   ¬ : Attend de vous une validation (entrée par exemple)
|\t  @¬ : Attend de vous d'entrer une valeur numérique
|\t  ß¬ : Attend de vous d'entrer une chaîne de charactères
|\n\\=====================================================================/''')
	trash=input("\t¬ ")
	var=random.randint(1,10)
	if(var==6):
		glitch()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def copyrights():
	sleep(0.1)
	system("clear")
	sleep(0.5)
	print('''/=====================================================================\\
|
|\t\tCopyright (C) 2022 CHARLIE PERRON D'ARC
|\t\tAuthor        : Charlie Perron d'Arc
|\t\tCreation date : 2022-04-09
|
|\t\t Progress bar code :
|\t\t bobber205
|\t\t Text in main menu :
|\t\t https://patorjk.com/software/taag/
|\n\\=====================================================================/''')
	trash=input("\t¬ ")

#==========================================================================================================================================================#
#==========================================================================================================================================================#
#==========================================================================================================================================================#

print("Chargement I.A.R.C.py...\n")
sleep(2)

callProgressBar()

print("\nLancement...\n")
sleep(1)

glitch()

while (mainMenuValue!=0):
	mainMenuValue, storyKey=mainMenu(storyKey)

print("")

# Omicro Fytpowp was here ~|.