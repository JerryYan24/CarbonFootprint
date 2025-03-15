# Introduction  
This project focuses on analyzing a dataset containing lifestyle activity data. The goal is to quantify the impact of different activities on carbon emissions and provide data-driven conclusions that can guide sustainable decision-making at both individual and community levels.

# File Structure
```
CarbonFootprint/
├── Data_extraction/
├── Notebooks/
├── Recommendation/
├── presentation_slides.pdf
└── merged_notebook.ipynb
```

**./Data_extraction/**  
This part of codebase focuses on the data extraction form the a main dataset and transforms the selected data into binary/numerical values for further analysis. 

**./Notebooks/**  
Collection of Jupyter Notebooks for the clustering, linear regression, and recommendation algorithms.
Includes visualizations for data analysis and model performance.

**./Recommendation/**  
Provides a user with actionable recommendations that would reduce their carbon emissions by a predetermined % - Utilizes the extracted parmeters from the linear regression run. 
Adopts a Targeted Top Contributor approach - Instead of tweaking all of the chosen 5 analysis features, it targets the top 2 carbon emission contributing features for the user.
Includes the before and post recommendation Carbon Emissions visualization relative to the mean and median of the entire dataset.


# How to Run

**Data extraction**  
- Takes the entire dataset and truncate it based on user selection and perform necessary encoding for non-numerical data columns within the truncated dataset to output a .csv file for analysis.
<code>./Data_extraction/Data_extraction_v1.py</code> 

**Data analysis**  

- Clustering  
[Description]

- Linear regression  
Generate parameters for the recommendation model by running the <code>./Notebooks/linear_regression.ipynb</code> file.

**Recommendation**  
- Suggest the new individual choices for the chosen user by applying practical constraints to the Recommendation model whilst maintaining logical consistency.
- Visualize the impact of the recommendations on the individual's Carbon Emissions relative to the mean/median of the dataset.
- Run : <code>./Notebooks/Before_After_Standing.ipynb</code> file 

# Modules
- os
- pandas
- numpy
- sklearn
- matplotlib.pyplot
- seaborn
