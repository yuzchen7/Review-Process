import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Function Name: make_plot

    General a bar graph base on the given data set with sentiments 
    in {negative, positive, neutral, irrelevant}, outputting into
    a png.

    Args:
        sentiments (List[str]): List of data sentiments, in str type
    
    Returns:
        no return value
    """
    sentiments_map = {
        "negative"   : 0,
        "positive"   : 0,
        "neutral"    : 0,
        "irrelevant" : 0
    }

    for sentiment in sentiments: 
        sentiments_map[sentiment] += 1
    
    sentiments_type = list(sentiments_map.keys())
    sentiments_count = list(sentiments_map.values())

    plt.figure(figsize=(12,6))
    fig, ax = plt.subplots()
    plt.title("Sentiments Review Count")
    ax.set_xlabel("Count")

    ax.barh( 
        sentiments_type,
        sentiments_count
    )
    fig.savefig("./images/sentiments.png")

def make_label(counts, labels):
    return [f'{label} ({count})' for label, count in zip(labels, counts)]