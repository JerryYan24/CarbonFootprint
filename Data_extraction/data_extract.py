import pandas as pd
import os



def list_to_columns(data1, column_name):
    # Make a copy of the DataFrame to avoid modifying the original DataFrame directly
    data1 = data1.copy()

    # Convert string representation of lists into actual lists (safely)
    data1[column_name] = data1[column_name].apply(lambda s: eval(s) if isinstance(s, str) and s != '[]' else [])

    # Create a set of unique items from all lists in the column
    unique_items = set(item for sublist in data1[column_name] for item in sublist)

    # Create a new column for each unique item, initializing with 0
    for item in unique_items:
        data1[item] = data1[column_name].apply(lambda x: 1 if item in x else 0)
    
    data1.drop(columns=[column_name], inplace=True)
    return data1



# list_to_columns("Data_extraction/CarbonEmission.csv","Cooking_With")


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
    # Perform one-hot encoding on the specified columns
    df_encoded = pd.get_dummies(df, columns=["Heating Energy Source", "Vehicle Type","Transport", "Waste Bag Size" ], prefix='', prefix_sep='')
    df_encoded.replace({True: 1, False: 0}, inplace=True)
    return df_encoded



def data_extracting(x):
        '''
        takes a file-name and creates new file with required data 

        :input: x : filename=str
        '''
        cwd = os.getcwd()

        columns_to_select=['Frequency of Traveling by Air', "Heating Energy Source", "Vehicle Type","Transport", 'Vehicle Monthly Distance Km', "Cooking_With","Waste Bag Size","Waste Bag Weekly Count" , 'CarbonEmission']

       
        
        data=pd.read_csv(x) #reading the required csv file for extraction of data
       
        

        # ENCODING FREQUENCY COLUMN
        # value_Frequency_of_Traveling_by_Air= data['Frequency of Traveling by Air'].unique().tolist()  
        # dict_of_encoding = {key: value_s.index(key) for key in value_s} #this has less brute-force but it is not in any particular order
        dict_of_encoding={'never':0, 'rarely': 1,'frequently': 2,'very frequently': 3} #brute force but in order
        data['Frequency of Traveling by Air'].replace(dict_of_encoding, inplace=True) # ordinally encoding the column
       

        #ONE-HOT-ENCODING
        new_df=data[columns_to_select]
        separated_df=list_to_columns(new_df, 'Cooking_With')
        final_df= encode_extracted_data(separated_df)
        
        

        # SAVING DATA
        file_path = os.path.join(cwd, "Data_extraction/extracted_data.csv")
        final_df.to_csv(file_path, index=False)



#function call to do the changes 
data_extracting("Data_extraction/CarbonEmission.csv")

