import os
from config import DATA_DIR, RESULTS_DIR
from load import get_fng_data1, get_fng_data2, get_bitcoin_price_data, process_fng_data
from analyze import run_full_analysis
from visualize import run_all_plots


if __name__ == "__main__":
    # load the data into data/ folder
    get_fng_data1()
    get_fng_data2()
    process_fng_data()
    get_bitcoin_price_data()

    # run the analyses 
    print("Running analyze.py functions ...")
    run_full_analysis()

    # run the visualizations 
    print("Running visualize.py functions ...")
    run_all_plots()


