# はじめに

# 値オブジェクト

## ユーザーストーリー

まず **ユーザーストーリー**
> をもとに仕様を整理します。

> ユーザーストーリーとは、ソフトウェアシステムに求められるふるまいをまとめたものだ。アジャイルソフトウェア開発の世界で広く使われており、大量の機能を細かく分解して計画作りに生かせるようにしている。
> 同じような概念を表す用語としてフィーチャーという言い方もあるが、
> 最近のアジャイル界隈では「ストーリー」とか「ユーザーストーリー」とかいう用語のほうが広まっている。
> 
> —  Martin Fowler's Bliki (ja) <https://bliki-ja.github.io/UserStory> 

SNS(ソーシャルネットワークサービス)のユーザー機能ということなので以下の **ユーザーストーリー** を作成しました。

    利用者として
    ユーザーを管理できるようにしたい
    なぜならユーザーはシステムを利用するために必要だから

## TODOリスト

**ユーザーストーリー** を作成したらそれをもとに **TODOリスト** を作成します。  
**TODOリスト** はプログラムとして実行できる粒度で具体的に記述します。

  - ❏ ユーザーを管理できるようにする
    
      - ❏ ユーザーを登録する
        
          - ❏ IDと名前を持ったユーザーを作成する

## 仮実装

### ユーザーを登録する

さっそく **TODOリスト** の１つ目を片付けましょう。  
まずは **テストファースト** で最初に失敗するコードを書きます。

``` ruby
class HelloTest < Minitest::Test
  def test_greeting
    assert_equal 'hello world', greeting
  end
end

def greeting
  'hello world'
end
```

サンプルコードを以下のコードに書き換えてテストを実行します。

``` ruby
class UserTest < Minitest::Test
  def test_IDと名前を持ったユーザーを作成する
    user = User.new
    assert_equal '1', user.id
    assert_equal 'Bob', user.name
  end
end
```

テストは失敗しました。 `NameError: uninitialized constant UserTest::User`
クラスが定義されていないからですね。

``` bash
$ ruby test/hello_test.rb
Started with run options --seed 44125

UserTest
  test_IDと名前を持ったユーザーを作成する                                        ERROR (0.00s)
Minitest::UnexpectedError:         NameError: uninitialized constant UserTest::User
            test/hello_test.rb:7:in test_IDと名前を持ったユーザーを作成する


Finished in 0.00135s
1 tests, 0 assertions, 0 failures, 1 errors, 0 skips
```

テストをパスさせるためにUserクラスを追加します。  
まずはテストをパスさせるために **仮実装** でベタ書きのコードを実装します。

``` ruby
class UserTest < Minitest::Test
  def test_IDと名前を持ったユーザーを作成する
    user = User.new
    assert_equal '1', user.id
    assert_equal 'Bob', user.name
  end
end

class User
  attr_accessor :id, :name

  def initialize
    @id = '1'
    @name = 'Bob'
  end
end
```

テストをパスさせてレッドからグリーンになりました。

``` bash
$ ruby test/hello_test.rb
Started with run options --seed 55832

UserTest
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)

Finished in 0.00072s
1 tests, 2 assertions, 0 failures, 0 errors, 0 skips
```

## 仮実装から実装へ

### ユーザーを登録する

テストは通りましたがコードはベタ書きのままです。

``` ruby
class UserTest < Minitest::Test
  def test_IDと名前を持ったユーザーを作成する
    user = User.new
    assert_equal '1', user.id
    assert_equal 'Bob', user.name
  end
end

class User
  attr_accessor :id, :name

  def initialize
    @id = '1'
    @name = 'Bob'
  end
end
```

**仮実装** のままでは別のユーザーを作ることが出来ないので、コンストラクタ経由で作成できるようにします。

``` ruby
class UserTest < Minitest::Test
  def test_IDと名前を持ったユーザーを作成する
    user = User.new('1', 'Bob')
    assert_equal '1', user.id
    assert_equal 'Bob', user.name
  end
end

class User
  attr_accessor :id, :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

テストが通りました。

``` bash
$ ruby test/hello_test.rb
Started with run options --seed 6402

UserTest
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)

Finished in 0.00089s
1 tests, 2 assertions, 0 failures, 0 errors, 0 skips
```

**仮実装から実装へ** を経て一つ目の **TODOリスト** を片付けたのでここでバージョン管理システムを使ってコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: ユーザーを登録する'
```

以下、 **TODOリスト** を片付けるたびにコミットしていきます。

## リファクタリング

  - ❏ ユーザーを管理できるようにする
    
      - ❏ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する

レッド・グリーンときたので続いて **リファクタリング** を実施します。

### メソッドの抽出

本来はコードの重複が発生してからやるのですが今回は予め **メソッドの抽出** を適用してフィクスチャーを抽出しておきます。

``` ruby
class UserTest < Minitest::Test
  def test_IDと名前を持ったユーザーを作成する
    user = User.new('1', 'Bob')
    assert_equal '1', user.id
    assert_equal 'Bob', user.name
  end
end
```

Rubyのテスティングフレームワークminitestではフィクスチャーはsetupメソッドです。

``` ruby
class UserTest < Minitest::Test
  def setup
    @user = User.new('1', 'Bob')
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id
    assert_equal 'Bob', @user.name
  end
end
```

テストが壊れていないことを確認したらコミットします。

## 明白な実装

続いて **TODOリスト** を追加します。

  - ❏ ユーザーを管理できるようにする
    
      - ❏ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ❏ **ユーザー名が３文字未満の場合はエラー**

### ユーザーを登録する

追加した **TODOリスト** に取り掛かります。

``` ruby
class UserTest < Minitest::Test
  def setup
    @user = User.new('1', 'Bob')
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id
    assert_equal 'Bob', @user.name
  end
end

class User
  attr_accessor :id, :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

まず、失敗するテストを書いて **明白な実装** でテストをパスするようにします。

``` ruby
class UserTest < Minitest::Test
  def setup
    @user = User.new('1', 'Bob')
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id
    assert_equal 'Bob', @user.name
  end

  def test_ユーザー名が３文字未満の場合はエラー
    e = assert_raises RuntimeError do
      User.new('1', 'a')
    end

    assert_equal 'ユーザー名は3文字以上です。', e.message
  end
end

class User
  attr_accessor :id, :name

  def initialize(id, name)
    raise 'ユーザー名は3文字以上です。' if name.length < 3

    @id = id
    @name = name
  end
end
```

レッドからグリーンになったことを確認したらコミットします。

## リファクタリング

  - ❏ ユーザーを管理できるようにする
    
      - ❏ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー

レッド・グリーン・リファクタリングです。

### クラスの抽出

**クラスの抽出** を適用して Userクラスから **値オブジェクト** を抽出する **リファクタリング** を適用します。

``` ruby
class UserTest < Minitest::Test
  def setup
    @user = User.new('1', 'Bob')
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id
    assert_equal 'Bob', @user.name
  end

  def test_ユーザー名が３文字未満で新規登録する場合はエラー
    e = assert_raises RuntimeError do
      User.new(1, 'a')
    end

    assert_equal 'ユーザー名は3文字以上です。', e.message
  end
end

class User
  attr_accessor :id, :name

  def initialize(id, name)
    raise 'ユーザー名は3文字以上です。' if name.length < 3

    @id = id
    @name = name
  end
end
```

まずはUserIdクラスを抽出します。テストコードをUserIdクラスを使って呼び出すように変更したらエラーを修正してグリーンの状態を維持します。

``` ruby
class UserTest < Minitest::Test
  def setup
    id = UserId.new('1')
    @user = User.new(id, 'Bob')
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id.value
    assert_equal 'Bob', @user.name
  end
...
end

class UserId
  attr_accessor :value

  def initialize(value)
    @value = value
  end
end

...
```

続いてUserNameクラスを抽出します。テストコードも同様に変更します。

``` ruby
class UserTest < Minitest::Test
  def setup
    id = UserId.new('1')
    name = UserName.new('Bob')
    @user = User.new(id, name)
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id.value
    assert_equal 'Bob', @user.name.value
  end
...
end

...

