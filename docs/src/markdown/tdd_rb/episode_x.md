# パフォーマンスチューニングから始めるテスト駆動開発

## 概要

[フィボナッチ数](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0)
を計算するプログラムを **テスト駆動開発** で作ります。

初めに **TODOリスト** をプログラミング作業をリストアップします。次に、最初に失敗するテストを作成します。 その後 **仮実装**
でベタ書き値を返すテストを実行します。 それから **三角測量** を使って慎重にアルゴリズムを一般化していきます。そして、
**明白な実装** によりアルゴリズムを完成させます。

アルゴリズムが完成したら **リファクタリング** を実施してコードベースを **動作するきれいなコード** に洗練していきます。

**動作するきれいなコード** になったらパフォーマンスの検証をするためパフォーマンスチューニングを実施します。 パフォーマンスチューニングでは
**プロファイラ** を使ったプログラムのボトルネック調査を実施します。アルゴリズムのパフォーマンスを改善したら別途追加したアルゴリズムと
**ベンチマーク** を実施してどのアルゴリズムを採用するかを決定します。

仕上げは、 **モジュール分割** によりRubyアプリケーションとしてリリースします。

## 仕様

仕様は以下の通りです。

> n 番目のフィボナッチ数を Fn で表すと、Fn は再帰的に
> 
> F0 = 0,
> 
> F1 = 1,
> 
> Fn + 2 = Fn + Fn + 1 (n ≧ 0)
> 
> で定義される。これは、2つの初期条件を持つ漸化式である。
> 
> この数列 (Fn)はフィボナッチ数列（フィボナッチすうれつ、（英: Fibonacci sequence）と呼ばれ、
> 
> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
> 1597, 2584, 4181, 6765, 10946, …（オンライン整数列大辞典の数列 A45） と続く。最初の二項は 0, 1
> であり、以後どの項もその直前の2つの項の和となっている。
> 
> —  Wikipedia


表形式にすると以下のようになります。

|   |   |   |   |   |   |   |    |    |    |    |    |     |     |     |     |     |      |      |    |
| - | - | - | - | - | - | - | -- | -- | -- | -- | -- | --- | --- | --- | --- | --- | ---- | ---- | -- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  | 8  | 9  | 10 | 11 | 12  | 13  | 14  | 15  | 16  | 18   | 19   | …​ |
| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | …​ |

## TODOリスト

> TODOリスト
> 
> 何をテストすべきだろうか----着手する前に、必要になりそうなテストをリストに書き出しておこう。
> 
> —  テスト駆動開発 

**TODOリスト** を書き出す取っ掛かりとして仕様で定義されている内容からプログラムで実施できる内容に分解してきましょう。
仕様では以下のように定義されているので。

|   |   |   |   |   |   |   |    |    |    |    |    |     |     |     |     |     |      |      |    |
| - | - | - | - | - | - | - | -- | -- | -- | -- | -- | --- | --- | --- | --- | --- | ---- | ---- | -- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  | 8  | 9  | 10 | 11 | 12  | 13  | 14  | 15  | 16  | 18   | 19   | …​ |
| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | …​ |

最初のタスクは `0を渡したら0を返す` 振る舞いをするプログラムを作ることにしましょう。

|   |    |
| - | -- |
| 0 | …​ |
| 0 | …​ |

同様のパターンで他のタスクも切り出してみましょう。

|   |   |    |
| - | - | -- |
| 0 | 1 | …​ |
| 0 | 1 | …​ |

|   |   |   |    |
| - | - | - | -- |
| 0 | 1 | 2 | …​ |
| 0 | 1 | 1 | …​ |

とりあえず、３件ほどタスクとして切り出したので **TODOリスト** の作成は一旦終了してプログラミング作業に入るとしましょう。

  - 0を渡したら0を返す

  - 1を渡したら1を返す

  - 2を渡したら1を返す

## 仮実装

> 仮実装を経て本実装へ
> 
> 失敗するテストを書いてから、最初に行う実装はどのようなものだろうか----ベタ書きの値を返そう。
> 
> —  テスト駆動開発 

### 0を渡したら0を返す

早速、 **TODOリスト**
の１つ目から片付けていくとしましょう。

  - **0を渡したら0を返す**

  - 1を渡したら1を返す

  - 2を渡したら1を返す

