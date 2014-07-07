#!/usr/bin/python
from math import sqrt
users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
    "Norah Jones": 4.5, "Phoenix": 5.0,
    "Slightly Stoopid": 1.5,
     "The Strokes": 2.5, "Vampire Weekend": 2.0},
      "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
           "Deadmau5": 4.0, "Phoenix": 2.0,
            "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
       "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
            "Deadmau5": 1.0, "Norah Jones": 3.0,
             "Phoenix": 5, "Slightly Stoopid": 1.0},
        "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
             "Deadmau5": 4.5, "Phoenix": 3.0,
              "Slightly Stoopid": 4.5, "The Strokes": 4.0,
               "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
              "Norah Jones": 4.0, "The Strokes": 4.0,
               "Vampire Weekend": 1.0},
          "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
               "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                "The Strokes": 4.0, "Vampire Weekend": 4.0},
           "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
                "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
            "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
                 "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                  "The Strokes": 3.0}}

""" give it data, which neighbor to use, which calculation to use, and
the number of recommendations it should make"""
class recommender:
    def __init__(self, data, k=1, metric='pearson', n=5):
        self.k = k
        self.n = n
        self.data = data
        self.username2id = {}
        self.productid2name = {}
        self.metric = metric
        if self.metric == 'pearson':
            self.fn = self.pearson


    #willl have to rewrite this part for our data
    def convertProudctID2name(self, id):
        # shoot in the product number, gives out the product name, should be easy enough
        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id

    def pearson(self, rating1, rating2):
        """ my implementation of the pearson correlation formula  wiki that shit if you forget what it is"""
        # numerator stuff
        xy = 0
        x = 0
        y = 0
        n = 0
        xx = 0
        yy = 0

        for key in rating1:
            if key in rating2:
                x = x + rating1[key]
                y = y + rating2[key]
                yy = yy + (rating2[key] ** 2)
                xx = xx + (rating1[key] ** 2)
                n = n + 1
                xy = xy + (rating1[key] * rating2[key])

        avgxy = (x * y) / n
        numerator = xy - avgxy
        denomenator = sqrt(abs(xx - ((x**2)/n))) * sqrt(abs(yy - (y**2)/n))
        if denomenator == 0:
            return 0
        else:
            return numerator/denomenator

    def computeNearestNeighbor(self, username):
        """ what user is most like, or closest to the other neighbors"""
        distances = []
        for instance in self.data:
            if instance != username:
                distance = self.fn(self.data[username], self.data[instance])
                distances.append((instance, distance))
        # need to figure out what this is really doing. why aren't we just sorting how we did last time?
        distances.sort(key=lambda beerTuple: beerTuple[1], reverse=True)
        return distances

    def recommend(self, user):
        """ shoot me the recommendations mothafucka!"""
        recommendations = {}
        #get the nearest neighbors + ratings
        nearest = self.computeNearestNeighbor(user)
        userRatings = self.data[user]

        totalDistance = 0.0
        #this part will take the range, k, right now is 1, and do this for the 0 to kth user
        for i in range(self.k):
            totalDistance += nearest[i][1]

        for i in range(self.k):
            weight = nearest[i][1] / totalDistance
            name = nearest[i][0]
            neighborRatings = self.data[name]

            # now find what the neighbor rated, but the user didnt

            for beer in neighborRatings:
                if not beer in userRatings:
                    if beer not in recommendations:
                        recommendations[beer] = neighborRatings[beer] * weight

        # make a list from this dictionary
        recommendations = list(recommendations.items())
        recommendations = [(self.convertProudctID2name(k), v) for (k, v) in recommendations]

        recommendations.sort(key=lambda beerTuple: beerTuple[1], reverse=True)

        return recommendations[:self.n]


r = recommender(users)

print(r.recommend('Jordyn'))
print(r.recommend('Hailey'))


