#*******************************#
#Title: An example of Pickling
#Dev: CBenner
#Date: Dec 6th, 2018
#ChangeLog: (Who, When, What)
#None Yet
#*******************************#

##Pickling a File#

import pickle

CatName_dict = {'Felix': 10, 'Pilaf': 12, 'Simpkin': 34, 'Rascal': 16}

filename = 'CatIndex' #This line of code specifies the name of the file that we will write to#
outfile = open(filename, 'wb') #This line of code specifies that the file should be opened for writing#
    #The 'w' above specifies that we will be writing to the file, and the 'b' indicates that it will be written in binary format
    #in the form of bytes

pickle.dump(CatName_dict,outfile) #this command takes two arguements, the first being the object (the dictionary) that we wish to pickle, and
#the file to which the object has to be saved.#
outfile.close() #This line of code closes the file#

print(CatName_dict)


##The above block of code will create a new file named CatIndex, appearing in the same directory as our python script##

##Unpickling the file##

infile = open(filename, 'rb') ##in this line of code the 'r' designates
# that we will be reading a file, and the 'b' signifies binary mode##

new_dict = pickle.load(infile) ##What this line of code is doing is creating
#  a new dictionary from the pickled 'Cat Index' file (containing the CatName_dict Data).
infile.close()

##Verifying that the data was succesfully unpickled##
print(new_dict)
print(new_dict==CatName_dict)
print(type(new_dict))#This line of code verifies that the
# pickled data has been correctly imported as 'dictionary' in python#


