def write_scores(filename, scores):
    """This is a utility function to save scores from a simulation

    :param filename: Filename to save scores under
    :param scores: List of scores to save to file
    :return: Void, writes to files stored in saved_scores
    """
    f = open(f"C:\Dev\Python\RL\Policy-Based-Methods\saved_scores\\{filename}.txt", 'w')
    score_string = '\n'.join([str(score) for score in scores])
    f.write(score_string)
    f.close()

def load_scores(filename):
    """Load in scores from a specific file and return them in a list

    :param filename: File to load scores from
    :return: list of all the scores
    """
    scores = []
    f = open(filename, 'r')
    for score in f:
        scores.append(int(score))
    return scores
