# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:53:31 2018

@author: fmuret
"""

import sys  # Importing the System Library
version = (3, 0)
cur_version = sys.version_info
if cur_version >= version:  # If the Current Version of Python is 3.0 or above
    # urllib library for Extracting web pages
    import urllib.request
    from urllib.request import Request, urlopen
    from urllib.request import URLError, HTTPError
    from urllib.parse import quote
else:  # If the Current Version of Python is 2.x
    # urllib library for Extracting web pages
    import urllib2
    from urllib2 import Request, urlopen
    from urllib2 import URLError, HTTPError
    from urllib import quote
import time  # Importing the time library to check the time of code execution
import os
import argparse
import ssl
import datetime



def download_page(url):
    version = (3, 0)
    cur_version = sys.version_info
    if cur_version >= version:  # If the Current Version of Python is 3.0 or above
        try:
            headers = {}
            headers[
                'User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:  # If the Current Version of Python is 2.x
        try:
            headers = {}
            headers[
                'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers=headers)
            try:
                response = urllib2.urlopen(req)
            except URLError:  # Handling SSL certificate failed
                context = ssl._create_unverified_context()
                response = urlopen(req, context=context)
            page = response.read()
            return page
        except:
            return "Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:  # If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"', start_line + 1)
        end_content = s.find(',"ow"', start_content + 1)
        content_raw = str(s[start_content + 6:end_content - 1])
        return content_raw, end_content


# Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    compteur=5
    for i in range (0,compteur,1):
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)  # Append all the links in the list named 'Links'
            time.sleep(0.1)  # Timer could be used to slow down the request for image downloads
            page = page[end_content:]

    return items





def folder_creation(main_directory):
    existe=False
    fichier = os.listdir(rep)
    taille=len(fichier)
    for k in range (0,taille):
        current_str=fichier[k]
        if current_str=='ALBUM IMAGE FOLDER':
            existe=True
            break
    if existe !=True:
        os.makedirs(main_directory)
    







def lister_fichier_mp3():  #1 return the list of the files present in current folder
    
    fichier = os.listdir(rep)
    taille=len(fichier)
    fichier_mp3=[]
    for k in range (0,taille):
        current_str=fichier[k]
        value=current_str.find('.mp3')
        if value != -1:
            fichier_mp3.append(current_str)
        
    
    return fichier_mp3



def get_album_name(nom_en_str): #2 return name of a single album
    rep=os.getcwd()
    ultrapath=os.path.join(rep,nom_en_str)
    mp3 = MP3File(ultrapath)
    alb=mp3.album
    s=str(alb[0])
    
    start_line = s.find('ID3')
    start_content = s.find('album:', start_line + 1)
    end_content = s.find(')', start_content+1)
    name_album = str(s[start_content + 6:end_content])
    
    return name_album


def get_artist_name(nom_en_str): #2 bis return name of a single artist
    rep=os.getcwd()
    ultrapath=os.path.join(rep,nom_en_str)
    mp3 = MP3File(ultrapath)
    art=mp3.artist
    s=str(art[0])
    
    start_line = s.find('gV2')
    start_content = s.find('artist:', start_line + 1)
    end_content = s.find(')', start_content+1)
    name_artist = str(s[start_content + 6:end_content])
    
    return name_artist



def get_liste_information_name(new_liste):  # 3 return in a list the name of all ablum of mp3 file here
    liste_name_album=[]
    for k in range(0,len(new_liste)):
        top=get_album_name(new_liste[k])
        if top == '':           #if no alubm
            top=get_artist_name(new_liste[k])   #if no artist
            if top =='':
                top=str(new_liste[k])
                top=top.replace('.mp3','')
        top = top + ' album couverture'
        print(top)
        liste_name_album.append(top)
        
    return liste_name_album


def image_replacement(title_music,title_img):
    rep=os.getcwd()
    
    path_music=os.path.join(rep,title_music)
    path_img=os.path.join(rep,'ALBUM IMAGE FOLDER\\'+title_img+'.jpg')
    
    mp3 = stagger.read_tag(path_music)
    mp3.picture =path_img
    mp3.write()
    













