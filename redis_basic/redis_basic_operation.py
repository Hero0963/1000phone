# ref= https://tw511.com/a/01/34723.html
# ref= https://xken831.pixnet.net/blog/post/533610970-%5Bpython%5D%5Bredis%5D


import redis

conn = redis.Redis(host='127.0.0.1', port=6379)
# 可以使用url方式連線到資料庫
# conn = Redis.from_url('redis://@localhost:6379/1')
conn.set('name', 'LinWOW')
print(conn.get('name'))
