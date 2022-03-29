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
        return -1


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


def calculate_pearson_coefficients(target_user, reviews):
    coefficients = []

    for user in reviews:
        if user != target_user:
            coefficient = pearson(reviews[user], reviews[target_user])
            coefficients.append((user, coefficient))

    return sorted(coefficients, key=lambda tuple_: tuple_[1], reverse=True)


def recommend(user):
    reviews = get_reviews()
    recommendations = set()
    end_search = False

    for neighbor, _ in calculate_pearson_coefficients(user, reviews):
        neighbor_games = list(reviews[neighbor].keys())
        unplayed_games = list(filter(lambda game: game not in reviews[user], neighbor_games))

        for game in unplayed_games:
            recommendations.add(game)
            if len(recommendations) == 3:
                break
        
        if len(recommendations) == 3:
            break

    return recommendations


def review(user, game, score):
    reviews = get_reviews()

    if game not in get_games():
        raise ValueError('Game is not in game list')

    if user not in reviews.keys():
        reviews.update({user: {game: score}})
    else:
        reviews[user].update({game: score})

    save_reviews(reviews)
