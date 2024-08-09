from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
  {
    'id':1,
    'title': "frontend-dev",
    'location': 'Islamabad,Pakistan',
    'salary': 'Rs. 2000000'
  },
  {
    'id':2,
    'title': "backend-dev",
    'location': 'Karachi,Pakistan',
    'salary': 'Rs. 1500000'
  },
  {
    'id':3,
    'title': "fullstack-dev",
    'location': 'Lahore,Pakistan'
    
  },
  {
    'id':4,
    'title': "flutter-dev",
    'location': 'remote',
    'salary': 'Rs. 1200000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

# print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
