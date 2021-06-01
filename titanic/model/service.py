from titanic.model.dataset import Dataset
from pandas import Series, DataFrame
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
        return this.train.drop("Survived", axis=1) #생사여부 제외 return

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] #생사여부만 return

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train["Embarked"] = this.train["Embarked"].map({'S':1, 'C':2, 'Q':3})
        # map함수를 사용해 S : 1, C: 2, Q : 3

        return this

    @staticmethod
    def fare_band_fill_na(this) -> object:
        return this

    @staticmethod
    def title_nominal(this) -> object:
        # this.train = this.train.fillna({"Name": 0})
        # this.test = this.test.fillna({"Name": 0})
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].fillna(0)
            dataset['Sex'] = dataset['Sex'].map(gender_mapping)
            dataset.rename(columns={"Sex": "Gender"}, inplace=True)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        return this

    @staticmethod
    def create_k_fold(this) -> object:
        return
    