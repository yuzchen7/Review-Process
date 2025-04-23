from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Function Name: run

    General a bar graph and a list of sentiments label for each comment base
    on the input data
    
    Args:
        filepath (str): path STRING of input file
    
    Returns:
        List[str]: the result of the sentiments label for each comment.
    """
    # open the json object
    with open("data/raw/reviews.json") as j:
        json_data = json.load(j)

    # extract the reviews from the json file
    reviews = json_data["results"]

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
