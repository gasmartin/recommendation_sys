from math import sqrt

from database import *


def pearson(r, r2):
    sum_xy = 0.0
    sum_x = 0.0
    sum_y = 0.0
    sum_x2 = 0.0
    sum_y2 = 0.0
    n = 0

    for key in r:
        if key in r2:
            n += 1
            x = r[key]
            y = r2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += (x ** 2)
            sum_y2 += (y ** 2)      

    try:
        dem = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
        return (sum_xy - (sum_x * sum_y) / n) / dem
    except ZeroDivisionError:
        return 0


def euclidean_distance(r, r2):
    has_ratings = False
    acm = 0.0

    for key in r:
        if key in r2:
            has_ratings = True
            acm += pow(abs(r[key] - r2[key]), 2)

    if not has_ratings:
        return 999
    
    return sqrt(acm)


def get_distances(target_user, reviews):
    distances = []

    for user in reviews:
        if user != target_user:
            distance = euclidean_distance(reviews[user], reviews[target_user])
            distances.append((user, distance))

    return sorted(distances, key=lambda tuple_: tuple_[1])


def recommend(user):
    reviews = get_reviews()
    recommendation = None

    for neighbor, distance in get_distances(user, reviews):
        neighbor_games = list(reviews[neighbor].keys())
        unplayed_games = list(filter(lambda game: game not in reviews[user], neighbor_games))

        if unplayed_games:
            recommendation = unplayed_games[0]
            break

    return recommendation


def review(user, game, score):
    reviews = get_reviews()

    if game not in get_games():
        raise ValueError('Game is not in game list')

    if user not in reviews.keys():
        reviews.update({user: {game: score}})
    else:
        reviews[user].update({game: score})

    save_reviews(reviews)
