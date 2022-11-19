# Copyright (C) 2022 CHARLIE PERRON D'ARC
# Author        : Charlie Perron d'Arc
# Creation date : 2022-04-11
# Description	: Program intend to be imported to chapters programs of the I.A.R.C interactive story

from os import system
from time import sleep
import random

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def keyToString (keyRow, interact=False):
	print("Encryptage clée de sauvegarde...\n")
	key=''
	for i in range (len(keyRow)):
		if(interact):
			print(key)
			glitch(x=len(keyRow), y=1, timerRow=0.1)
		key=str(key+keyRow[i])
	if(interact):
		print("")
		inputEnter()
	return key

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def keyCrypting (chapterStep, datas, interact=False):

	if(chapterStep[0]==1):

		if(chapterStep[1]==1):
			# chapter 1.1

			lvoo=str(datas[1])
			lvoh=str(datas[2])
			lvoc=str(datas[3])
			if(datas[4]):
				# identities=True
				if(datas[5]=='nw mexic'):
					# tarmer='nw mexic'
					keyPart='3'
				else:
					keyPart='2'
			else:
				if(datas[5]=='nw mexic'):
					keyPart='1'
				else:
					keyPart='0'
			return(keyToString(["011",lvoo,lvoh,lvoc,keyPart], interact))

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def inputNumeric(nbChoices, options=False):
	if(options):
		lenC=0
		print("\t\t", end='')
		for i in range (len(options)):
			print(i+1, ':', options[i], '\t', end='')
			lenC+=len(options[i])
			if(lenC>=42):
				print("\n\t\t", end='')
				lenC=0
		print("")
	
	choice=input("@¬ ")
	try:
	    choice=int(choice)    
	except ValueError:
	    nbCheck=False
	else:
		nbCheck=(choice>=1 and choice<=nbChoices)
#loop check that choice is int and valid
	while(nbCheck==False):
		choice=input("Entrer une valeur valide @¬ ")
		try:
		    choice=int(choice)       
		except ValueError:
		    continue
		else:
			nbCheck=(choice>=1 and choice<=nbChoices)
			continue
	print("")
	return choice

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def inputEnter():
	trash=input("¬ ")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def talk(txt, name=False, enter=True, tab=False):
	print("\t", end='')
	if(tab):
		print("\t", end='')
	if(name=="me"):
		print(txt)
	elif(name!=False):
		print(name, " : \"", txt, "\"", sep='')
	else:
		print("\"", txt, "\"", sep='')

	if(enter):
		inputEnter()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def think(txt, enter=True):
	print('\t(', txt, ')', sep='')
	if(enter):
		inputEnter()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def action(txt, enter=True):
	print('\t*', txt, '*', sep='')
	if(enter):
		inputEnter()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def clearTerminalTxt(time=0, stryKey=False):
	if(stryKey!=False):
		print("Clée de sauvegarde :", stryKey)
		inputEnter()
		clearTerminalTxt(2)

	system("clear")
	sleep(time)
	print("")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def title(chapterNumber=0, chapterName='Empty'):
	clearTerminalTxt(time=2)
	print("\t--------|I.A.R.C. Chapitre ", chapterNumber, "|--------", sep='')
	print("\n\t\t", chapterName)
	inputEnter()
	clearTerminalTxt(3)

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def glitch(x=100, y=150, timerLine=0, timerRow=0, uniqueRandChar=False):
	randomErrorCharacter=['#', '$', 'þ', '¶', '§', '@', '█', '€', '&', 'C', '6']
	if(uniqueRandChar):
		var=random.randint(0,len(randomErrorCharacter)-1)
	for i in range (y):
		for j in range (x):
			if(uniqueRandChar==False):
				var=random.randint(0,len(randomErrorCharacter)-1)
			print(randomErrorCharacter[var], end='')
			sleep(timerLine)
		print("")
		sleep(timerRow)

# Omicro Fytpowp was here ~|.