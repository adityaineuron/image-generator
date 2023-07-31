from flask import Flask, request, render_template
from src.image_generator import ImageGenerator





app = Flask(__name__)


def image_url_retriever(text_prompt: str) -> list:
    try:
        image_urls = []
        
        image_generator = ImageGenerator(text_prompt=text_prompt)
        
        url_data = image_generator.generate_image_from_text()

        for object in url_data:
            image_urls.append(object['url'])

        return image_urls
    
    except Exception as e:
        print(e)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/generate", methods=["POST"])
def generate():

    text_prompt = request.form.get("text_prompt")
    
    image_urls = image_url_retriever(text_prompt=text_prompt)

    return render_template('home.html', image_urls=image_urls)



if __name__ == "__main__":
    app.run(debug=True)