import pyshorteners as py
link = 'https://varchasaaggarwal.herokuapp.com'

s=pysh.Shortener()
print(s.tinyurl.short(link))
