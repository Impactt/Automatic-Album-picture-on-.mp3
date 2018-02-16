# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:31:04 2018

@author: fmuret
"""

import functions_bot

#==========================   INIT   ==========================================

new_liste=lister_fichier_mp3()  #list of the file in the current repertory
search_term=get_liste_information_name(new_liste)   #list of the key word to search and DL
#search_term=['genji','hanzo','fatale','symetra overwatch','faucheur','sombra','mc cree']
lengh=len(search_term)  #number of the term to search, number of music as well

main_directory="ALBUM IMAGE FOLDER"
folder_creation(main_directory) #check if there is already a folder which exist
print('\n')



#====================== IMAGE DL ==============================================
for p in range (0,lengh,1):
    
    url = 'https://www.google.com/search?q=' + quote(search_term[p]) + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch'
    raw_html = (download_page(url))
    items =(_images_get_all_items(raw_html))    #sort and find all the picture  of the web page
    #print("Total Image Links = " + str(len(items)))       #display the number of all the picture string found
    
    k=0
    limit=5     #limit of attempt before to find a good picture, in case of error
    errorCount=0
    
    while (k < limit):      #DL start
                try:
                    req = Request(items[k], headers={
                        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
                    response = urlopen(req, None, 15)
                    image_name = str(items[k][(items[k].rfind('/')) + 1:])
                    if '?' in image_name:
                        image_name = image_name[:image_name.find('?')]
                    if ".jpg" in image_name or ".png" in image_name or ".jpeg" in image_name or ".svg" in image_name:
                        output_file = open(main_directory + "/" + "/" + search_term[p] + ".jpg", 'wb')
                    else:
                        output_file = open(main_directory + "/" + "/" + search_term[p] + ".jpg", 'wb')
                        image_name = image_name + ".jpg"
                        
                    data = response.read()
                    output_file.write(data)
                    response.close()
    
                    print("completed ====> " + str(k + 1) + ". " + image_name)
                    break
                    k = k + 1
    
                except IOError:  # If there is any IOError
                    errorCount += 1
                    print("IOError on image " + str(k + 1))
                    k = k + 1
    
                except HTTPError as e:  # If there is any HTTPError
                    errorCount += 1
                    print("HTTPError" + str(k))
                    k = k + 1
    
                except URLError as e:
                    errorCount += 1
                    print("URLError " + str(k))
                    k = k + 1
    
                except ssl.CertificateError as e:
                    errorCount += 1
                    print("CertificateError " + str(k))
                    k = k + 1
    
                if args.delay:
                    time.sleep(int(args.delay))

#================ IMAGE REPLACEMENT ===========================================



for n in range (0,lengh,1):
    path_music=new_liste[n]
    path_image=search_term[n]
    image_replacement(path_music,path_image)
    
    
    
    
    
    
    
    






















