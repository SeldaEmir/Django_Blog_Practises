from __future__ import unicode_literals


word = ["A Hole in the Fence","A Common Man","Fox who got cought in the tree trunk","A Merchant and his Donkey","Friends","The Milk maid and her Pail","True Wealth"]
meaning = ["Once when a lion, the king of the jungle, was asleep, a little mouse began running up and down on him. This soon awakened the lion, who placed his huge paw on the mouse, and opened his big jaws to swallow him.",
            "Forgive me this time. I shall never repeat it and I shall never forget your kindness. And who knows, I may be able to do you a good turn one of these days!",
            "The lion was so tickled by the idea of the mouse being able to help him that he lifted his paw and let him go.",
            "Sometime later, a few hunters captured the lion, and tied him to a tree. After that they went in search of a wagon, to take him to the zoo.",
            "Sometimes, we are not content with what we have, and wish for more. Such discontentment always results in unhappiness, and regret.",
            "Once upon a time, a man and his wife had the good fortune to have a goose which laid a golden egg every day. Lucky though they were, they soon began to think they were not getting rich fast enough.",
            "Young Johnny had a very kind and generous uncle. Every time Johnny visited him with his parents, he was given five cents. One day, Johnny thought of buying a bike. The next time he met his uncle, he asked him for 50 dollars."]
entrylist=[]

for i in range(0, len(word)):
    entrylist.append((word[i],meaning[i]))