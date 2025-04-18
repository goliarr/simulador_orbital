from poliastro.plotting.static import StaticOrbitPlotter
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
from poliastro.ephem import Ephem
from poliastro.twobody import Orbit
from poliastro.bodies import Mercury, Venus, Earth, Mars, Sun

def mostrar_orbita_2d(orbita):
    # Visualización básica de una órbita
    fig, ax = plt.subplots(figsize=(6, 6))
    plotter = StaticOrbitPlotter(ax)
    
    nombre_cuerpo = orbita.attractor.name if hasattr(orbita, 'attractor') else "Desconocido"
    
    plotter.plot(orbita, label=f"Órbita alrededor de {nombre_cuerpo}")
    ax.set_title(f"Simulación Orbital 2D - {nombre_cuerpo}")
    plt.grid()
    plt.legend()
    plt.show()

def mostrar_orbitas_2d(orbitas):
    # Visualización múltiple de órbitas
    fig, ax = plt.subplots(figsize=(8, 8))
    plotter = StaticOrbitPlotter(ax)
    
    for orbita in orbitas:
        nombre = orbita.attractor.name if hasattr(orbita, 'attractor') else "Desconocido"
        plotter.plot(orbita, label=nombre)
    
    ax.set_title("Comparación de Órbitas")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

def comparar_orbitas_planetas():
    # Comparativa de órbitas planetarias
    fig, ax = plt.subplots(figsize=(10, 10))
    plotter = StaticOrbitPlotter(ax)
    
    planetas = [Mercury, Venus, Earth, Mars]
    colores = ['gray', 'orange', 'blue', 'red']
    nombres = ['Mercurio', 'Venus', 'Tierra', 'Marte']
    epoch = Time.now()
    
    for planeta, color, nombre in zip(planetas, colores, nombres):
        # Método actualizado para obtener efemérides
        ephem = Ephem.from_body(planeta, epoch)
        orb = Orbit.from_ephem(Sun, ephem, epoch)
        plotter.plot(orb, label=nombre, color=color)
    
    ax.set_title("Órbitas Planetarias Comparadas")
    plt.grid()
    plt.legend()
    plt.show()