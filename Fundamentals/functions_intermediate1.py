import random
def randInt(min=0,max=100):
    if (min>max) :
        max=min+max
        min=max-min
        max=max-min
    num = (random.random()*(max-min)+min)
    return round(num)
#print(randInt()) 		            # should print a random integer between 0 to 100
#print(randInt(max=50)) 	        # should print a random integer between 0 to 50
#print(randInt(min=50)) 	        # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
#print(randInt(max=-20))            # should print a random integer between -20 and 0
#print(randInt(min=-20,max=-30))    # should print a random integer between -30 and -20