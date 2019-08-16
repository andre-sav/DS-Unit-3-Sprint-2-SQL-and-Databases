import sqlite3


# In[2]:


con = sqlite3.connect('demo_data.sqlite3')


# In[3]:


curs = con.cursor()


# In[4]:


statement = """CREATE TABLE demo (
                s VARCHAR(10),
                x INT,
                y INT);
            """


# In[5]:


curs.execute(statement)


# In[13]:


statement = """
            INSERT INTO demo VALUES
                ('g', 3, 9),
                ('v', 5, 7),
                ('f', 8, 7);
            """


# In[14]:


curs.execute(statement)


# In[15]:


query = 'SELECT COUNT(*) FROM demo;'


# In[16]:


curs.execute(query).fetchall()


# In[17]:


query = 'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5;'


# In[18]:


curs.execute(query).fetchall()


# In[24]:


query = 'SELECT COUNT(DISTINCT y) FROM demo;'


# In[25]:


curs.execute(query).fetchall()


# In[ ]:


con.commit()

