# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'dev/jupyter/sample'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # PythonでTDD
# 
# 
# ## 仕様
# 
# >1 から 100 までの数をプリントするプログラムを書け。 
# 
# >ただし 3 の倍数のときは数の代わりに｢Fizz｣と、
# 
# >5 の倍数のときは｢Buzz｣とプリントし、
# 
# >3 と 5 両方の倍数の場合には｢FizzBuzz｣とプリントすること。
# 
# ## 設計
# 
# ### TODO リスト
# 
# -  1 から 100 まで数をプリントできるようにする。
# -  3 の倍数のときは数の代わりに｢Fizz｣をプリントできるようにする。
# -  5 の倍数のときは｢Buzz｣とプリントできるようにする。
# -  3 と 5 両方の倍数の場合には｢FizzBuzz｣とプリントできるようにする。

#%%
import unittest

def fizz_buzz(number):
    return 'Fizz'

class FizzBuzzTest(unittest.TestCase):
    def test3の倍数のときはFizzを出す(self):
        self.assertEqual(fizz_buzz(3),'Fizz')


unittest.main(argv=['first-arg-is-ignored'],exit=False)


