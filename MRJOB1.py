#!/usr/bin/env python
# coding: utf-8

# In[5]:


from mrjob.job import MRJob
from mrjob.step import MRStep
class RatingBreakDown(MRJob):
    def steps(self):
        return [
         MRStep(mapper = mapper_get_rating,
                reducer = reducer_count_ratings)
        ]
    def mapper_get_rating(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield rating, 1
    def reducer_count_ratings(self, key, values):
        yield key, sum(values)


# In[ ]:




