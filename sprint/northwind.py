import sqlite3

con = sqlite3.connect('northwind_small.sqlite3')

curs = con.cursor()


# In[32]:


curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()


# In[33]:


curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()


# In[37]:


query = 'SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;'

curs.execute(query).fetchall()


# In[41]:


query = 'SELECT AVG(HireDate-Birthdate) FROM Employee;'

curs.execute(query).fetchall()


# In[74]:


query = """
        SELECT City, AVG(HireDate-Birthdate)
        FROM Employee
        GROUP BY City
        """
curs.execute(query).fetchall()


# In[56]:


curs.execute('SELECT sql FROM sqlite_master WHERE name="Product";').fetchall()


# In[55]:


curs.execute('SELECT sql FROM sqlite_master WHERE name="Supplier";').fetchall()


# In[57]:


query = """
        SELECT ProductName, UnitPrice, CompanyName
        FROM Product
        INNER JOIN Supplier ON Product.SupplierID = Supplier.Id
        ORDER BY UnitPrice DESC
        LIMIT 10
        """

curs.execute(query).fetchall()


# In[58]:


curs.execute('SELECT sql FROM sqlite_master WHERE name="Category";').fetchall()


# In[66]:


query = """
        SELECT CategoryName, COUNT(Product.Id)
        FROM Category
        INNER JOIN Product ON Category.Id = Product.CategoryID
        GROUP BY CategoryName
        ORDER BY COUNT(Product.Id) DESC
        """

curs.execute(query).fetchall()


# In[76]:


curs.execute('SELECT sql FROM sqlite_master WHERE name="Employee";').fetchall()


# In[77]:


curs.execute('SELECT sql FROM sqlite_master WHERE name="EmployeeTerritory";').fetchall()


# In[83]:


query = """
        SELECT FirstName, LastName, COUNT(EmployeeTerritory.Id) AS Territories
        FROM Employee
        INNER JOIN EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId
        GROUP BY Employee.Id
        ORDER BY Territories DESC
        """

curs.execute(query).fetchall()


# The relationship between Employee and Territory is many to many. They are not directly connected via the schema. Logically, given a large enough company multiple personel may be assigned to a single territory and vica versa, if the company is small a sigle employee may be assigned multiple territories. 
# 
# MongoDB may be appropriate in a situation that requires ad hoc data insertion and has no urgency for retrieval, and or is working with large amounts of unstructed data. It is invaluable in situations where the user cannot pre define the schema. There are few limitations placed upon the user to organize their data, which makes it very easy to upload. If done in an unstructured manner, the data will be difficult to organize and retrieve efficiently. To avoid this one must use proper indexing. 
# 
# MongoDB is not appropriate for use where stability is of the utmost importance. A relational database such as MySQL would serve better, as it is a mature platform with widespread adoption. Getting technical support is trivial and operational memory requirements are lower for those who are infrastructure limited. Also, MongoDB doesn't support joins in a straightforward fashion. Doing so is computationally expensive and one is better off using a structured database instead. 
# 
# NewSQL is an evolved form of SQL currently being developed to solve the lingering problems with the legacy structured database paradigm, while retaining its best attributes. The chief issue it aims to solve being scalability, meaning the database should continue functioning properly as its contents increase. The end goal is to create a system that will adhere to the principles of ACID (Atomicity, Consistency, Isolation, Durability) while scaling without an exponential increase in compute power necessary.
