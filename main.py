import json
import updatedf
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for


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