まずは最初に失敗するテストを書きますがまずは以下のサンプルコードを使ってテスティングフレームワークの動作確認をしておきましょう。今回利用するRubyのテスティングフレームワークは
[minitest](https://github.com/seattlerb/minitest) です。 `test` フォルダ以下に
`fibonacci_test.rb` ファイルを追加して以下のコードを入力します。

`test/fibonacci_test.rb`

``` ruby
# frozen_string_literal: true

require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'

class FibonacciTest < Minitest::Test
  def greeting
    'hello world'
  end

  def test_greeting
    assert_equal 'hello world', greeting
  end
end
```

今回テスト結果を見やすくするため `minitest/reporters` というgemを使っているのでまずインストールしておきます。

``` bash
$ gem install minitest-reporters
```

gemインストールが完了したらコマンドラインに `ruby test/fibonacci_test.rb`
コマンドを入力してテストを実施します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 28548

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01040s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
...
```

テストは無事実行されたようですね。続いてテストが失敗するか確認しておきましょう。 `greeting` メソッドの `hello world`
を `hello world!` に変更してテストを実行します。

``` ruby
...
class Fibonacci < Minitest::Test
  def greeting
    'hello world!'
  end
...
end
```

テストは失敗して以下のようなメッセージが表示されました。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 30787

 FAIL["test_greeting", <Minitest::Reporters::Suite:0x000055eaefeef5e0 @name="Fibonacci">, 0.003157061990350485]
 test_greeting#Fibonacci (0.00s)
        Expected: "hello world"
          Actual: "hello world!"
        test/fibonacci_test.rb:13:in `test_greeting`

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00398s
1 tests, 1 assertions, 1 failures, 0 errors, 0 skips
```

テスティングフレームワークのセットアップと動作確認が終了したので最初の失敗するテストを書きます。まずは
**アサーションファースト**　でサンプルコードを削除して以下のコードにします。

``` ruby
...
class FibonacciTest < Minitest::Test
  def test_fibonacci
    assert_equal 0, fib(0)
  end
end
```

テストは無事？失敗します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 21656

ERROR["test_fibonacci", <Minitest::Reporters::Suite:0x0000559acae8d068 @name="FibonacciTest">, 0.001314591965638101]
 test_fibonacci#FibonacciTest (0.00s)
Minitest::UnexpectedError:         NoMethodError: undefined method `fib' for #<FibonacciTest:0x0000559acae8d860>
            test/fibonacci_test.rb:9:in `test_fibonacci'`

  1/1: [========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00419s
1 tests, 0 assertions, 0 failures, 1 errors, 0 skips
```

まずは **仮実装** でテストを通すようにしましょう。

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    0
  end

  def test_fibonacci
    assert_equal 0, fib(0)
  end
end
```

テストはレッドからグリーンになりました。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 2885

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00352s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
```

テストが通ったのでバージョン管理システムにコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: 0を渡したら0を返す'
```

  - *0を渡したら0を返す*

  - 1を渡したら1を返す

  - 2を渡したら1を返す

## 三角測量

> 三角測量
> 
> テストから最も慎重に一般化を引き出すやり方はどのようなものだろうか----２つ以上の例があるときだけ、一般化を行うようにしよう。
> 
> —  テスト駆動開発 

### 1を渡したら1を返す

１つ目の **TODOリスト** を片付けたので２つ目の **TODOリスト** に取り掛かるとしましょう。

  - *0を渡したら0を返す*

  - **1を渡したら1を返す**

  - 2を渡したら1を返す

**テストファースト**　**アサーションファースト** なのでまずはテストを追加するとこから始めます。

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    0
  end

  def test_fibonacci
    assert_equal 0, fib(0)
    assert_equal 1, fib(1)
  end
end
```

テストは失敗します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 21207

 FAIL["test_fibonacci", <Minitest::Reporters::Suite:0x000056525007ccb0 @name="FibonacciTest">, 0.0014098359970375896]
 test_fibonacci#FibonacciTest (0.00s)
        Expected: 1
          Actual: 0
        test/fibonacci_test.rb:14:in `test_fibonacci`

  1/1: [========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00196s
1 tests, 2 assertions, 1 failures, 0 errors, 0 skips
```

**仮実装** で0しか返さないベタ書きのコードなのだから当然ですよね。0ならば0を返してそれ以外の場合は1を返すようにプログラムを変更します。

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?

    1
  end
...
end
```

プログラムの変更によりテストはレッドからグリーンに戻りました。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 58331

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00169s
1 tests, 2 assertions, 0 failures, 0 errors, 0 skips
```

ここでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: 1を渡したら1を返す'
```

### リファクタリング

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - 2を渡したら1を返す

次の **TODOリスト**
に着手する前にテストケース内の重複が気になり始めたので、共通部分をアサーションからくくり出して、入力値と期待値の組でテストを回すようにテストコードを
**リファクタリング** します。

``` ruby
...
class Fibonacci < Minitest::Test
...
  def test_fibonacci
    cases = [[0, 0], [1, 1]]
    cases.each do |i|
      assert_equal i[1], fib(i[0])
    end
  end
end
```

テストを実行してプログラムが壊れていないことを確認します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 5991

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00200s
1 tests, 2 assertions, 0 failures, 0 errors, 0 skips
```

プログラムが壊れていないことが確認できたのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: アルゴリズムの置き換え'
```

### 1を渡したら2を返す

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - **2を渡したら1を返す**

テストコードの　**リファクタリング** を実施したので続いて　**TODOリスト** の３つ目に着手します。まずは **アサーション**
の追加ですね。

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?

    1
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1]]
    cases.each do |i|
      assert_equal i[1], fib(i[0])
    end
  end
end
```

おや、今回はプロダクトコードを変更しなくてもテストは通るようです。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 26882

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00287s
1 tests, 3 assertions, 0 failures, 0 errors, 0 skips
```

ここでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: 1を渡したら2を返す'
```

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - *2を渡したら1を返す*

## 明白な実装

> 明白な実装
> 
> シンプルな操作を実現するにはどうすればいいだろうか----そのまま実装しよう。
> 
> 仮実装や三角測量は、細かく細かく刻んだ小さなステップだ。だが、ときには実装をどうすべきか既に見えていることが。
> そのまま進もう。例えば先ほどのplusメソッドくらいシンプルなものを仮実装する必要が本当にあるだろうか。
> 普通は、その必要はない。頭に浮かんだ明白な実装をただ単にコードに落とすだけだ。もしもレッドバーが出て驚いたら、あらためてもう少し歩幅を小さくしよう。
> 
> —  テスト駆動開発 

### 3を渡したら2を返す

最初に定義した **TODOリスト**
の内容は完了しましたがプログラムの一般化にはまだテストケースが足りないでしょう。3を渡した場合のテストケースを追加します。

|   |   |   |   |    |
| - | - | - | - | -- |
| 0 | 1 | 2 | 3 | …​ |
| 0 | 1 | 1 | 2 | …​ |

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - *2を渡したら1を返す*

  - **3を渡したら2を返す**

テストケースを追加してテストを実施します。

``` ruby
...
class FibonacciTest < Minitest::Test
...
  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2]]
    cases.each do |i|
      assert_equal i[1], fib(i[0])
    end
  end
end
```

テストが失敗しました。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 7598

 FAIL["test_fibonacci", <Minitest::Reporters::Suite:0x000055c987498120 @name="FibonacciTest">, 0.00104286998976022]
 test_fibonacci#FibonacciTest (0.00s)
        Expected: 2
          Actual: 1
        test/fibonacci_test.rb:17:in `block in test_fibonacci''
        test/fibonacci_test.rb:16:in `each'
        test/fibonacci_test.rb:16:in `test_fibonacci'

  1/1: [========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00160s
1 tests, 4 assertions, 1 failures, 0 errors, 0 skips
```

2までは1を返すので条件分岐を追加します。

``` ruby
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n <= 2

    1
  end
...
end
```

まだ、失敗したままです。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 26066

 FAIL["test_fibonacci", <Minitest::Reporters::Suite:0x0000562bc96ee330 @name="Fibonacci">, 0.0055934099946171045]
 test_fibonacci#Fibonacci (0.01s)
        Expected: 2
          Actual: 1
        test/fibonacci_test.rb:24:in `block in test_fibonacci'
        test/fibonacci_test.rb:23:in `each'
        test/fibonacci_test.rb:23:in `test_fibonacci''

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00882s
1 tests, 4 assertions, 1 failures, 0 errors, 0 skips
```

どの条件にも該当としない場合は2を返すように変更します。

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n <= 2

    2
  end
...
end
```

グリーンになりました。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 25117

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01680s
1 tests, 4 assertions, 0 failures, 0 errors, 0 skips
```

ここでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: 3を渡したら2を返す'
```

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - *2を渡したら1を返す*

  - *3を渡したら2を返す*

### フィボナッチ数計算

そろそろゴールが見えてきました。**TODOリスト** を追加してフィボナッチ数計算アルゴリズムを完成させましょう。

|   |   |   |   |   |    |
| - | - | - | - | - | -- |
| 0 | 1 | 2 | 3 | 4 | …​ |
| 0 | 1 | 1 | 2 | 3 | …​ |

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - *2を渡したら1を返す*

  - *3を渡したら2を返す*

  - **4を渡したら3を返す**

**テストファースト** **アサートファースト** です。

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n <= 2

    2
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3]]
    cases.each do |i|
      assert_equal i[1], fib(i[0])
    end
  end
end
```

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 34595

 FAIL["test_fibonacci", <Minitest::Reporters::Suite:0x0000564fdbd6dfe0 @name="Fibonacci">, 0.005386559059843421]
 test_fibonacci#Fibonacci (0.01s)
        Expected: 3
          Actual: 2
        test/fibonacci_test.rb:24:in `block in test_fibonacci'
        test/fibonacci_test.rb:23:in `each'
        test/fibonacci_test.rb:23:in `test_fibonacci''

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01030s
1 tests, 5 assertions, 1 failures, 0 errors, 0 skips
```

最後に2を返すのではなく合計値をかえすのだから

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n <= 2

    1 + 1
  end
...
end
```

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 10848

 FAIL["test_fibonacci", <Minitest::Reporters::Suite:0x00005621247c9f48 @name="Fibonacci">, 0.0007573128677904606]
 test_fibonacci#Fibonacci (0.00s)
        Expected: 3
          Actual: 2
        test/fibonacci_test.rb:24:in `block in test_fibonacci'
        test/fibonacci_test.rb:23:in `each'
        test/fibonacci_test.rb:23:in `test_fibonacci''

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00130s
1 tests, 5 assertions, 1 failures, 0 errors, 0 skips
```

一つ前の `fib` の結果を足すのだから

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n <= 2

    fib(n - 1) + 1
  end
...
end
```

グリーンになりました。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 25629

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00467s
1 tests, 5 assertions, 0 failures, 0 errors, 0 skips
```

ここでコミット。。。しないで今回は更に進めます。 **TODOリスト** を追加します。

|   |   |   |   |   |   |    |
| - | - | - | - | - | - | -- |
| 0 | 1 | 2 | 3 | 4 | 5 | …​ |
| 0 | 1 | 1 | 2 | 3 | 5 | …​ |

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - *2を渡したら1を返す*

  - *3を渡したら2を返す*

  - *4を渡したら3を返す*

  - **5を渡したら5を返す**

テストケースを追加して

``` ruby
...
class FibonacciTest < Minitest::Test
...
  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], fib(i[0])
    end
  end
end
```

レッド

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 54754

 FAIL["test_fibonacci", <Minitest::Reporters::Suite:0x000055c42397e108 @name="Fibonacci">, 0.00174815789796412]
 test_fibonacci#Fibonacci (0.00s)
        Expected: 5
          Actual: 4
        test/fibonacci_test.rb:24:in `block in test_fibonacci'
        test/fibonacci_test.rb:23:in `each'
        test/fibonacci_test.rb:23:in `test_fibonacci''

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00237s
1 tests, 6 assertions, 1 failures, 0 errors, 0 skips
```

結局1つ前と2つ前の `fib` の結果を合計して返しているのだから

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n <= 2

    fib(n - 1) + fib(n - 2)
  end
...
end
```

グリーン

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 8399

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00107s
1 tests, 6 assertions, 0 failures, 0 errors, 0 skips
```

一般化ができたので0の場合と1の場合は与えらた値を返せば良くなったので

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n == 1

    fib(n - 1) + fib(n - 2)
  end
...
end
```

リファクター

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 42476

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00162s
1 tests, 6 assertions, 0 failures, 0 errors, 0 skips
```

フィボナッチ数計算アルゴリズムが完成したのでコミットします。

``` bash
$ git add .
$ git commit -m 'feat: フィボナッチ数計算'
```

  - *0を渡したら0を返す*

  - *1を渡したら1を返す*

  - *2を渡したら1を返す*

  - *3を渡したら2を返す*

  - *4を渡したら3を返す*

  - *5を渡したら5を返す*

## リファクタリング

> リファクタリング(名詞) 外部から見たときの振る舞いを保ちつつ、理解や修正が簡単になるように、ソフトウェアの内部構造を変化させること。
> 
> —  リファクタリング(第2版) 

> リファクタリングする(動詞) 一連のリファクタリングを適用して、外部から見た振る舞いの変更なしに、ソフトウェアを再構築すること。
> 
> —  リファクタリング(第2版 

アルゴリズムの実装は出来ましたがアプリケーションとしては不十分なので **リファクタリング** を適用してコードを
**動作するきれいなコード** に洗練していきます。

### クラスの抽出

まず、テストケース内でメソッドを定義していますがこれでは一つのクラスでアルゴリズムの実行とテストの実行という２つの責務を
`FibonacciTest` クラスが担当しています。 **単一責任の原則** に違反しているので **クラスの抽出**
を実施して責務を分担させましょう。

``` ruby
...
class FibonacciTest < Minitest::Test
  def fib(n)
    return 0 if n.zero?
    return 1 if n == 1

    fib(n - 1) + 1
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], fib(i[0])
    end
  end
