#########################################################################
#Title: Python project 
#Description: This program displays the top three countries in SEA region that visited Singapore from 1988 to 1998
#Name: Edwin Ngow Sheng Xiang
#Group Name: Visitor Information
#Class:PN2004Y
#Date: 20 July 2021
#Version: V1.0
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import matplotlib for piechart
import matplotlib.pyplot as plt
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthlyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  #print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  #Replacing the Value of na to 0
  df = df.replace(to_replace =[" na ", "na"],value ="0")

  #Countries that are in S.E.A region
  SEA= df.columns[2] + "," + df.columns[3] + ","+ df.columns[4] + "," + df.columns[5] + "," + df.columns[6] + "," + df.columns[7] + ","+ df.columns[8]
  print(SEA+ "were selected")

  #print("checkpoint")
  #SouthEastAsia = df.columns[2] + df.columns[3] + df.columns[4] + df.columns
  #[5] + df.columns[6] + df.columns[7] + df.columns[8]
  #df.columns

  #Sorting my rows and columns
  print("\nThe following data for SEA region from 1988 to 1998 are shown below : \n")

  SortedSEA = (df[['Year', 'Month', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ']][120:252])
  print(SortedSEA)

  #remove year & month
  NewSEA = SortedSEA.drop(columns=["Year", "Month"])

  #convert to int
  NewSEA = NewSEA.astype(str).astype(int)
  #print(NewSEA.columns)
  
  #Total sum
  TotalSEA=NewSEA.sum()

  #Sort in order
  SortednewSEA = TotalSEA.sort_values(ascending=False)

  #back to object
  SortednewSEA = SortednewSEA.reset_index()

  #adding columns
  SortednewSEA.columns = ['Countries', 'Visitor']

  #Display of all the countries
  print("\nThe numbers visitor from the SEA region are as follow:\n")
  #topthree = (SortednewSEA.head())
  print(SortednewSEA)

  #piechart
  visitorss = [3164529, 1902547, 646889]
  Countries = ['Indonesia','Malaysia','Thailand']
  plt.pie(visitorss,labels= Countries,autopct='%1.1f%%')
  plt.title('Insert Title')
  plt.axis('equal')
  plt.legend(loc="lower right")
  plt.show()
  

  
  #display a specific country (Australia) in column #33
  #country_label = df.columns[33]
  #print("\n\n" + country_label + "was selected.")

  #display a sorted dataframe based on selected country
  #print(" The" + country_label + "was sorted in ascending order. \n")
  #sorted_df =df.sort_values(country_label,ascending=[0])
  #print(sorted_df)

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()



            



        



 
#########################################################################
#End of Code#
#########################################################################