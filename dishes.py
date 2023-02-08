import pandas as pd
import xldata

class dishesclass:
    def __init__(self):
        self.dishdf= pd.DataFrame();

    def getdishesdf(self):
        self.dishdf = xldata.xltodf("static/database/dishnutri.xlsx");
        return self.dishdf;

    def dishsbyCond(self, col, cond, limit, dishdf= " "):
        if dishdf == " ":
            dishdf= self.dishdf;
        if cond == '<':
            df = dishdf[dishdf[col] < limit];
        if cond == '>':
            df = dishdf[dishdf[col] > limit];
        if cond == '=':
            df = dishdf[dishdf[col] == limit];
            return df;

class defnutrireq:
    def __init__(self):
        #self.dishmethfrqreqdf = xldata.xltodf("static/database/dishmethfrqreq.xlsx");
        #self.nutrireqdf= xldata.xltodf("static/database/nutrirew.xlsx");
        print("dishes py");