from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')       
def checkerboard():
    return render_template("checkerboard.html",x=8,y=8)

@app.route('/4')       
def checkerboard_x():
    return render_template("checkerboard.html", x = 4,y=8 )

@app.route('/<int:x_value>/<int:y_value>')       
def checkerboard_x_y(x_value, y_value):
    return render_template("checkerboard.html", x=x_value, y = y_value)

# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.