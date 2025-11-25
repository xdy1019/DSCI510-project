# Project description
The scope of the project is to analyze the correlations among Fear and Greed Index, Bitcoin Price, and the S&P Cryptocurrency Broad Digital Asset (BDA) Index. In particular, The Fear and Greed Index measures crypto market sentiment. The BDA Index is the cryptocurrency market benchmark index. This index is designed to track the performance of a wide range of investable digital assets that meet specific liquidity and market capitalization criteria. 

# Data sources
For the timeframe, I chose the historical data timeframe to be from 05/02/2024 to 11/06/2025. The number of rows is 554, which corresponds to 554 days, around one and a half years. 
All three datasets are within this timeframe. 
The Fear and Greed Index and the Bitcoin Price historical data are both obtained through calling API. The BDA Index is obtained from the S&P Global website. 

I also added the `datasets/` folder in this project. The `datasets/` folder contains the finalized versions of the data files of fng index, bitcoin price, and bda index within that timeframe. When you call the APIs now, the timeframe will shift, and consider the fact that the bda index data file is directly downloaded from S&P Global website, I think it's necessary to create the datasets folder in order to run the other files. To run the other files, you need to have the `datasets/` folder in the repository. 

# Results 
_describe your findings_

# Installation
The Fear and Greed Index and the Bitcoin Price historical data are both obtained through writing Python code and calling API. The BDA Index is obtained from the S&P Global website.

For the API, I use the coinmarketcap API.

https://coinmarketcap.com/api/documentation/v1/ 

The above link contains the instruction on setting up your API key in order to call the APIs. 

# Running analysis 
_update these instructions_


From `src/` directory run:

`python main.py`

Results will appear in `results/` folder. All obtained data files will be stored in `data/`

  