end
```

`Fibonacci` クラスを作成して **クラスメソッド** の `Fibonacci.fib` をコピー＆ペーストで作成します。

``` ruby
...
class Fibonacci
  def self.fib(n)
    return 0 if n.zero?
    return 1 if n == 1

    fib(n - 1) + fib(n - 2)
  end
end

class FibonacciTest < Minitest::Test
  def self.fib(n)
    return 0 if n.zero?
    return 1 if n == 1

    fib(n - 1) + fib(n - 2)
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], fib(i[0])
    end
  end
end
```

テストが壊れていないことを確認したら `FibonacciTest` クラス内の **クラスメソッド** `FIbonacciTest.fib`
を削除して **フィクスチャー** `setup` メソッドを作成して **インスタンス変数** `@fib` に `Fibonacci`
クラスの参照を代入します。

``` ruby
...
class Fibonacci
  def self.fib(n)
    return 0 if n.zero?
    return 1 if n == 1

    fib(n - 1) + fib(n - 2)
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.fib(i[0])
    end
  end
end
```

テストが壊れていないかを確認します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 40694

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00393s
1 tests, 6 assertions, 0 failures, 0 errors, 0 skips
```

**クラスの抽出** の **リファクタリング** 適用が完了したのでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: クラスの抽出'
```

### 変数名の変更

続いて、 `Fibonacci` クラスに移動した **クラスメソッド** ですが引数が `n` というのは分かりづらいですね。

``` ruby
...
class Fibonacci
  def self.fib(n)
    return 0 if n.zero?
    return 1 if n == 1

    fib(n - 1) + fib(n - 2)
  end
