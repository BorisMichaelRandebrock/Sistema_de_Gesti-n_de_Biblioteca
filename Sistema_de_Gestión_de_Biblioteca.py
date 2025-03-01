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
        return (
            f"- {self.titulo}  ({self.autor}) - ISBN: {self.isbn} - "
            f"Disponible: {disponible}"
        )


    def prestar(self): # método que cambia el estado del libro a no disponible si
        # el libro esta disponible, de lo contrario muestra un mensaje de error.
        print("\n")
        if self.disponible:
            self.disponible = False
            print(f"{GREEN}\nLibro: {self.titulo} prestado con éxito. {RESET}📚")
            return True
        else:
            print(f"{RED} \nLibro: {self.titulo} ya está prestado. {RESET} 😱")
            return False

    def devolver(self): # método que cambia el estado del libro a disponible si el
        # libro no esta disponible, de lo contrario muestra un mensaje de error.
        print("\n")
        if not self.disponible:
            self.disponible = True
            print(f"{GREEN} \nLibro: {self.titulo} devuelto con éxito.{RESET} 🤓")
            return True
        else:
            print(f"{RED}\nEl libro: {self.titulo} ya se ha devuelto.{RESET} 😱")
            return False

    # A partir de aquí se definen los métodos estáticos de la clase Libro, 
    # métodos que no requieren una instancia de la clase para ser llamados y por 
    # tanto no reciben el parámetro self.
    # se definen como estáticos dentro de la clase con el decorador @staticmethod
    # para mayor cohesion y claridad del código.

    @staticmethod # método estático que agrega un libro a la biblioteca, solicita
    def agregar(biblioteca): # solicita al usuario el titulo, autor y isbn del libro. 
        # Se verifica que el isbn sea un numero entero usando el método "get_valid_isbn".
        print("\n")
        titulo = input("Título: ")
        if not titulo:
            print(f"{RED}\nEl título no puede estar vacío. {RESET} 😡")
            return
        autor = input("Autor: ")
        if not autor:
            print(f"{RED}\nEl autor no puede estar vacío. {RESET} 😡")
            return
        isbn = Libro.get_valid_isbn()
        for libro in biblioteca:
            if libro.isbn == isbn:
                print(
                    (
                        (
                            f"{RED}\n Ya existe un libro con el ISBN {isbn}" 
                            " en la biblioteca. "
                            f"{RESET} 😱"
                        )
                    )
                )
                return
        libro = Libro(titulo, autor, isbn)
        biblioteca.append(libro)
        print(
            f"{GREEN}\nLibro: {YELLOW}{libro.titulo}{GREEN}, "
            f"Autor: {YELLOW}{libro.autor}{GREEN} agregado con éxito. {RESET}🥳"
        )

    @staticmethod # método estático que elimina todos los libros de la biblioteca.
    # Esta función es un bonus escondido, no se muestra en el menu y se llama con
    # la opción 7.
    def delete(biblioteca):
        print("\n")
        if not biblioteca:
            print(f"{RED}\nNo hay Libros en esta Biblioteca. {RESET} 😢")
            return
        for libro in biblioteca[:]:# se crea una copia de la lista para poder 
            # eliminar los libros de la lista original. iterando sobre la copia
            # de la lista, eliminando el original para no falsear el conteo.
            print(f"{GREEN}\nLibro: {MAGENTA}{libro.titulo}{GREEN} eliminado con éxito. {RESET} 👾")
            biblioteca.remove(libro)
        print(f"{BLUE}\nTodos los libros han sido eliminados con éxito. {RESET}✟")

    # Método mostrar original, -> siguiendo las instrucciones ->
    # como el resultado era algo desordenado a la vista, se opto por una version 
    # mejorada que muestra los libros en forma de tabla.
    # se mantiene para ser revisionado en la evaluación
    @staticmethod
    def mostrarOriginal(biblioteca):
        print("\n")
        if not biblioteca:
            print(f"{BLUE}\nNo hay libros en la biblioteca. {RESET} 😢")
        else:
            for libro in biblioteca:
                print(libro)

    @staticmethod # Método estático que muestra todos los libros de la biblioteca
    # en forma de tabla.
    def mostrar(biblioteca):
        print("\n")
        if not biblioteca:# Si no hay libros en la biblioteca, muestra un mensaje
            # de error y se sale de la función
            print(f"{BLUE}\nNo hay libros en la biblioteca. {RESET} 😢")
        else:
            # Se define el ancho de las columnas de la tabla
            titulo_width = 40
            autor_width = 30
            isbn_width = 20

            # Imprime la cabecera de la tabla
            header = (
                f"{MAGENTA}{'Título'.ljust(titulo_width)}  "
                f"{'Autor'.ljust(autor_width)}  "
                f"{'ISBN'.ljust(isbn_width)}         Disponible{RESET}"
            )
            print(header)
            print("*" * (titulo_width + autor_width + isbn_width + 30))  # Ajuste de longitud requerida
            print("\n")
            # Bucle para imprimir cada libro en la biblioteca
            for libro in biblioteca:
                sleep(0.1)
                titulo = libro.titulo.ljust(titulo_width)
                autor = libro.autor.ljust(autor_width)
                isbn = libro.isbn.ljust(isbn_width)
                disponible = f"{GREEN}Sí{RESET}" if libro.disponible else f"{RED}No{RESET}"
                print(f"- {titulo} {autor} - ISBN: {isbn} - Disponible: {disponible}")

    @staticmethod # Método estático que busca un libro por ISBN, si el libro no 
    # se encuentra, muestra un mensaje de error.
    def buscar(biblioteca, isbn):
        print("\n")
        for libro in biblioteca:
            if libro.isbn == isbn:
                print(libro)
                return libro
        sleep(1)
        print(f"{BLUE}\nLibro con ISBN {isbn} no encontrado. {RESET} 😢")
        return None

    @staticmethod # Método estático que solicita al usuario un ISBN válido, si el
    # ISBN no es un número entero, muestra un mensaje de error.
    def get_valid_isbn():
        while True:
            isbn = input(f"\n{YELLOW}Ingresa el ISBN: {RESET}")
            try:# Utilización un bloque try-except para manejar la excepción 
                # ValueError que se lanza si el usuario ingresa un ISBN que no es
                # un numero entero.
                isbn_int = int(isbn)
                return str(isbn_int)
            except ValueError:
                print(f"\n{RED}El ISBN debe ser un número entero.{RESET} 😡")

    @staticmethod # ultimo método estático de la clase Libro, método que ejecuta 
    # el programa principal.
    def run_library():
        #  Create a list of books in order to have already some books in the store.
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
                Libro.agregar(biblioteca)
            elif option == "2":
                isbn = Libro.get_valid_isbn()
                libro = Libro.buscar(biblioteca, isbn)
                if libro:
                    libro.prestar()
            elif option == "3":
                isbn = Libro.get_valid_isbn()
                libro = Libro.buscar(biblioteca, isbn)
                if libro:
                    libro.devolver()
            elif option == "4":
                Libro.mostrar(biblioteca)
            elif option == "5":
                isbn = input(f"{YELLOW}Ingresa el ISBN: {RESET} ")
                Libro.buscar(biblioteca, isbn)
            elif option == "6":
                print(f"{BLUE}\nGracias por usar el Sistema de Gestión de "
                      f"Biblioteca {RESET}")
                print("\n 😊\n")
                break
            elif option == "7":
                Libro.delete(biblioteca)
            elif option == "8":
                Libro.mostrarOriginal(biblioteca)
            else:
                print(f"{RED}\nOpción inválida. "
                      f"Por favor, elige una opción válida. {RESET} 😡")


if __name__ == "__main__":
    Libro.run_library()# Llamada a la función run_library, de la clase Libro para 
#ejecutar el programa principal.