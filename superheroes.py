
nombreS = {
    "a": "Sobaco",
    "b": "Asesino",
    "c": "Capitán",
    "d": "Pezón",
    "e": "Trueno",
    "f": "Lobo",
    "g": "Conejo",
    "h": "Halcón",
    "i": "Sargento",
    "j": "Prepucio",
    "k": "El Milagro",
    "l": "El Rey",
    "m": "Maestro",
    "n": "Robot",
    "o": "Vigilante",
    "p": "Avispa",
    "q": "Doctor",
    "r": "Orificio",
    "s": "Pepino",
    "t": "Príncipe",
    "u": "Tiburón",
    "v": "Agujón",
    "w": "Fantasma",
    "x": "Agente",
    "y": "Tornado",
    "z": "Brujo",
        }
apellidoS = {
    "a": "Elástico",
    "b": "Carmesí",
    "c": "Radiactivo",
    "d": "Volador",
    "e": "Espacial",
    "f": "Letal",
    "g": "Flácido",
    "h": "Marciano",
    "i": "Venenoso",
    "j": "Invisible",
    "k": "Mutante",
    "l": "Vengador",
    "m": "Amoroso",
    "n": "Apestoso",
    "o": "Mágico",
    "p": "Gigante",
    "q": "Nazi",
    "r": "Bionico",
    "s": "Celestial",
    "t": "Sangriento",
    "u": "Rocoso",
    "v": "De Hierro",
    "w": "Psíquico",
    "x": "Maravilla",
    "y": "Hipster",
    "z": "Invencible",
}

colorS = ["Escarlata", "Dorada", "Amarillo", "Oscuro", "Verde", "Blanco", "Azul", "Gris", "Plateado", "Rojo"]
superpoderS = ["None", "Convertir todo en Algodon", "Velocidad de la luz", "Hablar con Animales", "Súper fuerza", "Control mental", "Invisibilidad", "Control de Fuego", "Crear tormentas", "Convertir agua en Cerveza", "Destruir planetas", "Saltar 20 metros", "Volar"]
armaS = ["None", "Bastón", "Espada", "Hacha", "Sombrilla", "Escudo", "Barita Mágica", "Rifle", "Cuchillo", "Bat de Baseball", "Cuerda", "Arco y Flecha", "Guante de Boxeo", "Sarten", "Pistola", "Manopla", "Martilo", "Motosierra", "Cadenas", "Destornillador", "Escoba", "Dagas", "Bumerangs", "Estrella Ninja", "Extintor", "Tijeras", "Destapacaños", "Lanza misiles", "Basto de Jokey", "Cepillo de Dientes", "Espada Mágica"]



nuevosDatos = []


def name():
    nombre =input ("¿Cómo te llamas? ")
    if nombre.isalpha() == True:
        n_super = nombreS [nombre[0].lower()]
        nuevosDatos.append(n_super)
    else:
        print (f"{nombre} no es un nombre")
    
    

def apellido():
    apellido = input ("¿Cuál es tu apellido? ")
    if apellido.isalpha() == True:
        n_super2 = apellidoS[apellido[0].lower()]
        nuevosDatos.append(n_super2)
    else:
        print (f"{apellido} no es un apellido")


def comprobar_fecha():
    try:
        datetime.datetime.strptime(text, '%d/%m/%Y')
    except:
        return "El formato debe ser  DD/MM/AAAA"
    return datetime.datetime.strptime(text, '%d/%m/%Y')



    
# def color ():    
#     year = (input ("¿en qué año naciste? "))
#     year = int (year[3])
#     color = colorS[year]
#     nuevosDatos.append(color)

# def superpoder():
#     mes = int (input ("¿En qué mes? "))
#     mes = int(mes)
#     superpoder = superpoderS [mes] 
#     nuevosDatos.append(superpoder)

# def arma():
#     dia = input ("¿En qué día? ")
#     dia = int(dia)
#     arma = armaS [dia] 
#     nuevosDatos.append(arma)
    
    
# apellido()
# apellido()
fecha = input("¿Cual es tu fecha de nacimiento? DD/MM/AAAA  ")
comprobar_fecha()
# color ()
# superpoder()
# arma()


# print (f"Soy {nuevosDatos[0]} {nuevosDatos[1]} {nuevosDatos[2]}, mi poder es el {nuevosDatos[3]} y voy a luchar contra la injusticia con mi {nuevosDatos[4]}!!")


