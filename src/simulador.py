from poliastro.bodies import Earth, Mercury, Venus, Mars, Sun
from poliastro.twobody import Orbit
from astropy import units as u
from astropy.time import Time

# Órbita circular terrestre
def crear_orbita():
    altitud = 700 * u.km
    epoca = Time.now()
    return Orbit.circular(Earth, alt=altitud, epoch=epoca)

# Mercurio
def crear_orbita_mercurio():
    return Orbit.from_body_ephem(Mercury, Time.now())

# Venus
def crear_orbita_venus():
    return Orbit.from_body_ephem(Venus, Time.now())

# Marte
def crear_orbita_marte():
    return Orbit.from_body_ephem(Mars, Time.now())

# Alrededor del Sol
def crear_orbita_heliocentrica(altitud=1 * u.AU):
    return Orbit.circular(Sun, alt=altitud)