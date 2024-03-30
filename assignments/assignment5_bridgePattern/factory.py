f=Factory('myhouse.json')
data = f.get()

for i in data:
    # for j in data[i]:
    #     print(j, data[i][j])
    #     print('-----------------')
    print(i, data[i])