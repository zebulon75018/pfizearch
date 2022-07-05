import multidict as multidict

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
import pprint

with open('json_data.json', 'r') as f:
    data = json.load(f)

result ={}
for d in data["word"].keys():
    count = 0
    for n in data["word"][d].keys():
        count = count + data["word"][d][n]
    result[d] = count

fullTermsDict = multidict.MultiDict()
for t in result.keys():
    fullTermsDict.add(t, result[t])

x, y = np.ogrid[:300, :300]

#mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
#mask = 255 * mask.astype(int)


#wc = WordCloud(background_color="white", repeat=True, mask=mask)
wc = WordCloud(background_color="white", max_words=20000, repeat=False,width=800,height=800)
wc.generate_from_frequencies(fullTermsDict)
wc.to_file("cloud.png")

#plt.axis("off")
#plt.imshow(wc, interpolation="bilinear")
#plt.show()

