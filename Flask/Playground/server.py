from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          
def hello_world():
    return "Hello, Flask!"

@app.route('/play')
def play():
    return render_template("index.html", times=3)	

@app.route('/play/<int:num>') 
def playx(num):
    print(num)
    return render_template('index.html', times=num) 


@app.route('/play/<int:num>/<name>')
def playxcolor(num , name):
    print(num)
    print(name)
    return render_template('index.html', phrase=name,times=num) 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
