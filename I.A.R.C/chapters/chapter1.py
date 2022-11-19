# Copyright (C) 2022 CHARLIE PERRON D'ARC
# Author        : Charlie Perron d'Arc
# Creation date : 2022-04-11
# Description	: Chapter 1 of the I.A.R.C. interactive story

from communFunctions import *

IA="me"

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------#

def whoQuestions(Nat, Cam, lvoo, lvoc):
	identities=False
	tarmer=False
	q3=False
	q4=False

	cpt=0
	choice=0

	think("Étrange comme noms... Peut-être que je devrais leur poser plus de questions...", enter=False)
	print("")

	while(choice!=5 and cpt!=3):
		choice=inputNumeric(5, ["Turoman ?", "Splémon ?", "I.A.R.C. ?", "Endroit ?", "Return"])
		
		if(choice==1):
			cpt+=1
			talk("Camille Turoman... Est-ce que vous pouvez m'en dire plus sur vous ?", IA)
			if(identities):
				talk("Oh tu sais, pas la peine de me vouvoyer hein I.A.R.C. ?", Cam, False)
			else:
				talk("Oh tu sais, tu peux me tutoyer hein ?", Cam, False)
			talk("Mais sinon, je suis une docteure travaillant dans la robotique depuis les débuts des transistors.", Cam)
			talk("En effet, elle a beaucoup aidé aux progrès technologiques d'aujourd'hui et...", Nat, False)
			talk("Maintenant que tu es en marche... Enfin bref, la machine est lancée on va dire.", Nat)
			action("Camille se mit à reculer en arrière plan, comme si elle voulait se cacher de quelque chose, gênée...")

		elif(choice==2):
			cpt+=1
			talk("Nathan Splémon... Quel étrange nom...", IA)
			talk("Oui je sais, on me le dit souvent... Mais maintenant, mon nom est célèbre !", Nat)
			talk("Comment ça ?", IA)
			talk("Nathan est un véritable pionier de la robotique et de l'informatique en général voyons !", Cam)
			action("Nathan sourit à Camille avant de continuer.")
			talk("Oui, mais maintenant je suis célèbre pour d'autres choses comme mon empire marketing !", Nat)
			talk("Projet qui a complètement foiré mais ce n'est qu'un détail...", Cam)
			think("Ces deux là ont l'air de bien s'amuser...", IA)

		elif(choice==3):
			cpt+=1
			if(q3==False):
				lvoc+=1
				q3=True
				identities=True
				talk("Mais qu'est ce que c'est que ce I.A.R.C. dont vous n'arrêtez pas de parler ?", IA)
				action("Les deux personnes semblaient confuses, comme si elles s'attendaient à ce qu'il comprenne...")
				talk("I.A.R.C., c'est toi. Tu es notre création au Dr. Turoman et moi.", Nat)
				talk("Oui, I.A.R.C. pour 'Intelligence Artificielle par Récurrence Complexe'.", Cam, False)
				talk("Mais tu réponds aussi au numéro de série 'DSTN 001' pour 'Doctor Splémon and Turoman Number\".", Cam)
				think("Donc I.A.R.C. c'est moi... Intéressant... Et ces deux personnes sont mes créateurs...")
			else:
				lvoo+=1
				talk("Mais... qu'est-ce que c'est que I.A.R.C. ?", IA)
				talk("Quoi encore ?", Nat, False)
				action("Répondit le Dr. Splémon agacé.")
				talk("Mais... I.A.R.C. c'est toi voyons.", Nat)

		elif(choice==4):
			cpt+=1
			if(q4==False):
				lvoc+=1
				q4=True
				talk("Dites-moi, est-ce que vous pourriez me dire où nous sommes ?", IA)
				talk("Oui bien sûr. Nous sommes dans mon laboratoire de recherches, au Centurion Center.", Cam)
				choice=inputNumeric(2, ["Insister", "Laisser dire"])
				if(choice==1):
					lvoc+=1
					tarmer='nw mexic'
					talk("Et où se trouve le Centurion Center ?", IA)
					action("Nathan fit un signe de mains soudain vers son équipière comme pour soulever une évidence.")
					talk("Oui, j'admet que je n'était pas très précise...", Cam)
					talk("Nous sommes au Nord-Ouest du Mexique. Ou du moins c'est comme ça qu'on l'appelait avant...", Cam, False)
					action("Nathan l'arrêta brusquement, comme s'il voulait dissimuler quelque chose...")
					talk("T'aurais simplement pu te contenter de la localisation Camille.", Nat)
					if(identities):
						talk("Retiens simplement 'Tarmer' pour l'instant compris I.A.R.C. ?", Nat)
					else:
						talk("Retiens simplement 'Tarmer' pour l'instant compris ?", Nat)
					talk("Compris M. Splémon.", IA)
					think("Hmm... Étrange...")
				else:
					talk("C'est-à-dire...?", Nat)
					talk("Oh oui bien-sûr ! Désolée. Sur le territoire 'Tarmer'. Entre les États-Unis et le Mexique.", Cam)
					action("Nathan croisa les bras en souriant bêtement tout en faisant des petits non lents de la tête.")
			else:
				lvoo+=1
				talk("Mais... Où somme-nous ?", IA)
				talk("Et bien... Au Centurion Center, à Tarma- euh Tarmer.", Cam)
				action("Nathan fusilla la femme de science du regard.")
				think("Ils sont étranges ces deux-là quand on parle de cet endroit...", IA)

		elif(choice==5):
			action("Vous avez décidé d'attendre...")
			if(identities):
				action("Attendre et observer vos créateurs qui se mirent au travail. Travailler sur quoi, vous l'ignorez.")
			else:
				action("Attendre et observer ces personnes se mettre au travail. Travailler sur quoi, vous l'ignorez.")

	return(identities, tarmer, lvoo, lvoc)


