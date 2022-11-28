from functools import lru_cache  
  
@lru_cache(maxsize=4)  
def get_value(key):  
  print("Cache miss with "+key)  
  return key + ":value"  
   
print(get_value("1"))  
print(get_value("2"))  
print(get_value("3"))  
print(get_value("4")) 
 
print(get_value("4"))  
print(get_value("3"))  
print(get_value("1"))  

print(get_value("7"))  
print(get_value("6"))  

print(get_value("3"))  
print(get_value("1"))  
