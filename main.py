# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:11:19 2023

@author: Santiago
"""
from reader import read_csv
from charter import generate_bar_chart
from utils import get_country
from utils import population_country_dict


def run():
    
    country = 'Colombia'
    data = read_csv('data.csv')
    
    country_list = get_country(data, country)
    print(country_list)
    labels, values = population_country_dict(country_list)
    int_values = [int(val) for val in values]
    print(labels, values)
    if len(country_list) > 0:
        
        country = 'Colombia'
        print(country)
        generate_bar_chart(labels, int_values)

if __name__ == '__main__':
    run()
      