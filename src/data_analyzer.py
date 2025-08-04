import pandas as pd
import read_and_clean_data

class Analyzer:
    def __init__(self):
        self.RD=read_and_clean_data.Load_and_clean_data()
        self.df=None