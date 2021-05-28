from dataclasses import dataclass


@dataclass #2칸 띄우기 PEP에 따라서
class Dataset(object):
    context: str
    fname: str
    train: str
    test: str
    id: str
    label: str

    @property
    def context(self) -> str: return self._context #getter
    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fnmae): self._fname = fnmae

    @property
    def train(self) -> str: return self._train
    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test
    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id
    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label
    @label.setter
    def label(self, label): self._label = label