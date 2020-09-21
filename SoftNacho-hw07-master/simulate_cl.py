#!/usr/bin/python3

import chutes_and_ladders

def main():
	min_moves = 100
	mean_moves = 0
	max_moves = 0
	total = 0

	for i in range(1,1000000):
		result=chutes_and_ladders.play_chutes_and_ladders(False)
		
		if result < min_moves:
			min_moves = result
		elif result > max_moves:
			max_moves = result
		
		total += result
		
	mean_moves = total / 1000000

	#printing
	print("X	", min_moves)
	print("Y	", mean_moves)
	print("Z	", max_moves)


if __name__ == "__main__":
        main()
else:
	exit