class UserName
  attr_accessor :value

  def initialize(value)
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end

...
```

テストコードを修正してグリーンになったらコミットして **クラスの抽出** の **リファクタリング** 完了です。

``` bash
$ruby test/hello_test.rb
Started with run options --seed 59746

UserTest
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)

Finished in 0.00071s
2 tests, 4 assertions, 0 failures, 0 errors, 0 skips
```

### setメソッドの削除

**クラスの抽出** により **値オブジェクト** を抽出することは出来ましたがインスタンスの値が変更可能な状態です。  
**setメソッドの削除** を適用して **値オブジェクト** の要求を満たす不変オブジェクトに **リファクタリング** しましょう。

``` ruby
class UserTest < Minitest::Test
  def setup
    id = UserId.new('1')
    name = UserName.new('Bob')
    @user = User.new(id, name)
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id.value
    assert_equal 'Bob', @user.name.value
  end

  def test_ユーザー名が３文字未満の場合はエラー
    e = assert_raises RuntimeError do
      UserName.new('a')
    end

    assert_equal 'ユーザー名は3文字以上です。', e.message
  end
end

class UserId
  attr_accessor :value

  def initialize(value)
    @value = value
  end
end

class UserName
  attr_accessor :value

  def initialize(value)
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end

class User
  attr_accessor :id, :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

アックセッサメソッドを読み取り専用に変更します。

``` ruby
...

class UserId
  attr_reader :value

...
end

class UserName
  attr_reader :value

...
end

class User
  attr_reader :id, :name

...
end
```

テストが壊れていないことを確認したらコミットします。

``` bash
$ ruby test/hello_test.rb
Started with run options --seed 62273

UserTest
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)

Finished in 0.00075s
2 tests, 4 assertions, 0 failures, 0 errors, 0 skips
```

## 例外ケース

正常系の実装が出来たので続いて例外系の実装に入りたいと思います。  
まず **TODOリスト** を追加します。

  - ❏ ユーザーを管理できるようにする
    
      - ❏ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ❏ **ユーザー名が４文字の場合は登録される**
        
          - ❏ **ユーザー名を指定しない場合はエラー**
        
          - ❏ **IDを指定しない場合はエラー**

### ユーザーを登録する

追加した **TODOリスト** をテストを壊さないように１つづつ片付けていくとしましょう。

``` ruby
class UserTest < Minitest::Test
  def setup
    id = UserId.new('1')
    name = UserName.new('Bob')
    @user = User.new(id, name)
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id.value
    assert_equal 'Bob', @user.name.value
  end

  def test_ユーザー名が３文字未満の場合はエラー
    e = assert_raises RuntimeError do
      UserName.new('a')
    end

    assert_equal 'ユーザー名は3文字以上です。', e.message
  end
end

class UserId
  attr_reader :value

  def initialize(value)
    @value = value
  end
end

class UserName
  attr_reader :value

  def initialize(value)
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end

class User
  attr_reader :id, :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

実装後のコードです。  
実際は１つテストコードを追加したらプロダクトコードを実装してレッド・グリーンのサイクルを回しています。

``` ruby
class UserTest < Minitest::Test
  def setup
    id = UserId.new('1')
    name = UserName.new('Bob')
    @user = User.new(id, name)
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id.value
    assert_equal 'Bob', @user.name.value
  end

  def test_ユーザー名が３文字未満の場合はエラー
    e = assert_raises RuntimeError do
      UserName.new('a')
    end

    assert_equal 'ユーザー名は3文字以上です。', e.message
  end

  def test_ユーザー名が4文字の場合は登録される
    user = User.new(UserId.new('1'), UserName.new('abcd'))
    assert_equal 'abcd', user.name.value
  end

  def test_ユーザー名を指定しない場合はエラー
    assert_raises RuntimeError do
      UserName.new(nil)
    end
  end

  def test_IDを指定しない場合はエラー
    assert_raises RuntimeError do
      UserId.new(nil)
    end
  end
end

class UserId
  attr_reader :value

  def initialize(value)
    raise if value.nil?

    @value = value
  end
end

class UserName
  attr_reader :value

  def initialize(value)
    raise if value.nil?
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end

class User
  attr_reader :id, :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

例外系の機能を追加してテストもパスしたのでコミットします。

## リファクタリング

  - ❏ ユーザーを管理できるようにする
    
      - ✓ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ✓ ユーザー名を指定しない場合はエラー
        
          - ✓ ユーザー名が４文字の場合は登録される
        
          - ✓ IDを指定しない場合はエラー

今回はコードの可読性を改善する観点で **リファクタリング** を実施してみたいと思います。

### メソッドのインライン化

テストコードが増えてきましたここでテストコードをグルーピングするため **メソッドのインライン化** を適用します。

``` ruby
class UserTest < Minitest::Test
  def setup
    id = UserId.new('1')
    name = UserName.new('Bob')
    @user = User.new(id, name)
  end

  def test_IDと名前を持ったユーザーを作成する
    assert_equal '1', @user.id.value
    assert_equal 'Bob', @user.name.value
  end

  def test_ユーザー名が３文字未満の場合はエラー
    e = assert_raises RuntimeError do
      UserName.new('a')
    end

    assert_equal 'ユーザー名は3文字以上です。', e.message
  end

  def test_ユーザー名が４文字の場合は登録される
    user = User.new(UserId.new('1'), UserName.new('abcd'))
    assert_equal 'abcd', user.name.value
  end

  def test_ユーザー名を指定しない場合はエラー
    assert_raises RuntimeError do
      UserName.new(nil)
    end
  end

  def test_IDを指定しない場合はエラー
    assert_raises RuntimeError do
      UserId.new(nil)
    end
  end
end

class UserId
  attr_reader :value

  def initialize(value)
    raise if value.nil?

    @value = value
  end
end

class UserName
  attr_reader :value

  def initialize(value)
    raise if value.nil?
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end

class User
  attr_reader :id, :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

テストコードの構造を **TODOリスト** の構造に合わせることで可読性を改善します。

``` ruby
class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(id, name)
    end

    def test_IDと名前を持ったユーザーを作成する
      assert_equal '1', @user.id.value
      assert_equal 'Bob', @user.name.value
    end

    def test_ユーザー名が３文字未満の場合はエラー
      e = assert_raises RuntimeError do
        UserName.new('a')
      end

      assert_equal 'ユーザー名は3文字以上です。', e.message
    end

    def test_ユーザー名が４文字の場合は登録される
      user = User.new(UserId.new('1'), UserName.new('abcd'))
      assert_equal 'abcd', user.name.value
    end

    def test_ユーザー名を指定しない場合はエラー
      assert_raises RuntimeError do
        UserName.new(nil)
      end
    end

    def test_IDを指定しない場合はエラー
      assert_raises RuntimeError do
        UserId.new(nil)
      end
    end
  end
end

...
```

実行結果もわかりやすいなりました。 テストは壊れていないのでコミットします。

``` bash
$ ruby test/hello_test.rb
Started with run options --seed 39340

ユーザーを登録する
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)
  test_IDを指定しない場合はエラー                                             PASS (0.00s)
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_ユーザー名を指定しない場合はエラー                                          PASS (0.00s)
  test_ユーザー名が４文字の場合は登録される                                         PASS (0.00s)

Finished in 0.00217s
5 tests, 7 assertions, 0 failures, 0 errors, 0 skips
```

### キーワード引数の導入

テストコードは読みやすくなりました。続いてプロダクトコードを改善しましょう。  
動的言語であるRubyでは型を明示しないため引数の値がリテラルなのか **値オブジェクト**
なのかメソッドの定義だけでは把握できません。**キーワード引数の導入**
をしてできるだけ引数の型を把握しやすいように **リファクタリング** しましょう。

``` ruby
class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(id, name)
    end

    def test_IDと名前を持ったユーザーを作成する
      assert_equal '1', @user.id.value
      assert_equal 'Bob', @user.name.value
    end

    def test_ユーザー名が３文字未満の場合はエラー
      e = assert_raises RuntimeError do
        UserName.new('a')
      end

      assert_equal 'ユーザー名は3文字以上です。', e.message
    end

    def test_ユーザー名が４文字の場合は登録される
      user = User.new(UserId.new('1'), UserName.new('abcd'))
      assert_equal 'abcd', user.name.value
    end

    def test_ユーザー名を指定しない場合はエラー
      assert_raises RuntimeError do
        UserName.new(nil)
      end
    end

    def test_IDを指定しない場合はエラー
      assert_raises RuntimeError do
        UserId.new(nil)
      end
    end
  end
