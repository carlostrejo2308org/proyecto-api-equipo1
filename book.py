from os import times
import json
import urllib.request
class Book:
    def __init__(self) -> None:
        self.id = 0
        self.dictlibros = {}
        self.dictLibrosTres = {}
        self.url="https://www.googleapis.com/books/v1/volumes/"

    def ExtraerElementos(self,id):
        self.id = id
        try:
            with urllib.request.urlopen(self.url+id) as url:
                data = json.loads(url.read().decode()) # Convert the JSON to string
            self.dictlibros = data
            title = self.dictlibros["volumeInfo"].get("title", "")
            subtitle = self.dictlibros["volumeInfo"].get("subtitle", "")
            authors = self.dictlibros["volumeInfo"].get("authors", "")
            publisher = self.dictlibros["volumeInfo"].get("publisher", "")
            publishedDate = self.dictlibros["volumeInfo"].get("publishedDate", "")
            description = self.dictlibros["volumeInfo"].get("description", "")
            pageCount = self.dictlibros["volumeInfo"].get("pageCount", "")
            categories = self.dictlibros["volumeInfo"].get("categories", "")

            # The extracted data is saved to the new dictionary
            self.dictLibrosTres = {
                "title": title,
                "subtitle":subtitle,
                "authors": authors,
                "publisher":publisher,
                "publishedDate":publishedDate,
                "description": description,
                "pageCount": pageCount,
                "categories": categories
            }
            return self.dictLibrosTres
        except:
            return "No Existe"
'''
if __name__ == "__main__":
    libro = Book()
    a = libro.ExtraerElementos("UpNHAQAAMAAJ")
    print(a)
'''