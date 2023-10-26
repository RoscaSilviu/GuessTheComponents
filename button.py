import pygame

#button class
class Button():
	def __init__(self, x, y, image_path, scale):
		self.image = pygame.image.load(image_path).convert_alpha()
		width = self.image.get_width()
		height = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.locked = False

	def lock(self):
		self.locked=True
	def unlock(self):
		self.locked=False
		
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		if self.locked==True:
			locked_image = self.image.copy()
			locked_image.fill((128, 128, 128, 128), special_flags=pygame.BLEND_RGBA_MULT)
			screen.blit(locked_image, self.rect)
		if self.locked==False:
			screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if self.locked==True:
			return 
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False
