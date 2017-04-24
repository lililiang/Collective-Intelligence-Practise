#coding:utf-8
import math

'''
names = [
    'Lisa Rose',
    'Gene Seymour',
    'Michael Phillips',
    'Claudia Puig',
    'Mick LaSalle',
    'Jack Matthews',
    'Toby'
]

movies = [
    'Lady in the Water',
    'Snakes on a Plane',
    'Just My Luck',
    'Superman Returns',
    'You, Me and Dupree',
    'The Night Listener'
]
'''

critics_data = {
    'Lisa Rose' : {
        'Lady in the Water' : 2.5,
        'Snakes on a Plane' : 3.5,
        'Just My Luck' : 3.0,
        'Superman Returns' : 3.5,
        'You, Me and Dupree' : 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour' : {
        'Lady in the Water' : 3.0,
        'Snakes on a Plane' : 3.5,
        'Just My Luck' : 1.5,
        'Superman Returns' : 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree' : 3.5
    },
    'Michael Phillips' : {
        'Lady in the Water' : 2.5,
        'Snakes on a Plane' : 3.0,
        'Superman Returns' : 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig' : {
        'Snakes on a Plane' : 3.5,
        'Just My Luck' : 3.0,
        'The Night Listener': 4.5,
        'Superman Returns' : 4.0,
        'You, Me and Dupree' : 2.5
    },
    'Mick LaSalle' : {
        'Lady in the Water' : 3.0,
        'Snakes on a Plane' : 4.0,
        'Just My Luck' : 2.0,
        'Superman Returns' : 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree' : 2.0
    },
    'Jack Matthews' : {
        'Lady in the Water' : 3.0,
        'Snakes on a Plane' : 4.0,
        'The Night Listener': 3.0,
        'Superman Returns' : 5.0,
        'You, Me and Dupree' : 3.5
    },
    'Toby' : {
        'Snakes on a Plane' : 4.5,
        'You, Me and Dupree' : 1.0,
        'Superman Returns' : 4.0
    },
}

def similarity_euclidean_distance(critics_data, one_person_name, another_person_name) :
    same_items_count = {}

    # count same movies the two watched
    for item in critics_data[one_person_name]:
        if item in critics_data[another_person_name]:
            same_items_count[item] = 1

    if len(same_items_count) == 0 : return 0;

    sum_of_quares = sum([
        pow(critics_data[one_person_name][item] - critics_data[another_person_name][item], 2)
        for item in critics_data[one_person_name] if item in critics_data[another_person_name]
    ])

    euclidean_distance = 1 / (1 + math.sqrt(sum_of_quares))

    return euclidean_distance

def similarity_pearson(critics_data, one_person_name, another_person_name) :
    same_items_count = {}

    # count same movies the two watched
    for item in critics_data[one_person_name]:
        if item in critics_data[another_person_name]:
            same_items_count[item] = 1

    if len(same_items_count) == 0 : return 0;

    sum_of_quares = sum([
        pow(critics_data[one_person_name][item] - critics_data[another_person_name][item], 2)
        for item in critics_data[one_person_name] if item in critics_data[another_person_name]
    ])

    euclidean_distance = 1 / (1 + math.sqrt(sum_of_quares))

    return euclidean_distance
