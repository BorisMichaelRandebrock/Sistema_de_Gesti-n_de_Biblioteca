""" 
Sistema de Gestión de Biblioteca
Este programa simula un sistema de gestión de biblioteca. El usuario puede agregar libros a la biblioteca, prestar libros, devolver libros, mostrar todos los libros y buscar libros por ISBN.
"""
"""Colores de texto en la terminal para ser usado en el programa. araves de la syntaxis f"{COLOR}Texto{RESET}" """
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

"""definimos la clase Libro con los atributos titulo, autor, isbn y disponible. 
El método __init__ inicializa los atributos de la clase. El método __str__ 
devuelve una cadena con los atributos del libro. El método agregar agrega un l
ibro a la biblioteca. El método prestar cambia el estado del libro a no disponible. 

El método devolver cambia el estado del libro a disponible. 
Los metodos staticos a continuacion son metodos que no requieren una instancia de la clase para ser llamados y por
tanto no reciben el parametro self.
Se definen como estaticos dentro de la clase con el decorador @staticmethod para mayoor cohesion y claridad del codigo.
El método statico delete elimina todos los libros de la biblioteca.Esta funcion es un bonus escondido, no se muestra en el menu.
El método statico mostrar muestra todos los libros de la biblioteca. 
El método statico buscar busca un libro por ISBN. 
El método statico get_valid_isbn solicita al usuario un ISBN válido. 
El método statico run_librery ejecuta el programa principal."""
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"- {self.titulo}  ({self.autor}) - ISBN: {self.isbn} - Disponible: {'Sí' if self.disponible else 'No'}"

    def agregar(self, biblioteca):
        print("\n")
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = Libro.get_valid_isbn()
        libro = Libro(titulo, autor, isbn)
        biblioteca.append(libro)
        print(f"{GREEN}\nLibro agregado con éxito. {RESET} 🥳")

    def prestar(self):
        print("\n")
        if self.disponible:
            self.disponible = False
            print(f"{GREEN}\nLibro prestado con éxito. {RESET} 📚")
        else:
            print(f"{RED} \nEl libro ya está prestado. {RESET} 😱")

    def devolver(self):
        print("\n")
        if not self.disponible:
            self.disponible = True
            print(f"{GREEN} \nLibro devuelto con éxito.{RESET}   🤓 ")
        else:
            print(f"{RED}\nEl libro ya se ha devuelto. {RESET} 😱")
    
    @staticmethod
    def delete(biblioteca):
        print("\n")
        if not biblioteca:
            print(f"{RED}\nNo hay Libros en esta Biblioteca. {RESET} 😢")
            return
        for libro in biblioteca[:]:
            print(f"{GREEN}\nLibro {MAGENTA}{libro.titulo}{GREEN} eliminado con éxito. {RESET} 🥳")
            biblioteca.remove(libro)
        print(f"{BLUE}\nTodos los libros han sido eliminados con éxito. {RESET} 🥳")
    #original method, as requested ... since I wanted something more organized, I created a new method below
    #but kept this for evaluation purpose
    # @staticmethod
    # def mostrar(biblioteca):
    #     print("\n")
    #     if not biblioteca:
    #         print(f"{BLUE}\nNo hay libros en la biblioteca. {RESET} 😢")
    #     else:
    #         for libro in biblioteca:
    #             print(libro)
    @staticmethod
    def mostrar(biblioteca):
        print("\n")
        if not biblioteca:
            print(f"{BLUE}\nNo hay libros en la biblioteca. {RESET} 😢")
        else:
            # Define column widths
            titulo_width = 40
            autor_width = 30
            isbn_width = 20

            # Print header
            print(f"{MAGENTA}{'Título'.ljust(titulo_width)} {'Autor'.ljust(autor_width)} {'ISBN'.ljust(isbn_width)} Disponible{RESET}")
            print("*" * (titulo_width + autor_width + isbn_width + 15))  # Adjust the total width as needed
            print("\n")
            # Print each book
            for libro in biblioteca:
                titulo = libro.titulo.ljust(titulo_width)
                autor = libro.autor.ljust(autor_width)
                isbn = libro.isbn.ljust(isbn_width)
                disponible = 'Sí' if libro.disponible else 'No'
                print(f"- {titulo} {autor} - ISBN: {isbn} - Disponible: {disponible}")

    @staticmethod
    def buscar(biblioteca, isbn):
        print("\n")
        for libro in biblioteca:
            if libro.isbn == isbn:
                print(libro)
                return libro
        print(f"{BLUE}\nLibro no encontrado. {RESET} 😢")
        return None

    @staticmethod
    def get_valid_isbn():
        while True:
            isbn = input(f"\n{YELLOW}Ingresa el ISBN: {RESET}")
            try:
                isbn_int = int(isbn)
                return str(isbn_int)
            except ValueError:
                print(f"\n{RED}El ISBN debe ser un número entero.{RESET} 😡")

    @staticmethod
    def run_librery():
        # Create a list of books in order to have already some books in the store.
        biblioteca = [
            Libro("El Quijote", "Miguel de Cervantes", "12345"),
            Libro("Cien Años de Soledad", "Gabriel García Márquez", "67890"),
            Libro("1984", "George Orwell", "11223"),
            Libro("El Señor de los Anillos", "J.R.R. Tolkien", "44556"),
            Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "77889"),
            Libro("The Hithchiker's Guide to the Galaxy", "Douglas Adams", "33445"),
            Libro("The Catcher in the Rye", "J.D. Salinger", "55678"),
            Libro("The Great Gatsby", "F. Scott Fitzgerald", "99001"),
            Libro("The Da Vinci Code", "Dan Brown", "11223"),
            Libro("The Alchemist", "Paulo Coelho", "33445"),
        ]
        while True:#menu principal
            print(f"\n{CYAN} Bienvenido al Sistema de Gestión de Biblioteca {RESET}\n ")
            print("*******************************************************\n")
            print(f"{CYAN} 1. {YELLOW} Agregar libro {RESET}")
            print(f"{CYAN} 2. {YELLOW} Prestar libro {RESET}")
            print(f"{CYAN} 3. {YELLOW} Devolver libro {RESET}")
            print(f"{CYAN} 4. {YELLOW} Mostrar libros {RESET}")
            print(f"{CYAN} 5. {YELLOW} Buscar libro por ISBN{RESET}")
            print(f"{CYAN} 6. {YELLOW} Salir {RESET}")
            print("\n*******************************************************\n")
            opcion = input(f"{CYAN} \nElige una opción: {RESET}")

            if opcion == "1":
                Libro.agregar(Libro, biblioteca)
            elif opcion == "2":
                isbn = Libro.get_valid_isbn()
                libro = Libro.buscar(biblioteca, isbn)
                if libro:
                    libro.prestar()
            elif opcion == "3":
                isbn = Libro.get_valid_isbn()
                libro = Libro.buscar(biblioteca, isbn)
                if libro:
                    libro.devolver()
            elif opcion == "4":
                Libro.mostrar(biblioteca)
            elif opcion == "5":
                isbn = input(f"{YELLOW}Ingresa el ISBN: {RESET} ")
                Libro.buscar(biblioteca, isbn)
            elif opcion == "6":
                print(f"{BLUE}\nGracias por usar el Sistema de Gestión de Biblioteca {RESET}\n 😊\n")
                break
            elif opcion == "7":
                Libro.delete(biblioteca)
            else:
                print(f"{RED}\nOpción inválida. Por favor, elige una opción válida. {RESET} 😡")


Libro.run_librery()