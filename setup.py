from distutils.core import setup
import py2exe, sys, os
import pygame

sys.argv.append('py2exe')

files = [('music', ['C:\\Users\\Kulsoom\\PycharmProjects\\FoodFetcher\\music\\music.wav',
                    'C:\\Users\\Kulsoom\\PycharmProjects\\FoodFetcher\\music\\lostitem.wav',
                    'C:\\Users\\Kulsoom\\PycharmProjects\\FoodFetcher\\music\\gotitem.wav']),
         ('images', ['C:\\Users\\Kulsoom\\PycharmProjects\\FoodFetcher\\images\\foodFetcherImg.png',
                     'C:\\Users\\Kulsoom\\PycharmProjects\\FoodFetcher\\images\\basketImg.png',
                     'C:\\Users\\Kulsoom\\PycharmProjects\\FoodFetcher\\images\\foodImg.png',
                     'C:\\Users\\Kulsoom\\PycharmProjects\\FoodFetcher\\images\\poisonImg.png'])]

setup(
    options={'py2exe': {'bundle_files': 1}},
    windows=[{'script': "food_fetcher.py"}],
    zipfile=None,
    data_files=files, requires=['pygame']
)
