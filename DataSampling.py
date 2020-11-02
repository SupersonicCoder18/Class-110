import pandas as pd
import plotly.figure_factory as ff
import statistics
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("Temp.csv")
Temp = df["temp"].to_list()

TempMean = statistics.mean(Temp)
TempMedian = statistics.median(Temp)
TempMode = statistics.mode(Temp)
TempStdev = statistics.stdev(Temp)

print("Mean, Median, Mode and Standard Deviation of the Temperature are {}, {}, {}, {} respectively".format(TempMean, TempMedian, TempMode, TempStdev))
fig = ff.create_distplot([Temp], ["Temperature"], show_hist = False)
fig.show()

#DataSet = []

#for i in range(0, 100):
#    randomIndex = random.randint(0, len(Temp))
#    value = Temp[randomIndex]
#    DataSet.append(value)

#mean = statistics.mean(DataSet)
#std = statistics.stdev(DataSet)

#print("Mean and Standard Deviation of Sample Data is {} and {} respectively".format(mean, std))

def RandomSetOfMean(counter):
    DataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(Temp) - 1)
        value = Temp[randomIndex]
        DataSet.append(value)
    mean = statistics.mean(DataSet)
    return mean

def ShowFig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["Temp"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "mean"))
    fig.show()

def Setup():
    mean_list = []
    for i in range(0, 1000):
        setOfMeans = RandomSetOfMean(100)
        mean_list.append(setOfMeans)
    ShowFig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of the sampling distribution is ", mean)

Setup()

def StDev():
    mean_list = []
    for i in range(0, 1000):
        setOfMeans = RandomSetOfMean(100)
        mean_list.append(setOfMeans)
    std = statistics.stdev(mean_list)
    print("Std of sampling distribution is ", std)
StDev()