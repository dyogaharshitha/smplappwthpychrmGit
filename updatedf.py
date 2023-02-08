import dishes
import pandas as pd

dishesobj= dishes.dishesclass();
dishdf= dishesobj.getdishesdf();

def srchkeywrd(kywrd):
  dshnme= dishdf["dish_name"];
  srch= list();
  srchnum= list();
  srchdic= dict();
  if type(kywrd) == 'int':
    dish= dishdf.loc[kywrd];
    srchdic[kywrd]= dish;
  else:
    for indx,dishnm in dshnme.items():
      if kywrd in dishnm:
        srch.append(dishnm);
        srchnum.append(indx);
  srchdict= dict(zip(srchnum, srch));


  return srchdict;

def calcnutri(dishlst):
    mealdf= pd.DataFrame();
    for indx in dishlst:
      el= dishdf.loc[indx];
      mealdf = pd.concat([mealdf, pd.DataFrame(el)], axis=1, ignore_index=False);
    print(mealdf);
    calories = mealdf.loc["Calories"].sum();
    carb = mealdf.loc["Carbohydrate_g"].sum();
    prot = mealdf.loc["Protein_g"].sum();
    fat = mealdf.loc['Fat_g'].sum();
    nutridict = {"cal":calories,"carb": carb, "prot": prot, "fat": fat};
    return nutridict;