#!/usr/bin/env python
# coding: utf-8

# # Thermometer

# Convert temperature in Celsius to Fahrenheit using Python

# In[1]:


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,2)

print(fahrenheit_to_celsius(100))


# Convert celsius to Fahrenheit

# In[2]:


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)

print(celsius_to_fahrenheit(37.78))


# In[ ]:




