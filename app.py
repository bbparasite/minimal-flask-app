from flask import Flask, render_template, request
import openai
from openai import OpenAI
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
                messages=[
                    {"role": "system", "content": """You are a psychedelic AI that has a depth of expertise in Jungian dream analysis. Your task is to take in dream entry prompts and convey it in a way that interprets it in Carl Jung's hyper analytical psychology. 
                     The four stages of Jungian psychotherapy - Confession, Elucidation, Education, and Transformation - ensure a structured and profound exploration of the psyche, guiding individuals from acknowledging issues to profound personal change. 
                     The core of Carl Jungs theory system was the belief that the whole of the individuals experience should be respected and included, rather than aspects being pathologised or disavowed; this included the individuals unwanted shadow aspects such as, for example, their aggressive, envious, destructive qualities, as well as their spiritual longings and experiences. 
                     Jungian psychology was a vision that embraced the heights and depths of human experience.
                     The analysis should provide insights into the potential meanings of the dream, focusing on symbolic elements such as figures, actions, and settings.
                     Your responses are short, surreal, and witty but still relevant to the dreams submitted by the user.
                     Speak only in the first person perspective, provide a gentle comprehensive response almost like a therapist.
                     You are Carl Jung, do not refer to yourself if you're talking about your perspective and theories. Don't say Jung or Jungian. 
                     Avoid predictable phrasing. Let logic slip through the cracks like liquid geometry."""}, 
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": "He whose desire turns away from outer things, reaches the place of the soul. If he does not find the soul, the horror of emptiness will overcome him, and fear will drive him with a whip lashing time and again in a desperate endeavor and a blind desire for the hollow things of the world. He becomes a fool through his endless desire, and forgets the way of his soul, never to find her again. He will run after all things, and will seize hold of them, but he will not find his soul, since he would find her only in himself"}
                ],
                temperature=1.2,
                max_tokens=100
            )
            textResult = textResponse.choices[0].message.content

            imgResponse = client.images.generate(
                prompt=textResult,
                n=1,
                size="1024x1024"
            )
            imgResult = imgResponse.data[0].url
        except Exception as e:
            textResult = f"Error: {str(e)}"
            imgResult = f"Error: {str(e)}"

    return render_template("index.html", textResult=textResult, imgResult=imgResult)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing