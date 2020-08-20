def get_high_score(score, file):
    # Saves new score record
    with open(file, 'a') as f:
        f.write(str(score) + '\n')

    # Seeks for largest score
    scores = []
    with open(file, 'r') as score_file:
        for line in score_file.readlines():
            scores.append(int((line.split(','))[0]))
    return max(scores)