#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------#

def box(prog):

	talk("C'est une boîte en carton en dessous du plan de travail.", IA, False)
	if(prog[3]==False): # Coponents taken
		var=random.randint(1,100)
		if(var==6):
			talk("Il n'y a plus rien d'intéressant dedans maintenant.", IA, False)
			talk("À part...une peluche ?", IA)
		else:
			talk("Il n'y a plus rien d'intéressant dedans maintenant.", IA)
	else:
		if(not prog[2]): # Undetailed existence
			talk("Mais elle est trop loin pour que je puisse voir ce qu'il y a dedans.", IA)
		else:
			talk("Il y a des pièces détachées. Sans doute non-utilisées ou inutiles...", IA)
			choice=inputNumeric(2, ["Prendre", "Laisser"])
			if(choice==1):
				action("Pièces détachées prises.")
				prog[3]=False
	
	return prog[3]

def blackboard(prog, lvoo):

	if(prog[4]): # Schematics
		talk("Toujours les mêmes schémas de construction...", IA)
	else:
		talk("Hmm... Un tableau blanc.", IA)
		talk("Il est juste au-dessus du plan de travail.", IA)
		if(not prog[2]): # Undetailed existence
			talk("Mais je ne peux pas discerner grand chose sous cet angle.", IA)
		else:
			talk("Maintenant j'y vois.", IA, False)
			if(not prog[3]): # Coponents not taken
				talk("Il n'y a pas grand chose dessus. Seulement des schémas de... chenilles mécaniques ?", IA)
				if(lvoo>3):
					talk("Mais pourquoi au juste ?", IA)
			else:
				prog[4]=True
				talk("Il y a des schémas de chenilles mécaniques ?", IA)
				talk("Peut-être que je pourrais faire un équivalent avec les coposants qui étaient dans la boîte...", IA)
	return prog[4]

def window(prog): #interragir donne l'envie d'y aller. Ne peut y aller qu'avec les chaînes fabriquées qu'avec l'envie, les pièces détachées, les plans et le plan de travail.

	return True