end

class UserId
  attr_reader :value

  def initialize(value)
    raise if value.nil?

    @value = value
  end
end

class UserName
  attr_reader :value

  def initialize(value)
    raise if value.nil?
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end

class User
  attr_reader :id, :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

**キーワード引数** を **値オブジェクト** と同じ名称にします。

``` ruby
class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end
...
end

...

class User
  attr_reader :id, :name

  def initialize(user_id:, user_name:)
    @id = user_id
    @name = user_name
  end
end
```

テストを修正してグリーンになったらコミットします。  
ちなみに **キーワード引数の導入**
という名称はリファクタリングのカタログにはない用語です。Ruby固有のパターンとして便宜上命名しています。

## モジュール分割

**TODOリスト** を全部片付けたのでここで単一ファイルから各クラスモジュールごとに **モジュール分割** を実施します。

### TODOリスト

  - ❏ ユーザーを管理できるようにする
    
      - ✓ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ✓ ユーザー名を指定しない場合はエラー
        
          - ✓ ユーザー名が４文字の場合は登録される
        
          - ✓ IDを指定しない場合はエラー

### クラス図

    class User {
      UserId id
      UserName name
    }
    class UserId {
      String value
    }
    class UserName {
      String value
    }
    
    User *-l UserId
    User *-r UserName

### ファイル構成

    /main.rb
      |--lib/
          |
           -- sns.rb
           -- user_id.rb
           -- user_name.rb
           -- user.rb
      |--test/
          |
           -- user_test.rb

**/main.rb.**

``` ruby
require './test/user_test.rb'
```

**/lib/sns.rb.**

``` ruby
# frozen_string_literal: true

require './lib/user_id.rb'
require './lib/user_name.rb'
require './lib/user.rb'
```

**/lib/user\_id.rb.**

``` ruby
# frozen_string_literal: true

# User ID value object
class UserId
  attr_reader :value

  def initialize(value)
    raise if value.nil?

    @value = value
  end
end
```

**/lib/user\_name.rb.**

``` ruby
# frozen_string_literal: true

# User name value object
class UserName
  attr_reader :value

  def initialize(value)
    raise if value.nil?
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end
```

**/lib/user.rb.**

``` ruby
# frozen_string_literal: true

# User
class User
  attr_reader :id, :name

  def initialize(user_id:, user_name:)
    @id = user_id
    @name = user_name
  end
end
```

**/test/user\_test.rb.**

``` ruby
# frozen_string_literal: true

require 'minitest/reporters'
Minitest::Reporters.use! [Minitest::Reporters::SpecReporter.new(color: true)]
require 'minitest/autorun'
require './lib/sns.rb'

class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_IDと名前を持ったユーザーを作成する
      assert_equal '1', @user.id.value
      assert_equal 'Bob', @user.name.value
    end

    def test_ユーザー名が３文字未満の場合はエラー
      e = assert_raises RuntimeError do
        UserName.new('a')
      end

      assert_equal 'ユーザー名は3文字以上です。', e.message
    end

    def test_ユーザー名が４文字の場合は登録される
      user = User.new(user_id: UserId.new('1'),
                      user_name: UserName.new('abcd'))
      assert_equal 'abcd', user.name.value
    end

    def test_ユーザー名を指定しない場合はエラー
      assert_raises RuntimeError do
        UserName.new(nil)
      end
    end

    def test_IDを指定しない場合はエラー
      assert_raises RuntimeError do
        UserId.new(nil)
      end
    end
  end
end
```

## リリース

