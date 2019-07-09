# 1. select the number of clusters to be identified
#   i.e select a value for k = 3 in this case
# 2. randomly select 3 distinct data point
# 3. measure the distance between the first point and selected 3 cluster
# 4. assing the first point ro nearest cluster
# 5. calculate the mean value including the new point for the red cluster

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
#mathplotlib inline

def assigment(df, centroids):
    #define color
    colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'y'}
    #melakukan pengulangan sebanyak centroids
    for i in centroids.keys():
        #sqrt((x1-x2)^2 - (y1-y2)^2) mengukur jarak masing2 titik kepada semua centroids
        df['distance_from_{}'.format(i)] = (
            np.sqrt((df['x'] - centroids[i][0]) ** 2 + (df['y'] - centroids[i][1]) ** 2)
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()] #menampung header dari cols\
    #mengambil header indeks terkecil dari suatu titik
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    #melakukan substring pada header indeks terkecil dan menyimpannya dalam bentuk map
    df['closest'] = df['closest'].map(lambda x : int(x.lstrip('distance_from_')))
    #menentukan color untuk setiap titik
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

def update(k):
    for i in centroids.keys():
        #menghitung rata2 dari titik centroid terdekat
        centroids[i][0] = np.mean(df[df['closest']==i]['x'])
        centroids[i][1] = np.mean(df[df['closest']==i]['y'])
    return k
csvFile = open('df.csv','r')
reader = pd.read_csv(csvFile)
df = reader
# df = pd.DataFrame({
#     'x' : [12,20,28,18,29,33,24,45,45,52,51,52,55,53,55,61,64,69,72],
#     'y' : [39,36,30,52,54,46,55,59,63,70,66,63,58,23,14,8,19,7,24]
# })

np.random.seed()
k = 4
# centroids[i] = [x,y] mengambil 3 titik secara random
centroids = {
    i+1: [np.random.randint(0,80), np.random.randint(0, 80)] for i in range(k)
}
print(centroids)
#menentukan jarak titik ke setiap centroid
df = assigment(df, centroids)
print(df)
#mengupdate data centroids
centroids = update(centroids)
# print(centroids)

while True:
    #menyimpan data df ke centroid
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assigment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

#setup gui
fig = plt.figure(figsize=(5,5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
colmap = {1: 'r', 2: 'g', 3: 'b', 4:'y'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0,80)
plt.ylim(0,80)
plt.show()

# ax = plt.axes()
# for i in old_centroids.keys():
#     old_x = old_centroids[i][0]
#     old_y = old_centroids[i][1]
#     dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
#     dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
#     ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
    





