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
[Description]

**./Notebooks/**  
Collection of Jupyter Notebooks for the clustering, linear regression, and recommendation algorithms.
Includes visualizations for data analysis and model performance.

**./Recommendation/**  
[Description]

# How to Run

**Data extraction**  
- Takes the entire dataset and truncate it based on user selection and perform necessary encoding for non-numerical data columns within the truncated dataset to output a .csv file for analysis.
<code>./Data_extraction/Data_extraction_v1.py

**Data analysis**  

- Clustering  
[Description]

- Linear regression  
Generate parameters for the recommendation model by running the <code>./Notebooks/linear_regression.ipynb</code> file.

**Recommendation**  
[Description]

# Modules
- os
- pandas
- numpy
- sklearn
- matplotlib.pyplot
- seaborn
