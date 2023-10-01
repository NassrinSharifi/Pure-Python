import torch
from torch import nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


class HousingModel(nn.Module):
    def __init__(self, hidden_layer1_size, hidden_layer2_size):
        super(HousingModel, self).__init__()
        self.hide1 = nn.Linear(12, hidden_layer1_size)
        self.act1 = nn.ReLU()
        self.hide2 = nn.Linear(hidden_layer1_size, hidden_layer2_size)
        self.act2 = nn.ReLU()
        self.out = nn.Linear(hidden_layer2_size, 1)
        # self.act3 = nn.ReLU()

    def forward(self, x):
        x = self.hide1(x)
        x = self.act1(x)
        x = self.act2(self.hide2(x))
        x = self.out(x)
        return x


class DataLoader:
    def __init__(self, data):
        self.data = data

    def data_prepare(self, random_state):
        data_x = self.data.iloc[:, 1:].values
        data_y = self.data.iloc[:, 0].values
        # data_x =torch.tensor(data_x , dtype=torch.float32)
        # data_y =torch.tensor(data_y , dtype=torch.float32).reshape(-1,1)
        train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.2, random_state=random_state)
        val_x, test_x, val_y, test_y = train_test_split(test_x, test_y, test_size=0.5, random_state=random_state)
        scale = MinMaxScaler(feature_range=(0, 1))
        train_x = scale.fit_transform(train_x)
        val_x, test_x = scale.transform(val_x), scale.transform(test_x)
        train_x = torch.tensor(train_x, dtype=torch.float32)
        val_x = torch.tensor(val_x, dtype=torch.float32)
        test_x = torch.tensor(test_x, dtype=torch.float32)
        train_y = torch.tensor(train_y, dtype=torch.float32).reshape(-1, 1)
        val_y = torch.tensor(val_y, dtype=torch.float32).reshape(-1, 1)
        test_y = torch.tensor(test_y, dtype=torch.float32).reshape(-1, 1)
        return train_x, train_y, val_x, val_y, test_x, test_y
