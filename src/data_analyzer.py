import pandas as pd
import read_and_clean_data

class Analyzer:
    def __init__(self):
        self.RD=read_and_clean_data.Load_and_clean_data()
        self.RD.Load_data()
        self.df=self.RD.Get_data()
        self.target_col = "Biased"



    def Count_biased(self):
        pass
        self.typas=self.df[self.target_col].value_counts()
        self.amount_antisemi = self.typas[0]
        self.amount_not_antisemi = self.typas[1]



AA=Analyzer()
AA.Count_biased()
