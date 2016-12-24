from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dominikm/Coding/Projects/short-latex/short_latex.db'
db = SQLAlchemy(app)

########## Errors ###########
# 1: empty latex


########## MODELS ###########

class Latex(db.Model):
    url = db.Column(db.String(32), primary_key=True)
    latex = db.Column(db.Text)

    def __init__(self, latex):
        self.latex = latex
        self.url = str(uuid4())


    
@app.route('/')
def home():
    page_data = {
        'save_url': url_for('save')
    }
    return render_template('latex_producer.html', page_data=page_data)

@app.route('/<latex_id>')
def show_latex(latex_id):
    latex = Latex.query.get(latex_id)
    if latex is not None:
        return render_template('latex_view.html', latex="$$" + latex.latex + "$$")
    else:
        return redirect(url_for('home'))
    
    

@app.route('/save/', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':
        latex_text = ''
        # TODO: strip malicious code (maybe in model?)
        if request.form['latex_text'] != '':
            latex_text = request.form['latex_text']
        else:
            return jsonify(result="fail", error=1)

        new_latex = Latex(latex_text)
        db.session.add(new_latex)
        db.session.commit()
        latex_url = url_for('show_latex', _external=True, latex_id = new_latex.url)

        return jsonify(result="success", latex_url=latex_url)

    else:
        return redirect(url_for('home'))
    
