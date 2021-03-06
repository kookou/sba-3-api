from dataclasses import dataclass
import os
import pandas as pd
@dataclass
class FileReader:
    # def __init__(self, context, fname, train, test, id, label):
    #     self._context = context  # _ 1개는 default 접근, _ 2개는 private 접근

    # 3.7부터 간소화되서 dataclass 데코 후, key: value 형식으로 써도 됨 (롬복 형식)
    context : str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id : str = ''
    lable : str = ''

    def new_file(self) -> str:
        return os.path.join(self.context,self.fname)

    def csv_to_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='UTF-8', thousands=',')

    