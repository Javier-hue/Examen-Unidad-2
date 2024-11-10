usuario_predeterminado = "usuario"
contrasena_predeterminada = "12212005"

biblioteca = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "editorial": "Sudamericana"},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "editorial": "Francisco de Robles"}
]

def iniciar_sesion():
    print("Bienvenido al sistema de la Biblioteca de Lázaro Cárdenas")
    usuario = input("Ingrese su nombre de usuario: ")
    while True:
        contrasena = input("Ingrese su contraseña: ")
        if contrasena == contrasena_predeterminada:
            print("Bienvenido a la biblioteca de Lázaro Cárdenas")
            return True
        else:
            print("Contraseña inválida. Intente de nuevo.")

def buscar_libro():
    criterio = input("¿Desea buscar por título o por autor? (escriba 'titulo' o 'autor'): ").lower()
    if criterio == "titulo":
        titulo = input("Ingrese el título del libro: ")
        for libro in biblioteca:
            if libro["titulo"].lower() == titulo.lower():
                print(f"Libro encontrado: {libro}")
                return
        print("Libro no encontrado.")
    elif criterio == "autor":
        autor = input("Ingrese el nombre del autor: ")
        for libro in biblioteca:
            if libro["autor"].lower() == autor.lower():
                print(f"Libro encontrado: {libro}")
                return
        print("Libro no encontrado.")
    else:
        print("Criterio inválido.")

def ingresar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    nuevo_libro = {"titulo": titulo, "autor": autor, "editorial": editorial}
    biblioteca.append(nuevo_libro)
    print("Libro ingresado con éxito.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Buscar libro")
        print("2. Ingresar libro")
        print("3. Salir")
        opcion = input("Seleccione una opción (1, 2 o 3): ")
        if opcion == "1":
            buscar_libro()
        elif opcion == "2":
            ingresar_libro()
        elif opcion == "3":
            print("Gracias por utilizar la Biblioteca de Lázaro Cárdenas. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if iniciar_sesion():
    menu()
