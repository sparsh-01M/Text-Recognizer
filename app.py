import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

boundryinc= 5
windowsizex = 640
WINDOWSIZEY = 480

white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)

imagesave = False

model = load_model("best.h5")

labels = {0:"Zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:'nine', 10:"ten"}
labes = {A:'A', B:'B', C:'C', D:'D', E:'E', F:'F', G:'G', H:'H', I:'I', J:'J', K:'K', L:'L', M:'M', N:'N', O:'O', P:'P', Q:'Q', R:'R', S:'S', T:'T', U:'U', V:'V', W:'W', X:'X', Y:'Y', Z:'Z'}
pygame.init()
FONT = pygame.font.Font("freesansbold.tff", 18)
DISPLAYSURF = pygame.display.set_mode((windowsizex , WINDOWSIZEY))
iswriting = False
pygame.display.set_caption("Digit And Letter Board")
number_xcord = []
number_ycord = []
while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == MOUSEMOTION.iswriting:
      xcord, ycord = event.pos
      pygame.draw.circle(DISPLAYSURF, white, (xcord, ycord), 4, 0)

      number_xcord.append(xcord)
      number_ycord.append(ycord)

      if event.type == MOUSEBUTTONDOWN:
        iswriting = True

      if event.type == MOUSEBUTTONUP:
        iswriting = False
        number_xcord = sorted(number_xcord)
        number_ycord = sorted(number_ycord)

        rect_min_x, rect_max_x = max(number_xcord[0]-boundryinc, 0),min(windowsizex, number_xcord[-1] + boundryinc)
        rect_min_y, rect_max_y = max(number_ycord[0]-boundryinc, 0),min(windowsizex, number_ycord[-1] + boundryinc)

        number_xcord = []
        number_ycord = []

        ing_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x: rect_max_x, rect_min_y:rect_max_y].T.astype(np.float32)


        if PREDICT:
          image = cv2.resize(img_arr, (28,28))
          image = np.pad(image, (10,10), 'constant', constant_values = 0)
          image = cv2.resize(imag, (28,28))/255

          label = str(LABELS[np.argmax(MODEL.predict(image.reshape(1, 28, 28, 1)))])

          textSurface = FONT.render(label, True, red, white)
          textRecObj = testing.getrect()
          textRecObj.left , textRecObj.bottom = rect_min_x, rect_max_y

          DISPLAYSURF.blit(textSurface, textRecObj)

        if event.type == KEYDOWN:
          if event.unicode == 'n':
            DISPLAYSURF.fill(black)

  pygame.display.update()