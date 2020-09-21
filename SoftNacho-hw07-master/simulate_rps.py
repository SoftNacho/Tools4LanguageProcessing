#!/usr/bin/python3

import myrandom

def main():
	rock_count = 0
	paper_count = 0
	scissors_count = 0

	for i in range(1,1000000):
		result=myrandom.rock_paper_scissors()

		#increment counters appropriately
		if result == "rock":
			rock_count += 1

		elif result == "paper":
			paper_count += 1

		elif result == "scissors":
			scissors_count += 1

	#print results
	print("R	", rock_count)
	print("P	", paper_count)
	print("S	", scissors_count)


if __name__ == "__main__":
        main()
else:
	exit			
