#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
 f_path = "/Library/Fonts/Arial Unicode.ttf"

font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)
print("Hangul font is set!")


# In[ ]:





# In[ ]:




