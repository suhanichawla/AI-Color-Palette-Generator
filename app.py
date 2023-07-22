from flask import Flask, render_template, request
import openai, json
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


app = Flask(__name__, 
    template_folder='templates',
    static_url_path='',
    static_folder='static'
)


def get_api_response(text, max_tokens=200, model='text-davinci-003'):
    prompt = f"""You are a color palete generating assistant that responds to text prompts for color palettes
    you should generate color palettes that fir the theme, mood or instructions in the prompt. The palette should be between two and eight colors

    Output format: JSON array of hexadecimal color codes

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]

    Q: Convert the following verbal description of a color palette into a list of colors: {text} 
    A:

    """
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=max_tokens
    )
    #print(response)
    return json.loads(response["choices"][0]["text"])


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/palette', methods=["POST"])
def get_palette():
    text = request.form.get("query")
    
    colors = get_api_response(text)
    app.logger.info(colors)
    return {"colors": colors}

if __name__ == "__main__":
    app.run(debug=True)

