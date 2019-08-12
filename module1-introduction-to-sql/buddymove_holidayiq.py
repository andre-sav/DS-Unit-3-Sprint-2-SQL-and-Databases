import pandas as pd
import sqlite3


# In[84]:


data = pd.read_csv('buddymove_holidayiq.csv')


# In[93]:


data.head()


# In[117]:


data.loc[(data['Nature']>100) & (data['Shopping']>100)].shape


# In[85]:


conn = sqlite3.connect('buddymove_holidayiq.sqlite3')


# In[90]:


data.to_sql(con=conn,name='review')


# In[91]:


query = 'SELECT COUNT(*) FROM review'

curs = conn.cursor()

print(curs.execute(query).fetchall())


# In[96]:


query = 'SELECT COUNT(*) FROM review WHERE "User Id" IN (SELECT "User Id" WHERE Nature > 100 AND Shopping > 100)'


# In[97]:


print(curs.execute(query).fetchall())


# In[102]:


query = 'SELECT AVG(Sports), AVG(Religious) FROM review'


# In[103]:


print(curs.execute(query).fetchall())

