from unittest import result
import pandas as pd
import read_and_clean_data
import json


class Analyzer:
    def __init__(self):
        self.RD=read_and_clean_data.Load_and_clean_data()
        self.RD.Load_data()
        self.df=self.RD.Get_data()
        self.target_col = "Biased"
        self.amounts ={}
        self.new_df={}
        self.avrg_word ={}
        self.words ={}
        self.top3={}
        self.upper={}
        self.result={}



    def Count_biased(self):
        self.typas=self.df[self.target_col].value_counts()
        for k in self.typas.index:
            self.amounts[k]=self.typas[k]
            mask = self.df[self.target_col] == k
            filterd = self.df[mask].copy()
            filterd.drop(self.target_col, axis=1, inplace=True)
            self.new_df[k] = filterd
        self.typas_dict=self.typas.to_dict()
        return self.typas_dict


    def find_avrg_len(self):
        sum=0
        for k in self.new_df.keys():
            for v in self.new_df[k]["Text"]:
                Text_arr=v.split()
                sum=sum+len(Text_arr)
            sum=sum/self.amounts[k]
            self.avrg_word[k]=float(sum)
        total=0
        for i in self.avrg_word.keys():
            total=total+self.avrg_word[i]
        self.avrg_word["total"]=total
        return self.avrg_word

    def Finding_longest_tweet(self):
        for k in self.new_df.keys():
            temp_df = self.new_df[k]
            temp_df["char_count"] = temp_df["Text"].str.len()
            self.new_df[k] = temp_df

            # ניקח את שלושת הציוצים הארוכים ביותר  ל dict
            top3_df = temp_df.sort_values(by="char_count", ascending=False).head(3)
            self.top3[k] = top3_df.to_dict(orient="records")

        return self.top3

    def  Find_10_most_commen_w(self):
        words={}
        for k in self.new_df.keys():
            for v in self.new_df[k]["Text"]:
                for word in str(v).lower().split():
                    if word in words:
                        words[word]=words[word]+1
                    else:
                        words[word]=1
        words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        self.words = words[:10]
        self.words1=[]
        for i in self.words:
            self.words1.append(i[0])
        return self.words1


    def count_uppercase_words(self):

        for k in self.new_df.keys():
            count = 0
            for text in self.new_df[k]["Text"].dropna():
                words = str(text).split()
                for word in words:
                    if word.isalpha() and word.isupper():
                        count += 1
            self.upper[k]=count
        total=0
        for i in self.upper:
            total += self.upper[i]
        self.upper["total"]=total
        return self.upper

    def ading_to_json(self):
        #משתנה עם כמות השורות מכל סוג
        typs=self.Count_biased()
        #משתנה שיסכום את כל השורות יחד
        totel=0
        #נעשה דיקשנרי שמקבלם את הערכים
        self.result["total_tweets"]={}
        #נעבור בלולאה על כל סוג אופציה
        for k in typs.keys():
            self.result["total_tweets"][k]=int(typs[k])
            totel=totel+typs[k]
        self.result["total_tweets"]["totel"]=int(totel)

        #משתנה שיכיל את הממוצעים
        avrg=self.find_avrg_len()
        self.result["average_length"]=avrg

        #נכניס את עשר המילים הכי נפוצות
        common_words =self.Find_10_most_commen_w()
        self.result["common_words"]=common_words

        #נכניס את השלוש ציוצים הכי ארוכים לכל קטגוריה
        longest_3_tweets=self.Finding_longest_tweet()
        self.result["longest_tweets"]=longest_3_tweets

        #נכניס אתהמילים שהם אותיות גדולות
        uppercase_words=self.count_uppercase_words()
        self.result["uppercase_words"]=uppercase_words

        with open(r"C:\Users\gmth0\OneDrive\Desktop\data golan\mini project\.venv\resullts\ results.json", "w", encoding="utf-8") as f:
            json.dump(self.result, f, indent=4, ensure_ascii=False)
            print("saved successfully")



        print(self.result)







A=Analyzer()
A.ading_to_json()