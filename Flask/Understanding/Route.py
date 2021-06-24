from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/Dojo')
def Dojo():
    return "Dojo!"  # Return the string 'Dojo!' as a response

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi!, " + name

@app.route('/repeat/<int:num>/<name>')
def repeat(num , name):
    print(num)
    print(name)
    arr=""
    for i in range(num):
        arr+=name+" "
    return  arr

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.