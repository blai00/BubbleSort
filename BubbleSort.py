import random
my_array = random.sample(xrange(1,10001),100)
def bubblesort(num = []):
	for count in range(len(num)-1,0,-1):
		for i in range(count):
			if(num[i+1] < num[i]):
				temp = num[i]
				num[i] = num[i+1]
				num [i+1] = temp




bubblesort(my_array)
print my_array
