# WTW Assessment RUNME document

## Running Instructions
Put the input file in the wtw_assessment directory, then input the name of your text file (**without .txt**) 
within the file_name variable in the main.py and run the main method. The output of the program will be saved as 
your_filename_output.txt within the same folder as the main method. Expect that each of the triangle objects will
be printed on the terminal in the format outlined in the __repr__ function of that class.

## Program feature explanation

### Triangle Class
The triangle class provides a platform to manipulate and store the data from the input file. It contains a 2D array of rows
which contains a list of each row, decreasing by one as it moves down the table. The class also contains a function that
is able to restructure the data contained within into the output format, suitably named 'output_format'. The repr function
is designed to print out the data contained within in a legible format for the user to see. 

The accumulate method within the triangle class allows for the conversion of the data held from incremental form to accumulative format. 
The add point and add raw data methods are separate incase amendments are required in which single datapoints may need to be added. 
Raw data can be added upon initialisation of later depending on requirements, but it is added when the object is initialised in this
demonstrative program.

### File Reader
The file reader (files.py) is a simple python file reading class containing two functions that manipulate the input and
output of data from the program. From the input, the title line is removed and the lines are broken into a 2D array. 
The required format of the output data is reformed upon writing to the output text file.

### Data Split
The data splitting file (data_split.py) splits the imported data into keys within a dictionary containing each respective
product on the input file. This means that the program is built to handle many products, and it also ascertains the maximum
span and minimum start year in order to make all of the output arrays a consistent length of triangle data structure as required
by the instructions given. The dictionary is also sorted by a lambda function according to the start year for later processing.

It is also able to allow for messy data and years with zero claims, as the latter is demonstrated by the example file.

### Main
The main method has a space to change the input variable name (file_name), and has simple loops calling the other functions
and classes from their respective files. The data is imported, then processed, then added to the output file.
