from django.http import JsonResponse

pokemonAccesoriesList = [
  "Gorra de Ash Ketchum",
  "Bufanda de Pikachu",
  "Mochila de Pokémon",
  "Calcetines con diseños de Poké Balls",
  "Camiseta con el logotipo de Pikachu",
  "Sudadera con capucha de Eevee",
  "Zapatillas con estampado de Poké Balls",
  "Pulsera con colgantes de los distintos tipos de Pokémon",
  "Pañuelo con ilustraciones de los Pokémon iniciales",
  "Cinturón con un broche en forma de Poké Ball",
  "Pendientes en forma de Pikachu",
  "Chaqueta con el estampado del mapa de la región de Kanto",
  "Guantes con diseño de Pikachu",
  "Gafas de sol con forma de Poké Balls",
  "Pañuelo con estampado de Pokémon legendarios",
  "Parche o pin de la insignia de un líder de gimnasio",
  "Cartera con ilustraciones de los iniciales de todas las generaciones",
  "Reloj con la esfera con forma de Poké Ball",
  "Pijama con estampado de Pokémon",
  "Anillo con incrustaciones de gemas en forma de Pokémon"
]

priceList = [
  5175,
  14326,
  8250,
  12008,
  6387,
  17392,
  4563,
  9891,
  2154,
  15279,
  3866,
  10943,
  6331,
  18457,
  7926,
  3982,
  11873,
  2955,
  16240,
  7451,
]

discountList = [
  30,
  57,
  12,
  84,
  41,
  76,
  5,
  93,
  23,
  68,
  38,
  71,
  16,
  89,
  47,
  63,
  9,
  77,
  52,
  88,
]

data = {}
for i in range(len(pokemonAccesoriesList)):
  data[str(i)] = {
    'name': pokemonAccesoriesList[i],
    'price': priceList[i],
    'discount': discountList[i]
  }

offerList = [
  5,
  14,
  3,
  11,
  7,
  18,
  2,
  9,
  13,
  1,
]

offerData = {}
for i in range(len(offerList)):
  offerData[str(i)] = {
    'name': pokemonAccesoriesList[offerList[i]],
    'price': priceList[offerList[i]],
    'discount': discountList[offerList[i]]
  }


def products(request):
  return JsonResponse(data)

def offer(request):
  return JsonResponse(offerData)
