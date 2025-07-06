from openai import OpenAI

def explain_prediction(news_summary, ml_prediction):
    prompt = f"Stock news: {news_summary}\nPrediction: {ml_prediction}\nExplain the reasoning and provide investment advice."
    response = OpenAI.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content