def tierra(segundos):
    gravedad = 9.81
    return calculoAltura(gravedad, segundos)

def marte(segundos):
    gravedad = 3.7
    return calculoAltura(gravedad, segundos)

def jupiter(segundos):
    gravedad = 24.8
    return calculoAltura(gravedad, segundos)

def calculoAltura(gravedad, segundos):
    return 1/2*gravedad*segundos**2