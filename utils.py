import re
from reader import read_csv
def get_country(data, country):
      ##filtrar pais 
      country_list = list(filter(lambda i : i['Country/Territory']==country, data))  
      return country_list
    
def population_country_dict(country_list):
            
        # find keys and values in list then create a dict, using regular expresions
    pattern = re.findall(r"'([0-9]+\s[Population]+)' *: *'([^']+)'",
                         str(country_list)) #key words groupend in touples with reexp
    population_dictionary = {k:v for k,v in pattern} 
    labels = population_dictionary.keys() 
    values = population_dictionary.values()
    
    return labels, values

if __name__ == '__main__':
    data = read_csv('data.csv')