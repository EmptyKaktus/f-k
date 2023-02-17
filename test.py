import pygame
import requests
import os
import sys

toponym = pt['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
toponym_coordinates = toponym['Point']['pos']
pt = ','.join(toponym_coordinates.split())

toponym = ir['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
toponym_coordinates = toponym['Point']['pos']
ir = ','.join(toponym_coordinates.split())

map_request = f'https://static-maps.yandex.ru/1.x/?l=map&pl={pt},{ir}'
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