**モジュール分割** により最初のリリースの準備が出来ました。  
リリース前に **静的コード解析** と **コードカバレッジ** を実施してコードの品質を確認しておきましょう。  
手順の詳細は [こちらの記事](https://qiita.com/k2works/items/385dc16333e065d69bd6)
をご参照ください。

### 静的コード解析

``` bash
$ rubocop
Inspecting 5 files
....C

Offenses:

test/user_test.rb:11:3: C: Metrics/BlockLength: Block has too many lines. [30/25]
  describe 'ユーザーを登録する' do ...
  ^^^^^^^^^^^^^^^^^^^^^^^
test/user_test.rb:18:9: C: Naming/MethodName: Use snake_case for method names.
    def test_IDと名前を持ったユーザーを作成する
        ^^^^^^^^^^^^^^^^^^^^^^^
test/user_test.rb:18:16: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_IDと名前を持ったユーザーを作成する
               ^^^^^^^^^^^^^^^^
test/user_test.rb:23:9: C: Naming/MethodName: Use snake_case for method names.
    def test_ユーザー名が３文字未満の場合はエラー
        ^^^^^^^^^^^^^^^^^^^^^^^
test/user_test.rb:23:14: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_ユーザー名が３文字未満の場合はエラー
             ^^^^^^^^^^^^^^^^^^
test/user_test.rb:31:9: C: Naming/MethodName: Use snake_case for method names.
    def test_ユーザー名が４文字の場合は登録される
        ^^^^^^^^^^^^^^^^^^^^^^^
test/user_test.rb:31:14: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_ユーザー名が４文字の場合は登録される
             ^^^^^^^^^^^^^^^^^^
test/user_test.rb:37:9: C: Naming/MethodName: Use snake_case for method names.
    def test_ユーザー名を指定しない場合はエラー
        ^^^^^^^^^^^^^^^^^^^^^^
test/user_test.rb:37:14: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_ユーザー名を指定しない場合はエラー
             ^^^^^^^^^^^^^^^^^
test/user_test.rb:43:9: C: Naming/MethodName: Use snake_case for method names.
    def test_IDを指定しない場合はエラー
        ^^^^^^^^^^^^^^^^^^^
test/user_test.rb:43:16: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_IDを指定しない場合はエラー
               ^^^^^^^^^^^^

5 files inspected, 11 offenses detected
```

いくつか警告が表示されていますがテストコードの日本語に関する内容なのでチェック対象から除外することにします。 \`.

rubocop.yml\` ファイルを以下に更新します。

``` yml
inherit_from: .rubocop_todo.yml

AllCops:
    Include:
      - 'lib/**/*.rb'
      - 'test/**/*_test.rb'
    Exclude:
      - 'docs'

Style/AsciiComments:
  Enabled: false

Naming/MethodName:
  Exclude:
    - 'test/**'

Naming/AsciiIdentifiers:
  Exclude:
    - 'test/**'

Metrics/BlockLength:
  Exclude:
    - 'test/**'
```

警告は無くなりました。

``` bash
$ rubocop
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

### コードカバレッジ

まず、テストコードからコードカバレッジを実行できるようにします。

`user_test.rb` の先頭を以下に更新します。

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use! [Minitest::Reporters::SpecReporter.new(color: true)]
require 'minitest/autorun'
require './lib/sns.rb'

...
```

テストを実行します。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 24571

ユーザーを登録する
  test_IDを指定しない場合はエラー                                             PASS (0.00s)
  test_ユーザー名が４文字の場合は登録される                                         PASS (0.00s)
  test_ユーザー名を指定しない場合はエラー                                          PASS (0.00s)
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)

Finished in 0.00106s
5 tests, 7 assertions, 0 failures, 0 errors, 0 skips
Coverage report generated for Unit Tests to /Users/k2works/Projects/sandbox/tdd_itddd/coverage. 19 / 19 LOC (100.0%) covered.
```

テストカバレッジは100%です。

![20200222](../../images/asciidoc/tdd_itddd/20200222.png)

## ふりかえり

最初のリリースが完了したのでここでやってきたことのふりかえりをしておきましょう。

まず、**ユーザーストーリー** から **TODOリスト** を作成しました。  
**TODOリスト** の１つめを **仮実装** でまずベタ書きのコードを書いてテストをパスするようにしました。  
テストをパスしてグリーンになったら **仮実装から実装へ** を経て最初の **TODOリスト** を完了させました。

次の **TODOリスト** を追加する前にテストコードに **メソッドの抽出** を適用して **リファクタリング** を実施しました。  
**リファクタリング** を実施してテストが壊れていないことを確認してから **TODOリスト** を追加して次の作業に入りました。  
次の作業ではまず **TODOリスト** を追加してその内容を **明白な実装** で片付けました。

**明白な実装** により再びテストがレッドからグリーンになったので **クラスの抽出** と **setメソッドの削除** を適用して
**リファクタリング** を実施することにより **値オブジェクト** を追加しました。  
**リファクタリング** を実施してテストが壊れていないことを確認したら 次は例外ケースの **TODOリスト** を追加しました。

追加した例外ケースを **明白な実装** で片付けたら、まずテストコードに **メソッドのインライン化** を適用して プロダクトコードに
**キーワード引数の導入** を適用してコードの可読性を改善する **リファクタリング** を実施しました。

仕上げに **モジュール分割** を実施しました。  
続いて **静的コード** と **コードカバレッジ** を実施してコードの品質を確認して、最初のリリースを完了しました。

今回のテーマである **値オブジェクト** は書籍『テスト駆動開発』では *第１部 他国通貨* の中でMoneyクラスとして実装されていますし
**Value Objectパターン** として紹介されています。

> Value
> Objectパターン
> 
> 広く共有されるものの、同一インスタンスであることはさほど重要でないオブジェクトを設計するにはどうしたらよいだろうか-----オブジェクト作成時に状態を設定したら、その後決して変えないようにする。オブジェクトへの操作は必ず新しいオブジェクトを返すようにしよう。
> 
> —  テスト駆動開発 

また、書籍『リファクタリング』では *第３章　コードの不吉な臭い* の中の **基本データ型への執着**
> で言及されています。

> 基本データ型への執着
> 
> オブジェクト指向を始めたばかりの人は、小さなオブジェクトを使ってちょっとしたことをさせるのを嫌がる傾向があります。金額と通貨単位を組み合わせたMoney(貨幣)クラス、上限と下限と持つRange(範囲)クラス、電話番号や郵便番号を表すための特殊な文字列クラスなどがこの例に該当します。
> 
> —  新装版 リファクタリング 

アプリケーション開発の過程でどのように **値オブジェクト** を適用するかは
[こちらの記事](https://qiita.com/k2works/items/928d519a7afe99361ff2#%E5%80%A4%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88)をご参照ください。

今回のリリースでユーザーは登録することは出来ましたがユーザー名を変更することが出来ません。

次回は **エンティティ** の実装に取り組んでみたいと思います。

# エンティティ

## ユーザーストーリー

前回の **値オブジェクト** に続いて今回は **エンティティ** を作成します。まず **ユーザーストーリー** から追加作業を
**TODOリスト** に追加します。

    利用者として
    ユーザーを管理できるようにしたい
    なぜならユーザーはシステムを利用するために必要だから

## TODOリスト

  - ❏ ユーザーを管理できるようにする
    
      - ✓ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ✓ ユーザー名を指定しない場合はエラー
        
          - ✓ ユーザー名が４文字の場合は登録される
        
          - ✓ IDを指定しない場合はエラー
    
      - ❏ ユーザー名を変更できるようにする
    
      - ❏ ユーザーの同一性を判断できるようにする
        
          - ❏ 識別子を追加する
        
          - ❏ エンティティの比較のを行う

## 明白な実装

### ユーザー名を変更する

追加した **TODOリスト** を **テストファースト** で片づけるため最初にテストコードの追加から始めます。

``` ruby
...
  describe 'ユーザーを更新する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_ユーザー名を更新する
      @user.change_name('Alice')
      assert_equal 'Alice', @user.name
    end
  end
end
```

テストを実行して失敗することを確認します。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 16647

ユーザーを登録する
  test_IDを指定しない場合はエラー                                             PASS (0.00s)
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)
  test_ユーザー名が４文字の場合は登録される                                         PASS (0.00s)
  test_ユーザー名を指定しない場合はエラー                                          PASS (0.00s)

ユーザーを更新する
  test_ユーザー名を更新する                                                ERROR (0.00s)
Minitest::UnexpectedError:         NoMethodError: undefined method change_name' for #<User:0x00007fdc9101e850>
            test/user_test.rb:61:in `test_ユーザー名を更新する'


Finished in 0.00382s
6 tests, 7 assertions, 0 failures, 1 errors, 0 skips
```

続いて、メソッドの追加します。簡単な実装なので **明白な実装** で片づけるとします。

``` ruby
class User
  attr_reader :id, :name

  def initialize(user_id:, user_name:)
    @id = user_id
    @name = user_name
  end

  def change_name(name)
    raise if name.nil?

    @name = name
  end
end
```

続いて、テストが通ることを確認します。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 6624

ユーザーを登録する
  test_IDを指定しない場合はエラー                                             PASS (0.00s)
  test_ユーザー名が４文字の場合は登録される                                         PASS (0.00s)
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_ユーザー名を指定しない場合はエラー                                          PASS (0.00s)

ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

Finished in 0.00127s
6 tests, 8 assertions, 0 failures, 0 errors, 0 skips
```

### ユーザーの同一性を判断する

**エンティティ** として同一性を判断するためのテストケースを追加します。

``` ruby
...
  describe 'ユーザーの同一性を判断する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_同じ名前の異なるユーザー
      id = UserId.new('2')
      name = UserName.new('Bob')
      @user2 = User.new(user_id: id, user_name: name)

      refute @user.eql?(@user2)
    end

    def test_同じ名前の同じユーザー
      assert @user.eql?(@user)
    end

    def test_名前を変更した同じユーザー
      @user.change_name('Alice')

      assert @user.eql?(@user)
    end
  end
end
```

``` bash
$ ruby test/user_test.rb
Started with run options --seed 20456

ユーザーの同一性を判断する
  test_同じ名前の同じユーザー                                                PASS (0.00s)
  test_同じ名前の異なるユーザー                                               PASS (0.00s)
  test_名前を変更した同じユーザー                                              PASS (0.00s)

ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

ユーザーを登録する
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_ユーザー名を指定しない場合はエラー                                          PASS (0.00s)
  test_IDを指定しない場合はエラー                                             PASS (0.00s)
  test_ユーザー名が４文字の場合は登録される                                         PASS (0.00s)
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)

Finished in 0.00166s
9 tests, 11 assertions, 0 failures, 0 errors, 0 skips
```

比較メソッドを識別子で判定するようにオーバーライドします。

``` ruby
class User
  attr_reader :id, :name

  def initialize(user_id:, user_name:)
    @id = user_id
    @name = user_name
  end

  def change_name(name)
    raise if name.nil?

    @name = name
  end

  def eql?(other)
    @id == other.id
  end
end
```

``` bash
 $ ruby test/user_test.rb
Started with run options --seed 1326

ユーザーを登録する
  test_IDを指定しない場合はエラー                                             PASS (0.00s)
  test_ユーザー名が４文字の場合は登録される                                         PASS (0.00s)
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_ユーザー名を指定しない場合はエラー                                          PASS (0.00s)
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)

ユーザーの同一性を判断する
  test_同じ名前の同じユーザー                                                PASS (0.00s)
  test_同じ名前の異なるユーザー                                               PASS (0.00s)
  test_名前を変更した同じユーザー                                              PASS (0.00s)

ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

