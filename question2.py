#########################################
# Name: Yiming Chen                     #
# Student Number: 423960                #
# Course: software enginnering          #
# Question Number: 2                    #
#########################################






def Result():

	answer = 0

	a = 1  # Current number

	b = 2  # Next number

	while a <= 4000000:

		if a % 2 == 0:

			answer += a

		a, b = b, a + b

	return str(answer)


if __name__ == "__main__":

	print(Result())