from functions.files import * 
from functions.data_split import *
from classes.triangle import *

def run():
    '''Add your filename as string in the variable called file_name'''
    file_name = 'input'
    raw_data = file_reader(file_name)
    data_dict, start_year, year_span = data_split(raw_data)
    
    accumulated_data = []
    for key in data_dict.keys():
        accumulated_data.append(triangle(key, year_span,start_year,data_dict[key]))
    
    # print out each of the inputs
    for each in accumulated_data:
        print(each)
    # return the file as file_name_output to the same folder as the main py file
    file_writer(file_name, accumulated_data, start_year, year_span)
    
    return None

if __name__ == "__main__":
    run()
    
