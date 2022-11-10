from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/<int:numRow>/<int:numCol>')
def rowCol(numRow, numCol):
    num = numRow
    numCl = numCol
    return render_template('index.html', numRows = num, numCol = numCl)

@app.route('/<int:numRow>')
def row(numRow):
    num = numRow
    return render_template('index.html', numRows = num)

@app.route('/<string:col1>/<string:col2>')
def color(col1, col2):
    color1 = col1
    color2 = col2
    return render_template('index.html', col1 = color1, col2 = color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

