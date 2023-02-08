import pandas as pd

def xltodf(flpath):
    df = pd.read_excel(flpath);
    col = list(df.columns);
    df.set_index(col[0], inplace=True);

    return df;




#print(df);
# df.to_excel(r"C:\Users\Harshitha\Desktop\fdlimit.xlsx");
"""
with pd.ExcelWriter('/path/to/file.xlsx',engine = "openpyxl",  mode='a') as writer:
 workBook = writer.book
 try:
  workBook.remove(workBook['Town_names'])
 except:
  print("worksheet doesn't exist")
 finally:
  df.to_excel(writer, sheet_name='Town_names')
 writer.save()
"""

"""
class fdlimit:
    def __init__(self):
        self.df1= self.getdf();
    def getdf(self):
        data={'method':['boil','steam','roast','fry','deep fry','raw'], 'max_times_per_week':[14,14,5,3,2,10]};
        dishmethreq= pd.DataFrame(data);
        dishmethreq.set_index('method', inplace=True);
        return dishmethreq
"""