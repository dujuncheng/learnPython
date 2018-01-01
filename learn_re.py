# encode = 'utf-8'

import re

pattern = 'hello'

text1 = 'hello'

pattern = re.compile(pattern)

res = re.match(pattern, text1)

print(res.re)
