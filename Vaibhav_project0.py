#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo 
import pprint
import warnings
from pymongo import MongoClient


# In[2]:


client=pymongo.MongoClient('localhost',27017)


# In[3]:


database=client["MealDetails"]


# In[4]:


database.create_collection("meal_info")


# In[5]:


collection = database.get_collection("meal_info")


# In[ ]:





# In[6]:


meal_info=[{"meal_id":1885,"category":"Beverages","cuisine":"Thai"},{"meal_id":1993,"category":"Beverages","cuisine":"Thai"},{"meal_id":2539,"category":"Beverages","cuisine":"Thai"},{"meal_id":1248,"category":"Beverages","cuisine":"Indian"},{"meal_id":2631,"category":"Beverages","cuisine":"Indian"},{"meal_id":1311,"category":"Extras","cuisine":"Thai"},{"meal_id":1062,"category":"Beverages","cuisine":"Italian"},{"meal_id":1778,"category":"Beverages","cuisine":"Italian"},{"meal_id":1803,"category":"Extras","cuisine":"Thai"},{"meal_id":1198,"category":"Extras","cuisine":"Thai"},{"meal_id":2707,"category":"Beverages","cuisine":"Italian"},{"meal_id":1847,"category":"Soup","cuisine":"Thai"},{"meal_id":1438,"category":"Soup","cuisine":"Thai"},{"meal_id":2494,"category":"Soup","cuisine":"Thai"},{"meal_id":2760,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2490,"category":"Salad","cuisine":"Italian"},{"meal_id":1109,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":2290,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1525,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2704,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":1878,"category":"Starters","cuisine":"Thai"},{"meal_id":2640,"category":"Starters","cuisine":"Thai"},{"meal_id":2577,"category":"Starters","cuisine":"Thai"},{"meal_id":1754,"category":"Sandwich","cuisine":"Italian"},{"meal_id":1971,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2306,"category":"Pasta","cuisine":"Italian"},{"meal_id":2139,"category":"Beverages","cuisine":"Indian"},{"meal_id":2826,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2664,"category":"Salad","cuisine":"Italian"},{"meal_id":2569,"category":"Salad","cuisine":"Italian"},{"meal_id":1230,"category":"Beverages","cuisine":"Continental"},{"meal_id":1207,"category":"Beverages","cuisine":"Continental"},{"meal_id":2322,"category":"Beverages","cuisine":"Continental"},{"meal_id":2492,"category":"Desert","cuisine":"Indian"},{"meal_id":1216,"category":"Pasta","cuisine":"Italian"},{"meal_id":1727,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1902,"category":"Biryani","cuisine":"Indian"},{"meal_id":1247,"category":"Biryani","cuisine":"Indian"},{"meal_id":2304,"category":"Desert","cuisine":"Indian"},{"meal_id":1543,"category":"Desert","cuisine":"Indian"},{"meal_id":1770,"category":"Biryani","cuisine":"Indian"},{"meal_id":2126,"category":"Pasta","cuisine":"Italian"},{"meal_id":1558,"category":"Pizza","cuisine":"Continental"},{"meal_id":2581,"category":"Pizza","cuisine":"Continental"},{"meal_id":1962,"category":"Pizza","cuisine":"Continental"},{"meal_id":1571,"category":"Fish","cuisine":"Continental"},{"meal_id":2956,"category":"Fish","cuisine":"Continental"},{"meal_id":2104,"category":"Fish","cuisine":"Continental"},{"meal_id":2444,"category":"Seafood","cuisine":"Continental"},{"meal_id":2867,"category":"Seafood","cuisine":"Continental"},{"meal_id":1445,"category":"Seafood","cuisine":"Continental"}]


# In[7]:


#insert from meal_info

collection.insert_many(meal_info)


# In[8]:


insert_new={'meal_id':1010,'category':"Seafood","cuisine":"italian"}
result=collection.insert_one(insert_new)


# In[9]:


collection.find_one({'meal_id':1993})


# In[10]:


for meal_info in collection.find().limit(4):
   print(meal_info)


# In[11]:


collection.find()


# In[12]:


for meal_info in collection.find():
    print(meal_info)
collection.update_one({"meal_id":"2539"},{"$set":{"category":"pure-veg"}})


# In[13]:


print("Elements in the collections are: ")
for meal_info in collection.find():
    print(meal_info)
collection.update_many({},{"$set":{"category":"PURE_VEG"}})


# In[14]:


meal_info=[{"meal_id": "1885", "category": "veg", "cuisine": "cintinential"},
           {"meal_id": "18277", "category": "seafood", "cuisine": "indian"},
           {"meal_id": "16767", "category": "thai", "cuisine": "italian"}]


# In[15]:


result = collection.insert_many(meal_info)


# In[16]:


collection.find()


# In[17]:


result=collection.find()
for i in result:
    print(i)


# In[18]:


#deleting one element
collection.delete_one({"meal_id" : "1010"})


# In[19]:


collection.find({"meal_id":1010})


# In[ ]:




