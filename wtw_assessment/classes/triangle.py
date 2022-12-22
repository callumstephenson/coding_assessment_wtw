# file containing the class responsible for creation of tables within accumulate.py

class triangle():
    '''triangle class containing the data in rows and columns for clarity rather than usage of basic 2d arrays
    input args:
    bool isComp, (determines if the data if for the competitive or noncompetitive product)'''
    def __init__(self, title, year_span, start_year, raw_data = False):
        # initialise class
        self.title = title
        self.year_span = year_span
        self.start_year = start_year
        self.rows = []
        
        for i in range(self.year_span):
            self.rows.append([0] * (self.year_span - i))
        
        if raw_data:
            self.add_raw_data(raw_data)
    
    def __repr__(self):
        '''Self print statement for the stream object'''
        d = "Product Type:      {}\n".format(self.title)
        d += "Origin year:     {}\n".format(self.start_year)
        d += "Year span:      {}\n".format(self.year_span)
        for each in self.rows:
            d += "{}\n".format(each)
        return d
    
    def add_data_point(self, origin_year, development_year, value):
        '''adds a datapoint to the triangle in a non-cumulative manner'''
        row_index = origin_year - self.start_year
        col_index = development_year - origin_year
        self.rows[row_index][col_index] = value
        
    def add_raw_data(self, raw_data):
        '''adds full sets of raw data to the triangle'''
        for each in raw_data:
            self.add_data_point(int(each[0]), int(each[1]), float(each[2]))
            
    def accumulate(self):
        '''converts the triangle to accumulative format rather than non-cumulative'''
        for each in self.rows:
            for i in range(len(each)):
                if i == 0:
                    continue
                else:
                    each[i] = each[i-1] + each[i]
    def output_format(self):
        '''convert the triangle data into the lit format as required by the example output data'''
        output = self.title + ', '
        output += str([i[j] for i in self.rows for j in range(len(i))]).replace('[','').replace(']','') # list generator for output processing, removing from array to 1D list
        output += '\n'
        return output
