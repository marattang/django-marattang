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
        return this # 데이터프레임

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train의 type은 {type(this.train)}이다.')
        print(f'Train의 column은 {this.test.columns}이다.')
        print(f'Test의 type는 {type(this.train)}이다.')
        print(f'Test의 column 데이터는 {this.test.columns}이다.')
        return this