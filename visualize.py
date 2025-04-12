import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    INSERT DOCSTRING HERE
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