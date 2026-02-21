from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('subject'))
    return render_template('register.html')

@app.route('/subject', methods=['GET','POST'])
def subject():
    return render_template('subject.html')
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run(debug=True)