from titanic.model.dataset import Dataset
from titanic.model.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Plot(object):

    dataset = Dataset()
    service = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)

    def draw_survived_dead(self):
        this = self.entity
        # print(f'Train의 type은 {type(this)}이다.')
        # print(f'Train의 column은 {type(this.columns)}이다.')
        # print(f'Train의 상위 5개 데이터는 {this.head()}이다.')
        # print(f'Train의 하위 5개 데이터는 {this.tail()}이다.')
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f', ax=ax[0], shadow=True)
        ax[0].set_title('0. 사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 1. 생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def draw_pclass(self):
        this = self.entity
        this['생존결과'] = this['Survived']\
            .replace(0, '사망자').replace(1, '생존자')
        this['Pclass'] = this['Pclass'].replace(1, '1등석').replace(2, '2등석').replace(3, '3등석')
        sns.countplot(data=this, x='Pclass', hue='생존결과')
        plt.show()

    def draw_sex(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존 비율 0.사망자 1.생존자')
        ax[1].set_title('여성의 생존 비율 0.사망자 1.생존자')

        plt.show()

    def draw_embarked(self):
        this = self.entity
        this['승선항구'] = this['Embarked']\
            .replace("C", "쉘버그").replace("S", "사우스햄톤").replace("Q", "퀸즈타운")
        this['생존결과'] = this['Survived']\
            .replace(0, '사망자').replace(1, '생존자')
        sns.countplot(data=this, x='승선항구', hue='생존결과')
        plt.show()
'''
Train의 type은 <class 'pandas.core.frame.DataFrame'>이다.
Train의 column은 <class 'pandas.core.indexes.base.Index'>이다.
Train의 상위 5개 데이터는    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]이다.
Train의 하위 5개 데이터는      PassengerId  Survived  Pclass  ...   Fare Cabin  Embarked
886          887         0       2  ...  13.00   NaN         S
887          888         1       1  ...  30.00   B42         S
888          889         0       3  ...  23.45   NaN         S
889          890         1       1  ...  30.00  C148         C
890          891         0       3  ...   7.75   NaN         Q

[5 rows x 12 columns]이다.
0.Exit 1.data visualization
2. modeling
 3. machine learning
4. machine release
'''