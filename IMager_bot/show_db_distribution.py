from secrets import choice
import matplotlib.pyplot as plt

from IMager.imager.db_handler import ImagerDB as IDB
from settings.config import topics

if __name__ == '__main__':
    idb = IDB()
    topic_choice = list(topics.values())
    print('Выберите таблицу:')
    for topic_id, topic_name in enumerate(topic_choice):
        print(topic_id + 1, topic_name)
    choice_id = 0
    while not (0 <= choice_id - 1 < len(topic_choice)):
        choice_id = int(input())
    images = idb.get_images(topic_choice[choice_id - 1])
    xs = list()
    ys = list()
    zs = list()
    colors = list()
    for image in images:
        r = image[0]
        g = image[1]
        b = image[2]
        xs.append(r)
        ys.append(g)
        zs.append(b)
        colors.append((r / 255, g / 255, b / 255))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, c=colors)
    plt.show()
