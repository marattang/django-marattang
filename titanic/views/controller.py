from titanic.model.dataset import Dataset
from titanic.model.service import Service

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

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        # 불필요한 feature (Cabin, Ticket) 제거
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        # norminal, ordinal로 정형화
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        # 불필요한 Name 제거
        this = service.drop_feature(this, 'Name')
        this = service.gender_nominal(this)
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('<Type Check>')
        print(f'{type(this.train["Embarked"])}')
        print(f'Train의 type은 {type(this.train)}이다.')
        print(f'Train의 column은 {this.train.columns}이다.')
        print(f'Train의 상위 5개 행은 {this.train.head()}이다.')
        print(f'Test의 type은 {type(this.test)}이다.')
        print(f'Test의 상위 5개 행은 {this.test.head()}이다.')
        print(f'Test의 column 데이터는 {this.test.columns}이다.')
        print('*'*100)
