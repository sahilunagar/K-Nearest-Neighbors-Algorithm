#necessary imports

from math import sqrt             #for square root
from collections import Counter   #to find the most common group
import matplotlib.pyplot as plt   #for plotting
import warnings                   #to print the warnings

# example data with 2 groups and a key to find the group of

data = {'k':[[1,1], [1,2], [2,2]], 'r':[[4,4], [5,4], [6,5]]}
pred_key = [3,5]

# plotting data and key

for i in data:
    for j in data[i]:
        plt.scatter(j[0], j[1], color=i)
plt.scatter(pred_key[0], pred_key[1], color='b')
plt.show()

# Function to decide class of pred_key

def K_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('k is less than length of data!')
    
    distances = []
    for group in data:
        for feature in data[group]:
            euclidean_dist = sqrt((feature[0]-predict[0])**2 + (feature[1]-predict[1])**2)
            distances.append([euclidean_dist, group])
            
    votes = [i[1] for i in sorted(distances)[:k]]
    result = Counter(votes).most_common(1)[0][0]
    
    return result
  
result = K_nearest_neighbors(data, pred_key)
print('most common group for pred_key: ',result)

# plotting pred_key in the predicted group

#for i in data:
#    for j in data[i]:
#        plt.scatter(j[0], j[1], color=i)
        
[[plt.scatter(j[0],j[1], color=i) for j in data[i]] for i in data]
plt.scatter(pred_key[0], pred_key[1], color=result)
plt.show()
