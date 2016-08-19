import sys
import random
#import numpy as np
if sys.version_info < (3, 0):
    # Python 2
    from Tkinter import *
else:
    # Python 3
    from tkinter import *


def Call():
	try:
		number_signed_up = int(number_signed_up_field.get())
		capacity = int(capacity_field.get())
		if number_signed_up > capacity:
                	#rand_number_list = np.add(1,np.arange(number_signed_up))
                	#np.random.shuffle(rand_number_list)
                	#rand_number_list = np.sort(rand_number_list[:capacity])
                	rand_number_list = sorted(random.sample(range(number_signed_up), capacity))
			lab= Label(root, text = str(rand_number_list))
        	else:
                	lab= Label(root, text = "There are enough spots for everyone")

	except:
		lab= Label(root, text = "Please enter two integers")
	
	lab.pack()
        button['bg'] = 'blue'
        button['fg'] = 'white'

root = Tk()
root.title("RandomNumberGenerator")
root.geometry('700x300+950+170')

number_signed_up_label = Label(root, text= "Number Signed Up")
capacity_label = Label(root, text = "Capacity")

number_signed_up_field = Entry(root, text= "Number Signed Up", bg = 'white')
capacity_field = Entry(root, text = "Capacity", bg = 'white')


button = Button(root, text = "Generate", command = Call)

number_signed_up_label.pack(anchor = N)
number_signed_up_field.pack(anchor = N)
capacity_label.pack(anchor = N)
capacity_field.pack(anchor = N)

#number_signed_up_field.insert(0, "Number Signed Up")
#capacity_field.insert(0, "Capacity")

button.pack(anchor = N)




root.mainloop()
