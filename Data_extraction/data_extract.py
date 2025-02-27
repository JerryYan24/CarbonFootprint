import pandas as pd
import os

def data_extracting(x):
        '''
        takes a file-name and creates new file with required data 

        :input: x : filename=str
        '''
        cwd = os.getcwd()
        columns_to_select=['Heating Energy Source',  "Vehicle Type", "Transport",'Frequency of Traveling by Air', 'Vehicle Monthly Distance Km' ,'CarbonEmission']
       
        
        data=pd.read_csv(x) #reading the required csv file for extraction of data
       

        # ENCODING FREQUENCY COLUMN
        # value_Frequency_of_Traveling_by_Air= data['Frequency of Traveling by Air'].unique().tolist()  
       # dict_of_encoding = {key: value_s.index(key) for key in value_s} #this has less brute-force but it is not in any particular order
        dict_of_encoding={'never':0, 'rarely': 1,'frequently': 2,'very frequently': 3} #brute force but in order
        data['Frequency of Traveling by Air'].replace(dict_of_encoding, inplace=True) # ordinally encoding the column
        



        # ENCODING TRANSPORT COLUMN
        value_transport= data['Transport'].unique().tolist() #values in column
        columns_to_select+=value_transport #adding column names to selection list
        for i in value_transport:
                data[i] = data['Transport'].apply(lambda x: 1 if x == i else 0) #hot-encoding
            
        columns_to_select.remove('Transport') #removing transport column name from the required selectionn list





        # SAVING DATA
        #created df with selected columns
        select= data[columns_to_select]
        file_path = os.path.join(cwd, "Data_extraction/extracted_data.csv")
        select.to_csv(file_path, index=False)


        #uncomment to print the extracted data
        # a=pd.read_csv("extracted_data.csv")
        # print(a)
        

#function call to do the changes 
data_extracting("Data_extraction/CarbonEmission.csv")


