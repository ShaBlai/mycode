#!/usr/bin/python3


import pandas as pd

# these following two lines are for writing to file
# use this when you are not rendering to a windowimport matplotlib
import matplotlib
matplotlib.use('Agg')

#for creating the graphs
import matplotlib.pyplot as plt

def main ():
    
    #get the excel file
    excel_file2 = 'movies2.xls'
    
    
    #create the dataframe object 
    #and pass the excel file into panda
    movies_list = pd.read_excel(excel_file2)
    
    #show the last movies in the list
    print(movies_list.tail(10))
    
    
    #take the top IMDB Score 
    sorted_by_rating = movies_list.sort_values(["IMDB Score"], ascending=False)   
    print(sorted_by_rating.head(10))
    
    #created a bar graph
    sorted_by_rating["IMDB Score"].head(5).plot(kind="barh")
    #save the figure for the top movies
    plt.savefig("/home/student/static/top10IMDB.png", bbox_inches='tight') 
     
    
    #wireframe writeout those bottom in the list
    movies_list.to_json("bottom-5-movies-to-json.json")
     
    
if __name__=="__main__":
    main()    
    
    
    
    