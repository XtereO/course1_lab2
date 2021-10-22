

import csv
from api import (
                 csv_to_list,
                 collect_all_props,
                 require_params
                )

def main():
    
    
    # CONSTS
    FILE_NAME = 'anime.csv'
    
    
    # Read file
    anime_list = csv_to_list(FILE_NAME)


    # Program body
    tags = require_params(lambda: collect_all_props(anime_list,'Tags'), {title:'жанры'})
    

    # Generate answers


    # Output
    
   
main()
