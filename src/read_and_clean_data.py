import pandas as pd



class Load_and_clean_data:
    def __init__(self):
        self.df=None

    def Load_data(self):
        try:
            self.df= pd.read_csv(r"../data/tweets_dataset.csv")
            print("The data has been uploaded successfully.")
        except:
            print ("no dataset")


    def Clean_data(self):
        pass


    def Get_data(self):
        return self.df


r=Load_and_clean_data()
r.Load_data()