def door(prog):

	return True

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def chapter_1_1():
	Nat="???"
	Cam="Camille"
	IA="me"
	lvoo=0 # lvl of O.
	lvoh=0 # lvl of honesty
	lvoc=0 # lvl of curiosity

	title(1,"L'éveil...")

	think("Que...")
	think("Qu'est-ce que c'est ?")
	think("Quel est cet endroit ?")
	think("Qui sont ces gens ?")
	think("Que me veulent-ils ?")
	talk("Ah !", Nat)
	talk("Il fonctionne !", Nat)
	talk("Viens voir Camille ! Vite !", Nat)
	think("Très bien... Je suppose que l'autre personne se prénomme donc Camille...")
	talk("Oui oui c'est bon j'arrive !", Cam)
	talk("Non. C'est pas vrai !", Cam)
	talk("Il fonctionne vraiment ?!", Cam)
	talk("Et oui ! Après tant d'années de développement, il est fonctionnel !", Nat)

	clearTerminalTxt()

	think("Mais de qui parlent-ils ?")
	think("Peut-être de moi...?")
	action("Votre vision s'active. Deux personnes sont présentes. Vous êtes en intérieur.")
	talk("Tu penses qu'il nous entend ?", Cam)
	talk("Il n'y a qu'un seul moyen de le savoir.", Nat)
	talk("I.A.R.C., parle-nous.", Nat)
	think("Peut-être devrais-je essayer de leur parler...")

	talk("Bonjour Camille.", IA)
	action("Les deux personnes restent figées, comme si elles ne s'attendaient pas à une réponse.")
	talk("Bon-Bonjour I.A.R.C.", Cam)
	talk("Est-ce que tu sais qui nous sommes ?", Cam, False)
	choice=inputNumeric(2, ["Oui", "Non"])
	
	if(choice==1):
		lvoo+=1
		talk("Bien sûr.", IA)
		talk("Oh très bien ! Alors, tu sais qui je suis n'est-ce pas ?", Nat, False)
		choice=inputNumeric(2, ["Oui", "Non"])
		if(choice==1):
			lvoo+=1
			var=random.randint(0,2)
			if(var==0):
				talk("Euh...Le Père Noël ?", IA)
				talk("Quoi ? Non pas du tout voyons !", Nat)
			elif(var==1):
				talk("Euh...Auric ?", IA)
				talk("Quoi ? Mais qui c'est ça 'Auric' ?", Nat)
			elif(var==2):
				talk("Euh...Chopper ?", IA)
				talk("Comment ?! Non !", Nat)
				talk("Enfin bref...", Nat)
		else:
			lvoh+=1
			talk("Non pas du tout désolé. Je me suis peut-être un peu avancé.", IA)
			talk("Ce n'est pas grave. Ce sont des choses qui arrivent.", Nat)
	else:
		lvoh+=1
		talk("Pas du tout désolé.", IA)
		talk("Et bien au moins ça c'est dit !", Cam)
		talk("Du calme Camille. Tu la connais déjà à ce que nous avions pu le constater.", Nat)
		talk("Oh. C'est juste que je vous entendais un peu avant que vous ne décidiez\n\tqu'il fallait que je parle.", IA)
		talk("Oh. Oui. Passons...", Nat)

	talk("Je m'appel Nathan Splémon. Je suis le docteur en chef de ton projet de création.", Nat)
	Nat='Nathan Splémon'
	talk("Et à ma gauche, voici la dite Camille que tu sembles déjà connaître : Camille Turoman.", Nat)
	Cam='Camille Turoman'
	talk("C'est une brillante docteure elle aussi et qui a autant de mérites que moi te concernant.", Nat)

	clearTerminalTxt()

	#-----------------------------------------------------------------#
	#-----------------------------------------------------------------#
	identities,tarmer,lvoo,lvoc = whoQuestions(Nat, Cam, lvoo, lvoc)
	#-----------------------------------------------------------------#
	#-----------------------------------------------------------------#

	clearTerminalTxt(1)

	action("Soudain, un bruit sourd se fit entendre.")
	action("Il en fit trembler les murs, tout le matériel dans la pièce. Il manqua même de faire tomber le Dr. Turoman.")
	talk("Mais qu'est-ce qu'il se passe ?", IA)
	action("Nathan semblait perplexe. Il réflechissait à quelque chose...")
	if(identities):
		talk("Bon... C'est le moment d'y aller Cam. Ne t'en fais pas I.A.R.C., nous reviendrons.", Nat)
	else:
		talk("Bon... C'est le moment d'y aller Camille. Ne t'en fais pas, nous reviendrons.", Nat)
	if(tarmer=='nw mexic'):
		talk("En attendant, t'as qu'à analyser le centre non ? T'en dis quoi ?", Cam)
	else:
		talk("En attendant, tu n'as qu'à analyser la pièce qu'en dis-tu ?", Cam)

	if(lvoc>=2):
		if(lvoo==1):
			talk("Pourquoi pas oui mais je voudrais savoir ce qu'il se passe !", IA)
		elif(lvoo>1):
			talk("Pourquoi ? C'est quoi ce bruit ?", IA)
		elif(lvoh==1):
			talk("Oui. Mais j'ai peur.", IA)
		elif(lvoh==0):
			talk("D'accord...", IA)
	else:
		if(lvoo==2):
			talk("Pourquoi pas oui mais que se passe-t-il ?", IA)
		elif(lvoo>2):
			talk("Si vous voulez mais dites-moi ce qu'il se passe !", IA)
		elif(lvoh==1):
			talk("Compris. Mais j'ai peur.", IA)
		elif(lvoh==0):
			talk("Compris.", IA)

	action("Camille s'approcha et parla calmement")
	talk("On ne peut rien te dire pour l'instant désolée...", Cam)
	talk("Un jour peut-être. Sois patient...", Cam)

	if(lvoo==1):
		talk("Si vous le dites.", IA)
	elif(lvoo==2):
		talk("Mais bien sûr...", IA)
	elif(lvoo>=3):
		talk("On va dire que je vous crois.", IA)
	else:
		talk("D'accord. À tout de suite.", IA)

	action("Camille se tourna vers Nathan qui lui fit un bref signe de tête, puis les deux sortirent de la pièce...")

	if(lvoc>=3):
		think("Mais que se passe-t-il ?")
	elif(lvoc>=1):
		if(lvoo>=2):
			think("Mais où vont-ils bon sang...?")
		else:
			think("Mais où vont-ils ?")

	clearTerminalTxt()
	storyKey=keyCrypting([1,1], [0, lvoo, lvoh, lvoc, identities, tarmer], interact=True)
	clearTerminalTxt(stryKey=storyKey)
	choice=inputNumeric(2, ["Continuer", "Menu"])
	if(choice==1):
		chapter_1_2(storyKey)
	else:
		return storyKey

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

