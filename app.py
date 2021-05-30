from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///root.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email= db.Column(db.String(255),unique=True, nullable=False)
    message= db.Column(db.Text(278), nullable=False)

    def __tsl__(self):
        return '<Entry %>' % self.id 


@app.route("/") 
def homepage():
    task = Task.query.all()
    return render_template("index.html", task=task)


@app.route('/contact', methods = ['POST', 'GET'])
def index ():
    if request.method == 'POST':
        entry_content = request.form['content']
        new_entry = Task(content = entry_content)
        
        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('contact.html')
        except:
            return "Error Creating Task"
    else: 
        task = Task.query.order_by(Task.id).all()
        return render_template ('contact.html', task = task)

if __name__ == "__main__":
    app.run(debug=  True)