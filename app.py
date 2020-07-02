import warnings
warnings.filterwarnings('ignore')
from werkzeug.exceptions import HTTPException

from flask import Flask, request, render_template, abort
from  werkzeug.debug import get_current_traceback
import pandas as pd
import numpy as np
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

global df 
df = pd.read_csv("dataset.csv")
app = Flask(__name__)
application = app #
app.config.from_object('config.ConfigClass')
def unpak_gege(df_idx):
    df_id= df_idx["id"]
    df_nama = df_idx["nama"]
    df_img = df_idx["img"]  
    data = zip(df_id, df_nama, df_img)
    return data

def sear(dataku):
    dataku = dataku
    form = SearchForm()
    search_term = form.query.data
    inputan = search_term.lower()
    a = inputan.split(' ')
    str1 = '|'.join(str(e) for e in a)    
    df['nama'] = df['nama'].str.lower()
    data_cari = df[df["nama"].str.contains(str1)]        
    return data_cari

class SearchForm(FlaskForm):
    query  = StringField('query', validators=[DataRequired()])
@app.route("/", methods=['GET', 'POST'])
def index():
    dataset = df
    form = SearchForm() 
    if form.validate_on_submit():
        data_cari = sear(dataset)
        data_cari = unpak_gege(data_cari)
        return render_template('index.html',
        data_cari = data_cari,
        form = form)
    return render_template('index.html', form = form)	

if __name__ == '__main__':
    app.run(debug=False)
