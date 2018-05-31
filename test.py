print ("Hello world")
# user input
time = input("what time do you want to wake up? please enter an integer from 0 ~ 23\n")

for x in range(0, time):
	print "the remaining time is " + str(x)
print "It's now " + str(time) + " time is up, please wake up\n"