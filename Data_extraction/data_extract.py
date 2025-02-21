import pandas as pd
import os
def data_extracting(x):
        '''
        takes a file-name and creates new file with required data 

        :input: x : filename=str
        '''
        cwd = os.getcwd()

        #reading the required csv file for extraction of data
        data=pd.read_csv(x)
        print(data)

        #created df with selected columns
        select= data[['Heating Energy Source',  "Vehicle Type", "Transport",'Frequency of Traveling by Air', 'CarbonEmission']]

        #saves data extracted in a csv file named extracted_data
        file_path = os.path.join(cwd, "Data_extraction/extracted_data.csv")
        select.to_csv(file_path, index=False)


        #uncomment to print the extracted data
        # a=pd.read_csv("extracted_data.csv")
        # print(a)
        

#function call to do the changes 
data_extracting("Data_extraction/CarbonEmission.csv")


