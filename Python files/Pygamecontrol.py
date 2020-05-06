import pygame

def move(direction, num_pixels, item): # item must be a list containing 2 items first being the xpos second being the ypos
   if direction == "Left":
       item[0] -= num_pixels
   if direction == "Right":
       item[0] += num_pixels
   if direction == "Up":
       item[1] -= num_pixels
   if direction == "Down":
       item[1] += num_pixels
def rotate(degrees, item, centered=True_or_False, SURFACE): #item must be a surface declared like so: surface = pygame.Surface((Height, Width), pygame.SRCALPHA, how transparent you want it to be 0 transparent - 225 solid) also SURFACE is the screen you defin by the command pygame.display.set_mode((width, height))
   if centered == True:
      rotated_surface = pygame.transform.rotate(item, angle)
      rect = rotated_surface.get_rect(center = (100, 100))
      SURFACE.blit(rotated_surface, (rect.x, rect.y)) 
   if centered == False:
      rotated_surface = pygame.transform.rotate(surface, angle)
      rect = rotated_surface.get_rect()
      SURFACE.blit(rotated_surface, (rect.x, rect.y))
def onclick(what_to_do) # must be placed under the command: for event in pygame.event.get():
   if event.type == pygame.event.MOUSEBUTTONDOWN and event.type == pygame.event.MOUSEBUTTONUP:
      what_to_do
def onmousedown(what_to_do): # extras are same as above function
   if event.type == pygame.event.MOUSEBUTTONDOWN:
      what_to_do
def onmouseup(what_to_do): # extras are same as above function
   if event.type == pygame.event.MOUSEBUTTONUP:
      what_to_do   
def onkey(what_to_do, which_key, up_or_down): # extras are same as above function
   if up_or_down == "Up": 
      if event.type == pygame.event.KEYUP:
         if pygame.event.key =  which_key:
            what_to_do
   if up_or_down == "Down":
      if event.type == pygame.event.KEYDOWN:
         if pygame.event.key = which_key:
            what_to_do
