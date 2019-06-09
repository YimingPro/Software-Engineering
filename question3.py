#########################################
# Name: Yiming Chen                     #
# Student Number: 423960                #
# Course: software enginnering          #
# Question Number: 3                    #
#########################################



x = 600851475143

y = 2

while y < x:

    if x% y == 0:

        x = x // y

    else:
        y += 1

print(x)