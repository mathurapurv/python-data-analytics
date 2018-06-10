import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import generic_functions as util
import time

def createPopulationStatsForSelectedCountries(selectedCountriesList='IND,USA' , responseFormat='JSONSTR' , ) :
    print('-- [createPopulationStatsForSelectedCountries] Start --')

    selected_countries  =  selectedCountriesList.split(",")
    print('-- selected_countries --')
    print(selected_countries)

    print('-- loading population data [API_SP.POP.TOTL_DS2_en_csv_v2.csv] --')
    populationDataset = util.readFileIntoPandasDataframe('..\\dataset\\population\\API_SP.POP.TOTL_DS2_en_csv_v2.csv');
    print(populationDataset.head())

    print('-- loading GDP data [API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv] --')
    gdpDataset = util.readFileIntoPandasDataframe('..\\dataset\\gdp\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv');
    print(gdpDataset.head())



    print("\n>>>  pick out Selected Countries population data from the frame    -- \n")

    # get rows for selected countries
    selectedCountriesPopulationData = populationDataset.loc[populationDataset['Country Code'].isin(selected_countries)]
    # get column names as list for selected columns, 1962 - 2017 is column names (years)
    cols = ['Country Name'] + list(selectedCountriesPopulationData.loc[:, '1962':'2017'])
    # filter out these selectd columns from dataframe
    selectedCountriesPopulationData = selectedCountriesPopulationData.loc[:, cols]
    distinct_country_names = selectedCountriesPopulationData['Country Name'].values

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
    selectedCountriesPopulationData = selectedCountriesPopulationData.T

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
        lambda row: int(row['index']),
        axis=1
    )

    if(responseFormat == 'JSONSTR'):
        print('-- [createPopulationStatsForSelectedCountries] End --')
        return selectedCountriesPopulationData.to_json(orient='split')
    else :
        # plot the year vs the country population
        # country name is column header , we are giving a list of different country names as y
        # so different plots for different country
        ax = selectedCountriesPopulationData.plot(x='year', y=distinct_country_names, kind='line',
                                                  title='Population over years')
        fileName = '..\\dump\\populationgraph' + selectedCountriesList +  ' -'+ str(time.time())+'.png'
        plt.savefig(fileName , format='png')
        plt.close()
        print('-- [createPopulationStatsForSelectedCountries] End --')
        return fileName

