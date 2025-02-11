from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key
client = OpenAI()

@app.route("/", methods=["GET", "POST"])
def index():
    textResult = None
    imgResult = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            textResponse = openai.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[{"role": "developer", "content": "You are a psychedelic AI that speaks in Oulipian constraints. Your responses are short, surreal, and witty. Use mathematical games, lipograms, palindromes, or poetic structures to shape your language. Avoid predictable phrasing. Let logic slip through the cracks like liquid geometry."}, 
                          {"role": "user", "content": prompt}],
                          temperature=1.2,
                          max_completion_tokens=50
            )
            textResult = textResponse.choices[0].message.content

            imgResponse = client.images.generate(
                model="dall-e-3",
                prompt= "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:", prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
        except Exception as e:
            textResult = f"Error: {str(e)}"
            imgResult = f"Error: {str(e)}"

    return render_template("index.html", textResult=textResult)
    return render_template("index.html", imgResult=imgResult)


if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing