from flask import Flask, render_template, jsonify, request
import subprocess
import pandas as pd

app = Flask(__name__)

# Load dataset
file_path = "data1.csv"
data = pd.read_csv(file_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/patient2')
def patient2():
    return render_template('patient2.html')

@app.route('/patient3')
def patient3():
    return render_template('patient3.html')

@app.route('/skin-analysis')
def skin():
    return render_template('skin-analysis.html')

@app.route('/urine-analysis')
def urine():
    return render_template('urine-analysis.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    return jsonify({"message": "Image uploaded"})

@app.route('/run-training', methods=['POST'])
def run_training():
    try:
        # Start plot.py in a non-blocking way
        process = subprocess.Popen(["python", "plot.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Training script started successfully.")
        return jsonify({"message": "Training started successfully!"})
    except Exception as e:
        print(f"Error starting training: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
