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
        data = encode_extracted_data(data) 

        # ENCODING FREQUENCY COLUMN
        # value_Frequency_of_Traveling_by_Air= data['Frequency of Traveling by Air'].unique().tolist()  
       # dict_of_encoding = {key: value_s.index(key) for key in value_s} #this has less brute-force but it is not in any particular order
        dict_of_encoding={'never':0, 'rarely': 1,'frequently': 2,'very frequently': 3} #brute force but in order
        data['Frequency of Traveling by Air'].replace(dict_of_encoding, inplace=True) # ordinally encoding the column
        




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

#---------------------------------------------------------------------------------------

# Function to further encode the columns:
def encode_extracted_data(df):
    """
    This function takes an input CSV file, performs one-hot encoding on the 
    'Heating Energy Source' and 'Vehicle Type' columns, and returns the path to the 
    newly saved encoded CSV file.
    
    Parameters:
    input_csv (str): Path to the input CSV file.
    
    Returns:
    str: Path to the output encoded CSV file.
    """
    import pandas as pd
    
    # Load the CSV file
    #df = pd.read_csv(input_csv)

    # Perform one-hot encoding on the specified columns
    df_encoded = pd.get_dummies(df, columns=["Heating Energy Source", "Vehicle Type","Transport"], prefix='', prefix_sep='')

    return df_encoded


