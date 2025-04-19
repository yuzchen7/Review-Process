from openai import OpenAI
import json


def get_sentiment(text: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    if not isinstance(text, list) or len(text) == 0 or not text:
        return "Wrong input. text must be an array of strings."
    
    for item in text:
        if not isinstance(item, str):
            return "Wrong input. text must be an array of strings."

    system_prompt = f"""
        Your are the sentiment analysis assistant that to classify its sentiment.
        The result must be in a list with category labels as strings. 
        Respond **only** in this JSON format:
        {{
            "result": ["positive", "neutral", "negative", "irrelevant"]
        }}
        each sentiment only result in one labels.
        Which means that the length of result array must be same as the length of original array.
        The size of the original array will be {len(text)}
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    # pass
    client = OpenAI()
    print("input array size:", len(text))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
	        { "role": "system",  "content": system_prompt },
            { "role": "user",  "content": prompt }
        ]
    )
    
    content = response.choices[0].message.content

    try:
        json_result = json.loads(content)
        if isinstance(json_result, dict) and "result" in json_result:
            result = json_result["result"]
            print("output array size:", len(text))
            return result if isinstance(result, list) else "Unexpected result format"
        else:
            return "Unexpected response format"
    except json.JSONDecodeError:
        return "Invalid JSON format returned"
