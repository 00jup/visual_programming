import requests

hamlet_url = "http://ruby.bastardsbook.com/files/fundamentals/hamlet.txt"
response = requests.get(hamlet_url)
dictionary = {}

for element in response.text.split():
    if element:
        dictionary[element] = dictionary.get(element, 0) + 1

sorted_dictionary = dict(sorted(
    dictionary.items(), key=lambda x: x[1], reverse=True))

with open("web_result.csv", 'w') as f:
    for key, value in sorted_dictionary.items():
        f.write(f"{key},{value}\n")


# soup = BeautifulSoup(response.content, "html.parser")

# tag = soup.select_one('html > body > pre style')
# for string in tag.strings:
#     print(string)
