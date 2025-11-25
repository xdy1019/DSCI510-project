import os
from config import DATA_DIR, RESULTS_DIR
from load import get_fng_data1, get_fng_data2, get_bitcoin_price_data
import analyze
import visualize

if __name__ == "__main__":
    
    #load data from APIs
    get_fng_data1()
    get_fng_data2()
    get_bitcoin_price_data()
    
    #run analyze.py 
    print("Running analyze.py")
    analyze   

    #run visualize.py
    print("Running visualize.py")
    visualize 

