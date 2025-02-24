""" class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.isbn} - {self.disponible} "
    
    def agregar(self):
        pass

    def prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True

    def mostrar(self):
        pass


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def mostrar(self):
        for libro in self.libros:
            print(libro)

    def buscar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def prestar(self, titulo):
        libro = self.buscar(titulo)
        if libro is not None:
            libro.prestar()
        else:
            print("Libro no encontrado")

    def devolver(self, titulo):
        libro = self.buscar(titulo)
        if libro is not None:
            libro.devolver()
        else:
            print("Libro no encontrado")
    
    def mostrar_disponibles(self):
        for libro in self.libros:
            if libro.disponible:
                print(libro)

    def bienvenida(self):
        print("Bienvenido a la Biblioteca")
        print("1. Agregar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("2. Mostrar libros")
        print("3. Buscar")
        print("7. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            self.agregar()
        elif opcion == "2":
            self.mostrar()
        elif opcion == "3":
            self.buscar()
        elif opcion == "4":
            self.prestar()
        elif opcion == "5":
            self.devolver()
        elif opcion == "6":
            self.mostrar_disponibles()
        elif opcion == "7":
            print("Gracias por usar la Biblioteca")
            exit()

biblioteca = Biblioteca()
biblioteca.bienvenida()



 """
"""
La siguiente práctica simula una tarea que nuestro jefe de proyecto nos ha
encargado. Se debe seguir al pie de la letra las exigencias del enunciado.
Enunciado de la práctica
Título: Sistema de Gestión de Biblioteca
Descripción: Eres el desarrollador de un sistema básico de gestión para una
biblioteca. Debes crear un programa en Python que permita registrar libros y
gestionar préstamos a usuarios. El programa debe cumplir con los siguientes
requisitos:
1. Clase Libro:
• Crea una clase Libro con los
atributos titulo (str), autor (str), isbn (str) y disponible (bool,
inicialmente True).
• Incluye un método agregar() que permita introducir un nuevo libro
con sus características.
• Incluye un método prestar() que cambie el estado de disponible a
False si el libro está disponible, y muestre un mensaje si ya está
prestado.
• Incluye un método devolver() que cambie el estado de disponible a
True si estaba prestado, y muestre un mensaje si ya estaba
disponible.
• Incluye un método mostrar() que devuelva una lista con todos los
libros de la biblioteca y los muestre en pantalla con todos sus datos
y diga si estás disponible o no.
• Incluye un método buscar() que busque un libro en concreto por su
ISBM y lo muestre en pantalla con todos sus datos y diga si está
disponible o no.
2. Gestión del inventario:
• Usa una lista para almacenar objetos de la clase Libro.
• Implementa un bucle que permita al usuario interactuar con el
programa mediante un menú con las siguientes opciones:
• a) Agregar un nuevo libro ingresando título, autor e ISBN.
• b) Prestar un libro buscando por ISBN.
• c) Devolver un libro buscando por ISBN.
• d) Mostrar todos los libros y su estado (disponible o no).
• e) Salir del programa.
3. Condiciones:
• Valida que el ISBN ingresado exista en la lista antes de prestar o
devolver un libro.
• Si el usuario ingresa una opción inválida en el menú, muestra un
mensaje de error y vuelve a pedir una opción.
Entregable:
• Un script en Python que implemente todas las funcionalidades descritas.
• El código debe ser claro, con comentarios explicativos y usando buenas
prácticas.
Ejemplo de uso. Al ejecutar el programa el resultado debería ser como se ve
en el siguiente ejemplo:
Bienvenido al Sistema de Gestión de Biblioteca
1. Agregar libro
2. Prestar libro
3. Devolver libro
4. Mostrar libros
5. Buscar
6. Salir
Elige una opción: 1
Título: El Quijote
Autor: Cervantes
ISBN: 12345
Libro agregado con éxito.
Elige una opción: 4
- El Quijote (Cervantes) - ISBN: 12345 - Disponible: Sí
Elige una opción: 2
Ingresa el ISBN: 12345
Libro prestado con éxito.
Elige una opción: 4
- El Quijote (Cervantes) - ISBN: 12345 - Disponible: No
Consideraciones a tener en cuenta:
Se creará la clase:
• Libro
Con los atributos:
• Titulo
• Autor
• isbn
• disponible
Se crearán los métodos:
• agregar
• prestar
• devolver
• Mostrar
• buscar
El ejercicio se entregará en un solo archivo con extensión .py
El nombre de la clase, atributos y métodos será exactamente el que se pide en el
enunciado.
Solo se admitirá una sola subida por alumno. En el caso de que un alumno suba
más de una versión del ejercicio, solo se calificará la primera que se subiese,
ignorando el sistema las demás. Por lo que se recomienda encarecidamente que
se revisen detalladamente los ejercicios antes de proceder a su entrega.
Cualquier ejercicio que no cumpla escrupulosamente los requisitos pedidos NO
SERÁ CORREGIDO.
Todo aquel ejercicio que sea entregado posteriormente a las 00:00 horas del día
dd/mm/yyyy no será corregido por el sistema.
"""
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"


