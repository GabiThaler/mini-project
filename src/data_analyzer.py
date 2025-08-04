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



    def Finding_longest_tweet(self):
        top3={}
        for k in self.new_df.keys():
            temp_df = self.new_df[k]
            temp_df["char_count"] = temp_df["Text"].str.len()
            self.new_df[k] = temp_df
            top3[k] = temp_df.sort_values(by="char_count", ascending=False).head(3)


    def  Find_10_most_commen_w(self):
        words={}
        for k in self.new_df.keys():
            for v in self.new_df[k]["Text"]:
                for word in str(v).lower().split():
                    if word in words:
                        words[word]=words[word]+1
                    else:
                        words[word]=1
        sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        words = sorted_words[:10]




AA=Analyzer()
AA.Count_biased()
AA.count_worlds()
AA.Finding_longest_tweet()
AA.Find_10_most_commen_w()