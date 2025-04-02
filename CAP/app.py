from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the second page (Stages)
@app.route('/second')
def second():
    return render_template('stages.html')

# Route for the third page (Workflows)
@app.route('/workflows')
def workflows():
    return render_template('workflows.html')

# Route for the fourth page (tutorials)
@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

# Route for the fifth page (data)
@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/square1')
def square1():
    return render_template('externalExposure.html')

@app.route('/square2')
def square2():
    return render_template('internalExposure.html')

@app.route('/square3')
def square3():
    return render_template('molecularinitiatingevent.html')

@app.route('/square4')
def square4():
    return render_template('square4.html')

@app.route('/square5')
def square5():
    return render_template('square5.html')

@app.route('/square6')
def square6():
    return render_template('square6.html')

@app.route('/tut_vid')
def tut_vid():
    return render_template('tut_vid.html')

@app.route('/tut_man')
def tut_man():
    return render_template('tut_man.html') 


@app.route('/tut_test')
def tut_test():
    return render_template('tut_testrun.html') 


@app.route('/tut_man_thyroid')
def tut_man_thyroid():
    return render_template('tut_man_thyroid.html') 


@app.route('/tut_man_park')
def tut_man_park():
    return render_template('tut_man_parkinsons.html') 




if __name__ == "__main__":
    app.run(debug=True)

