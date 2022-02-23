import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df= pd.read_csv("data.csv")
data=df['reading_time'].tolist()

population_mean=statistics.mean(data)
stdev=statistics.stdev(data)
print('mean of the population data is:',population_mean)
print('standard deviation of the population data is:', stdev)

def random_set_of_mean(counter):   
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    print('mean of sampling distribution is-', mean)
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.show()
    
def standard_deviation():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    st_deviation=statistics.stdev(mean_list)
    print('standard deviation of the sampling distribution is-', st_deviation)

def setUp():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setUp()
standard_deviation()


