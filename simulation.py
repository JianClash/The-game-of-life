import pygame, random

pygame.init()

WIDTH, HEIGHT = 1020, 560
CELL_SLOT_SIZE = 20

black = (0, 0, 0)
white = (255, 255, 255)
purple = (128,0,128)

alive = purple 
dead = black

chance = 2 #1/chance = Chance for the cell to be alive for the first generation
fps = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("conway's game of life")
win.fill(black) #Applies background 

def draw_lines():
	for i in range(WIDTH//CELL_SLOT_SIZE): #Drawing lines verticaly
		pygame.draw.line(win, black, (CELL_SLOT_SIZE*i, 0), (CELL_SLOT_SIZE*i, HEIGHT), 2) 

	for i in range(HEIGHT//CELL_SLOT_SIZE): #Drawing lines horizontaly
		pygame.draw.line(win, black, (0, CELL_SLOT_SIZE*i), (WIDTH, CELL_SLOT_SIZE*i), 2)

def generate_cells(): #Generates cell in random cell slots
	cells = []
	for i in range(HEIGHT//CELL_SLOT_SIZE):
		cells.append([])
		for j in range(WIDTH//CELL_SLOT_SIZE):
			if random.randint(1, chance) < chance:
				cells[i].append(dead)
			else:
				cells[i].append(alive)
	return cells

def display_cells(cells):
	width_num, height_num = 0, 0
	for i in cells:
		for j in i:
			if j == alive:
				pygame.draw.rect(win, j, (0 + width_num + 2, 0 + height_num + 2, CELL_SLOT_SIZE - 2, CELL_SLOT_SIZE - 2 ))
			else:
				pygame.draw.rect(win, j, (0 + width_num + 2, 0 + height_num + 2, CELL_SLOT_SIZE - 2, CELL_SLOT_SIZE - 2))
			width_num += 20
		width_num = 0
		height_num += 20
 
def update_cell(cells): #Updates the every cells state by the rules
	cells_copy = [[cells[x][y] for y in range(len(cells[0]))] for x in range(len(cells))] #Copies the cells list without pointing to the same referance

	for i in range(len(cells)): #Finding every cells neibhors and updating the cells in a different list(cells_copy)
		for j in range(len(cells[i])):
			alive_cells = 0
			top_left, top_right = False, False
			bottom_left, bottom_right = False, False

			if j != 0: #All left side cell checking arguments
				if cells[i][j - 1] == alive: #left to current cell
					alive_cells += 1
				if i != len(cells) - 1: #bottom left corner
					bottom_left = True
					if cells[i + 1][j - 1] == alive:
						alive_cells += 1
				if i != 0: #top left corner
					top_left = True
					if cells[i - 1][j - 1] == alive:
						alive_cells += 1

			if i != len(cells) - 1: #All bottom cell checking arguments
				if cells[i + 1][j] == alive: #bottom
					alive_cells += 1
				if j != len(cells[i]) - 1: #bottom right corner
					bottom_right = True
					if cells[i + 1][j + 1] == alive:
						alive_cells += 1
				if j != 0: #bottom left corner
					if bottom_left != True:
						if cells[i + 1][j - 1] == alive:
							alive_cells += 1
				
			if j != len(cells[i]) - 1: #All right cells checking arguments
				if cells[i][j + 1] == alive: #right
					alive_cells += 1
				if i != len(cells) - 1: #bottom right corner
					if bottom_right != True:
						if cells[i + 1][j + 1] == alive:
							alive_cells += 1
				if i != 0: #top right corner
					top_right = True
					if cells[i - 1][j + 1] == alive: 
						alive_cells += 1

			if i != 0: #All top cell checking arguments
				if cells[i - 1][j] == alive: #top
					alive_cells += 1 
				if j != 0:#top left corner
					if top_left != True:
						if cells[i - 1][j - 1] == alive:
							alive_cells += 1 
				if j != len(cells[i]) - 1: #top right
					if top_right != True:
						if cells[i - 1][j + 1] == alive:
							alive_cells += 1
				
			if cells[i][j] == alive:
				if alive_cells < 2 or alive_cells > 3:
					cells_copy[i][j] = dead
			else:
				if alive_cells == 3:
					cells_copy[i][j] = alive

	#OPTIONAL
	# if cells == cells_copy: #Creates a new generation if there is know change
	# 	pygame.time.delay(1000)
	# 	return generate_cells()

	return cells_copy

def main():
	draw_lines()
	cells = generate_cells()
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick_busy_loop(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				run = False
				break
			if event.type == pygame.KEYDOWN:
				cells = generate_cells()
		if run:
			display_cells(cells)
			pygame.display.update()
			cells = update_cell(cells)
			
main()
