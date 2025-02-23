from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Handle image upload
    return jsonify({"message": "Image uploaded"})


###### Flask Possible method for image recognition: ################################################################################
# @app.route('/upload_image', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image uploaded'}), 400

#     image = request.files['image']
#     upload_type = request.form.get('uploadType')
#     body_area = request.form.get('bodyArea')

#     # Save the image and get its path
#     image_path = save_uploaded_image(image)

#     # Analyze the image using your trained model
#     if upload_type == 'skin':
#         result = your_trained_model.analyze_skin_image(image_path, body_area)
#     else:  # urine
#         result = your_trained_model.analyze_urine_image(image_path)

#     return jsonify({
#         'image_url': image_path,
#         'analysis_result': result
#     })
#################################################################################################################

# Handle 404 errors
def page_not_found(e):
    return render_template('404.html'), 404

app.register_error_handler(404, page_not_found)

if __name__ == "__main__":
    app.run(debug=True)
