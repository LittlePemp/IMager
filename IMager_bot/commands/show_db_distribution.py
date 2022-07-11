import matplotlib.pyplot as plt
from IMager.db_handler import ImagerDB as IDB

idb = IDB()
tables = idb.get_tables()
print('Выберите таблицу:')
for topic_id, topic_name in enumerate(tables):
    print(f'{topic_id}: {topic_name}')
choice_id = input()
while not (choice_id.isdigit() and (0 <= int(choice_id) < len(tables))):
    print('Введите предложенный вариант')
    choice_id = input()
choice_id = int(choice_id)
images = idb.get_images(tables[choice_id])
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
