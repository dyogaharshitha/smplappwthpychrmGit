import json
import updatedf
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import requests
from requests.auth import HTTPBasicAuth


app= Flask(__name__);

@app.route("/", methods=['GET', 'POST'])
def showhomepg():
    print("show home page func");
    return render_template('homepg.html');


@app.route("/calnutri", methods=['GET', 'POST'])
def calnutri():
    print("cal nutri func");
    if request.method== 'POST':
        print("cal nutri post");
        jdat = json.loads(request.data);
        if jdat['srch']=='yes':
            dshlst= jdat['dat']; # print(jdat['dat']);
            srchlst= updatedf.srchkeywrd(dshlst);
            print(updatedf.srchkeywrd(dshlst));
            snd= json.dumps(srchlst);
          #  urlsrc= "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb";
          #  #urlsrc = "https://api.nal.usda.gov/fdc/v1/foods/search";
          #  usdt = {"query": "sharp cheddar cheese"};
          #  headr = {'Content-type': 'application/json', 'Accept': 'application/json'};
          #  auth = HTTPBasicAuth('api_key','X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb');  # "api_key": "X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb" };
          #  reslt = requests.get(url= urlsrc, data=usdt, headers=headr);
          #  jsn= reslt.json(); #print(jsn["totalHits"]);
          #  print(jsn["foods"][0]["fdcId"]);
            return snd;
        if jdat['srch']== 'no':
            print("log data"); print(jdat['dat']);
            dshlst= jdat['dat'];
            dsh= list();
            for el in dshlst:
                dsh.append(int(el));

            nutrijsn= updatedf.calcnutri(dsh);
            snd = json.dumps(nutrijsn); print(snd);

            return snd;
    return render_template('calcnutri.html');

app.run(host="0.0.0.0")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
