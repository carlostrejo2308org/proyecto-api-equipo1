import tkinter as ktr
from tkinter import Frame, ttk
from book import Book as Bk

class VentanaId:
    def __init__(self,master) -> None:
        '''Creando la ventana principal'''
        self.master = master
        self.width = 200
        self.height = 10
        master.title("Id")
        
        self.c = ktr.Canvas(master, width=self.width, height=self.height)
        self.c.pack()

        self.etiqueta = ktr.Label(master, text="Ingrese Id:")
        self.etiqueta.pack()

        self.Id = ktr.Entry()
        self.Id.pack()

        self.BttnFind = ktr.Button(master, text="Buscar", command = self.get_information)
        self.BttnFind.pack()

        self.BttnClose = ktr.Button(master, text="Cerrar", command=master.quit)
        self.BttnClose.pack()

    def get_information(self):
        '''Funcion Para obtener el id deseado por medio de la interfaz'''
        id = self.Id.get()
        self.buscar(id)


    def buscar(self,id):
        '''Funcion que se comunica con el modulo de extraccion de informacion del Api'''
        InstanciaLibro = Bk()
        Libros = InstanciaLibro.ExtraerElementos(id)
        if Libros == "No Existe":
            self.ErrorWindow(self.master)
        else:
            Titulo = Libros.get("title")
            Subtitulo = Libros.get("subtitle")
            Autor = Libros.get("authors")
            Publicacion = Libros.get("publisher")
            FechaPublicacion = Libros.get("publishedDate")
            Descripcion = Libros.get("description")
            NumPaginas = Libros.get("pageCount")
            Categoria =Libros.get("categories")
            self.ShowInformation(self.master, Titulo, Subtitulo,Autor,Publicacion,FechaPublicacion,Descripcion,NumPaginas,Categoria)
            
    def ShowInformation(self,master, titulo,subtitulo,autor,publicacion,fecha,descripcion,paginas,categoria):
        '''Funcion para nueva ventana que muestra el contenido si el Id existe'''
        self.width = 200
        self.height = 400
        window = ktr.Toplevel(master)
        window.title("Information")

        #Creando un frame principal
        main_frame = ktr.Frame(window)
        main_frame.pack(fill=ktr.BOTH, expand=1)

        #Creando un canvas
        my_canvas = ktr.Canvas(main_frame)
        my_canvas.pack(side=ktr.LEFT, fill=ktr.BOTH, expand=1)

        #Agregando un scrollbar al canvas
        my_scrollbar = ttk.Scrollbar(main_frame,orient=ktr.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=ktr.RIGHT, fill= ktr.Y)

        #Configurando el canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        #Creando otro frame dentro del canvas
        second_frame = Frame(my_canvas)

        #Agragando el nuevo frame a la ventana en el canvas
        my_canvas.create_window((0,0),window=second_frame, anchor = "center")

        #Titulo
        title_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LableTitle = ktr.Label(second_frame, text="Titulo:")
        LableTitle.pack()
        
        title_box.pack(expand=True)
        title_box.insert('end', titulo)
        title_box.config(state='disable')

        #Subtitulo
        subtitle_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LableSubitle = ktr.Label(second_frame, text="Subtitulo:")
        LableSubitle.pack()
        
        subtitle_box.pack(expand=True)
        subtitle_box.insert('end', subtitulo)
        subtitle_box.config(state='disable')
        
        #Autor
        author_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LableAuthor = ktr.Label(second_frame, text="Autor:")
        LableAuthor.pack()
        
        author_box.pack(expand=True)
        author_box.insert('end', autor)
        author_box.config(state='disable')

        #publicación
        publicator_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LablePublicator = ktr.Label(second_frame, text="Publicación:")
        LablePublicator.pack()
        
        publicator_box.pack(expand=True)
        publicator_box.insert('end', publicacion)
        publicator_box.config(state='disable')

        #Fecha de publicación
        date_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LableDate = ktr.Label(second_frame, text="Fecha de publicación:")
        LableDate.pack()
        
        date_box.pack(expand=True)
        date_box.insert('end', fecha)
        date_box.config(state='disable')

        #Descripcion
        description_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LableDescription = ktr.Label(second_frame, text="Descripcion:")
        LableDescription.pack()
        
        description_box.pack(expand=True)
        description_box.insert('end', descripcion)
        description_box.config(state='disable')
        
        #Paginas
        pages_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LablePages = ktr.Label(second_frame, text="Numero de páginas:")
        LablePages.pack()
        
        pages_box.pack(expand=True)
        pages_box.insert('end', paginas)
        pages_box.config(state='disable')
        
        #Categoria
        category_box = ktr.Text(
            second_frame,
            height=5,
            width=40
        )
        LableCategory = ktr.Label(second_frame, text="Categoria:")
        LableCategory.pack()
        
        category_box.pack(expand=True)
        category_box.insert('end', categoria)
        category_box.config(state='disable')

        

    def ErrorWindow(self,master):
        '''Funcion que manda una ventana de error'''
        self.width = 200
        self.height = 10
        window = ktr.Toplevel(master)
        window.title("Error")
        
        self.c = ktr.Canvas(window, width=self.width, height=self.height)
        self.c.pack()
        
        self.etiqueta = ktr.Label(window, text="No se encontro el ID")
        self.etiqueta.pack()

if __name__ == "__main__":
    root = ktr.Tk()
    Ventada = VentanaId(root)
    root.mainloop()
