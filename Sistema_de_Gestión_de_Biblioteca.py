"""
Después de la realización y implementación del enunciado, se realizo una mejora 
en varios aspectos del código:
- Se opto por mejorar el método estático "mostrar", mostrando los libros en 
forma de tabla, para una mejor visualización de los datos.
- Se agrego un método estático "delete", que elimina todos los libros de la 
biblioteca, como un bonus escondido, ya que no se muestra en el menu y se 
llama con la opción 7.
- Se mantuvo el método original de "mostrar" como "mostrarOriginal" para su
evaluación en la posición 8, no reflejada en el menu.
- Se agrego un método estático "get_valid_isbn", que solicita al usuario un ISBN 
válido, si el ISBN no es un número entero, muestra un mensaje de error.

Algunas lineas superan los 79 caracteres, pero se mantuvieron para mejorar la
legibilidad del código y/o el formato (en el popup).

A fin de cumplir con las buenas practicas de programación (utilización del 
ingles en los nombres de las variables, métodos y atributos), se opto por
mantener la nomenclatura de las variables, no-predeterminadas por el enunciado,
en ingles.
"""

# Colores de texto en la terminal para ser usado en el programa. a traves de la: 
# sintaxis: f"{COLOR}Texto{RESET}" 
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# import tkinter as tk
# from tkinter import Label, Button
from time import sleep
#sudo apt-get install python3-tk

# Función que crea un popup de bienvenida al usuario al inicio del programa
# def introduce():
#     root = tk.Tk()
#     root.title("📚")
#     root.geometry("1250x750")
    
#     # Creación de un mensaje de bienvenida en la ventana tipo popup
#     message = Label(
#         root,
#         text="\nWelcome to the grand opening of the Library Management System!!!\n\nNos hemos tomado la libertad de añadir una selección de libros a la biblioteca para que puedas empezar a disfrutar de ellos.\n\nFuera de las opciones del menú incluimos 2 opciones adicionales:\n\n1. Eliminar todos los libros de la biblioteca (opción 7)\n2. Mostrar los libros como pedido en el enunciado (opción 8)\n\nEsperamos que disfruten de la lectura y de esta experiencia.\n\nGracias por usar el Sistema de Gestión de Biblioteca. 😊",
#         font=("Arial", 14),
#         wraplength=1200
#     )
#     message.pack(pady=10)
#     # Creación de un botón para cerrar la ventana
#     button = Button(
#         root, 
#         text="Cerrar", 
#         command=root.destroy, 
#         font=("Arial", 12)
#     )
#     button.pack(pady=10)
#     root.bind("<Return>", lambda event: root.destroy())
#     button.focus_set()
#     button.key = "Return"
    
#     # Correr el popup de bienvenida
#     root.mainloop()

# # Iniciar el popup de bienvenida al principio del programa
# if __name__ == "__main__":
#     introduce()

