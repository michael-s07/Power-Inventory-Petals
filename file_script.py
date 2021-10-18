#!/usr/bin/env python
# coding: utf-8

# In[5]:



import pandas as pd
inventory=pd.read_csv('inventory.csv')
print(inventory.head(10))
staten_island=inventory.iloc[0:10]
print(staten_island)
product_request=staten_island.product_description
print(product_request)
seed_request=inventory[(inventory.location=='Brooklyn') & (inventory.product_type=='seeds')]
print(seed_request)
inventory['in_stock']=inventory.quantity.apply(lambda x: 'True' if x > 0 else 'False')

inventory['total_value']=inventory.quantity * inventory.price
print(inventory)



# In[9]:


pricombine_lambda= lambda row: '{}'-'{}'.format(row.product_type,row.product_description)
print(combine_lambda)
inventory['full_description']=combine_lambda
print(inventory)


# In[ ]:




