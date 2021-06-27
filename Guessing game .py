import numpy as np

def binary_search(lst, integer):


    lower_bound = 0
    upper_bound = len(lst) - 1
    number_guesses = 0

    while True:
        index = (lower_bound + upper_bound) // 2

        guess = lst[index]
        number_guesses += 1

        if guess == integer:
            break

        if guess > integer:
            upper_bound = index - 1
        else:
            lower_bound = index + 1

    return number_guesses


def score_game(game_core):

    list_of_numbers = list(range(0, 101))
    predict = np.random.randint(1, 101)
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(100))
    for number in random_array:
        count_ls.append(binary_search(list_of_numbers, predict))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(binary_search)

