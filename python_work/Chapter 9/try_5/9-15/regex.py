import re

pattern = "duct"
text = "The production is going very smoothly!"

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom "{}" to "{}" ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))
