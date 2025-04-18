from astropy import units as u

from src.simulador import (
    crear_orbita,
    crear_orbita_mercurio,
    crear_orbita_venus,
    crear_orbita_marte,
    crear_orbita_heliocentrica
)
from src.visualizacion import (
    mostrar_orbita_2d,
    mostrar_orbitas_2d,
    comparar_orbitas_planetas
)

def menu():
    print("\n=== Simulador Orbital 2D ===")
    print("1. Órbita terrestre")
    print("2. Órbita de Mercurio")
    print("3. Órbita de Venus")
    print("4. Órbita de Marte")
    print("5. Órbita heliocéntrica personalizada") # Para 1 sola órbita x que eliges dependiendo de UA
    print("6. Sistema Solar Interior (4 planetas)") # Vista rápida a las órbitas reales 
    print("7. Comparativa de órbitas planetarias") # Plus de la opción 6 más detallada
    print("8. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            orbita = crear_orbita()
            mostrar_orbita_2d(orbita)
        elif opcion == "2":
            orbita = crear_orbita_mercurio()
            mostrar_orbita_2d(orbita)
        elif opcion == "3":
            orbita = crear_orbita_venus()
            mostrar_orbita_2d(orbita)
        elif opcion == "4":
            orbita = crear_orbita_marte()
            mostrar_orbita_2d(orbita)
        elif opcion == "5":
            altitud = float(input("Ingrese altitud en UA: "))
            orbita = crear_orbita_heliocentrica(altitud * u.AU)
            mostrar_orbita_2d(orbita)
        elif opcion == "6":
            orbitas = [
                crear_orbita_mercurio(),
                crear_orbita_venus(),
                crear_orbita(),
                crear_orbita_marte()
            ]
            mostrar_orbitas_2d(orbitas)
        elif opcion == "7":
            comparar_orbitas_planetas()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()