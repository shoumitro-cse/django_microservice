from collections import OrderedDict  


class LRUCache:
	
	def __init__(self, size):
		self.size = size
		self.lru_cache = OrderedDict()
	
	def get(self, key):
		try:
			value = self.lru_cache.pop(key)
			self.lru_cache[key] = value
			return value
		except KeyError:
			return -1
	
	def put(self, key, value):
		try:
			self.lru_cache.pop(key) # # remove key item
		except KeyError:
			if len(self.lru_cache) >= self.size:
				self.lru_cache.popitem(last=False) # remove first item
		self.lru_cache[key] = value
	
	def display_caches(self):
		print(self.lru_cache)

lru = LRUCache(3)

lru.put("1","1")  
lru.put("2","2")  
lru.put("3","3")  
   
lru.get("1")  
lru.get("3")  
   
lru.put("4","4")   
lru.display_caches()   
lru.put("5","5")   
lru.display_caches()  


"""
Explanation

Let's breakdown the code -

We created a cache that can hold the three items.
1. The cache.put('1', '1') function stored 1 at last in OrderedDict and same cache.put('2', '2') and cache.put('3', '3'). 
   Now the elements are stored as [1, 2, 3].
2. When the cache.get('1') is called, 1 is removed from the front and added to last. Now the elements are stored as [2, 3, 1].
3. When the cache.get('3') is called, 3 is removed from the middle and added to last. Now the elements are stored as [2, 1, 3].
4. When we called cache.put('4', '4'), removed from the front and added in last, now the elements are stored as [1, 3, 4].
5. When we called cache.put('5', '5'), removed from the front and added in last, finally, the elements are stored as [3, 4, 5].
"""

		