end
...
```

ここは省略せず、引数の型を表す名前に変更して可読性を上げておきましょう。

``` ruby
...
class Fibonacci
  def self.fib(number)
    return 0 if number.zero?
    return 1 if number == 1

    fib(number - 1) + fib(number - 2)
  end
end
...
```

テストが壊れていないか確認します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 37760

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00744s
1 tests, 6 assertions, 0 failures, 0 errors, 0 skips
```

コミットします。

``` bash
$ git add .
$ git commit -m 'refactor: 変数名の変更'
```

### メソッド名の変更

`Fibonacci` クラスの **クラスメソッド** `Fibonacci.fib`
はフィボナッチ数を計算するメソッドですが名前が紛らわしいので
**メソッド名の変更** を適用します。

``` ruby
...
class Fibonacci
  def self.fib(number)
    return 0 if number.zero?
    return 1 if number == 1

    fib(number - 1) + fib(number - 2)
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.fib(i[0])
    end
  end
end
```

**インスタンスメソッド** を `fib` から `calc` に変更します。今回は呼び出し先の `FibonacciTest`
のテストコードも修正する必要があります。

``` ruby
...
class Fibonacci
  def self.calc(number)
    return 0 if number.zero?
    return 1 if number == 1

    calc(number - 1) + calc(number - 2)
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.calc(i[0])
    end
  end
end
```

テストが壊れていないか確認します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 15099

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00285s
1 tests, 6 assertions, 0 failures, 0 errors, 0 skips
```

**メソッド名の変更** の適用が完了したのでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: メソッド名の変更'
```

## パフォーマンスチューニング

> 心がけるべきことは、他のパフォーマンス分析とおなじように、実際のデータを使い、リアルな利用パターンを試し、プロファイリングを行ってからでないと、パフォーマンスを問題にする資格はない、ということだ。
> 
> —  テスト駆動開発 

