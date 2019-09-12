from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_():

  return "It's the first line from Flak!"
  
if __name__ == "__main__":

  app.run()
