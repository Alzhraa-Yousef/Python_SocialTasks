#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello from Jupyter')


# In[2]:


#1.1 Printing and inspecting variables
my_str = 'Hello'
my_int = 16

print(my_str)
print(my_int)


# In[3]:


#We can also just execute a cell with the name of a variable:
my_str


# In[4]:


#The big difference here between the two approaches is that print() statements can output multiple items per cell, while the latter approach will only display the last variable named.
my_str
my_int


# In[5]:


#2. Conditionals
number_of_apples = 5
if number_of_apples < 1:
    print('You have no apples')
elif number_of_apples == 1:
    print('You have one apple')
elif number_of_apples < 4:
    print('You have a few apples')
else:
    print('You have many apples!')


# In[6]:


#3. Lists -Ordered -By ordered, we mean that the items are addressed by their index in the collection:
student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[1]


# In[7]:


#Indices in Python start at zero, so the head of the list has index 0:
student_names[0]


# In[8]:


#We can get the last item in a list by using negative indexing:
student_names[-1]


# In[9]:


#Lists can also be sliced to get a subset of the list items:
student_names[0:2]


# In[10]:


student_names[1:3]


# In[11]:


#When slicing from the beginning of the list, or to the end of the list, we can leave out the index:
student_names[:2]


# In[12]:


student_names[2:]


# In[13]:


#3.2 Mutable By mutable, we mean that the list can be changed by adding or removing items. We most often add items to the end of the list with .append():
student_names.append('Esther')
student_names


# In[14]:


student_names.insert(2, 'Xavier')
student_names


# In[15]:


del student_names[2]
student_names


# In[16]:


#3.3 Non-unique Note that nothing stops us from repeatedly adding the same name to this list:
student_names.append('Esther')
student_names.append('Esther')
student_names


# In[17]:


#4. Loops
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

for student_name in student_names:
    print('Hello ' + student_name + '!')


# In[18]:


#4.2 Loops, lists, and conditionals
# Initialize an empty list and add to it the
# student names containing more than four characters
long_names = []
for student_name in student_names:
    # This is our criterion
    if len(student_name) > 4:
        long_names.append(student_name)

long_names


# In[19]:


#4.3 Nested loops
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs


# In[20]:


student_pairs[0]


# In[21]:


#We'll talk more about tuples in the next section. The second thing to notice is that we're including pairs with two of the same student. Suppose we wish to exclude those. We can accomplish this by adding an if-statement in the second for-loop to filter out those repeats:
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        # This is the criterion we added
        if student_name_0 != student_name_1:
            student_pairs.append(
                (student_name_0, student_name_1)
            )

student_pairs


# In[22]:


#5. Tuples
student_grade = ('Alice', 'Spanish', 'A-')
student_grade


# In[23]:


student_grade[0]


# In[24]:


#tuples are immutable.
student_grade.append('IU Bloomington')


# In[25]:


#tuples are immutable.
del student_grade[2]


# In[26]:


#tuples are immutable.
student_grade[2] = 'C'


# In[27]:


#5.2 Unpacking Tuples' immutability makes them useful for unpacking. At its simplest, tuple unpacking allows the following:
student_grade = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)


# In[28]:


student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)


# In[29]:


#Compare this to the same code using indices:
for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations', student_grade[0],
              'on getting an', student_grade[2],
              'in', student_grade[1])


# In[30]:


#6. Dictionaries -6.1 Unordered By unordered, we mean that dictionary items aren't referred to by their position, or index, in the collection. Instead, dictionary items have keys, each of which is associated with a value. Here's a very basic example:
foreign_languages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}


# In[31]:


foreign_languages['Carol']


# In[32]:


#Trying to get the value for a key that does not exist in the dictionary results in a KeyError:
foreign_languages['Zeke']


# In[33]:


#We can check if a particular key is in a dictionary with the in keyword:
'Zeke' in foreign_languages


# In[34]:


'Alice' in foreign_languages


# In[35]:


'alice' in foreign_languages


# In[36]:


# 6.2 Mutable We can add, delete, and change entries in a dictionary ,Add an entry that doesn't exist:
foreign_languages['Esther'] = 'French'
foreign_languages


# In[37]:


# Delete an entry that exists
del foreign_languages['Bob']
foreign_languages


# In[38]:


# Change an entry that does exist
foreign_languages['Esther'] = 'Italian'
foreign_languages


# In[39]:


# 6.4 Looping over dictionaries
for key in foreign_languages:
    value = foreign_languages[key]
    print(key, 'is taking', value)


# In[40]:


for key, value in foreign_languages.items():
    print(key, 'is taking', value)


# In[41]:


# 6.5 Dictionaries as records
student_grade = ('Alice', 'Spanish', 'A')


# In[42]:


# Here we know that the items in each of these tuples is a name, subject, and grade:
student_name, subject, grade = student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)


# In[43]:


#We could instead represent this data as a dictionary and use it as such. A dictionary of information describing a single item is often referred to as a record:

record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])


# In[44]:


#7. Combining Data Types ,7.1 List of tuples
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]


# In[48]:


student_grades[1]


# In[46]:


student_grades[1][2]


# In[47]:


# 7.2 List of dictionaries
student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records


# In[49]:


# Now each item in the list is a dictionary:
student_grade_records[1]


# In[50]:


# and we can work with the individual records as such:
student_grade_records[1]['grade']


# In[51]:


for record in student_grade_records:
    if record['grade'].startswith('A'):
        print('Congratulations', record['name'], 
              'on getting an', record['grade'], 
              'in', record['subject'])


# In[52]:


# 7.3 Dictionary of dictionaries
foreign_language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    foreign_language_grades[student_name] = record
    
foreign_language_grades


# In[53]:


# Now we can refer to these by student name:
foreign_language_grades['Alice']


# In[54]:


# And we can get the individual data that we care about:
foreign_language_grades['Alice']['grade']


# In[55]:


#7.4 Dictionary with tuple keys
student_course_grades = {}
for student_name, subject, grade in student_grades:
    student_course_grades[student_name, subject] = grade
    
student_course_grades


# In[56]:


# Now we can represent all of a student's grades:
student_course_grades['Alice', 'Math'] = 'A'
student_course_grades['Alice', 'History'] = 'B'


# In[57]:


student_course_grades


# In[58]:


# 7.5 Another dictionary of dictionaries
student_report_cards = {}
for student_name, subject, grade in student_grades:
    # If there is no report card for a student,
    # we need to create a blank one
    if student_name not in student_report_cards:
        student_report_cards[student_name] = {}
    student_report_cards[student_name][subject] = grade


# In[59]:


student_report_cards


# In[61]:


# The advantage of this extra work is that we can now easily have multiple grades per student:
student_report_cards['Alice']['Math'] = 'A'
student_report_cards['Alice']['History'] = 'B'


# In[62]:


student_report_cards


# In[63]:


student_report_cards['Alice']


# In[ ]:




