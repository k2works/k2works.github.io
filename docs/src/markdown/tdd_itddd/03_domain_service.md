# ユーザーストーリー

前回の **エンティティ** に続いて今回は **ドメインサービス** を作成します。 まず **ユーザーストーリー** をもとに追加作業を
**TODOリスト** に追加します。

    利用者として
    ユーザーを管理できるようにしたい
    なぜならユーザーはシステムを利用するために必要だから

# TODOリスト

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

# 仮実装を経て本実装へ

## セットアップ

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

## 仮実装

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

## 本実装

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

## テスト

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

# リファクタリング

レッド、グリーン、となったので次はリファクタです。

## クラスの抽出

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

## メソッドの移動

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

# TODOリスト

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

# リファクタリング

## パラメータの削除

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

# ドメインモデル貧血症

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

# リリース

## 静的コード解析

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

## コードカバレッジ

![2020060501](../../images/asciidoc/tdd_itddd/2020060501.png)

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
    
      - ✓ ユーザーを重複して登録できないようにする
    
      - ✓ IDを自動生成する

## ファイル構成

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

# ふりかえり

まず、**ユーザーストーリー** から追加の **TODOリスト** を作成しました。  
**TODOリスト** の内容を実装するにあたって今回は **仮実装を経て本実装へ** のアプローチで作業を進めていきました。

続いて、 **クラスの抽出** で **ドメインサービス** を抽出して **エンティティ** から対象メソッドを **メソッドの移動** で
**ドメインサービス** に移しました。

UUIDによる識別子を導入した後 **エンティティ** から **メソッドの移動** をさらに実施した結果 **ドメインモデル貧血症**
を起こしてしまったので変更を取り消しました。

次回は **リポジトリ** の実装に取り組んでみたいと思います。
