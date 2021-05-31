from titanic.model.dataset import Dataset
import pandas as pd


class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        # 원래 값은 dictionary지만, datafrmae으로 전환해서 return함. csv파일은 내부적으로 딕셔너리다.
        # 그래서 데이터 프레임으로 전환해주어야 함.
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop("Survived", axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.train.drop([feature], axis = 1)
        return this