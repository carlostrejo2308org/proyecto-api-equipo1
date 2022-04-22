from os import times
import json
import urllib.request
 
# It connects to the Google API and opens it as a file, then what is brought from the API converts it into a JSON
#id = "gqDf__ULmR8C"
id="UpNHAQAAMAAJ"
url="https://www.googleapis.com/books/v1/volumes/"
with urllib.request.urlopen(url+id) as url:
 
    data = json.loads(url.read().decode()) # Convert the JSON to string
    # print(data) Print data
 
# After the variable dictlibros, add the key "items" of the json data
dictlibros = {}

dictlibros = data
 
dictLibrosDos = {}
 
dictLibrosTres = {}

# Iterate the dictionary dictlibros to add more values ​​to the new dictionary dictLibrosDos

dictLibrosDos = dictlibros

# Add all books to dicLibrosDos

    
    # Extract the required fields from the API
title = dictLibrosDos["volumeInfo"].get("title", "")
subtitle = dictLibrosDos["volumeInfo"].get("subtitle", "")
authors = dictLibrosDos["volumeInfo"].get("authors", "")
publisher = dictLibrosDos["volumeInfo"].get("publisher", "")
publishedDate = dictLibrosDos["volumeInfo"].get("publishedDate", "")
description = dictLibrosDos["volumeInfo"].get("description", "")
pageCount = dictLibrosDos["volumeInfo"].get("pageCount", "")
categories = dictLibrosDos["volumeInfo"].get("categories", "")
   
    # The extracted data is saved to the new dictionary
dictLibrosTres = {
    "title": title,
    "subtitle":subtitle,
    "authors": authors,
    "publisher":publisher,
    "publishedDate":publishedDate,
    "description": description,
    "pageCount": pageCount,
    "categories": categories
}
    
  
  # Go through the dictionary of dicLibrosTres

print(dictLibrosTres) # Insert books to the collection