これまでのテストケースでは小さな値を使ってきましたが大きな値の場合のプログラムの挙動が問題無いか確認しておく必要があります
[１００番目までのフィボナッチ数列](http://www.suguru.jp/Fibonacci/Fib100.html)
を参考に大きな値の場合のテストケースを追加してアプリケーションのパフォーマンスを検証しましょう。

### メモ化によるパフォーマンス改善

**TODOリスト** に新しいタスクを追加します。

|   |   |    |          |          |           |    |
| - | - | -- | -------- | -------- | --------- | -- |
| 0 | 1 | …​ | 38       | 39       | 40        | …​ |
| 0 | 1 | …​ | 39088169 | 63245986 | 102334155 | …​ |

  - 大きな数値を計算する

テストケースを追加します。

``` ruby
...
class FibonacciTest < Minitest::Test
...
  def test_large_number
    assert_equal 102_334_155, @fib.calc(40)
  end
end
```

テストを実行します

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 1160

  2/2: [=========================================] 100% Time: 00:00:51, Time: 00:00:51

Finished in 51.15914s
2 tests, 7 assertions, 0 failures, 0 errors, 0 skips
```

テストが完了するのが随分遅くなってしまいました。これはアルゴリズムを改善する必要がありそうです。 まずは **プロファイラ**
を使って実行状況を確認します。今回は
[profileライブラリ](https://docs.ruby-lang.org/ja/latest/library/profile.html)
を使います。

``` bash
$ ruby -r profile test/fibonacci_test.rb
Started with run options --seed 42383

  2/1: [======================                      ] 50% Time: 00:00:00,  ETA: 00:00:00
```

処理が終わらないようなら `ctr-c` で強制終了すれば結果が出力されます。出力内容の `Fibonacci.calc`
がフィボナッチ数計算メソッド実行部分です。

``` bash
...
  %   cumulative   self              self     total
 time   seconds   seconds    calls  ms/call  ms/call  name
192.39    25.50     25.50        2 12750.69 12750.69  Thread::Queue#pop
 75.32    35.49      9.98   246940     0.04     1.65  Fibonacci.calc
....
```

再帰呼び出しが何度も実行された結果パフォーマンスを低下させているようです。ここは
[メモ化](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%A2%E5%8C%96)
を使ってパフォーマンスを改善させましょう。

``` ruby
...
class Fibonacci
  def self.calc(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= calc(number - 1, memo) + calc(number - 2, memo)
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.calc(i[0])
    end
  end

  def test_large_number
    assert_equal 102_334_155, @fib.calc(40)
  end
end
```

**プロファイラ** で確認します。

``` bash
$ ruby -r profile test/fibonacci_test.rb
Started with run options --seed 20468

  2/2: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.04214s
2 tests, 7 assertions, 0 failures, 0 errors, 0 skips
  %   cumulative   self              self     total
 time   seconds   seconds    calls  ms/call  ms/call  name
...
 12.09     0.06      0.06        2    32.09    32.09  Thread::Queue#pop
...
  1.33     0.26      0.01      105     0.07     1.41  Fibonacci.calc
...
```

一気に再帰呼び出し回数が減りパフォーマンスを改善することが出来ましたのでコミットします。

``` bash
$ git add .
$ git commit -m 'perf: メモ化によるパフォーマンス改善'
```

## ベンチマーク

続いて、異なるフィボナッチ数計算アルゴリズムを実装してどのアルゴリズムを採用するべきかを
[ベンチマーク](https://ja.wikipedia.org/wiki/%E3%83%99%E3%83%B3%E3%83%81%E3%83%9E%E3%83%BC%E3%82%AF)
を取って判断したいと思います。

### ループ処理による実装

まずはループ処理によるフィボナッチ数計算のアルゴリズムを実装します。以下が **テストファースト** **アサートファースト**
で作成したコードです。

``` ruby
...
class Fibonacci
  def self.calc(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= calc(number - 1, memo) + calc(number - 2, memo)
  end

  def self.calc2(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |i|
      a = b
      b = c
      c = a + b
    end
    c
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.calc(i[0])
    end
  end

  def test_large_number
    assert_equal 102_334_155, @fib.calc(40)
  end

  def test_large_number_calc2
    assert_equal 102_334_155, @fib.calc2(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rb -n test_large_number_calc2 Started with run options -n test_large_number_calc2 --seed 18167

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00123s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
```

テストが通ることを確認したらコミットします。

``` bash
$ git add .
$ git commit -m 'feat: ループ処理による実装'
```

### 一般項による実装

[フィボナッチ数列の一般項](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0#%E4%B8%80%E8%88%AC%E9%A0%85)
で定義されているのでこれを **テストファースト** **アサートファースト** で実装します。

``` ruby
...
class Fibonacci
  def self.calc(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= calc(number - 1, memo) + calc(number - 2, memo)
  end

  def self.calc2(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |i|
      a = b
      b = c
      c = a + b
    end
    c
  end

  def self.calc3(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.calc(i[0])
    end
  end

  def test_large_number
    assert_equal 102_334_155, @fib.calc(40)
  end

  def test_large_number_calc2
    assert_equal 102_334_155, @fib.calc2(40)
  end

  def test_large_number_calc3
    assert_equal 102_334_155, @fib.calc3(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rb -n test_large_number_calc3
Started with run options -n test_large_number_calc3 --seed 55659

  1/1: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00111s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
```

テストが壊れていないか確認したらコミットします。

``` bash
$ git add .
$ git commit -m 'feat: 一般項による実装'
```

### メソッド名の変更

各アルゴリズムのメソッド名が `calc` では分かりづらいので **メソッド名の変更** を適用して **リファクタリング** します。

``` ruby
...
class Fibonacci
  def self.recursive(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= recursive(number - 1, memo) + recursive(number - 2, memo)
  end

  def self.calc2(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |i|
      a = b
      b = c
      c = a + b
    end
    c
  end

  def self.calc3(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.recursive(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @fib.recursive(40)
  end

  def test_large_number_calc2
    assert_equal 102_334_155, @fib.calc2(40)
  end

  def test_large_number_calc3
    assert_equal 102_334_155, @fib.calc3(40)
  end
end
```

まず、最初に実装した再帰呼び出しアルゴリズムのメソッド名を `Fibonacci.calc` から `Fibonacci.recursive`
に変更します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 15174

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00137s
4 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

続いて、ループアルゴリズムのメソッド名を `Fibonacci.calc2` から `Fibonacci.loop` に変更します。

``` ruby
class Fibonacci
  def self.recursive(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= recursive(number - 1, memo) + recursive(number - 2, memo)
  end

  def self.loop(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |i|
      a = b
      b = c
      c = a + b
    end
    c
  end

  def self.calc3(number)
    a = ((1 + Math.sqrt(5)) / 2) ** number
    b = ((1 - Math.sqrt(5)) / 2) ** number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.recursive(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @fib.recursive(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @fib.loop(40)
  end

  def test_large_number_calc3
    assert_equal 102_334_155, @fib.calc3(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 28586

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00188s
4 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

最後に、一般項アルゴリズムのメソッド名を `Fibonacci.calc3` から `Fibonacci.general_term`
に変更します。

``` ruby
...
class Fibonacci
  def self.recursive(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= recursive(number - 1, memo) + recursive(number - 2, memo)
  end

  def self.loop(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |i|
      a = b
      b = c
      c = a + b
    end
    c
  end

  def self.general_term(number)
    a = ((1 + Math.sqrt(5)) / 2) ** number
    b = ((1 - Math.sqrt(5)) / 2) ** number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.recursive(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @fib.recursive(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @fib.loop(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @fib.general_term(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 42729

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00736s
4 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

変更によりテストが壊れていないことを確認したらコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: メソッド名の変更'
```

### サブクラスによるタイプコードの置き換え 1

現在の `Fibonacci`
クラスはアルゴリズムを追加する場合クラスを編集する必要があります。その際に既存のアルゴリズムを壊してしまう可能性があります。これは
**オープン・クローズド原則** に違反しているので **サブクラスによるタイプコードの置き換え** を適用してアルゴリズムを
**カプセル化** して、安全に追加・変更できる設計に **リファクタリング** します。

``` ruby
...
class Fibonacci
  def self.recursive(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= recursive(number - 1, memo) + recursive(number - 2, memo)
  end

  def self.loop(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |_i|
      a = b
      b = c
      c = a + b
    end
    c
  end

  def self.general_term(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciRecursive
  def calc(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= calc(number - 1, memo) + calc(number - 2, memo)
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
    @recursive = FibonacciRecursive.new
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @recursive.calc(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @recursive.calc(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @fib.loop(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @fib.general_term(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 12762

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00130s
4 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

まず、**クラスの抽出** により再帰呼び出しアルゴリズムの **メソッドオブジェクト** `FibonacciRecursive`
クラスを作成して テスト **フィクスチャー** で **インスタンス化** して **インスタンス変数**
にオブジェクトの参照を代入します。ここではメソッドの呼び出しが `exec`
に変更されているのでテストコードもそれに合わせて変更します。

``` ruby
...
class Fibonacci
  def self.loop(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |_i|
      a = b
      b = c
      c = a + b
    end
    c
  end

  def self.general_term(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciRecursive
  def exec(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= exec(number - 1, memo) + exec(number - 2, memo)
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
    @recursive = FibonacciRecursive.new
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @recursive.exec(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @recursive.exec(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @fib.loop(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @fib.general_term(40)
  end
end
```

まだ、 仕掛ですがコードが壊れていない状態でコミットをしておきます。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): サブクラスによるタイプコードの置き換え'
```

### サブクラスによるタイプコードの置き換え 2

続いて、 **メソッドオブジェクト** `FibonacciLoop` クラスを抽出します。

``` ruby
...
class Fibonacci
  def self.general_term(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciRecursive
  def exec(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= exec(number - 1, memo) + exec(number - 2, memo)
  end
end

class FibonacciLoop
  def exec(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |_i|
      a = b
      b = c
      c = a + b
    end
    c
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
    @recursive = FibonacciRecursive.new
    @loop = FibonacciLoop.new
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @recursive.exec(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @recursive.exec(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @loop.exec(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @fib.general_term(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rbStarted with run options --seed 33171

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00337s
4 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

コミットします。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): サブクラスによるタイプコードの置き換え'
```

### サブクラスによるタイプコードの置き換え 3

続いて、 **メソッドオブジェクト** `FibonacciGeneralTerm` クラスを抽出します。

``` ruby
...
class Fibonacci
end

class FibonacciRecursive
  def exec(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= exec(number - 1, memo) + exec(number - 2, memo)
  end
end

class FibonacciLoop
  def exec(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |_i|
      a = b
      b = c
      c = a + b
    end
    c
  end
end

class FibonacciGeneralTerm
  def exec(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci
    @recursive = FibonacciRecursive.new
    @loop = FibonacciLoop.new
    @general_term = FibonacciGeneralTerm.new
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @recursive.exec(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @recursive.exec(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @loop.exec(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @general_term.exec(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rbStarted with run options --seed 65058

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01576s
4 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

コミットします。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): サブクラスによるタイプコードの置き換え'
```

### サブクラスによるタイプコードの置き換え 4

最後に、 `Fibonacci` クラスに **Strategyパターン** を適用して各アルゴリズムの実行を **委譲** します。

[Strategy
パターン](https://ja.wikipedia.org/wiki/Strategy_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)

    abstract class Protocol {
    }
    Protocol <--r Fibonacci
    Protocol <|-- FibonacciRecursive
    Protocol <|-- FibonacciLoop
    Protocol <|-- FibonacciGeneralTerm
    
    class Fibonacci {
    -algorithm
    exec()
    }
    class FibonacciRecursive {
    exec()
    }
    class FibonacciLoop {
    exec()
    }
    class FibonacciGeneralTerm {
    exec()
    }

``` ruby
...
class Fibonacci
  def initialize(algorithm)
    @algorithm = algorithm
  end

  def exec(number)
    @algorithm.exec(number)
  end
end

class FibonacciRecursive
  def exec(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= exec(number - 1, memo) + exec(number - 2, memo)
  end
end

class FibonacciLoop
  def exec(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |_i|
      a = b
      b = c
      c = a + b
    end
    c
  end
end

class FibonacciGeneralTerm
  def exec(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end

class FibonacciTest < Minitest::Test
  def setup
    @recursive = Fibonacci.new(FibonacciRecursive.new)
    @loop = Fibonacci.new(FibonacciLoop.new)
    @general_term = Fibonacci.new(FibonacciGeneralTerm.new)
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @recursive.exec(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @recursive.exec(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @loop.exec(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @general_term.exec(40)
  end
end
```

**サブクラスによるタイプコードの置き換え** の適用が完了したのでコメントから `(WIP)` を外してコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: サブクラスによるタイプコードの置き換え'
```

### ファイル分割

続いてテストとアプリケーションを分割します。 `lib` ディレクトリを作成して `fibonacci.rb`
ファイルを追加してアプリケーションコード部分をカット＆ペーストします。

`lib/fibonacci.rb`

``` ruby
# frozen_string_literal: true

# Fibonacci Calcultor
class Fibonacci
  def initialize(algorithm)
    @algorithm = algorithm
  end

  def exec(number)
    @algorithm.exec(number)
  end
end

# Fibonacci Recursive algorithm
class FibonacciRecursive
  def exec(number, memo = {})
    return 0 if number.zero?
    return 1 if number == 1

    memo[number] ||= exec(number - 1, memo) + exec(number - 2, memo)
  end
end

# Fibonacci Loop algorithm
class FibonacciLoop
  def exec(number)
    a = 0
    b = 1
    c = 0
    (0...number).each do |_i|
      a = b
      b = c
      c = a + b
    end
    c
  end
end

# Fibonacci General Term algorithm
class FibonacciGeneralTerm
  def exec(number)
    a = ((1 + Math.sqrt(5)) / 2)**number
    b = ((1 - Math.sqrt(5)) / 2)**number
    ((a - b) / Math.sqrt(5)).round
  end
end
```

続いて、分割した `fibonacci.rb` ファイル内に定義されたクラスを読み込むようにテストクラスを修正します。 ファイルの読み込みには
`require` を使います。

`test/fibonacci_test.rb`

``` ruby
# frozen_string_literal: true

require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fibonacci'

class FibonacciTest < Minitest::Test
  def setup
    @fib = Fibonacci.new(FibonacciRecursive.new)
    @recursive = Fibonacci.new(FibonacciRecursive.new)
    @loop = Fibonacci.new(FibonacciLoop.new)
    @general_term = Fibonacci.new(FibonacciGeneralTerm.new)
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @fib.calc(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @recursive.calc(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @loop.calc(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @general_term.calc(40)
  end
end
```

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 39723

  4/4: [==========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00227s
4 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

分割したファイルからクラスが読み込まれテストが通ることを確認したらコミットします。

``` bash
$ git add .
$ git commit -m 'feat: ファイル分割'
```

### ベンチマークの実施

**ベンチマーク** を実施する準備が出来たので `test` ディレクトリに以下の `fibonacci_benchmark.rb`
ファイルを追加します。

`test/fibonacci_benchmark.rb`

``` ruby
# frozen_string_literal: true

require 'minitest'
require 'minitest/autorun'
require 'minitest/benchmark'
require './lib/fibonacci'

class FibonacciTestBenchmark < Minitest::Benchmark
  def setup
    @recursive = Fibonacci.new(FibonacciRecursive.new)
    @loop = Fibonacci.new(FibonacciLoop.new)
    @general_term = Fibonacci.new(FibonacciGeneralTerm.new)
  end

  def bench_recursive
    assert_performance_constant do |_n|
      1000.times do |i|
        @recursive.exec(i)
      end
    end
  end

  def bench_loop
    assert_performance_constant do |_n|
      1000.times.each do |i|
        @loop.exec(i)
      end
    end
  end

  def bench_general_term
    assert_performance_constant do |_n|
      1000.times.each do |i|
        @general_term.exec(i)
      end
    end
  end
end
```

**ベンチマーク** を実行します。

``` bash
$ ruby test/fibonacci_benchmark.rb
Run options: --seed 1009

# Running:

bench_recursive  0.438420        0.436003        0.437170        0.453267        0.428123
.bench_loop      0.157816        0.160366        0.159504        0.160275        0.162165
.bench_general_term      0.001215        0.001200        0.001255        0.001204      0.001184
.

Finished in 3.074021s, 0.9759 runs/s, 0.9759 assertions/s.

3 runs, 3 assertions, 0 failures, 0 errors, 0 skips
```

結果を見たところ、再帰処理アルゴリズムが一番遅く、一般項アルゴリズムが一番早く実行されるようです。

**ベンチマーク** を実施してアルゴリズムの性能を比較できたのでコミットします。

``` bash
$ git add .
$ git commit -m 'perf: ベンチマークの実施'
```

## モジュール分割

### アプリケーションのリリース

**動作するきれいなコード** をリリースするにあたってクラスモジュールごとにファイル分割して **エントリーポイント**
からアプリケーションを実行できるようにしたいと思います。

    /
      |--lib/
          |
           -- fibonacci.rb
      |--test/
          |
           -- fibonacci_test.rb
           -- fibonacci_benchmark.rb

まず、 `lib` に `fibonacci` フォルダを追加します。クラスモジュールは `Fibonacci` の **名前空間**
で管理するようにします。

`lib/fibonacci/command.rb`

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci Calcultor
  class Command
    def initialize(algorithm)
      @algorithm = algorithm
    end

    def exec(number)
      @algorithm.exec(number)
    end
  end
end
```

`lib/fibonacci/recursive.rb`

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci Recursive algorithm
  class Recursive
    def exec(number, memo = {})
      return 0 if number.zero?
      return 1 if number == 1

      memo[number] ||= exec(number - 1, memo) + exec(number - 2, memo)
    end
  end
end
```

`lib/fibonacci/loop.rb`

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci Loop algorithm
  class Loop
    def exec(number)
      a = 0
      b = 1
      c = 0
      (0...number).each do |_i|
        a = b
        b = c
        c = a + b
      end
      c
    end
  end
end
```

`lib/fibonacci/general_term.rb`

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci General Term algorithm
  class GeneralTerm
    def exec(number)
      a = ((1 + Math.sqrt(5)) / 2)**number
      b = ((1 - Math.sqrt(5)) / 2)**number
      ((a - b) / Math.sqrt(5)).round
    end
  end
end
```

`fibonacci.rb` は分割したクラスモジュールを読み込むエントリーポイントに変更します。

`lib/fibonacci.rb`

``` ruby
# frozen_string_literal: true

require './lib/fibonacci/command'
require './lib/fibonacci/recursive'
require './lib/fibonacci/loop'
require './lib/fibonacci/general_term'
```

**名前空間** を変更して呼び出すクラスが変わったのでテストとベンチマークを修正します。

``` ruby
...
require './lib/fibonacci'

class FibonacciTest < Minitest::Test
  def setup
    @recursive = Fibonacci.new(FibonacciRecursive.new)
    @loop = Fibonacci.new(FibonacciLoop.new)
    @general_term = Fibonacci.new(FibonacciGeneralTerm.new)
  end
...
```

まず、テストを修正してテストが通ることを確認します。

``` ruby
...
require './lib/fibonacci'

class FibonacciTest < Minitest::Test
  def setup
    @recursive = Fibonacci::Command.new(Fibonacci::Recursive.new)
    @loop = Fibonacci::Command.new(Fibonacci::Loop.new)
    @general_term = Fibonacci::Command.new(Fibonacci::GeneralTerm.new)
  end
...
```

``` ruby
...
require './lib/fibonacci'

class FibonacciTestBenchmark < Minitest::Benchmark
  def setup
    @recursive = Fibonacci.new(FibonacciRecursive.new)
    @loop = Fibonacci.new(FibonacciLoop.new)
    @general_term = Fibonacci.new(FibonacciGeneralTerm.new)
  end
...
```

続いてベンチマークを修正して実行できることを確認します。

``` ruby
...
require './lib/fibonacci'

class FibonacciTestBenchmark < Minitest::Benchmark
  def setup
    @recursive = Fibonacci::Command.new(Fibonacci::Recursive.new)
    @loop = Fibonacci::Command.new(Fibonacci::Loop.new)
    @general_term = Fibonacci::Command.new(Fibonacci::GeneralTerm.new)
  end
...
```

仕上げはコマンドラインから実行できるようにします。 ルート直下に `main.rb` を追加して以下のコードを追加します。 ここでは
**ベンチマーク** で一番良い結果の出た一般項のアルゴリズムを使うことにします。

`main.rb`

``` ruby
require './lib/fibonacci'

number = ARGV[0].to_i
command = Fibonacci::Command.new(Fibonacci::GeneralTerm.new)
puts command.exec(number)
```

コマンドラインから引数に番号を指定して実行します。

``` bash
$ ruby main.rb 0
0
$ ruby main.rb 1
1
$ ruby main.rb 2
1
$ ruby main.rb 3
2
$ ruby main.rb 4
3
```

アプリケーションの完成したのでコミットします。

``` bash
$ git add .
$ git commit -m 'feat: モジュール分割'
```

### アプリケーションの構成

    package Fibonacci {
      abstract class Protocol {
      }
      Protocol <--r Command
      Protocol <|-- Recursive
      Protocol <|-- Loop
      Protocol <|-- GeneralTerm
    }
    main --> Command
    
    package Fibonacci {
      class Command {
      -algorithm
      exec()
      }
      class Recursive {
      exec()
      }
      class Loop {
      exec()
      }
      class GeneralTerm {
      exec()
      }
    }

    /main.rb
      |--lib/
          |
           -- fibonacci.rb
         fibonacci/
          |
           -- command.rb
           -- general_term.rb
           -- loop.rb
           -- recursive.rb
      |--test/
          |
           -- fibonacci_test.rb
           -- fibonacci_benchmark.rb

**/main.rb.**

``` ruby
require './lib/fibonacci'

number = ARGV[0].to_i
command = Fibonacci::Command.new(Fibonacci::GeneralTerm.new)
puts command.exec(number)
```

**/lib/fibonacci.rb.**

``` ruby
# frozen_string_literal: true

require './lib/fibonacci/command'
require './lib/fibonacci/recursive'
require './lib/fibonacci/loop'
require './lib/fibonacci/general_term'
```

**/lib/fibonacci/command.rb.**

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci Calcultor
  class Command
    def initialize(algorithm)
      @algorithm = algorithm
    end

    def exec(number)
      @algorithm.exec(number)
    end
  end
end
```

**/lib/fibonacci/recursive.rb.**

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci Recursive algorithm
  class Recursive
    def exec(number, memo = {})
      return 0 if number.zero?
      return 1 if number == 1

      memo[number] ||= exec(number - 1, memo) + exec(number - 2, memo)
    end
  end
end
```

**/lib/fibonacci/loop.rb.**

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci Loop algorithm
  class Loop
    def exec(number)
      a = 0
      b = 1
      c = 0
      (0...number).each do |_i|
        a = b
        b = c
        c = a + b
      end
      c
    end
  end
end
```

**/lib/fibonacci/general\_term.rb.**

``` ruby
# frozen_string_literal: true

module Fibonacci
  # Fibonacci General Term algorithm
  class GeneralTerm
    def exec(number)
      a = ((1 + Math.sqrt(5)) / 2)**number
      b = ((1 - Math.sqrt(5)) / 2)**number
      ((a - b) / Math.sqrt(5)).round
    end
  end
end
```

**/test/fibonacci\_test.rb.**

``` ruby
# frozen_string_literal: true

require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fibonacci'

class FibonacciTest < Minitest::Test
  def setup
    @recursive = Fibonacci::Command.new(Fibonacci::Recursive.new)
    @loop = Fibonacci::Command.new(Fibonacci::Loop.new)
    @general_term = Fibonacci::Command.new(Fibonacci::GeneralTerm.new)
  end

  def test_fibonacci
    cases = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5]]
    cases.each do |i|
      assert_equal i[1], @recursive.exec(i[0])
    end
  end

  def test_large_number_recursive
    assert_equal 102_334_155, @recursive.exec(40)
  end

  def test_large_number_loop
    assert_equal 102_334_155, @loop.exec(40)
  end

  def test_large_number_general_term
    assert_equal 102_334_155, @general_term.exec(40)
  end
end
```

**/test/fibonacci\_benchmark.rb.**

``` ruby
# frozen_string_literal: true

require 'minitest'
require 'minitest/autorun'
require 'minitest/benchmark'
require './lib/fibonacci'

class FibonacciTestBenchmark < Minitest::Benchmark
  def setup
    @recursive = Fibonacci::Command.new(Fibonacci::Recursive.new)
    @loop = Fibonacci::Command.new(Fibonacci::Loop.new)
    @general_term = Fibonacci::Command.new(Fibonacci::GeneralTerm.new)
  end

  def bench_recursive
    assert_performance_constant do |_n|
      1000.times do |i|
        @recursive.exec(i)
      end
    end
  end

  def bench_loop
    assert_performance_constant do |_n|
      1000.times.each do |i|
        @loop.exec(i)
      end
    end
  end

  def bench_general_term
    assert_performance_constant do |_n|
      1000.times.each do |i|
        @general_term.exec(i)
      end
    end
  end
end
```
