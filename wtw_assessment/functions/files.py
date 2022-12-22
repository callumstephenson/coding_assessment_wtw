# file containing function to open and import input files into the program

def file_reader(file_name):
    '''A function that accepts argument file_name in the form
    'Name.txt' and imports the contents of the file into a 2d list'''
    file_name += '.txt'
    with open(file_name) as infile:
        lines = (infile.readlines())[1:]
        output = []
        for line in lines:
            output.append(line.replace(' ','').replace('\n','').split(','))
    return output

def file_writer(file_name, accumulated_data, start_year, year_span):
    '''A function that accepts the output triangles and
    returns them in the form of Name_output.txt'''
    file_name += '_output.txt'
    with open(file_name, 'w+') as outfile:
        data_out = [str(start_year) + ", " , str(year_span) + '\n']
        for each in accumulated_data:
            data_out.append(each.output_format())
        outfile.writelines(data_out)
