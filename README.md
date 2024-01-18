## TIME SERIES MODELING FOR ZILLOW REAL ESTATE PRICES.
![Alt text](https://www.bis.org/img/featureimg/pp_residential_2111.jpg)

## Problem Statement
To develop a time series model that can be used to predict and help determine the top five zip codes in which to invest.

## Project Overview
The dataset encompasses details on a range of attributes, including RegionID, RegionName, City, State, Metro, SizeRank, CountyName, and the value representing real estate prices. This dataset, known as the Zillow Housing Dataset, has been obtained from the Zillow Research Page.

## Business Understanding
Real estate investment stands as a profitable and ever-evolving industry, demanding meticulous analysis and strategic decision-making. A fictitious real estate investment firm is currently in search of insights to pinpoint the top five zip codes offering promising investment opportunities. To tackle this inquiry, we leverage historical data sourced from Zillow Research.

## Components

* **Jupyter Notebook**
The [Jupyter Notebook](https://github.com/Kelvin-Rotich824/Phase_4_Project_Time_Series_Analysis/blob/master/Phase 4 Project Notebook.ipynb) is our key deliverable and contains details of our approach and methodology, data cleaning, exploratory data analysis and model building and validation.

I recommend using [nbviewer](https://nbviewer.jupyter.org/) to view the Jupyter Notebook.

* **Presentation**
The [presentation](https://) gives a high-level overview of our approach, findings and recommendations for non-technical stakeholders. It is aimed to be between 5 and 10 minutes long.

* **Data**

The dataset can be found in the file *"zillow_data.csv"* in the Data folder, in this repository. It was originally provided in the following [repository](https://github.com/Kelvin-Rotich824/Phase_4_Project_Time_Series_Analysis/blob/master/Phase 4 Project Notebook.ipynb.

## Technologies/ Packages

* Python version: 3.11.9
* Matplotlib version: 3.1.3
* Seaborn version: 0.9.0
* Pandas version: 0.25.1
* Numpy version: 1.16.5
* Statsmodels version: 0.10.1
* Scikit-learn version: 0.21.2 
* TensorFlow version: v2.15.0

## To get started

1. Clone this repository - [guidance](https://help.github.com/articles/cloning-a-repository/).
2. Dataset can be found in the file "zillow_data.csv".
3. Check requirements in Technologies section above and download libraries if necessary.

## 1. Data Wrangling
Here we will work on data cleaning, handling missing values, data transformation, handling duplicates, data reshaping and other processes to ensure that we have a clean, structured, and suitable format for analysis and modeling

## 2. Exploratory Data Analysis (EDA)
Here we will explore the different features of the dataset to gain a better understanding of the data. We will use data vizualization to uncover trends and patterns. We will use Feature Engineering to create new features from existing ones and perform One-Hot Encoding on categorical variables that we will require for analysis.

### 2.1 Univariate Analysis
![Alt text](image.png)
From the histogram above we can conclude that the distribution is positively skewed meaning a majority of the observations have lower ROI values, while a smaller number of observations have higher ROI values, leading to a rightward tail in the distribution.

### 2.3 Bivariate Analysis
From the bar graph we can conclude the Region with  Zip code 11211 located in New York State had the highest Return on Investment.
![Alt text](image-1.png)

The graph below shows the relationship between the Return on Investment and the Different cities provided. We can therefore conclude that New York City has the highest Return on Investment followed by Jersey  City, Wainscott, Amagansett, Hartsel, Los Angeles and  Washington with lowest Return on Investment.
![Alt text](image-2.png)

## 3. Modeling


## 4. Evaluation

## 5. Conclusion


## Contributors:
|Name     |  GitHub   |
|---------|-----------------|
|Kelvin Rotich |https://github.com/Kelvin-Rotich824|
|Crystal Wanjiru |https://github.com/CrystalW123|
|Miriam Nguru |https://github.com/|
|Celiajoy Omiah |https://github.com/celiahjoyomiah|
|Paul Mbugua |https://github.com/Paulwaweru|
|Stephen Butiya |https://github.com/obystephen|
