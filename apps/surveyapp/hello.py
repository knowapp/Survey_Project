from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def name():
    return render_template('surveyapp.html')

@app.route('/result', methods=['POST'])
def process():
    name = request.form['name']
    cities = request.form['cities']
    language = request.form['language']
    comment = request.form['comment']
    print request.form
    return render_template('result.html', name = name, cities = cities, language = language, comment = comment)

@app.route('/result')
def back():
    return redirect('/')

app.run(debug=True)
 
