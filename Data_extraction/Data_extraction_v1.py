import pandas as pd
import os

def truncate_df(df: pd.DataFrame, columns:list):
    '''
    This function extracts the specified colums from given df
    '''
    assert isinstance(df, pd.DataFrame), "Input df must be a pandas DataFrame"
    assert isinstance(columns, list), "columns must be a list"
    valid_columns = []
    
    for col in columns:
        if col in df.columns:
            valid_columns.append(col)

    new_df = df[valid_columns]
    
    return new_df


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def encode_extracted_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs one-hot encoding on specified columns while preserving the original column order.
    
    Parameters:
    df (pd.DataFrame): The input dataframe.
    
    Returns:
    pd.DataFrame: The one-hot encoded dataframe with the original column structure preserved.
    """  
    assert isinstance(df, pd.DataFrame), "Input df must be a pandas DataFrame"
    # Columns to be one-hot encoded
    columns_to_encode = ["Heating Energy Source", "Vehicle Type", "Transport", "Waste Bag Size"]
    
    # Dictionary to store one-hot encoded columns
    encoded_dfs = {}
    
    # Perform one-hot encoding for each specified column individually
    for col in columns_to_encode:
        if col in df.columns:
            encoded_dfs[col] = pd.get_dummies(df[col], prefix='', prefix_sep='').astype(int)

    # Reconstruct the dataframe with the original order
    final_columns = []
    final_df = pd.DataFrame(index=df.index)  # Preserve original index

    for col in df.columns:
        if col in encoded_dfs:
            # Insert one-hot encoded columns in place of original column
            encoded_cols = encoded_dfs[col].columns
            final_df[encoded_cols] = encoded_dfs[col]
            final_columns.extend(encoded_cols)
        else:
            # Retain non-encoded columns in their original positions
            final_df[col] = df[col]
            final_columns.append(col)

    # Ensure final column order matches original structure with inserted encodings
    return final_df[final_columns]

#---------------------------------------------------------------------------------

def map_travel_frequency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps the 'Frequency of Traveling by Air' column to numerical values.
    
    Parameters:
    df (pd.DataFrame): The input dataframe.
    
    Returns:
    pd.DataFrame: The dataframe with the mapped 'Frequency of Traveling by Air' column.
    """
    assert isinstance(df, pd.DataFrame), "Input df must be a pandas DataFrame"
    mapping = {
        "never": 0,
        "rarely": 1,
        "frequently": 2,
        "very frequently": 3
    }
    if "Frequency of Traveling by Air" in df.columns:
        df["Frequency of Traveling by Air"] = df["Frequency of Traveling by Air"].map(mapping).fillna(df["Frequency of Traveling by Air"])
    return df

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def process_and_save(csv_file: str):
    """
    Reads a dataset from a CSV file, processes it, and saves the final dataframe to a specified GitHub repository directory.
    
    Parameters:
    csv_file (str): The path to the input CSV file.
    github_repo_path (str): The local path to the GitHub repository directory.
    extracted_columns (list): List of columns to extract from the dataframe.
    output_filename (str): Name of the output CSV file to be saved.
    """
    assert isinstance(csv_file, str), "csv_file must be a string"
    assert os.path.exists(csv_file), f"File {csv_file} does not exist"
    cwd = os.getcwd()
    
    # Read the dataset
    df = pd.read_csv(csv_file)

    extracted_columns = ['Heating Energy Source', 'Cooking_with', 'Transport', 'Vehicle Type','Vehicle Monthly Distance Km', 'Frequency of Traveling by Air', 'Waste Bag Size', 'Waste Bag Weekly Count','CarbonEmission']
    
    # Extract specified columns
    new_df = truncate_df(df, extracted_columns)
    
    # Map travel frequency column
    new_df = map_travel_frequency(new_df)
    
    # Perform one-hot encoding
    final_df = encode_extracted_data(new_df)

    # Rename Waste Bag Size encoded columns
    waste_bag_prefix = "Waste Bag Size"
    final_df.rename(columns={col: f"{col} waste bag" for col in final_df.columns if waste_bag_prefix in extracted_columns and col in new_df[waste_bag_prefix].unique()}, inplace=True)
    
    # Save the processed dataframe to CSV in the GitHub repo directory
    file_path = os.path.join(cwd, "Data_extraction/extracted_data_v1.csv")
    final_df.to_csv(file_path, index=False)

    print(f"Processed file saved at: {file_path}")




# -------------------------------------------------------------------------------------

#Example usage: 
process_and_save("Data_extraction/CarbonEmission.csv")