class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"- {self.titulo} - {self.autor} - ISBN: {self.isbn} - Disponible: {'Sí' if self.disponible else 'No'}"

    def agregar(self, biblioteca):
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = get_valid_isbn()
        libro = Libro(titulo, autor, isbn)
        biblioteca.append(libro)
        print(f"{GREEN}Libro agregado con éxito. {RESET} 🥳")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"{GREEN}Libro prestado con éxito. {RESET} 📚")
        else:
            print(f"{RED} El libro ya está prestado. {RESET} 😱")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"{GREEN} Libro devuelto con éxito.{RESET}   🤓 ")
        else:
            print(f"{RED} El libro ya se ha devuelto. {RESET} 😱")

    @staticmethod
    def mostrar(biblioteca):
        if not biblioteca:
            print(f"{BLUE} No hay libros en la biblioteca. {RESET} 😢")
        else:
            for libro in biblioteca:
                print(libro)

    @staticmethod
    def buscar(biblioteca, isbn):
        for libro in biblioteca:
            if libro.isbn == isbn:
                print(libro)
                return libro
        print("Libro no encontrado.")
        return None


def get_valid_isbn():
    while True:
        isbn = input(f"{YELLOW}Ingresa el ISBN: {RESET}")
        try:
            isbn_int = int(isbn)
            return str(isbn_int)
        except ValueError:
            print(f"{RED}El ISBN debe ser un número entero.{RESET} 😡")


def gestionar_biblioteca():
    biblioteca = [
        Libro("El Quijote", "Miguel de Cervantes", "12345"),
        Libro("Cien Años de Soledad", "Gabriel García Márquez", "67890"),
        Libro("1984", "George Orwell", "11223"),
        Libro("El Señor de los Anillos", "J.R.R. Tolkien", "44556"),
        Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "77889"),
    ]
    while True:
        print(f"\n{CYAN} Bienvenido al Sistema de Gestión de Biblioteca {RESET}")
        print(f"{CYAN} 1. {YELLOW} Agregar libro {RESET}")
        print(f"{CYAN} 2. {YELLOW} Prestar libro {RESET}")
        print(f"{CYAN} 3. {YELLOW} Devolver libro {RESET}")
        print(f"{CYAN} 4. {YELLOW} Mostrar libros {RESET}")
        print(f"{CYAN} 5. {YELLOW} Buscar libro por ISBN{RESET}")
        print(f"{CYAN} 6. {YELLOW} Salir {RESET}")
        opcion = input(f"{CYAN} Elige una opción: {RESET} ")

        if opcion == "1":
            Libro.agregar(Libro, biblioteca)
        elif opcion == "2":
            isbn = get_valid_isbn()
            libro = Libro.buscar(biblioteca, isbn)
            if libro:
                libro.prestar()
        elif opcion == "3":
            isbn = get_valid_isbn()
            libro = Libro.buscar(biblioteca, isbn)
            if libro:
                libro.devolver()
        elif opcion == "4":
            Libro.mostrar(biblioteca)
        elif opcion == "5":
            isbn = input(f"{YELLOW}Ingresa el ISBN: {RESET} ")
            Libro.buscar(biblioteca, isbn)
        elif opcion == "6":
            print(f"{BLUE} Gracias por usar el Sistema de Gestión de Biblioteca {RESET} 😊")
            break
        else:
            print(f"{RED}Opción inválida. Por favor, elige una opción válida. {RESET} 😡")


gestionar_biblioteca()