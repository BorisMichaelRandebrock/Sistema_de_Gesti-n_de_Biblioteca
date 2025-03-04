import pytest
from Sistema_de_Gestión_de_Biblioteca import Libro, GREEN, RED, RESET

# Fixture para crear un libro de prueba
@pytest.fixture
def libro():
    return Libro("El Quijote", "Miguel de Cervantes", "12345")

# Pruebas para el método __init__
def test_libro_initialization(libro):
    assert libro.titulo == "El Quijote"
    assert libro.autor == "Miguel de Cervantes"
    assert libro.isbn == "12345"
    assert libro.disponible == True

# Pruebas para el método __str__
def test_libro_str(libro):
    expected_str = (
        "- El Quijote  (Miguel de Cervantes) - ISBN: 12345 - "
        f"Disponible: {GREEN}Sí{RESET}"
    )
    assert str(libro) == expected_str

# Pruebas para el método prestar
def test_libro_prestar(libro):
    assert libro.prestar() == True  # Préstamo exitoso
    assert libro.disponible == False  # El libro ya no está disponible
    assert libro.prestar() == False  # No se puede prestar dos veces

# Pruebas para el método devolver
def test_libro_devolver(libro):
    libro.prestar()  # Prestamos el libro primero
    assert libro.devolver() == True  # Devolución exitosa
    assert libro.disponible == True  # El libro está disponible nuevamente
    assert libro.devolver() == False  # No se puede devolver dos veces

# Pruebas para el método agregar
def test_libro_agregar(monkeypatch):
    biblioteca = []
    # Simula la entrada del usuario
    inputs = ["El Principito", "Antoine de Saint-Exupéry", "12345"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    
    Libro.agregar(biblioteca)
    
    assert len(biblioteca) == 1
    assert biblioteca[0].titulo == "El Principito"
    assert biblioteca[0].autor == "Antoine de Saint-Exupéry"
    assert biblioteca[0].isbn == "12345"

# Pruebas para el método buscar
def test_libro_buscar():
    biblioteca = [Libro("1984", "George Orwell", "11223")]
    libro = Libro.buscar(biblioteca, "11223")
    assert libro.titulo == "1984"
    assert Libro.buscar(biblioteca, "99999") == None  # ISBN no existe

# Pruebas para el método delete
def test_libro_delete():
    biblioteca = [Libro("1984", "George Orwell", "11223")]
    Libro.delete(biblioteca)
    assert len(biblioteca) == 0

# Pruebas para el método get_valid_isbn
def test_libro_get_valid_isbn(monkeypatch):
    # Simula la entrada del usuario
    monkeypatch.setattr('builtins.input', lambda _: "12345")
    isbn = Libro.get_valid_isbn()
    assert isbn == "12345"

    # Simula una entrada inválida seguida de una válida
    inputs = iter(["abc", "12345"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    isbn = Libro.get_valid_isbn()
    assert isbn == "12345"

def agregar_libros_de_prueba(biblioteca):
    result = Libro.agregar("", "El Quijote", "", "")
    assert result == False  # No se puede agregar un libro sin datos
    assert result == "El título no puede estar vacío.  😡"
    print("That's all folks!")