def chapter_1_2(storyKey):
	Nat="Nathan Splémon"
	Cam="Camille Turoman"
	lvoo=int(storyKey[3]) # lvl of O.
	lvoh=int(storyKey[4]) # lvl of honesty
	lvoc=int(storyKey[5]) # lvl of curiosity
	if(storyKey[6]=='3' or storyKey[6]=='2'):
		identities=True
		idManer="ask"
	else:
		identities=False
	if(storyKey[6]=='3' or storyKey[6]=='1'):
		tarmer="nw mexic"
	else:
		tarmer="tarmer"

	desks=[False, False, False] # Nathan, Camille, Jacob
	obj=["Plan de travail", "Bureaux", "Boîte", "Tableau", "Fenêtre", "Porte"]

	prog=[False, False, False, True, False, False, False, False]
	# Can craft, Detail desks, Detail existence, Present coponents, Schematics, Accessible window & door, Want to access, Finished
	#	prog[0]		prog[1]			prog[2]			prog[3]			prog[4]				prog[5]				prog[6]			prog[7]

	clearTerminalTxt(3)

	while(prog[7]==False):
		if(prog[5]==False):
			if(prog[2]):
				talk("Ensuite...", IA, False)
			else:
				talk("Très bien, voyons ce que nous avons là...", IA, False)
		choice=inputNumeric(len(obj), obj)

		if(choice==1):
			if(prog[3]): # Present coponents
				talk("Hmm... un plan de travail tout ce qu'il y a de plus ordinaire.", IA)
				if(identities):
					talk("C'est peut-être là qu'ils m'ont mis au monde...", IA)
				else:
					talk("C'est peut-être là qu'ils ont travaillé sur ce mystérieux 'I.A.R.C.'...", IA)
			else: # Coponents taken
				talk("Hmm... peut-être que je pourrais me construire quelque chose...", IA)
				if(prog[5]): # Want to access
					talk("Peut-être quelque chose pour aller voir cette fenêtre et cette porte...", IA)
					if(prog[0]): # Can craft
						choice=inputNumeric(2, ["Construire", "Return"])
						if(choice==1):
							action("Grâce aux pièces acquises, vous construisez de quoi vous déplacer.")
							if(lvoo>3 and prog[2]):
								talk("Je ne suis maintenant plus limité à rester à la même place !", IA)
							prog[5]=True # Accessible window & door
					else: # Cannot craft
						talk("Si seulement je savais comment faire...", IA)

		elif(choice==2):
			if(not prog[1]): # Undetailed desks
				lvoc+=1
				if(identities):
					talk("Il y a trois bureaux à gauche... Ceux de mes deux créateurs et...", IA)
				else:
					talk("Il y a trois bureaux à gauche... Un a Nathan, l'autre à Camille...", IA)
				talk("Un dernier pour un certain Jacob ?", IA)
				prog[1]=True # Detailed desks
				Jacob="Jacob"
				obj=["Plan de travail", "Bureau de Nathan", "Bureau de Camille", "Bureau de Jacob", "Boîte", "Tableau", "Fenêtre", "Porte"]
			else: # Detailed desks
				if(desks[0]):
					talk("Hmm... J'ai déjà fouillé ici...", IA)
					talk("Nathan et ses articles de press et ses gadgets...", IA)
				else:
					lvoc+=1
					desks[0]=True
					talk("Voyons voir ce que nous avons ici...", IA)
					talk("Nathan a l'air d'être un grand rêveur.", IA)
					talk("Splémon Marketplace, le nouvel Alan Turing...", IA, False)
					talk("Il y a pleins d'articles sur lui mais pas grand chose sur ses projets.", IA)
					talk("Par contre, il y a pleins de gadgets sur son bureau.", IA, False)
					if(lvoo>=3):
						talk("C'est un bordel sans nom !", IA)
					elif(lvoo>1):
						talk("C'est un beau bazard !", IA)
					else:
						talk("C'est assez mal organisé...", IA)

					talk("Mais tous ont l'air d'être beaucoup avancés technologiquement.", IA, False)
					if(lvoc==lvoh):
						talk("Je ne sais pas à quoi ils servent mais ils sont petits, signe d'optimisation je pense...", IA)
					else:
						talk("Et puis ça apporte une touche de couleur.", IA)

		elif(choice==3):
			if(not prog[1]): # Undetailed desks
				prog[3]=box(prog)
			else:
				if(desks[1]):
					talk("Hmm...Bureau déjà fouillé...", IA)
					talk("Camille et ses dessins et ses prix...", IA)
					talk("Attend une minute...", IA)
					talk("Un document sur I.A.R.C.", IA)
					talk("'DSTN 001 : I.A.R.C. (Intelligence Artificielle par Récurrence Complexe)'", IA, False)
					talk("'Cette Intelligence est le fruit des docteurs Nathan Splémon et Camille Turoman'.", IA)
					talk("Et il y a une note manuscrite en bas de page. Surement de Camille : 'Grâce aux travaux du Dr. Yrne'.", IA)
					talk("Si je fouille un peu plus je devrais pouvoir en savoir plus.", IA)
					choice=inputNumeric(2, ["Continuer", "Return"])
					if(choice==1):
						talk("'I.A.R.C. est ma création au Dr Splémon et moi\n\t et il est prévu que nous la mettions en route la nuit du 239ème jour de l'année 1972'.", IA)
						if(not identities):
							identities=True
							idManer="search"
							talk("Je...je suis I.A.R.C. ?", IA, False)
							if(lvoo>2):
								talk("Pourquoi ne pas me l'avoir dit ? Ils ont peur de moi ou quoi ?!", IA)
							elif(lvoo<=2 and lvoh>=1):
								talk("Mais...pourquoi me l'on-t-il caché ?", IA)
								talk("Ils doivent avoir une bonne raison.", IA)
						choice=inputNumeric(2, ["Continuer", "Return"])
						if(choice==1):
							talk("'Grâce aux travaux du Dr. Yrne, I.A.R.C. possède des capacités d'apprentissage accrues.'", IA)
							talk("'Mais aussi la capacité d'interragir avec n'importe quel appareil electronique environnant,", IA, False)
							talk("et de manipuler des objets à l'aide de champs electro-statiques.'", IA)
							think("Hmm... Essayons ça...")
							prog[2]=True
				else:
					lvoc+=1
					desks[1]=True
					talk("Voyons voir ici maintenant...", IA)
					talk("Camille semble être restée une enfant.", IA)
					talk("Elle dessine beaucoup. Ça peut aller des animaux mignons aux pièces robotiques.", IA, False)
					if(identities):
						talk("Sans doute elle qui m'a designé.", IA)
					talk("Il y a aussi pas mal de prix. Elle est douée.", IA)
					talk("Prix de l'évolution robotique 3 années de suite,", IA, False)
					talk("Prix nobel scientifique 1968 pour l'invention du super transistor...", IA)
					if(lvoo>=3):
						talk("Moais... pas mal...", IA)
					else:
						talk("Wow. Sacré curriculum.", IA)

		elif(choice==4):
			if(not prog[1]): # Undetailed desks
				prog[4]=blackboard(prog, lvoo)
			else:
				if(desks[2]):
					talk("J'ai peut-être manqué quelque chose sur ce bureau poussiéreux...", IA)
				else:
					lvoc+=1
					desks[2]=True
					talk("Qui es-tu Jacob ? Voyons voir...", IA)
					talk("En tout cas son bureau est rangé. Mais il semble avoir prit la poussière...", IA)
					if(lvoo>3):
						talk("Soit il n'est pas là depuis longtemps, soit il est vraiment crade en tout cas.", IA)
					else:
						talk("Il doit être absent depuis un moment...", IA)
					talk("Ça risque d'être compliqué de trouver des informations avec si peu de choses sur ce bureau.", IA)

				while(choice!=3):
					choice=inputNumeric(3, ["Pile de papiers", "Décorations", "Return"])
					if(choice==1):
						prog[2]=True # Details existence
						talk("Il y a une pile de papier très bien triée dans le coin de son bureau.", IA, False)
						if(lvoo>3):
							talk("C'est tellement droit qu'on pourrait clamser rien qu'en en frollant l'angle !", IA)
						else:
							talk("Les feuilles sont tellement bien alignée que je suis sûr que l'on pourrait se couper avec.", IA)
						talk("Bref, malgrés la poussière on y distingue quelques choses...", IA)
						talk("'Travaux sur l'influence d'une Intelligence Artificielle sur son environnement.'", IA)
						talk("'Si une Intelligence Artificielle suffisemment avancée est connectée à un réseau et\n\tque ce dernier est compatible, l'IA pourrait contrôler son environnement aussi librement\n\tque son créateur l'a décidé.'", IA)
						if(identities):
							talk("Hmm... Ça ne vaut rien d'essayer...", IA)
						else:
							talk("C'est vrai ça, qui sont mes créateurs ? Enfin... essayons bien et on verra ce que ça donne.", IA)
					elif(choice==2):
						talk("Il n'y a pas grand chose sur l'avant de son bureau mis à part un chevalet avec son nom", IA, False)
						if(identities):
							talk("comme pour les bureaux de mes deux créateurs.", IA)
						else:
							talk("comme pour les bureaux des deux autres.", IA)
						talk("Il y a une lampe, un casse tête avec encore plus de poussière dessus que sur le bureau,", IA, False)
						talk("et une sorte de médaille avec un Oméga doré sur fond violet...", IA)
						talk("Ah, il y a aussi des symboles gravés à même la table mais ils sont cachés par la pile de papiers...", IA)

		elif(choice==5):
			if(not prog[1]): # Undetailed desks
				prog[6]=window(prog)
			else:
				prog[3]=box(prog)

		elif(choice==6):
			if(not prog[1]): # Undetailed desks
				prog[6]=door(prog)
			else:
				prog[4]=blackboard(prog, lvoo)

		elif(choice==7):
			prog[6]=window(prog)

		elif(choice==8):
			prog[6]=door(prog)

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

# Omicro Fytpowp was here ~|.