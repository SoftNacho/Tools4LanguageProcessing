#!/usr/bin/python3
import myrandom

#starting_space=0

def move(starting_space, distance):
	#distance=myrandom.chutes_and_ladders_spinner()
	new_pos = starting_space + distance
	
	#new position over limit
	if new_pos > 100:
		new_pos -= distance
	
	#new position bottom of ladder
	elif new_pos == 1:
		new_pos = 38
	elif new_pos == 4:
                new_pos = 14
	elif new_pos == 9:
                new_pos = 31
	elif new_pos == 21:
                new_pos = 42
	elif new_pos == 28:
                new_pos = 84
	elif new_pos == 36:
                new_pos = 44
	elif new_pos == 51:
                new_pos = 67
	elif new_pos == 71:
                new_pos = 91
	elif new_pos == 80:
                new_pos = 100

	#new position on top of slide
	elif new_pos == 16:
                new_pos = 6
	elif new_pos == 47:
                new_pos = 26
	elif new_pos == 49:
                new_pos = 11
	elif new_pos == 56:
                new_pos = 53
	elif new_pos == 62:
                new_pos = 19
	elif new_pos == 64:
                new_pos = 60
	elif new_pos == 87:
                new_pos = 24
	elif new_pos == 93:
                new_pos = 73
	elif new_pos == 95:
		new_pos = 75
	elif new_pos == 98:
                new_pos = 78


	return new_pos
	#starting_space = new_pos

def play_chutes_and_ladders(game_print):
	current_position = 0
	moves = 0

	while (current_position != 100):
		dist=myrandom.chutes_and_ladders_spinner()
		moves += 1

		#call move function with position and result of spinner
		new=move(current_position, dist)
		
		if game_print == True:
			print(current_position, "	", dist, "	", new)

		#updating current_posistion
		current_position = new

	return moves


if __name__ == "__main__":
        play_chutes_and_ladders(True)
else:
	exit
