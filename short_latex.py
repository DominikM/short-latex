# uncompyle6 version 2.9.8
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
# [GCC 5.4.0 20160609]
# Embedded file name: /home/dominikm/Coding/Projects/short-latex/short_latex.py
# Compiled at: 2016-12-24 11:47:23
from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + base_dir + '/short_latex.db'
db = SQLAlchemy(app)

class Latex(db.Model):
    url = db.Column(db.String(32), primary_key=True)
    latex = db.Column(db.Text)

    def __init__(self, latex):
        self.latex = latex
        self.url = str(uuid4())


@app.route('/')
def home():
    page_data = {'save_url': url_for('save')
       }
    return render_template('latex_home.j2', page_data=page_data)


@app.route('/<latex_id>')
def show_latex(latex_id):
    latex = Latex.query.get(latex_id)
    if latex is not None:
        return render_template('latex_view.j2', latex='$$' + latex.latex + '$$')
    else:
        return redirect(url_for('home'))
        return


@app.route('/save/', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':
        latex_text = ''
        if request.form['latex_text'] != '':
            latex_text = request.form['latex_text']
        else:
            return jsonify(result='fail', error=1)
        new_latex = Latex(latex_text)
        db.session.add(new_latex)
        db.session.commit()
        latex_url = url_for('show_latex', _external=True, latex_id=new_latex.url)
        return jsonify(result='success', latex_url=latex_url)
    else:
        return redirect(url_for('home'))
