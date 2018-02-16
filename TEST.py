# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:47:25 2018

@author: fmuret
"""

import functions_bot
import os


from tkinter import *
import taglib
import stagger
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

#def lister_fichier_mp3():   #1 return the list of the files present in current folder
#def get_album_name(nom_en_str): #2 return name of an album
#def get_liste_album_name(new_liste): # 3 return in a list the name of all ablum of mp3 file here

from tkinter import * 

def calculerBARRE() :
	
	listeESSAI=[0]*223719
	
	# Compteur pour la barre de progression . 
	cptBARRE=0 

	for toto in range(len(listeESSAI)) :
		
		# Calcul du pourcentage
		calcPourcentage=((toto+1)*100)/len(listeESSAI)
		# Mise a jour de la barre de progression 
		# (par le Canvas c).
		c.update()

		# Creation des rectangles pour la barre de progression .
		while cptBARRE<=calcPourcentage*4 :

			c.create_rectangle((cptBARRE, 1, 4+cptBARRE, 21), outline="#e5c95b", fill="red", width=0)
			cptBARRE=cptBARRE+4
			
			# Pourcentage pour affichage a cote de la barre .
			pourcChiffre=" %d %s" % ((cptBARRE/4)-1, "%") 
			# Affichage du pourcentage en calcul dans le 
			# Label (se trouvant dans la Frame f2) .
			f2.update()
			lab1.config(text=pourcChiffre)
			
		# Des que la barre de progression arrive a 100 %, la barre de
		# progression disparait pour laisser la place au Canvas jaune .	
		if cptBARRE>100*4 :
			c.create_rectangle((0, 1, 403, 21), outline="#e5c95b", fill="#e5c95b", width=1)			
	
							
root=Tk()
root.geometry("496x100+0+0")
root.config(bg="#4c4c4c", relief=GROOVE)
root.title("Barre de progression pour EKD")

def interfaceBARRE() :
	
	# ... 
	b=Button(root, text="Calculer progression", command=calculerBARRE, bg="#4dccfe", fg="#4c4c4c", activebackground="#4dccfe", relief=GROOVE)
	b.place(x=22, y=10)
	# Widgets uniquement pour la barre de progression ################################
	f1=Frame(root, height=27, width=410, highlightbackground="#e5c95b", bg="#4c4c4c",bd=2, relief=GROOVE)
	f1.place(x=22, y=60)
	global c
	c=Canvas(f1, height=20, width=403, bg="#e5c95b")
	c.place(x=1, y=1)
	global f2
	f2=Frame(root, height=28, width=54, highlightbackground="#e5c95b", bg="#4c4c4c", relief=GROOVE)
	f2.place(x=433, y=60)
	global lab1
	lab1=Label(f2, bg="#4c4c4c", fg="#e5c95b") 
	lab1.place(x=1, y=4)
	# ################################################################################
	
interfaceBARRE()

if __name__ == '__main__' :
	root.mainloop()