Finished in 0.00226s
9 tests, 11 assertions, 0 failures, 0 errors, 0 skips
```

## リファクタリング

### メソッドの委譲

`eql?` メソッドを `==` に委譲します。

``` ruby
class User
  attr_reader :id, :name

  def initialize(user_id:, user_name:)
    @id = user_id
    @name = user_name
  end

  def change_name(name)
    raise if name.nil?

    @name = name
  end

  def eql?(other)
    self == other
  end

  def ==(other)
    other.equal?(self) || (other.instance_of?(self.class) && other.id == id
  end

  def hash
    id.hash
  end
end
```

変更によりコードが壊れていないことを確認します。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 37624

ユーザーの同一性を判断する
  test_同じ名前の異なるユーザー                                               PASS (0.00s)
  test_名前を変更した同じユーザー                                              PASS (0.00s)
  test_同じ名前の同じユーザー                                                PASS (0.00s)

ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

ユーザーを登録する
  test_IDと名前を持ったユーザーを作成する                                         PASS (0.00s)
  test_ユーザー名が３文字未満の場合はエラー                                         PASS (0.00s)
  test_IDを指定しない場合はエラー                                             PASS (0.00s)
  test_ユーザー名を指定しない場合はエラー                                          PASS (0.00s)
  test_ユーザー名が４文字の場合は登録される                                         PASS (0.00s)

Finished in 0.00164s
9 tests, 11 assertions, 0 failures, 0 errors, 0 skips
```

### モジュール分割

テストコードの基本部分をヘルパーとして分割して共通利用できるようにしておきます。

`test_helper.rb` を作成します。

``` ruby
require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use! [Minitest::Reporters::SpecReporter.new(color: true)]
require 'minitest/autorun'
```

`user_test.rb` の先頭部部を変更します。

``` ruby
require './test/test_helper'
require './lib/sns.rb'

class UserTest < Minitest::Test
...
```

## リリース

### 静的コード解析

``` bash
$ rubocop
The following cops were added to RuboCop, but are not configured. Please set Enabled to either `true` or `false` in your `.rubocop.yml` file:
 - Lint/RaiseException (0.81)
 - Lint/StructNewOverride (0.81)
 - Style/HashEachMethods (0.80)
 - Style/HashTransformKeys (0.80)
 - Style/HashTransformValues (0.80)
For more information: https://docs.rubocop.org/en/latest/versioning/
The following cops were added to RuboCop, but are not configured. Please set Enabled to either `true` or `false` in your `.rubocop.yml` file:
 - Lint/RaiseException (0.81)
 - Lint/StructNewOverride (0.81)
 - Style/HashEachMethods (0.80)
 - Style/HashTransformKeys (0.80)
 - Style/HashTransformValues (0.80)
For more information: https://docs.rubocop.org/en/latest/versioning/
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

### コードカバレッジ

![2020042201](../../images/asciidoc/tdd_itddd/2020042201.png)

![2020042202](../../images/asciidoc/tdd_itddd/2020042202.png)

### TODOリスト

  - ❏ ユーザーを管理できるようにする
    
      - ✓ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ✓ ユーザー名を指定しない場合はエラー
        
          - ✓ ユーザー名が４文字の場合は登録される
        
          - ✓ IDを指定しない場合はエラー
    
      - ✓ ユーザー名を変更できるようにする
    
      - ✓ ユーザーの同一性を判断できるようにする
        
          - ✓ 識別子を追加する
        
          - ✓ エンティティの比較のを行う

### ファイル構成

    /main.rb
      |--lib/
          |
           -- sns.rb
           -- user_id.rb
           -- user_name.rb
           -- user.rb
      |--test/
          |
           -- test_helper.rb
           -- user_test.rb

**/main.rb.**

``` ruby
require './test/user_test.rb'
```

**/lib/sns.rb.**

``` ruby
# frozen_string_literal: true

require './lib/user_id.rb'
require './lib/user_name.rb'
require './lib/user.rb'
```

**/lib/user\_id.rb.**

``` ruby
# frozen_string_literal: true

# User ID value object
class UserId
  attr_reader :value

  def initialize(value)
    raise if value.nil?

    @value = value
  end
end
```

**/lib/user\_name.rb.**

``` ruby
# frozen_string_literal: true

# User name value object
class UserName
  attr_reader :value

  def initialize(value)
    raise if value.nil?
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end
```

**/lib/user.rb.**

``` ruby
# frozen_string_literal: true

# User
class User
  attr_reader :id, :name

  def initialize(user_id:, user_name:)
    @id = user_id
    @name = user_name
  end

  def change_name(name)
    raise if name.nil?

    @name = name
  end

  def eql?(other)
    @id == other.id
  end

  def ==(other)
    other.equal?(self) || other.instance_of?(self.class) && other.id == id
  end

  def hash
    id.hash
  end
end
```

**/test/test\_helper.rb.**

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use! [Minitest::Reporters::SpecReporter.new(color: true)]
require 'minitest/autorun'
```

**/test/user\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require './lib/sns.rb'

class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_IDと名前を持ったユーザーを作成する
      assert_equal '1', @user.id.value
      assert_equal 'Bob', @user.name.value
    end

    def test_ユーザー名が３文字未満の場合はエラー
      e = assert_raises RuntimeError do
        UserName.new('a')
      end

      assert_equal 'ユーザー名は3文字以上です。', e.message
    end

    def test_ユーザー名が４文字の場合は登録される
      user = User.new(user_id: UserId.new('1'),
                      user_name: UserName.new('abcd'))
      assert_equal 'abcd', user.name.value
    end

    def test_ユーザー名を指定しない場合はエラー
      assert_raises RuntimeError do
        UserName.new(nil)
      end
    end

    def test_IDを指定しない場合はエラー
      assert_raises RuntimeError do
        UserId.new(nil)
      end
    end
  end

  describe 'ユーザーを更新する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_ユーザー名を更新する
      @user.change_name('Alice')
      assert_equal 'Alice', @user.name
    end
  end

  describe 'ユーザーの同一性を判断する' do
    def setup
      id = UserId.new('1')
      name = UserName.new('Bob')
      @user = User.new(user_id: id, user_name: name)
    end

    def test_同じ名前の異なるユーザー
      id = UserId.new('2')
      name = UserName.new('Bob')
      @user2 = User.new(user_id: id, user_name: name)

      refute @user.eql?(@user2)
    end

    def test_同じ名前の同じユーザー
      assert @user.eql?(@user)
    end

    def test_名前を変更した同じユーザー
      @user.change_name('Alice')

      assert @user.eql?(@user)
    end
  end
end
```

## ふりかえり

まず、**ユーザーストーリー** から追加の **TODOリスト** を作成しました。  
**テストファースト** で最初に失敗するテストから始めて **明白な実装** によりユーザ名を更新するメソッドを追加しました。

続いて、**値オブジェクト** であるユーザーオブジェクトを **エンティティ**
として扱えるようにするためユーザーの同一性を判断するためのメソッドを追加しました。  
そして、メソッドの委譲のリファクタリングを実施後、テストを実行してコードが壊れていないことを確認しました。

仕上げに、ヘルパーファイルを抽出してテストファイルで共有できるようにしました。

今回のテーマである **エンティティ**
> に関しては、書籍『リファクタリング』第８章　データの再編成　値から参照への変更で言及されています。

> 多くのシステムにおいて、参照オブジェクトと値オブジェクトを分けて考えることが役立ちます。「参照オブジェクト」とは、顧客とか勘定といったもので、実世界における１個のオブジェクトを表しており、それらが同じものかどうかを調べるには、オブジェクト識別が用いられます。「値オブジェクト」とは、日付やお金のようなもので、もっぱら、それ自体のデータ値によって定義されます。それらのコピーはいくつあってもかまいません。
> 
> —  新装版 リファクタリング 

**値オブジェクト** と **エンティティ** に関してはリファクタリングカタログで **値から参照への変更** と
**参照から値への変更** として解説されています。

> 値から参照への変更
> 
> 同じインスタンスが多数存在するクラスがある。それらを１つのオブジェクトに置き換えたい。
> 
> そのオブジェクトを参照オブジェクトに変える。
> 
> —  新装版 リファクタリング 

> 参照から値への変更
> 
> 小さくて、不変で、コントロールが煩わしい参照オブジェクトがある。
> 
> 値オブジェクトに変える。
> 
> —  新装版 リファクタリング 

次回は **ドメインサービス** の実装に取り組んでみたいと思います。

# ドメインサービス

## ユーザーストーリー

前回の **エンティティ** に続いて今回は **ドメインサービス** を作成します。 まず **ユーザーストーリー** をもとに追加作業を
**TODOリスト** に追加します。

    利用者として
    ユーザーを管理できるようにしたい
    なぜならユーザーはシステムを利用するために必要だから

## TODOリスト

  - ❏ ユーザーを管理できるようにする
    
      - ✓ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ✓ ユーザー名を指定しない場合はエラー
        
          - ✓ ユーザー名が４文字の場合は登録される
        
          - ✓ IDを指定しない場合はエラー
    
      - ✓ ユーザー名を変更できるようにする
    
      - ✓ ユーザーの同一性を判断できるようにする
        
          - ✓ 識別子を追加する
        
          - ✓ エンティティの比較のを行う
    
      - ❏ ユーザーを重複して登録できないようにする

## 仮実装を経て本実装へ

### セットアップ

ユーザーデータを永続化するため今回はSQLiteを使用します。Rubyでのセットアップ方法はまず `Gemfile`
にsqlite3ライブラリを追加します。

`Gemfile`

``` ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

...
gem 'sqlite3'
```

続いてライブラリを読み込んで利用できるようにします。

`lib/sns.rb`

``` ruby
# frozen_string_literal: true

require './lib/user_id.rb'
require './lib/user_name.rb'
require './lib/user.rb'
require 'sqlite3'
```

追加する機能のテストコードの準備をします。テスト実行の最初にユーザーテーブルを作成してテスト終了時にテーブルを削除するようにします。

`test/user_test.rb`

``` ruby
...
  describe 'ユーザーの重複を判定する' do
    def setup
      @db = SQLite3::Database.new('sns.db')
      sql = 'CREATE TABLE USERS(id string, name string)'
      @db.execute(sql)
    end

    def teardown
      sql = 'DROP TABLE USERS'
      @db.execute(sql)
      @db.close
    end
  end
end
```

準備が出来たら追加ライブラリをインストールします。

``` bash
$ bundle install
```

### 仮実装

ユーザーの重複を判定する機能を実装したいのですがまだ具体的なコードの実装イメージが湧きません。こんな時は **仮実装**
でまず失敗するテストから始めるとしましょう。

`test_user_test.rb`

``` ruby
...
    def test_登録するユーザーがすでに存在している
      id = UserId.new('1')
      name = UserName.new('Bob')
      user = User.new(user_id: id, user_name: name)

      sql = 'INSERT INTO USERS(id, name) VALUES(:id, :name)'
      @db.execute(sql, id: user.id.value, name: user.name.value)

      assert user.exist?(user)
    end
...
```

`User#exist?` メソッドが存在しないためテストは失敗しました。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 19263

ユーザーの重複を判定する
  test_登録するユーザーがすでに存在している                                        ERROR (0.04s)
Minitest::UnexpectedError:         NoMethodError: undefined method exist? for #<User:0x000055f6172730e0>
            test/user_test.rb:103:in test_登録するユーザーがすでに存在している
...
```

テストを通すために `User#exist?` メソッドを追加して最小限の実装をします。

`lib/user.rb`

``` ruby
class User
...
  def change_name(name)
    raise if name.nil?

    @name = name
  end

  def exist?(_user)
    true
  end

  def eql?(other)
    @id == other.id
  end
...
end
```

テストが成功してグリーンの状態になりました。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 21516

ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

...

ユーザーの重複を判定する
  test_登録するユーザーがすでに存在している                                         PASS (0.07s)

Finished in 0.07418s
10 tests, 12 assertions, 0 failures, 0 errors, 0 skips
```

### 本実装

**仮実装**
でテストは通るようになりましたがこのままではユーザーが存在しない場合もTrueを返すのでデータベースから該当するユーザーが存在するかを確認するコードを実装します。

``` ruby
...
  def exist?(user)
    db = SQLite3::Database.new('sns.db')
    sql = 'SELECT * FROM USERS WHERE name = :name'
    result = db.execute(sql, name: user.name.value)
    !result.empty?
  end
...
```

テストが通ることを確認します。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 47320

ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

...

ユーザーの重複を判定する
  test_登録するユーザーがすでに存在している                                         PASS (0.05s)

Finished in 0.05795s
10 tests, 12 assertions, 0 failures, 0 errors, 0 skips
```

### テスト

ユーザーが存在しない場合のテストも追加しておきます。

``` ruby
...
    def test_登録するユーザーが存在していない
      id = UserId.new('2')
      name = UserName.new('Alice')
      user = User.new(user_id: id, user_name: name)

      refute user.exist?(user)
    end
...
```

テストが通ることを確認します。

``` bash
$ ruby test/user_test.rb
Started with run options --seed 2872

ユーザーの同一性を判断する
  test_同じ名前の同じユーザー                                                PASS (0.00s)
  test_同じ名前の異なるユーザー                                               PASS (0.00s)
  test_名前を変更した同じユーザー                                              PASS (0.00s)

ユーザーの重複を判定する
  test_登録するユーザーがすでに存在している                                         PASS (0.19s)
  test_登録するユーザーが存在していない                                           PASS (0.12s)
...

Finished in 0.32139s
11 tests, 13 assertions, 0 failures, 0 errors, 0 skips
```

## リファクタリング

レッド、グリーン、となったので次はリファクタです。

### クラスの抽出

まず、ユーザー **エンティティ** にユーザーが存在するかを確認するメソッドが存在するのは不自然なので **クラスの抽出** を適用して
**ドメインサービス** クラスを抽出するとしましょう。まず、 **ドメインサービス** クラスとテストクラスを追加します。

`test/user_service_test.rb`

``` ruby
require './test/test_helper'
require './lib/sns.rb'

class UserServiceTest < Minitest::Test
end
```

続いて **ドメインサービス** クラスとなる `UserService` クラスを追加して読み込むようにします。

`lib/user_service.rb`

``` ruby
class UserService
end
```

`lib/sns.rb`

``` ruby
require './lib/user_id.rb'
require './lib/user_name.rb'
require './lib/user.rb'
require './lib/user_service.rb'
require 'sqlite3'
```

テストが壊れていないことを確認します。

``` bash
$ rake test
...
ユーザーの重複を判定する
  test_登録するユーザーがすでに存在している                                         PASS (0.16s)
  test_登録するユーザーが存在していない                                           PASS (0.12s)

Finished in 0.60710s
13 tests, 15 assertions, 0 failures, 0 errors, 0 skips
```

### メソッドの移動

**ドメインサービス** を **クラスの抽出** したので続いて **エンティティ** からユーザーの重複を確認する **メソッドの移動**
を実施します。

`test/user_service_test.rb`

``` ruby
class UserServiceTest < Minitest::Test
  describe 'ユーザーの重複を判定する' do
    def setup
      @db = SQLite3::Database.new('sns.db')
      sql = 'CREATE TABLE USERS(id string, name string)'
      @db.execute(sql)
    end

    def test_登録するユーザーがすでに存在している
      id = UserId.new('1')
      name = UserName.new('Bob')
      user = User.new(user_id: id, user_name: name)

      sql = 'INSERT INTO USERS(id, name) VALUES(:id, :name)'
      @db.execute(sql, id: user.id.value, name: user.name.value)

      assert user.exist?(user)
    end

    def test_登録するユーザーが存在していない
      id = UserId.new('2')
      name = UserName.new('Alice')
      user = User.new(user_id: id, user_name: name)

      refute user.exist?(user)
    end

    def teardown
      sql = 'DROP TABLE USERS'
      @db.execute(sql)
      @db.close
    end
  end
end
```

`test/user_service_test.rb`

``` ruby
rlass UserService
  def exist?(user)
    db = SQLite3::Database.new('sns.db')
    sql = 'SELECT * FROM USERS WHERE name = :name'
    result = db.execute(sql, name: user.name.value)
    !result.empty?
  end
end
```

テストを **ドメインサービス** 経由から実行するように変更します。

`test/user_service_test.rb`

``` ruby
require './test/test_helper'
require './lib/sns'

class UserServiceT.rbest < Minitest::Test
  describe 'ユーザーの重複を判定する' do
    def setup
      @db = SQLite3::Database.new('sns.db')
      sql = 'CREATE TABLE USERS(id string, name string)'
      @db.execute(sql)

      @service = UserService.new
    end

    def test_登録するユーザーがすでに存在している
      id = UserId.new('1')
      name = UserName.new('Bob')
      user = User.new(user_id: id, user_name: name)

      sql = 'INSERT INTO USERS(id, name) VALUES(:id, :name)'
      @db.execute(sql, id: user.id.value, name: user.name.value)

      assert @service.exist?(user)
    end

    def test_登録するユーザーが存在していない
      id = UserId.new('2')
      name = UserName.new('Alice')
      user = User.new(user_id: id, user_name: name)

      refute @service.exist?(user)
    end

    def teardown
      sql = 'DROP TABLE USERS'
      @db.execute(sql)
      @db.close
    end
  end
end
```

テストが壊れていないことを確認したら **ドメインサービス** の **クラスの抽出** と **メソッドの移動**
のリファクタリングは完了です。

``` bash
$ rake test
...
ユーザーの重複を判定する
  test_登録するユーザーがすでに存在している                                         PASS (0.12s)
  test_登録するユーザーが存在していない                                           PASS (0.06s)
...
ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

Finished in 0.18120s
11 tests, 13 assertions, 0 failures, 0 errors, 0 skips
```

## TODOリスト

続いてユーザーIDを **エンティティ** の生成時に引数として受け取っていますが重複したIDで **エンティティ**
を生成してしまう可能性があるので自動生成するようにリファクタリングしたいと思います。

  - ❏ ユーザーを管理できるようにする
    
      - ✓ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ✓ ユーザー名を指定しない場合はエラー
        
          - ✓ ユーザー名が４文字の場合は登録される
        
          - ✓ IDを指定しない場合はエラー
    
      - ✓ ユーザー名を変更できるようにする
    
      - ✓ ユーザーの同一性を判断できるようにする
        
          - ✓ 識別子を追加する
        
          - ✓ エンティティの比較のを行う
    
      - ✓ ユーザーを重複して登録できないようにする
    
      - ❏ IDを自動生成する

## リファクタリング

### パラメータの削除

[UUID](https://ja.wikipedia.org/wiki/UUID) による識別子を導入するため `securerandom`
ライブラリを追加します。なお `securerandom` は標準添付ライブラリなので `gem` によるインストールは必要ありません。

`lib/sns.rb`

``` ruby
require './lib/user_id.rb'
require './lib/user_name.rb'
require './lib/user.rb'
require './lib/user_service.rb'
require 'sqlite3'
require 'securerandom'
```

**エンティティ** のコンストラクタの引数からidを削除して、生成時にUUIDを自動生成するように変更します。

`lib/user.rb`

``` ruby
class User
  attr_reader :id, :name

  def initialize(user_name:)
    @id = UserId.new(SecureRandom.uuid.to_str)
    @name = user_name
  end
...
```

プロダクトコードの変更に合わせてテストコードも修正します。

`test/user_service_test.rb`

``` ruby
class UserServiceTest < Minitest::Test
  describe 'ユーザーの重複を判定する' do
    def setup
      @db = SQLite3::Database.new('sns.db')
      sql = 'CREATE TABLE USERS(id string, name string)'
      @db.execute(sql)

      @service = UserService.new
    end

    def test_登録するユーザーがすでに存在している
      name = UserName.new('Bob')
      user = User.new(user_name: name)

      sql = 'INSERT INTO USERS(id, name) VALUES(:id, :name)'
      @db.execute(sql, id: user.id.value, name: user.name.value)

      assert @service.exist?(user)
    end

    def test_登録するユーザーが存在していない
      name = UserName.new('Alice')
      user = User.new(user_name: name)

      refute @service.exist?(user)
    end

    def teardown
      sql = 'DROP TABLE USERS'
      @db.execute(sql)
      @db.close
    end
  end
end
```

`test/user_test.rb`

``` ruby
class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      name = UserName.new('Bob')
      @user = User.new(user_name: name)
    end

    def test_IDと名前を持ったユーザーを作成する
      assert_equal 'Bob', @user.name.value
    end

    def test_ユーザー名が３文字未満の場合はエラー
      e = assert_raises RuntimeError do
        UserName.new('a')
      end

      assert_equal 'ユーザー名は3文字以上です。', e.message
    end

    def test_ユーザー名が４文字の場合は登録される
      user = User.new(
        user_name: UserName.new('abcd')
      )
      assert_equal 'abcd', user.name.value
    end

    def test_ユーザー名を指定しない場合はエラー
      assert_raises RuntimeError do
        UserName.new(nil)
      end
    end

    def test_IDを指定しない場合はエラー
      assert_raises RuntimeError do
        UserId.new(nil)
      end
    end
  end

  describe 'ユーザーを更新する' do
    def setup
      name = UserName.new('Bob')
      @user = User.new(user_name: name)
    end

    def test_ユーザー名を更新する
      @user.change_name('Alice')
      assert_equal 'Alice', @user.name
    end
  end

  describe 'ユーザーの同一性を判断する' do
    def setup
      name = UserName.new('Bob')
      @user = User.new(user_name: name)
    end

    def test_同じ名前の異なるユーザー
      name = UserName.new('Bob')
      @user2 = User.new(user_name: name)

      refute @user.eql?(@user2)
    end

    def test_同じ名前の同じユーザー
      assert @user.eql?(@user)
    end

    def test_名前を変更した同じユーザー
      @user.change_name('Alice')

      assert @user.eql?(@user)
    end
  end
end
```

テストが正しく動作することが確認出来たらリファクタリング完了です。

``` bash
$ rake test
...
ユーザーの重複を判定する
  test_登録するユーザーがすでに存在している                                         PASS (0.12s)
  test_登録するユーザーが存在していない                                           PASS (0.06s)
...
ユーザーを更新する
  test_ユーザー名を更新する                                                 PASS (0.00s)

Finished in 0.18120s
11 tests, 13 assertions, 0 failures, 0 errors, 0 skips
```

## ドメインモデル貧血症

続いて **エンティティ** にある `change_name` メソッドに **メソッドの移動** を適用して **ドメインサービス**
に移動するリファクタリング適用してみましょう。

`lib/user.rb`

``` ruby
class User
  attr_reader :id, :name
  attr_writer :name

  def initialize(user_name:)
    @id = UserId.new(SecureRandom.uuid.to_str)
    @name = user_name
  end

  def eql?(other)
    @id == other.id
  end

  def ==(other)
    other.equal?(self) || other.instance_of?(self.class) && other.id == id
  end

  def hash
    id.hash
  end
end
```

`lib/user_service.rb`

``` ruby
class UserService
  def exist?(user)
    db = SQLite3::Database.new('sns.db')
    sql = 'SELECT * FROM USERS WHERE name = :name'
    result = db.execute(sql, name: user.name.value)
    !result.empty?
  end

  def change_name(user, name)
    raise if name.nil?

    user.name = name
  end
end
```

`test/user_test.rb`

``` ruby
...
    def test_ユーザー名を更新する
      service = UserService.new
      service.change_name(@user, UserName.new('Alice'))
      assert_equal 'Alice', @user.name.value
    end
...
    def test_名前を変更した同じユーザー
      service = UserService.new
      service.change_name(@user, UserName.new('Alice'))

      assert @user.eql?(@user)
    end
...
```

**メソッドの移動** の結果 **エンティティ** がスカスカになった上に **値オブジェクト**
を外部から更新するためのセッターを追加する必要が発生してしまいカプセル化が破壊されてしまう結果となりました。このような
**エンティティ** の実装は **ドメインモデル貧血症**
と呼ばれます。このリファクタリングはやりすぎだったようなので変更前に戻しておきましょう。

``` bash
$git checkout .
```

## リリース

### 静的コード解析

``` bash
$ rubocop
The following cops were added to RuboCop, but are not configured. Please set Enabled to either `true` or `false` in your `.rubocop.yml` file:
 - Layout/EmptyLinesAroundAttributeAccessor (0.83)
 - Layout/SpaceAroundMethodCallOperator (0.82)
 - Lint/RaiseException (0.81)
 - Lint/StructNewOverride (0.81)
 - Style/ExponentialNotation (0.82)
 - Style/HashEachMethods (0.80)
 - Style/HashTransformKeys (0.80)
 - Style/HashTransformValues (0.80)
 - Style/SlicingWithRange (0.83)
For more information: https://docs.rubocop.org/en/latest/versioning/
Inspecting 7 files
.......

7 files inspected, no offenses detected
```

### コードカバレッジ

![2020060501](../../images/asciidoc/tdd_itddd/2020060501.png)

### TODOリスト

  - ❏ ユーザーを管理できるようにする
    
      - ✓ ユーザーを登録する
        
          - ✓ IDと名前を持ったユーザーを作成する
        
          - ✓ ユーザー名が３文字未満の場合はエラー
        
          - ✓ ユーザー名を指定しない場合はエラー
        
          - ✓ ユーザー名が４文字の場合は登録される
        
          - ✓ IDを指定しない場合はエラー
    
      - ✓ ユーザー名を変更できるようにする
    
      - ✓ ユーザーの同一性を判断できるようにする
        
          - ✓ 識別子を追加する
        
          - ✓ エンティティの比較のを行う
    
      - ✓ ユーザーを重複して登録できないようにする
    
      - ✓ IDを自動生成する

### ファイル構成

    /main.rb
      |--lib/
          |
           -- sns.rb
           -- user.rb
           -- user_id.rb
           -- user_name.rb
           -- user_service.rb
      |--test/
          |
           -- test_helper.rb
           -- user_service_test.rb
           -- user_test.rb

**/main.rb.**

``` ruby
require './test/user_test.rb'
```

**/lib/sns.rb.**

``` ruby
# frozen_string_literal: true

require './lib/user_id.rb'
require './lib/user_name.rb'
require './lib/user.rb'
require './lib/user_service.rb'
require 'sqlite3'
require 'securerandom'
```

**/lib/user.rb.**

``` ruby
# frozen_string_literal: true

# User
class User
  attr_reader :id, :name

  def initialize(user_name:)
    @id = UserId.new(SecureRandom.uuid.to_str)
    @name = user_name
  end

  def change_name(name)
    raise if name.nil?

    @name = name
  end

  def eql?(other)
    @id == other.id
  end

  def ==(other)
    other.equal?(self) || other.instance_of?(self.class) && other.id == id
  end

  def hash
    id.hash
  end
end
```

**/lib/user\_id.rb.**

``` ruby
# frozen_string_literal: true

# User ID value object
class UserId
  attr_reader :value

  def initialize(value)
    raise if value.nil?

    @value = value
  end
end
```

**/lib/user\_name.rb.**

``` ruby
# frozen_string_literal: true

# User name value object
class UserName
  attr_reader :value

  def initialize(value)
    raise if value.nil?
    raise 'ユーザー名は3文字以上です。' if value.length < 3

    @value = value
  end
end
```

**/lib/user\_service.rb.**

``` ruby
# frozen_string_literal: true

# UserService
class UserService
  def exist?(user)
    db = SQLite3::Database.new('sns.db')
    sql = 'SELECT * FROM USERS WHERE name = :name'
    result = db.execute(sql, name: user.name.value)
    !result.empty?
  end
end
```

**/test/test\_helper.rb.**

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use! [Minitest::Reporters::SpecReporter.new(color: true)]
require 'minitest/autorun'
```

**/test/user\_service\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require './lib/sns.rb'

class UserServiceTest < Minitest::Test
  describe 'ユーザーの重複を判定する' do
    def setup
      @db = SQLite3::Database.new('sns.db')
      sql = 'CREATE TABLE USERS(id string, name string)'
      @db.execute(sql)

      @service = UserService.new
    end

    def test_登録するユーザーがすでに存在している
      name = UserName.new('Bob')
      user = User.new(user_name: name)

      sql = 'INSERT INTO USERS(id, name) VALUES(:id, :name)'
      @db.execute(sql, id: user.id.value, name: user.name.value)

      assert @service.exist?(user)
    end

    def test_登録するユーザーが存在していない
      name = UserName.new('Alice')
      user = User.new(user_name: name)

      refute @service.exist?(user)
    end

    def teardown
      sql = 'DROP TABLE USERS'
      @db.execute(sql)
      @db.close
    end
  end
end
```

**/test/user\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require './lib/sns.rb'


class UserTest < Minitest::Test
  describe 'ユーザーを登録する' do
    def setup
      name = UserName.new('Bob')
      @user = User.new(user_name: name)
    end

    def test_IDと名前を持ったユーザーを作成する
      assert_equal 'Bob', @user.name.value
    end

    def test_ユーザー名が３文字未満の場合はエラー
      e = assert_raises RuntimeError do
        UserName.new('a')
      end

      assert_equal 'ユーザー名は3文字以上です。', e.message
    end

    def test_ユーザー名が４文字の場合は登録される
      user = User.new(user_name: UserName.new('abcd'))
      assert_equal 'abcd', user.name.value
    end

    def test_ユーザー名を指定しない場合はエラー
      assert_raises RuntimeError do
        UserName.new(nil)
      end
    end

    def test_IDを指定しない場合はエラー
      assert_raises RuntimeError do
        UserId.new(nil)
      end
    end
  end

  describe 'ユーザーを更新する' do
    def setup
      name = UserName.new('Bob')
      @user = User.new(user_name: name)
    end

    def test_ユーザー名を更新する
      @user.change_name('Alice')
      assert_equal 'Alice', @user.name
    end
  end

  describe 'ユーザーの同一性を判断する' do
    def setup
      name = UserName.new('Bob')
      @user = User.new(user_name: name)
    end

    def test_同じ名前の異なるユーザー
      name = UserName.new('Bob')
      @user2 = User.new(user_name: name)

      refute @user.eql?(@user2)
    end

    def test_同じ名前の同じユーザー
      assert @user.eql?(@user)
    end

    def test_名前を変更した同じユーザー
      @user.change_name('Alice')

      assert @user.eql?(@user)
    end
  end
end
```

## ふりかえり

まず、**ユーザーストーリー** から追加の **TODOリスト** を作成しました。  
**TODOリスト** の内容を実装するにあたって今回は **仮実装を経て本実装へ** のアプローチで作業を進めていきました。

続いて、 **クラスの抽出** で **ドメインサービス** を抽出して **エンティティ** から対象メソッドを **メソッドの移動** で
**ドメインサービス** に移しました。

UUIDによる識別子を導入した後 **エンティティ** から **メソッドの移動** をさらに実施した結果 **ドメインモデル貧血症**
を起こしてしまったので変更を取り消しました。

次回は **リポジトリ** の実装に取り組んでみたいと思います。

# リポジトリ

# アプリケーションサービス

# 依存関係のコントロール

# ソフトウェアシステムを組み立てる

# ファクトリ

# データの整合性

# アプリケーションを1から組み立てる

# 集約

# 仕様

# アーキテクチャ

# 参照

## 参考サイト

  - [50
    分でわかるテスト駆動開発](https://channel9.msdn.com/Events/de-code/2017/DO03?ocid=player)

## 参考図書

# References

  - \[\] テスト駆動開発 Kent Beck (著), 和田 卓人 (翻訳): オーム社; 新訳版 (2017/10/14)

  - \[\] 新装版 リファクタリング―既存のコードを安全に改善する― (OBJECT TECHNOLOGY SERIES) Martin
    Fowler (著), 児玉 公信 (翻訳), 友野 晶夫 (翻訳), 平澤 章 (翻訳), その他: オーム社; 新装版
    (2014/7/26)

  - \[\] リファクタリング(第2版): 既存のコードを安全に改善する (OBJECT TECHNOLOGY SERIES) Martin
    Fowler (著), 児玉 公信 (翻訳), 友野 晶夫 (翻訳), 平澤 章 (翻訳), その他: オーム社; 第2版
    (2019/12/1)

  - \[\] ドメイン駆動設計入門 ボトムアップでわかる\! ドメイン駆動設計の基本 (日本語) 単行本（ソフトカバー） 成瀬 允宣 (著)
    翔泳社 (2020/2/13)
