import pandas as pd

from titanic.model.dataset import Dataset
from titanic.model.service import Service
from sklearn.ensemble import RandomForestClassifier

class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        print(f'this train : {this.train}')
        print(f'this label : {this.label}')
        return this # 데이터프레임

    def learning(self, train, test):
        this = self.modeling(train, test)
        print(f'사이킷 런의 SVC 알고리즘 정확도 {self.service.accuracy_by_svm(this)} %')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.train)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Age', 'Fare', 'Cabin', 'Ticket', 'Name')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('<Type Check>')
        print(f'{type(this.train["Embarked"])}')
        print(f'Train의 type은 {type(this.train)}이다.')
        print(f'Train의 column은 {this.train.columns}이다.')
        print(f'Train의 상위 5개 행은 {this.train.head()}이다.')
        print(f'Train의 null의 갯수 {this.train.isnull().sum()}이다.')
        print(f'Test의 type은 {type(this.test)}이다.')
        print(f'Test의 상위 5개 행은 {this.test.head()}이다.')
        print(f'Test의 column 데이터는 {this.test.columns}이다.')
        print(f'Test의 null의 갯수 {this.test.isnull().sum()}이다.')
        print('*'*100)
