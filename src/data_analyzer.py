import pandas as pd
import read_and_clean_data

class Analyzer:
    def __init__(self):
        self.RD=read_and_clean_data.Load_and_clean_data()
        self.RD.Load_data()
        self.df=self.RD.Get_data()
        self.target_col = "Biased"
        self.amounts ={}
        self.new_df={}
        self.avrg_word ={}



    def Count_biased(self):
        pass
        self.typas=self.df[self.target_col].value_counts()
        for k in self.typas.index:
            self.amounts[k]=self.typas[k]
            mask = self.df[self.target_col] == k
            filterd = self.df[mask].copy()
            filterd.drop(self.target_col, axis=1, inplace=True)
            self.new_df[k] = filterd


    def count_worlds(self):
        sum=0
        for k in self.new_df.keys():
            for v in self.new_df[k]["Text"]:
                Text_arr=v.split()
                sum=sum+len(Text_arr)
            sum=sum/self.amounts[k]
            self.avrg_word[k]=sum




AA=Analyzer()
AA.Count_biased()
AA.count_worlds()