# Definición la clase Libro con los atributos (string) -> titulo, autor, isbn
# (booleano) -> disponible.
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible # inicialización como disponible por defecto.

    def __str__(self): # método que devuelve una cadena con los atributos del 
        # libro, utilizo un operador ternario para mostrar si el libro esta 
        # disponible o no.
        disponible = (
            f"{GREEN}Sí{RESET}" if self.disponible else f"{RED}No{RESET}"
        )
        return ( # se retorna la cadena con los atributos del libro.
            f"- {self.titulo}  ({self.autor}) - ISBN: {self.isbn} - "
            f"Disponible: {disponible}"
        )


    def prestar(self): # método que cambia el estado del libro a no disponible si
        # el libro esta disponible, de lo contrario muestra un mensaje de error.
        print("\n")
        if self.disponible: # si el libro esta disponible, se cambia a no
            # disponible
            self.disponible = False
            print(f"{GREEN}\nLibro: {self.titulo} prestado con éxito. {RESET}📚")
            # y se muestra un mensaje de éxito.
            return True
        else: # si el libro no esta disponible, muestra un mensaje de error.
            print(f"{RED} \nLibro: {self.titulo} ya está prestado. {RESET} 😱")
            return False

    def devolver(self): # método que cambia el estado del libro a disponible si el
        # libro no esta disponible, de lo contrario muestra un mensaje de error.
        print("\n")
        if not self.disponible: # si el libro no esta disponible, se cambia a
            # disponible.
            self.disponible = True
            print(f"{GREEN} \nLibro: {self.titulo} devuelto con éxito.{RESET} 🤓") 
            # y se muestra un mensaje de éxito.
            return True
        else:
            print(f"{RED}\nEl libro: {self.titulo} ya se ha devuelto.{RESET} 😱") 
            # mensaje de error si el libro ya esta disponible y no se puede devolver.
            return False

    # A partir de aquí se definen los métodos estáticos de la clase Libro, 
    # métodos que no requieren una instancia de la clase para ser llamados y por 
    # tanto no reciben el parámetro self.
    # se definen como estáticos dentro de la clase con el decorador @staticmethod
    # para mayor cohesion y claridad del código.

    @staticmethod # método estático que agrega un libro a la biblioteca, solicita
    def agregar(biblioteca): # solicita al usuario el titulo, autor y isbn del libro. 
        # Se verifica que el isbn sea un numero entero usando el método "get_valid_isbn".
        print("\n") # se añañde un salto de linea para mejorar la visualización.
        titulo = input("Título: ") # se solicita al usuario el título del libro.
        if not titulo: # si el título esta vacío, muestra un mensaje de error.
            print(f"{RED}\nEl título no puede estar vacío. {RESET} 😡")
            return # y se sale de la función.
        autor = input("Autor: ") # se solicita al usuario el autor del libro.
        if not autor: # si el autor esta vacío, muestra un mensaje de error.
            print(f"{RED}\nEl autor no puede estar vacío. {RESET} 😡")
            return # y se sale de la función.
        isbn = Libro.get_valid_isbn() # se solicita al usuario el ISBN del libro.
        for libro in biblioteca: # se itera sobre la lista de libros en la biblioteca
            if libro.isbn == isbn: # si el ISBN del libro ya existe en la biblioteca
                print( # muestra un mensaje de error.
                    (
                        (
                            f"{RED}\n Ya existe un libro con el ISBN {isbn}" 
                            " en la biblioteca. "
                            f"{RESET} 😱"
                        )
                    )
                )
                return # y se sale de la función.
        libro = Libro(titulo, autor, isbn) # se crea una instancia de la clase Libro
        biblioteca.append(libro) # se añade el libro a la lista de libros en la biblioteca.
        print( # se muestra un mensaje de éxito.
            f"{GREEN}\nLibro: {YELLOW}{libro.titulo}{GREEN}, "
            f"Autor: {YELLOW}{libro.autor}{GREEN} agregado con éxito. {RESET}🥳"
        )

    @staticmethod # método estático que elimina todos los libros de la biblioteca.
    # Esta función es un bonus escondido, no se muestra en el menu y se llama con
    # la opción 7.
    def delete(biblioteca):
        print("\n") # se añade un salto de linea para mejorar la visualización.
        if not biblioteca: # si no hay libros en la biblioteca, muestra un mensaje
            # de error y se sale de la función.
            print(f"{RED}\nNo hay Libros en esta Biblioteca. {RESET} 😢")
            return
        for libro in biblioteca[:]:# se crea una copia de la lista para poder 
            # eliminar los libros de la lista original. iterando sobre la copia
            # de la lista, eliminando el original para no falsear el conteo.
            sleep(0.1) # se añade un retraso de 0.1 segundos para mejorar la
            # visualización y mejor userExperience.
            print(f"{GREEN}Libro: {MAGENTA}{libro.titulo}{GREEN} eliminado con éxito. {RESET} 👾")
            # se muestra un mensaje de éxito por cada libro eliminado.
            biblioteca.remove(libro) # se elimina el libro de la lista original.
        print(f"{BLUE}\nTodos los libros han sido eliminados con éxito. {RESET}✟")
        # se muestra un mensaje de éxito al finalizar la eliminación de los libros en azul.

    # Método mostrar original, -> siguiendo las instrucciones ->
    # como el resultado era algo desordenado a la vista, se opto por una version 
    # mejorada que muestra los libros en forma de tabla.
    # se mantiene para ser revisionado en la evaluación
    @staticmethod
    def mostrarOriginal(biblioteca):
        print("\n") # se añade un salto de linea para mejorar la visualización.
        if not biblioteca: # si no hay libros en la biblioteca, muestra un mensaje
            # de error y se sale de la función.
            print(f"{BLUE}\nNo hay libros en la biblioteca. {RESET} 😢")
        else:
            for libro in biblioteca: # se itera sobre la lista de libros en la biblioteca
                print(libro) # se imprime cada libro en la biblioteca.

    @staticmethod # Método estático que muestra todos los libros de la biblioteca
    # en forma de tabla.
    def mostrar(biblioteca):
        print("\n") # se añade un salto de linea para mejorar la visualización.
        if not biblioteca:# Si no hay libros en la biblioteca, muestra un mensaje
            # de error y se sale de la función
            print(f"{BLUE}\nNo hay libros en la biblioteca. {RESET} 😢")
        else:
            # Se define el ancho de las columnas de la tabla
            titulo_width = 40 # ancho de la columna del título para mejor visualización
            autor_width = 30 # ancho de la columna del autor para mejor visualización
            isbn_width = 20 # ancho de la columna del ISBN para mejor visualización

            # Imprime la cabecera de la tabla
            header = (
                f"{MAGENTA}{'Título'.ljust(titulo_width)}  "
                f"{'Autor'.ljust(autor_width)}  "
                f"{'ISBN'.ljust(isbn_width)}         Disponible{RESET}"
            )
            print(header) # se imprime la cabecera de la tabla
            print("*" * (titulo_width + autor_width + isbn_width + 30))  # Ajuste de longitud requerida
            print("\n") # se añade un salto de linea para mejorar la visualización.
            # Bucle para imprimir cada libro en la biblioteca
            for libro in biblioteca: # se itera sobre la lista de libros en la biblioteca
                sleep(0.1) # se añade un retraso de 0.1 segundos para mejorar la
                # visualización y mejor userExperience.
                titulo = libro.titulo.ljust(titulo_width) # se ajusta el ancho de la columna del título
                autor = libro.autor.ljust(autor_width) # se ajusta el ancho de la columna del autor
                isbn = libro.isbn.ljust(isbn_width) # se ajusta el ancho de la columna del ISBN
                disponible = f"{GREEN}Sí{RESET}" if libro.disponible else f"{RED}No{RESET}" 
                # se utiliza un operador ternario para mostrar si el libro esta disponible o no por colores.
                print(f"- {titulo} {autor} - ISBN: {isbn} - Disponible: {disponible}")

    @staticmethod # Método estático que busca un libro por ISBN, si el libro no 
    # se encuentra, muestra un mensaje de error.
    def buscar(biblioteca, isbn): # recibe la lista de libros en la biblioteca y
        # el ISBN del libro a buscar.
        print("\n") # se añade un salto de linea para mejorar la visualización.
        for libro in biblioteca: # se itera sobre la lista de libros en la biblioteca
            if libro.isbn == isbn: # si el ISBN del libro se encuentra en la
                # biblioteca, se muestra el libro y se retorna.
                print(libro) # se imprime el libro.
                return libro # se retorna el libro.
        sleep(1) # se añade un retraso de 1 segundo para crear la sensación de
        # que el programa esta buscando el libro.
        print(f"{BLUE}\nLibro con ISBN {isbn} no encontrado. {RESET} 😢")
        return None # si el libro no se encuentra, se retorna None porque no se
        # encontró el libro.

    @staticmethod # Método estático que solicita al usuario un ISBN válido, si el
    # ISBN no es un número entero, muestra un mensaje de error.
    def get_valid_isbn(): # no recibe parámetros.
        while True: # bucle infinito que solicita al usuario un ISBN válido.
            isbn = input(f"\n{YELLOW}Ingresa el ISBN: {RESET}") # solicita al
            # usuario el ISBN del libro.
            try:# Utilización un bloque try-except para manejar la excepción 
                # ValueError que se lanza si el usuario ingresa un ISBN que no es
                # un numero entero.
                isbn_int = int(isbn)#Se intenta convertir el ISBN a un número entero con un casting.
                return str(isbn_int) # si el ISBN es un número entero, se retorna
                # el ISBN como un string.
            except ValueError: # si el ISBN no es un número entero, muestra un
                # mensaje de error.
                print(f"\n{RED}El ISBN debe ser un número entero.{RESET} 😡")

    @staticmethod # ultimo método estático de la clase Libro, método que ejecuta 
    # el programa principal.
    def run_library():
        biblioteca = [# lista de libros predefinidos en la biblioteca, para que 
            # la librería sea como tal... una librería ya con libros.
            Libro("El Quijote", "Miguel de Cervantes", "12346"),
            Libro("Cien Años de Soledad", "Gabriel García Márquez", "67890"),
            Libro("1984", "George Orwell", "11223"),
            Libro("El Señor de los Anillos", "J.R.R. Tolkien", "44556"),
            Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "77889"),
            Libro("Harry Potter y la Cámara Secreta", "J.K. Rowling", "77890"),
            Libro("Harry Potter y el Prisionero de Azkaban", "J.K. Rowling", "77891"),
            Libro("Harry Potter y el Cáliz de Fuego", "J.K. Rowling", "77892"),
            Libro("Harry Potter y la Orden del Fénix", "J.K. Rowling", "77893"),
            Libro("Harry Potter y el Misterio del Príncipe", "J.K. Rowling", "77894"),
            Libro("H. Potter y las Reliquias de la Muerte", "J.K. Rowling", "77895"),
            Libro("The Hithchiker's Guide to the Galaxy", "Douglas Adams", "33445"),
            Libro("The Catcher in the Rye", "J.D. Salinger", "55678"),
            Libro("The Great Gatsby", "F. Scott Fitzgerald", "99001"),
            Libro("The Da Vinci Code", "Dan Brown", "12239"),
            Libro("The Alchemist", "Paulo Coelho", "93445"),
            Libro("The Little Prince", "Antoine de Saint-Exupéry", "55679"),
            Libro("The Hobbit", "J.R.R. Tolkien", "99002"),
            Libro("The Lion, the Witch and the Wardrobe", "C.S. Lewis", "12240"),
            Libro("El Péndulo de Foucault", "Umberto Eco", "93446"),
            Libro("El Nombre de la Rosa", "Umberto Eco", "55680"),
            Libro("Foucault's Pendulum", "Umberto Eco", "99003"),
        ]
        while True:# bucle infinito que muestra el menu principal del programa y
            # solicita al usuario que elija una opción.
            print(f"\n{CYAN} Bienvenido al Sistema de Gestión de Biblioteca {RESET}\n ")
            print("*******************************************************\n")
            print(f"{CYAN} 1. {YELLOW} Agregar libro {RESET}")
            print(f"{CYAN} 2. {YELLOW} Prestar libro {RESET}")
            print(f"{CYAN} 3. {YELLOW} Devolver libro {RESET}")
            print(f"{CYAN} 4. {YELLOW} Mostrar libros {RESET}")
            print(f"{CYAN} 5. {YELLOW} Buscar libro por ISBN{RESET}")
            print(f"{CYAN} 6. {YELLOW} Salir {RESET}")
            print("\n*******************************************************\n")
            option = input(f"{CYAN} \nElige una opción: {RESET}")# Solicita al 
            # usuario que elija una opción. Si no se elige una opción válida 
            #  (entre 1 y 7 - por la opción sorpresa), muestra un mensaje de error.
            # no precisa verificación de tipo de dato ya qe cualquier ingresado 
            #  que no coincide con los valores validos, muestra un mensaje de error.
            if option == "1":# en py no se puede usar switch-case, por lo que se
                # usa if-elif-else para evaluar la opción elegida por el usuario.
                # de hecho, podía usar el metodo match-case de python 3.10 que sería 
                # más limpio y eficiente y idoneo en este caso, pero el if-elif-else
                # es más compatible con versiones anteriores de python y ya esta hecho...
                Libro.agregar(biblioteca)
            elif option == "2": # si el usuario elige la opción 2, se solicita un
                isbn = Libro.get_valid_isbn() # solicita al usuario un ISBN válido
                libro = Libro.buscar(biblioteca, isbn) # busca el libro por ISBN
                if libro:
                    libro.prestar() # si el libro se encuentra, se presta.
            elif option == "3": # si el usuario elige la opción 3, 
                isbn = Libro.get_valid_isbn() # se solicita al usuario un ISBN válido
                libro = Libro.buscar(biblioteca, isbn) # busca el libro por ISBN
                if libro: # si el libro se encuentra, se devuelve.
                    libro.devolver()
            elif option == "4": # si el usuario elige la opción 4, se muestran los
                # libros de la biblioteca.
                Libro.mostrar(biblioteca)
            elif option == "5": # si el usuario elige la opción 5, se solicita un
                # ISBN válido al usuario y se busca el libro por ISBN.
                isbn = input(f"{YELLOW}Ingresa el ISBN: {RESET} ") 
                Libro.buscar(biblioteca, isbn) # y se busca el libro por ISBN.
            elif option == "6": # si el usuario elige la opción 6, se muestra un
                # mensaje de despedida y se sale del programa. y se sale del programa.
                print(f"{BLUE}\nGracias por usar el Sistema de Gestión de "
                      f"Biblioteca {RESET}")
                print("\n 😊\n")
                break
            elif option == "7": # si el usuario elige la opción 7, se eliminan todos
                # los libros de la biblioteca.
                Libro.delete(biblioteca)
            elif option == "8": # si el usuario elige la opción 8, se muestran los
                # libros de la biblioteca en el formato originalmnente solicitado.
                Libro.mostrarOriginal(biblioteca)
            else: # si el usuario elige una opción inválida, muestra un mensaje de
                # error.
                print(f"{RED}\nOpción inválida. "
                      f"Por favor, elige una opción válida. {RESET} 😡")


if __name__ == "__main__": # si el script se ejecuta directamente, se llama a la
    # función run_library de la clase Libro para ejecutar el programa principal.
    Libro.run_library()# Llamada a la función run_library, de la clase Libro para 
#ejecutar el programa principal.