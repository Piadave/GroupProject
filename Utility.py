#This is the file for all functions

#suppose the scraped data is stored in "data"
#user choice of genre is "genre"

#Function 1
#Function 2
def func2:
  positive_reviews = []
  for i in data:
      if i['review score']>=6:
          positive_reviews.appead(i)
  return positive_reviews

#Function 3
def func3:
  topfive = []
  n = 5
  for i in positive_reviews:
      while n > 0:
        max = max(positive_reviews, 'rating')
        topfive.append(max)
        data.remove(max)
        n = n - 1
      return topfive 
      
      
