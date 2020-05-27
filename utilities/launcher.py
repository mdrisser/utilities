import time

def countdown(n=10):
	print("Begining countdown to launch.")
	print("T minus")

	while n > 0:
		print(n)
		n = n - 1
		time.sleep(1)

	print("IGNITION!")


if __name__ == "__main__":
	countdown()