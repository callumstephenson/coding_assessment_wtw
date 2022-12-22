# file containing the comp/non-comp split function for claim data

def data_split(rawData):
    ''' splits the raw data to competitive and non-competitive product lines, and assertains their start and duration
    assumption made that the data is origin year ordered.'''
    data_dict = {}
    
    for each in rawData:
        # check if the key exists and if not then creates an empty list within that key
        if not (each[0] in data_dict.keys()):
            data_dict[each[0]] = []    
        data_dict[each[0]].append(each[1:])

    start_years = []
    year_spans = []
    
    for each in data_dict.keys():
        # sorting the dictionary entries
        data_dict[each].sort(key = lambda x: x[0])
        # find the minimum start year and maximum year span from all of the data provided
        start_year = int(data_dict[each][0][0])
        start_years.append(start_year)
        year_spans.append((1 + int(data_dict[each][-1][0])) - start_year)
    
    return data_dict, min(start_years), max(year_spans)
