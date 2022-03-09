#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello from Jupyter')


# In[2]:


my_str='hello'
my_int=16
print(my_str)
print(my_int)


# In[3]:


#print by variable name
my_str


# In[4]:


#print by variable name , this method just display last variable
my_str
my_int


# In[5]:


#condition
numberOfAppeles=5
if numberOfAppeles<1:
    print('you hav no apples')
elif numberOfAppeles==1:
    print('you have one apple')
elif numberOfAppeles<4:
    print('you have a few apple') 
else:
    print('you hav many apples')


# In[6]:


#Lists
student_names=['Alic','Bob','Carol','Dave']
student_names[1]


# In[7]:


student_names[0]


# In[8]:


student_names[-1]


# In[9]:


student_names[0:2]


# In[10]:


student_names[1:3]


# In[11]:


student_names[:2]


# In[12]:


student_names[2:]


# In[13]:


#List is mutable : list can be changed
student_names.append('Esther')
student_names


# In[14]:


student_names.insert(2,'Xavier')
student_names


# In[15]:


del student_names[2]
student_names


# In[16]:


#List is non-unique
student_names.append('Esther')
student_names.append('Esther')
student_names


# In[18]:


#Loop
for student_name in student_names:
    print('hello '+student_name+'!')


# In[19]:


# Initialize an empty list and add to it the student names containing more than 4 characters
long_names=[]
for student_name in student_names:
    if len(student_name)>4:
        long_names.append(student_name)
long_names       


# In[23]:


#nested loops
student_pairs=[]
for student_name0 in student_names:
    for student_name1 in student_names:
        student_pairs.append((student_name0,student_name1))
student_pairs        


# In[24]:


student_pairs[0]


# In[25]:


# list has no repeats
student_pairs=[]
for student_name0 in student_names:
    for student_name1 in student_names:
        if student_name0!=student_name1:
            student_pairs.append((student_name0,student_name1))
student_pairs 


# In[26]:


#Tuples
student_grade=('Alice','Spanish','A')
student_grade


# In[27]:


#Tuples is immutable
student_grade.append('IU Bloomington')


# In[28]:


#Tuples is immutable
del student_grade[2]


# In[30]:


#Tuples is immutable
student_grade[2]='C'


# In[31]:


#Unpacking
student_name,subject,grade=student_grade
print(student_name)
print(subject)
print(grade)


# In[33]:


student_grades=[
    ('Alice','Spanish','A'),
    ('Bob','French','C'),
    ('Carol','Italian','B+'),
    ('Dave','Italian','A-'),
]
for student_name,subject,grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations',student_name,
             'on getting an', grade,
              'in', subject)


# In[34]:


for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations',student_name,
             'on getting an', grade,
              'in', subject)


# In[35]:


#Dictionaries
foriegn_languages={
    'Alice':'Spanish',
    'Bob':'French',
    'Carol':'Italian',
    'Dave':'Italian',
}


# In[36]:


foriegn_languages['Carol']


# In[37]:


#KeyError:key not exist
foriegn_languages['Zake']


# In[38]:


#check if a particular key exist
'Zake' in foriegn_languages


# In[39]:


'Alice' in foriegn_languages


# In[40]:


'alice' in foriegn_languages


# In[41]:


#dictionary is mutable
foriegn_languages['Esther']='French'
foriegn_languages


# In[42]:


del foriegn_languages['Bob']
foriegn_languages


# In[43]:


foriegn_languages['Esther']='Italian'
foriegn_languages


# In[44]:


for key in foriegn_languages:
    value=foriegn_languages[key]
    print(key, 'is taking', value)


# In[46]:


for key,value in foriegn_languages.items():
    print(key, 'is taking', value)


# In[47]:


student_name,subject,grade=student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)


# In[49]:


record={
    'name':'Alice',
    'subject':'Spanish',
    'grade':'A',
}
print(record['name'], 'gor a grad of', record['grade'], 'in', record['subject'])


# In[50]:


#list of tuples
student_grades=[
    ('Alice','Spanish','A'),
    ('Bob','French','C'),
    ('Carol','Italian','B+'),
    ('Dave','Italian','A-'),
]


# In[51]:


student_grades[1]


# In[52]:


student_grades[1][2]


# In[57]:


#list of dictionaries
student_grade_records=[]
for student_name,subject,grade in student_grades:#student_grades is list of tuples
    record={
        'name':student_name,
        'subject':subject,
        'grade':grade,
    }
    student_grade_records.append(record)
student_grade_records


# In[58]:


student_grade_records[1]


# In[60]:


student_grade_records[1]['grade']


# In[64]:


for record in student_grade_records:
    if record['grade'].startswith('A'):
        print('congratulations', record['name'], 
               'on gitting an', record['grade'], 'in', record['subject'])


# In[66]:


#dictionary of dictionaries
foriegn_language_grades={}
for name,subject,grade in student_grades:
    record={
        'subject':subject,
        'grade':grade,
    }
    foriegn_language_grades[name]=(record)
foriegn_language_grades


# In[67]:


foriegn_language_grades['Alice']


# In[68]:


foriegn_language_grades['Alice']['grade']


# In[69]:


#dictionary with tuple keys
student_course_grade={}
for name,subject,grade in student_grades:
    student_course_grade[name,subject]=grade
student_course_grade


# In[70]:


student_course_grade['Alice','Math']='A'
student_course_grade['Alice','History']='B'
student_course_grade


# In[74]:


student_report_cards={}
for name,subject,grade in student_grades:
    if name not in student_report_cards:
            student_report_cards[name]={}
    student_report_cards[name][subject]=grade  

student_report_cards


# In[75]:


student_report_cards['Alice']['Math']='A'
student_report_cards['Alice']['History']='B'
student_report_cards


# In[76]:


student_report_cards['Alice']


# In[ ]:




