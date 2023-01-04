def load():
    scores = []
    with open("scores.txt", "r") as f:
        for line in f:
            position, name, score = line.strip().split(",")
            scores.append((name.strip(' '), score.strip(' ')))
    return scores

def insert(name, score):
    scores = load()
    scores.append((name, score))
    scores.sort(reverse=True, key=lambda x: int(x[1]))

    with open("scores.txt", "w") as f:
        for i, (name, score) in enumerate(scores):
            f.write(f"{i + 1}, {name}, {score}\n")


insert("tom", 777)

print(load())
