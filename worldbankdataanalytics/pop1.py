import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import generic_functions as util


print('-- Start --')

print('-- loading population data [API_SP.POP.TOTL_DS2_en_csv_v2.csv] --')
populationDataset =  util.readFileIntoPandasDataframe('..\\dataset\\population\\API_SP.POP.TOTL_DS2_en_csv_v2.csv' );
print(populationDataset.head())


print('-- loading GDP data [API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv] --')
gdpDataset =  util.readFileIntoPandasDataframe('..\\dataset\\gdp\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv' );
print(gdpDataset.head())

print('-- loading country metadata [Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2.csv] --')
countryMetaDataset =  util.readFileIntoPandasDataframe('..\\dataset\\population\\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2.csv' ) \
    .sort_values(by=['Region'])
print(countryMetaDataset.head())



print('-- investigate range of dataset -- ')
print('>>>>   populationDataset.index')
print(populationDataset.index)
print('>>>>   populationDataset.index.size')
print(populationDataset.index.size)
print('>>>>   populationDataset[\'Country Code\']')
print(populationDataset['Country Code'])
print('>>>>   populationDataset.ix[7]')
print(populationDataset.ix[7])

print("\n>>>  distinct values of Country Code , and number of occurence -- \n")
print(populationDataset['Country Code'].value_counts())
print("\n>>>  count of distinct values of Country Code  -- \n")
print(populationDataset['Country Code'].nunique())
print("\n>>>  name of all the column headers   -- \n")
print(populationDataset.columns)

print("\n>>>  pick out India population data from the frame    -- \n")
indiaPopulationData = populationDataset.loc[populationDataset['Country Code'].isin(['IND'])  ]
# selects all rows and all columns beginning at '1962' up to and including '2017'
indiaPopulationData = indiaPopulationData.loc[:, '1962':'2017'].iloc[0].reset_index()
indiaPopulationData.rename(columns={'index': 'year' , 107: 'India-population'}, inplace=True)

print(indiaPopulationData)

# indiaPopulationData.plot(x='year', y='India-population' , kind='line')
# plt.show()

print("\n>>>  pick out Selected Countries population data from the frame    -- \n")
selected_countries = ['IND' , 'PAK' , 'GBR', 'USA' , 'JPN' , 'CHN']
# get rows for selected countries
selectedCountriesPopulationData = populationDataset.loc[populationDataset['Country Code'].isin(selected_countries)  ]
# get column names as list for selected columns, 1962 - 2017 is column names (years)
cols = ['Country Name'] +  list(selectedCountriesPopulationData.loc[:,'1962':'2017'])
# filter out these selectd columns from dataframe
selectedCountriesPopulationData = selectedCountriesPopulationData.loc[: , cols]
distinct_country_names =selectedCountriesPopulationData['Country Name'].values

## the row numbers (index) from original DF is still used as index here
## removes this old index and use 'country name' as index
#        Country Name         1962         1963         1964         1965  \
# 79   United Kingdom   53250000.0   53650000.0   54000000.0   54348050.0
# 107           India  467852537.0  477527970.0  487484535.0  497702365.0
# 182        Pakistan   47119361.0   48309315.0   49551904.0   50845221.0
# 249   United States  186538000.0  189242000.0  191889000.0  194303000.0

selectedCountriesPopulationData = selectedCountriesPopulationData.set_index('Country Name')

## we would need to plot 'column header ' vs row value , hence need these two things in
##  column format (change rows to columns ). Hence transpose the frame
#                        1962         1963         1964         1965  \
# Country Name
# United Kingdom   53250000.0   53650000.0   54000000.0   54348050.0
# India           467852537.0  477527970.0  487484535.0  497702365.0
# Pakistan         47119361.0   48309315.0   49551904.0   50845221.0
# United States   186538000.0  189242000.0  191889000.0  194303000.0
selectedCountriesPopulationData = selectedCountriesPopulationData .T

## after transpose , the year becomes new index , we need this
## as a column , so reset index
# Country Name  United Kingdom         India     Pakistan  United States
# 1962              53250000.0  4.678525e+08   47119361.0    186538000.0
# 1963              53650000.0  4.775280e+08   48309315.0    189242000.0
# 1964              54000000.0  4.874845e+08   49551904.0    191889000.0
# 1965              54348050.0  4.977024e+08   50845221.0    194303000.0
# 1966              54648500.0  5.081619e+08   52191095.0    196560000.0
# 1967              54943600.0  5.188898e+08   53590929.0    198712000.0

selectedCountriesPopulationData = selectedCountriesPopulationData.reset_index()

## rename column name created from index
# Country Name index  United Kingdom         India     Pakistan  United States
# 0             1962      53250000.0  4.678525e+08   47119361.0    186538000.0
# 1             1963      53650000.0  4.775280e+08   48309315.0    189242000.0
# 2             1964      54000000.0  4.874845e+08   49551904.0    191889000.0
# 3             1965      54348050.0  4.977024e+08   50845221.0    194303000.0
# 4             1966      54648500.0  5.081619e+08   52191095.0    196560000.0
#
selectedCountriesPopulationData['year'] = selectedCountriesPopulationData.apply(
    lambda row : int(row['index']) ,
    axis=1
)

# selectedCountriesPopulationData.rename(columns={'index': 'year' }, inplace=True)
print(selectedCountriesPopulationData)

# year is of the type int64
#print(selectedCountriesPopulationData['year'][18].dtype)

# plot the year vs the country population
# country name is column header , we are giving a list of different country names as y
# so different plots for different country
ax = selectedCountriesPopulationData.plot(x='year', y=distinct_country_names , kind='line' , title='Population over years' )
plt.savefig('..\\dump\\populationgraph.png')
plt.close()



print('>>>  combining multiple data frames')
### set country code as index for all data frames since its
## common and unique key


populationDataset.set_index('Country Code' , inplace=True)
gdpDataset = gdpDataset .set_index('Country Code' , inplace=True)
countryMetaDataset = countryMetaDataset  .loc[:, ["Country Code","Region","IncomeGroup"]] .set_index('Country Code' )


print(populationDataset)


print('-- End --')


