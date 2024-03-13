from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'The server was created by @itsmyCareer, runs on Amazon Web Service, and will be used as an introductory page for the basketball team.'

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
    #app.run(debug=True)
