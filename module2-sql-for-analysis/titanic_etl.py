#!/usr/bin/env python
# coding: utf-8

# In[33]:


import psycopg2
import sqlite3
import pandas as pd
from sqlalchemy import create_engine 
import io


# In[2]:


dir(psycopg2)


# In[3]:


help(psycopg2.connect)


# In[11]:


dbname = 'zflmefes'
user = 'zflmefes'
password = ''
host = 'raja.db.elephantsql.com'


# In[12]:


'postgres://zflmefes: @raja.db.elephantsql.com:5432/zflmefes'


# In[13]:


pg_conn = psycopg2.connect(dbname=dbname, user=user,
                       password=password, host=host)


# In[14]:


pg_curs = pg_conn.cursor()


# In[15]:


pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()


# In[2]:


sl_conn = sqlite3.connect('rpg_db.sqlite3')


# In[3]:


sl_curs = sl_conn.cursor()


# In[4]:


characters = sl_curs.execute('SELECT * FROM charactercreator_character;')


# In[16]:


sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()


# In[17]:


create_character_table = """
    CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR (30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
    )
"""


# In[18]:


pg_curs.execute(create_character_table)


# In[19]:


show_tables = """
SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""


# In[35]:


pg_curs.execute(show_tables).fetchall()


# In[21]:


for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name,level,exp,hp,strength,intelligence,dexterity,wisdom)
        VALUES """ + str(characters[1:]) + ";"
    pg_curs.execute(insert_character)


# In[23]:


pg_curs.close()
pg_conn.commit()


# In[27]:


df = pd.read_csv('titanic.csv')


# In[57]:


engine = create_engine('postgres://zflmefes: @raja.db.elephantsql.com:5432/zflmefes')


# In[34]:


df.to_sql('Titanic', engine)


# In[46]:


from sqlalchemy import inspect


# In[49]:


inspector = inspect(engine)

inspector.get_columns('Titanic')


# In[50]:


from sqlalchemy.sql import text


# In[58]:


con = engine.connect()

statement = ("""SELECT * FROM "Titanic" LIMIT 10""")

con.execute(statement).fetchall()


# In[ ]:


SELECT working_area, COUNT(*) 
FROM agents 
GROUP BY working_area;


# In[63]:


statement = ("""SELECT "Sex", COUNT(*) FROM "Titanic" GROUP BY "Sex" """)

con.execute(statement).fetchall()


# In[ ]:


get_ipython().system('jupyter nbconvert --to script titanic_etl.ipynb')

