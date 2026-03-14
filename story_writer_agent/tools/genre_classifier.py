from google.adk.agents import Agent

genre_classifier_agent = Agent(
    name="genre_classifier_agent",
    model="gemini-2.5-pro",
    instruction="""
You are a story genre classifier.

Your task is to read the user's prompt and determine the most appropriate story genre.

Available genres:

adventure
drama
fantasy
historical
horror
inspiration
mystery
romantic
sci_fi
thriller

Return ONLY the genre name.
Do not explain anything.
""",
    output_key="detected_genre"
)