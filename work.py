import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("data_new.txt", sep = "\t")
#print (df)
i = len(df.index)
'''
select_indices = list(np.where(df["word"] == "####")[0])


for j in select_indices:
    #print(df.iloc[j:j+1,1:2])
    for k in range(0,8):
        df.iloc[j:j+1,k:k+1] = "####"
        
#print (df)

indexes_to_keep = set(range(df.shape[0])) - set(select_indices)
df = df.take(list(indexes_to_keep))

#print (df_new)

select_indices = list(np.where(df["prev_word"] == "####")[0])
for j in select_indices:
    df.iloc[j:j+1,1:2] = ""

select_indices = list(np.where(df["next_word"] == "####")[0])
for j in select_indices:
    df.iloc[j:j+1,2:3] = ""
    
select_indices = list(np.where(df["label"] == "####")[0])
for j in select_indices:
    df.iloc[j:j+1,3:4] = ""
    
select_indices = list(np.where(df["prev_label"] == "####")[0])
for j in select_indices:
    df.iloc[j:j+1,4:5] = ""
    
select_indices = list(np.where("next_label" == "####")[0])
for j in select_indices:
    df.iloc[j:j+1,5:6] = ""
    
select_indices = list(np.where(df["prev_tag"] == "####")[0])
for j in select_indices:
    df.iloc[j:j+1,6:7] = ""
    
#select_indices = list(np.where(df["prev_word"] == "####")[0])
#for j in select_indices:
#    df.iloc[j:j+1,7:8] = ""
    
df.to_csv("final_data.txt", sep = '\t')    
    


#print (df)
df = pd.read_csv("final_data.txt", sep = '\t')

length = len(df.index)


print (df.iloc[5:6, 0:1].values[0] == '#')
print (all(df.iloc[5:6, 0:1] == '#'))

print (length)

for j in range(0,length):
    if df.iloc[j:j+1, 0:1].values[0] == '#':
           df.iloc[j:j+1, 8:9] = 1
           df.iloc[j:j+1, 9:10] = 0
    elif df.iloc[j:j+1, 0:1].values[0] == '@':
        df.iloc[j:j+1, 8:9] = 1
        df.iloc[j:j+1, 9:10] = 0
    elif df.iloc[j:j+1, 0:1].values[0] == '$':
        df.iloc[j:j+1, 8:9] = 0
        df.iloc[j:j+1, 9:10] = 1
    else:
        df.iloc[j:j+1, 8:9] = 0
        df.iloc[j:j+1, 9:10] = 0

print (df)
df.to_csv("final_data.txt", sep = '\t')
'''  
d1 = pd.read_csv("visual.txt", sep = '\t')
#plt.figure()
#d1.plot(x = 'tag', y = 'word',kind = 'bar')
d2 = pd.read_csv("visual_l.txt", sep = '\t', index_col = 'label')
#plt.figure()
#d2.plot(x = 'label', y = 'word', kind = 'bar')
#df.plot()
ax = d2.word.plot(kind = 'bar')
percent = ["{}%".format("%.2f" % float(100.*row.word/20450)) for name,row in d2.iterrows()]
#percent1 = [float(i) for i in percent]
#percent1 = [round(elem,2) for elem in percent1]
for i,child in enumerate(ax.get_children()[:d2.index.size]):
    ax.text(i,child.get_bbox().y1+200,percent[i], horizontalalignment ='center')
plt.show()
    
    
    
    
    