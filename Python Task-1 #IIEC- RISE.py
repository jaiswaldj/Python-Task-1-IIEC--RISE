#!/usr/bin/env python
# coding: utf-8

# # Python Task-1 #IIEC- RISE

# In[1]:


import os


# In[2]:


APPLICATIONS = ['Notepad', 'Paint', 'Calculator', 'Explorer', 'Task Manager', 'Control Panel',                'Windows Media Player', 'Chrome Browser', 'WordPad']
COMMANDS = ['notepad', 'mspaint', 'calc','explorer', 'taskmgr', 'control',            'Program Files (x86)\\Windows Media Player\\wmplayer.exe', 'start chrome', 'write']


# In[3]:


print('Enter option number to launch a option:')
if os.sys.platform == 'win32' or os.sys.platform == 'win64':
      pass
else:
      print('Sorry we don\'t support this platform')
      exit()


# In[4]:


for i, j in enumerate(APPLICATIONS):
            print("{0}. {1}".format(i,j))


# In[ ]:


while(True):
      user_input = int(input())
      if user_input == 0:
            os.system(COMMANDS[0])
      elif user_input == 1:
            os.system(COMMANDS[1])
      elif user_input == 2:
            os.system(COMMANDS[2])
      elif user_input == 3:
            os.system(COMMANDS[3])
      elif user_input == 4:
            os.system(COMMANDS[4])
      elif user_input == 5:
            os.system(COMMANDS[5])
      elif user_input == 6:
            os.system("cd ../.. & cd \"Program Files (x86)\"/\"Windows Media Player\"/ & start wmplayer.exe")
      elif user_input == 7:
            os.system(COMMANDS[7])
      elif user_input == 8:
            os.system(COMMANDS[8])


# In[ ]:





# In[ ]:




