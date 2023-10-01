import torch
from torch import nn
from torch import optim
import NN_Class as nc
import pandas as pd
from sklearn.metrics import r2_score
r=[]
data = pd.read_csv("Housing.csv")

# print(data)
data.replace("yes", 1, inplace=True)
data.replace("no", 0, inplace=True)
data.replace("unfurnished", 0, inplace=True)
data.replace("semi-furnished", 0.5, inplace=True)
data.replace("furnished", 1, inplace=True)
data = nc.DataLoader(data)
for _ in range(10):

    train_x, train_y, val_x, val_y, test_x, test_y = data.data_prepare(None)
# hyperparameters
# for hidden2 in range(1,13):
#     for hidden1 in range(hidden2, 13):
# for learning_rate in range(100, 10001,100): #13.5
# for batch_size in range(10,50,5):
# for n_epochs in [100,200,300]:
    hidden1 = 6
    hidden2 = 5
    n_epochs = 100
    batch_size = 10
    learning_rate = 0.67
    # learning_rate /= 10000

    model = nc.HousingModel(hidden1, hidden2)
    loss_fun = nn.MSELoss()
    # loss_fun = nn.L1Loss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    # optimizer = optim.RMSprop(model.parameters(), lr=learning_rate)

    for epoch in range(n_epochs):
        for i in range(0, len(train_x), batch_size):
            train_x_batch = train_x[i: i + batch_size]
            train_y_batch = train_y[i: i + batch_size]
            train_predict = model(train_x_batch)

            loss = loss_fun(train_predict, train_y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # print((f"epoch {epoch} , latest loss {loss}"))

    with torch.no_grad():
        model.eval()
        validation = model(val_x)
        validation_loss = loss_fun(validation, val_y)
        r2 = r2_score(validation, val_y)
        print(f"batch = {batch_size}")
        print(f"n_epochs = {n_epochs}")
        print(f"learning rate = {learning_rate}")
        print(f"hidd = {hidden1} , {hidden2}")  # 4,4   12,10
        print(f"validation rate: {r2}")
        r.append([r2, learning_rate])


print(max(r))

