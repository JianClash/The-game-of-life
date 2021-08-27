import pygame, random

pygame.init()

WIDTH, HEIGHT = 1020, 560
SPACE_BETWEEN_CELLS = 20

black = (0, 0, 0)
white = (255, 255, 255)

alive = black
dead = white

chance = 50 #1/chance = Chance for the cell to be alive for the first generation
fps = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("conway's game of life")
win.fill(white) #Applies background color


def draw_lines():
	for i in range(WIDTH//20): #Drawing lines verticaly
		pygame.draw.line(win, black, (20*i, 0), (20*i, HEIGHT), 2) 

	for i in range(HEIGHT//20): #Drawing lines horizontaly
		pygame.draw.line(win, black, (0, 20*i), (WIDTH, 20*i), 2)

def generate_cells(): #Generates cell in random cell slots
	cells = []
	for i in range(HEIGHT//20):
		cells.append([])
		for j in range(WIDTH//20):
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
				pygame.draw.rect(win, j, (0+width_num + 2, 0+height_num + 2, 20 - 2, 20 - 2)) #Draws alive cells
			else:
				pygame.draw.rect(win, j, (0+width_num + 2, 0+height_num + 2, 20 - 2, 20 - 2)) #Draws dead cells
			width_num += 20
		width_num = 0
		height_num += 20
 
def update_cell(cells): #Updates the every cells state by the rules
	cells_copy = [[cells[x][y] for y in range(len(cells[0]))] for x in range(len(cells))]

	for i in range(len(cells)): #Finding every cells neibhors and updating the cells in a different list(cells_copy)
		for j in range(len(cells[i])):
			alive_cells = 0
			if j != 0: #All right side cell cheking arguments
				if cells[i][j - 1] == alive: #left to current cell
					alive_cells += 1
				if i != len(cells) - 1: #bottom left corner
					if cells[i + 1][j - 1] == alive:
						alive_cells += 1
				if i != 0: #top left corner
					if cells[i - 1][j - 1] == alive:
						alive_cells += 1

			if i != len(cells) - 1:
				if cells[i + 1][j] == alive: #bottom
					alive_cells += 1
				if j != len(cells[i]) - 1: #bottom right corner
					if cells[i + 1][j + 1] == alive:
						alive_cells += 1
				if j != 0: #bottom left corner
					if cells[i + 1][j - 1] == alive:
						alive_cells += 1
				
			if j != len(cells[i]) - 1:
				if cells[i][j + 1] == alive: #right
					alive_cells += 1
				if i != len(cells) - 1: #bottom right corner
					if cells[i + 1][j + 1] == alive:
						alive_cells += 1
				if i != 0: #top right corner
					if cells[i - 1][j + 1] == alive: 
						alive_cells += 1

			if i != 0:
				if cells[i - 1][j] == alive: #top
					alive_cells += 1 
				if j != 0:#top left corner
					if cells[i - 1][j - 1] == alive:
						alive_cells += 1 
				if j != len(cells[i]) - 1: #top right
					if cells[i - 1][j + 1] == alive:
						alive_cells += 1

			
			if cells[i][j] == alive:
				if alive_cells < 2 or alive_cells > 3:
					cells_copy[i][j] = dead
			else:
				if alive_cells == 3:
					cells_copy[i][j] = alive

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
		if run:
			display_cells(cells)
			pygame.display.update()
			cells = update_cell(cells)
			

if __name__ == '__main__':
	main()