# official site
https://docs.djangoproject.com/en/4.1/topics/cache/#the-low-level-cache-api
https://docs.djangoproject.com/en/4.1/topics/cache/
from django.core.cache import cache, caches
        
        
# find all keys
from django.core.cache.backends import locmem
print(locmem._caches)

from django.core.cache.backends import locmem
>>> all_keys = [item.replace(':1:', '')  for item in dict(locmem._caches['']).keys()]
['my_key', 'my_key2', 'my_key1']

>>> from django.core.cache import caches
>>> 
>>> caches['default'].make_key('test-key')
':1:test-key'
>>> 
>>> caches['default'].make_and_validate_key('my_key')
':1:my_key'



## Basic usage, The basic interface is:

from django.core.cache import cache, caches
cache.set(key, value, timeout=DEFAULT_TIMEOUT, version=None)
>>> cache.set('my_key', 'hello, world!', 30)

cache.get(key, default=None, version=None)
>>> cache.get('my_key')
'hello, world!'

# Wait 30 seconds for 'my_key' to expire...
>>> cache.get('my_key')
None


## add or set method
cache.add(key, value, timeout=DEFAULT_TIMEOUT, version=None)¶
To add a key only if it doesn’t already exist, use the add() method. 
It takes the same parameters as set(), but it will not attempt to update the cache if the key specified is already present:

>>> cache.set('add_key', 'Initial value')
>>> cache.add('add_key', 'New value')
>>> cache.get('add_key')
'Initial value'


## get or get_or_set method
cache.get_or_set(key, default, timeout=DEFAULT_TIMEOUT, version=None)¶
If you want to get a key’s value or set a value if the key isn’t in the cache, there is the get_or_set() method. It takes the same parameters as get() but the default is set as the new cache value for that key, rather than returned:

>>> cache.get('my_new_key')  # returns None
>>> cache.get_or_set('my_new_key', 'my new value', 100)
'my new value'

>>> import datetime
>>> cache.get_or_set('some-timestamp-key', datetime.datetime.now)
datetime.datetime(2014, 12, 11, 0, 15, 49, 457920)


## get_many and set_many method
cache.get_many(keys, version=None)¶
There’s also a get_many() interface that only hits the cache once. get_many() returns a dictionary with all the keys you asked for that actually exist in the cache (and haven’t expired):

>>> cache.set('a', 1)
>>> cache.set('b', 2)
>>> cache.set('c', 3)
>>> cache.get_many(['a', 'b', 'c'])
{'a': 1, 'b': 2, 'c': 3}

cache.set_many(dict, timeout)¶
To set multiple values more efficiently, use set_many() to pass a dictionary of key-value pairs:

>>> cache.set_many({'a': 1, 'b': 2, 'c': 3})
>>> cache.get_many(['a', 'b', 'c'])
{'a': 1, 'b': 2, 'c': 3}


# delete and delete_many method
cache.delete(key, version=None)¶
You can delete keys explicitly with delete() to clear the cache for a particular object:

>>> cache.delete('a')
True


cache.delete_many(keys, version=None)¶
If you want to clear a bunch of keys at once, delete_many() can take a list of keys to be cleared:

>>> cache.delete_many(['a', 'b', 'c'])


## clear, touch incr, decr,close method
cache.clear()
Finally, if you want to delete all the keys in the cache, use cache.clear(). Be careful with this; clear() will remove everything from the cache, not just the keys set by your application.
>>> cache.clear()

cache.touch(key, timeout=DEFAULT_TIMEOUT, version=None)¶
cache.touch() sets a new expiration for a key. For example, to update a key to expire 10 seconds from now:
>>> cache.touch('a', 10)
True

cache.incr(key, delta=1, version=None)¶
cache.decr(key, delta=1, version=None)

>>> cache.set('num', 1)
>>> cache.incr('num')
2
>>> cache.incr('num', 10)
12
>>> cache.decr('num')
11
>>> cache.decr('num', 5)
6

cache.close()
You can close the connection to your cache with close() if implemented by the cache backend.
>>> cache.close()


## Cache versioning

>>> # Set version 2 of a cache key
>>> cache.set('my_key', 'hello world!', version=2)
>>> # Get the default version (assuming version=1)
>>> cache.get('my_key')
None
>>> # Get version 2 of the same key
>>> cache.get('my_key', version=2)
'hello world!'

The version of a specific key can be incremented and decremented using the incr_version() and decr_version() methods. This enables specific keys to be bumped to a new version, leaving other keys unaffected. Continuing our previous example:

>>> # Increment the version of 'my_key'
>>> cache.incr_version('my_key')
>>> # The default version still isn't available
>>> cache.get('my_key')
None
# Version 2 isn't available, either
>>> cache.get('my_key', version=2)
None
>>> # But version 3 *is* available
>>> cache.get('my_key', version=3)
'hello world!'




#Caching in REST Framework
https://www.django-rest-framework.org/api-guide/caching/

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):
    # With cookie: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def list(self, request, format=None):
        content = {
            'user_feed': request.user.get_user_feed()
        }
        return Response(content)


class ProfileView(APIView):
    # With auth: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, request, format=None):
        content = {
            'user_feed': request.user.get_user_feed()
        }
        return Response(content)


class PostView(APIView):
    # Cache page for the requested url
    @method_decorator(cache_page(60*60*2))
    def get(self, request, format=None):
        content = {
            'title': 'Post title',
            'body': 'Post content'
        }
        return Response(content)

NOTE: The cache_page decorator only caches the GET and HEAD responses with status 200.




