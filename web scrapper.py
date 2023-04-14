import requests
from bs4 import BeautifulSoup
from os import system
from colorama import Fore
choice = 0
while(choice != 3):
    choice = int(input("Choose What you want to do: \n 1.View Someone's information using NIDA ID \n 2.Do a google search \n 3.exit \n >>>| "))
    if(choice == 1):
        idno = input("Enter your Nida Id(For Rwadans only): ")
        url = "https://brs.rdb.rw/busregonline/ESignature/GetDetailsFromNIDA?IDdocument=ID&Country=1003&IDdocumentNo=" + idno
        if(url == "https://brs.rdb.rw/busregonline/ESignature/GetDetailsFromNIDA?IDdocument=ID&Country=1003&IDdocumentNo="):
            url = "https://brs.rdb.rw/busregonline/ESignature/GetDetailsFromNIDA?IDdocument=ID&Country=1003&IDdocumentNo=1200280222231012"
    
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        Needed_information = ['IDdocumentNo','Name','ProvinceName','LastName','DistrictName','Gender','SectorName','DateOfBirth','CellName','VillageName','Streetname']
        for tag in soup.find_all():
            if "value" in tag.attrs and "name" in tag.attrs:
                if(tag['name'] in Needed_information):
                     if(tag['name'] == "Gender"):
                         # print(f"{tag['name']}: {tag['value']}")
                         if "checked" in tag.attrs:
                             # print(f"{tag['name']}: {tag['value']}")
                             print(tag['name'], ":", tag['value'])
                     else:
                         # print(f"{tag['name']}: {tag['value']}")
                         print(tag['name'], ":", tag['value'])
    elif(choice == 2):
         term = input("Enter the keyword to search: ")
         print("Seaching...")
         term = term.replace(" ","+")
         url = ["https://www.google.com/search?q="+term+"&sxsrf=AJOqlzWbZhBOERB6ACmY6z-A1trOAj6I0g:1676184468546&ei=lIvoY6TdINS7kdUPmr2a0AE&start=20&sa=N&ved=2ahUKEwik98zesY_9AhXUXaQEHZqeBho4ChDw0wN6BAgEEBc&biw=1280&bih=600&dpr=1","https://www.google.com/search?q="+term+"&sxsrf=AJOqlzWbZhBOERB6ACmY6z-A1trOAj6I0g:1676184468546&ei=lIvoY6TdINS7kdUPmr2a0AE&start=20&sa=N&ved=2ahUKEwik98zesY_9AhXUXaQEHZqeBho4ChDw0wN6BAgEEBc&biw=1280&bih=600&dpr=1","https://www.google.com/search?q="+term+"&sxsrf=AJOqlzWbZhBOERB6ACmY6z-A1trOAj6I0g:1676184468546&ei=lIvoY6TdINS7kdUPmr2a0AE&start=20&sa=N&ved=2ahUKEwik98zesY_9AhXUXaQEHZqeBho4ChDw0wN6BAgEEBc&biw=1280&bih=600&dpr=1","https://www.google.com/search?q="+term+"&sxsrf=AJOqlzWbZhBOERB6ACmY6z-A1trOAj6I0g:1676184468546&ei=lIvoY6TdINS7kdUPmr2a0AE&start=20&sa=N&ved=2ahUKEwik98zesY_9AhXUXaQEHZqeBho4ChDw0wN6BAgEEBc&biw=1280&bih=600&dpr=1"]
         for p in url:
             response = requests.get(p)
             soup = BeautifulSoup(response.text, "html.parser")
             title = (soup.find_all("a"))
             body = (soup.find_all("span"))
             tracker = 0 
             for i in title:
                 print(Fore.BLUE + str(i.text).replace("/url?q=", "") + "\n\n\t\t Link : " + str(i['href']))
                 print(Fore.WHITE + str(body[tracker]))
                 tracker +=1
         """url = "https://www.google.com/search?q=" + term + "&sxsrf=AJOqlzXbVUMfTBT8VBVdsGz6V3JHPkNmCA:1676177042204&ei=km7oY4L0C42jkdUP6rOA0AI&start=10&sa=N&ved=2ahUKEwiChbmJlo_9AhWNUaQEHeoZACoQ8tMDegQIAxAE"
         url = url.replace(" ","+")
         response = requests.get(url)
         soup = BeautifulSoup(response.text, "html.parser")
         for link in soup.find_all("h3"):
             print(link.text)
"""
