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
       

        
        #    has less brute-force but it is not in any particular order
        # value_s= data['Frequency of Traveling by Air'].unique().tolist()

        dict_of_encoding={'never':0, 'rarely': 1,'frequently': 2,'very frequently': 3}
        #                           or
        # dict_of_encoding = {key: value_s.index(key) for key in value_s}
        
        
        #ordinal encoding for 'Frequency of Traveling by Air' column -------if we want rarely to be 0 and so on 
        data['Frequency of Traveling by Air'].replace(dict_of_encoding, inplace=True) # ordinally encoding the column



        #saves data extracted in a csv file named extracted_data
        #created df with selected columns
        select= data[['Heating Energy Source',  "Vehicle Type", "Transport",'Frequency of Traveling by Air', 'Vehicle Monthly Distance Km' ,'CarbonEmission',]]
        file_path = os.path.join(cwd, "Data_extraction/extracted_data.csv")
        select.to_csv(file_path, index=False)


        #uncomment to print the extracted data
        # a=pd.read_csv("extracted_data.csv")
        # print(a)
        

#function call to do the changes 
data_extracting("Data_extraction/CarbonEmission.csv")


