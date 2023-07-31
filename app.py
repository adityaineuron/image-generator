from flask import Flask, request, render_template
from src.image_generator import ImageGenerator





app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/generate", methods=["POST"])
def generate():
    
    text_prompt = request.form.get("text_prompt")
    image_generator = ImageGenerator(text_prompt=text_prompt)
    image_url = image_generator.generate_image_from_text()
    return render_template('home.html', image_url=image_url)




if __name__ == "__main__":
    app.run(debug=True)