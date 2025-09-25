import hashlib
s='jamolplus'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
