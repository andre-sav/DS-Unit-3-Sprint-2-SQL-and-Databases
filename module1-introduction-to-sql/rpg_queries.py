#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('rpg_db.sqlite3')


# In[3]:


curs = conn.cursor()


# In[4]:


query = ('SELECT COUNT(*) FROM charactercreator_character')


# In[6]:


result = curs.execute(query).fetchall()


# In[9]:


print(f'There are {result[0][0]} characters')


# In[22]:


subclass_queries = ['SELECT COUNT(*) FROM charactercreator_mage',
'SELECT COUNT(*) FROM charactercreator_thief',
'SELECT COUNT(*) FROM charactercreator_cleric',
'SELECT COUNT(*) FROM charactercreator_fighter',
'SELECT COUNT(*) FROM charactercreator_necromancer']


# In[24]:


results = []

for query in subclass_queries:
    result = curs.execute(query).fetchall()
    results.append(result)


# In[21]:


results[2][0][0]


# In[33]:


print(f'''
There are {results[0][0][0]} thiefs, {results[1][0][0]} clerics, 
{results[2][0][0]} fighters, and {results[3][0][0]} necromancers
''')


# In[34]:


query = 'SELECT COUNT(*) FROM armory_item'

result = curs.execute(query).fetchall()


# In[36]:


print(f'There are {result[0][0]} items total')


# In[41]:


query = 'SELECT (SELECT COUNT(*) FROM armory_item) - (SELECT COUNT(*) FROM armory_weapon);'


# In[44]:


not_weapons = curs.execute(query).fetchall()


# In[45]:


query = 'SELECT COUNT(*) FROM armory_weapon'


# In[46]:


weapons = curs.execute(query).fetchall()


# In[48]:


print(f'There are {weapons[0][0]} weapons, and {not_weapons[0][0]} not weapons in items')


# In[51]:


query = '''
SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory
GROUP BY character_id LIMIT 20;
'''


# In[55]:


print('(character_id, item count)')
print(curs.execute(query).fetchall())


# In[56]:


query = '''
SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id LIMIT 20;
'''


# In[58]:


print('(character_id, weapon count)')
print(curs.execute(query).fetchall())


# In[82]:


query = 'SELECT (SELECT COUNT(*) * 1. FROM charactercreator_character_inventory) / (SELECT COUNT(*) *1. FROM charactercreator_character);'

print('Average items per character: ', curs.execute(query).fetchall())


# In[81]:


query = 'SELECT ((SELECT COUNT(*) * 1. FROM charactercreator_character_inventory WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)) / (SELECT COUNT(*) * 1. FROM charactercreator_character))'

print('Average weapons per character: ', curs.execute(query).fetchall())

