# Jungian Dream Interpreter
https://a04-jung-ai.onrender.com/

## How Jungian ideas were embeded in the AI for analysis
> The main process for influencing the AI to give back responses that aligned with Carl Jung's psychological methodology and writing style was mainly through the editing of the system role that guides how the prompt gets interpreted. Tuning the AI involved searching up the core principles of Jungian psychology and the methodology/semiotics that Carl Jung would often use within his writings about the subconcious and dreams. Some parts of the original prompt structuring was retained to structure the AI to a semi whimsical but informative perspective on the dream that the user submits. Another thing that I added from the original framework code provided was the addition of the assistant role within the prompt generation section. The assistant was fed a direct quote from Carl Jung's The Red Book, which provides an exact example of the type of verbiage and grammar that Jung would commonly use in his writing.

## User Guide to the site
  1. When landing on the page the user is asked to provide and example of a dream that they have had
  2. Creating the prompt for the AI bot can be somewhat specific or completely wild
  3. After writing out the dream prompt the user can then submit it for the AI to analyze
  4. The prompt gets sent to GPT4oMini and the prompt is interpted by the AI with the rulesets established above
  5. Once the response from the AI is complete it is then fed directly into DALL-E (not the original user prompt itself)
  6. Finally after processing both responses it is displayed on the HTML page

## Reflection on Challenges and Improvements
> One of the main challenges that I faced when working on this project was getting the proper implementation of the image generator up and running, partly due to human error in the syntax used for the Python and HTML files. Another challenge that I faced while working on the AI chatbot was the authencity of the response given back.
