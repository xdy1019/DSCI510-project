import os
from config import DATA_DIR, RESULTS_DIR
from load import get_fng_data1, get_fng_data2, get_bitcoin_price_data, process_fng_data
from analyze import run_full_analysis
from visualize import run_all_plots


if __name__ == "__main__":
    # 1. Download / refresh data from APIs into data/ folder
    get_fng_data1()
    get_fng_data2()
    process_fng_data()
    get_bitcoin_price_data()

    # 2. Run all analyses (correlations, rolling, heatmap)
    print("Running analyze.py functions ...")
    run_full_analysis()

    # 3. Run all visualizations (time series + combined plots)
    print("Running visualize.py functions ...")
    run_all_plots()


