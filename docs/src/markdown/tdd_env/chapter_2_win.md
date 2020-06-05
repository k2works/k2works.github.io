# Ruby環境のセットアップ(Windows版)

# インストール

[RubyInstaller](https://rubyinstaller.org/downloads/)からWITH
DEVKITをインストールします。

![ruby win install
001](../../images/asciidoc/tdd_env/ruby-win-install-001.png)

インストラーの指示に従います。

![ruby win install
002](../../images/asciidoc/tdd_env/ruby-win-install-002.png)

![ruby win install
003](../../images/asciidoc/tdd_env/ruby-win-install-003.png)

![ruby win install
004](../../images/asciidoc/tdd_env/ruby-win-install-004.png)

![ruby win install
005](../../images/asciidoc/tdd_env/ruby-win-install-005.png)

3を入力してエンターキーを押します。

![ruby win install
006](../../images/asciidoc/tdd_env/ruby-win-install-006.png)

# 追加パッケージのインストール

[Ruby for Visual Studio
Code](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby)

[Ruby
Solargraph](https://marketplace.visualstudio.com/items?itemName=castwide.solargraph)

[vscode-endwise](https://marketplace.visualstudio.com/items?itemName=kaiwood.endwise)

[ruby-rubocop](https://marketplace.visualstudio.com/items?itemName=misogi.ruby-rubocop)

[Test Explorer
UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

[Ruby Test
Explorer](https://marketplace.visualstudio.com/items?itemName=connorshea.vscode-ruby-test-adapter)

# 設定

既定のシェルをPowerShell Coreに変更します。

![ruby win vscode
001](../../images/asciidoc/tdd_env/ruby-win-vscode-001.png)

![ruby win vscode
002](../../images/asciidoc/tdd_env/ruby-win-vscode-002.png)

新しいターミナルを開いて以下のコマンドを入力します。

``` bash
gem install rubocop
gem install debase
gem install ruby-debug-ide
gem install solargraph
```

![ruby win vscode
003](../../images/asciidoc/tdd_env/ruby-win-vscode-003.png)

![ruby win vscode
004](../../images/asciidoc/tdd_env/ruby-win-vscode-004.png)

# Hello world

## プログラムを作成する

`Projects` フォルダ内に `Ruby` フォルダを作成してエディタからフォルダを開きます。

![ruby win hello
001](../../images/asciidoc/tdd_env/ruby-win-hello-001.png)

![ruby win hello
002](../../images/asciidoc/tdd_env/ruby-win-hello-002.png)

![ruby win hello
003](../../images/asciidoc/tdd_env/ruby-win-hello-003.png)

`新しいファイル` 作成アイコンを押します。

![ruby win hello
004](../../images/asciidoc/tdd_env/ruby-win-hello-004.png)

ファイル名は `main.rb` とします。

![ruby win hello
005](../../images/asciidoc/tdd_env/ruby-win-hello-005.png)

ファイルに以下のコードを入力したらRunアイコンを選択して `create a launch.json file`
を押してメニューからRubyを選択します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, false)
  end
end
```

![ruby win hello
006](../../images/asciidoc/tdd_env/ruby-win-hello-006.png)

`Debug Local File` を選択します。

![ruby win hello
007](../../images/asciidoc/tdd_env/ruby-win-hello-007.png)

`launch.json` ファイルが作成されたら `main.rb` タブに戻ってF5キーを押します。

![ruby win hello
008](../../images/asciidoc/tdd_env/ruby-win-hello-008.png)

デバッグコンソールに実行結果が表示されれば準備完了です。

![ruby win hello
009](../../images/asciidoc/tdd_env/ruby-win-hello-009.png)

テストをパスするようにコードを修正してF5キーを押します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

end
```

![ruby win hello
010](../../images/asciidoc/tdd_env/ruby-win-hello-010.png)

テスティングフレームワークの動作が確認できたので `hello_world`
関数の作成に入ります。まず以下のコードを追加してF5キーを押してテストが失敗することを確認します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

  def test_簡単な挨拶を返す
    assert_equal('Hello from Ruby', hello_world)
  end
end
```

![ruby win hello
011](../../images/asciidoc/tdd_env/ruby-win-hello-011.png)

`hello_world` 関数を追加してテストをパスさせます。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

  def test_簡単な挨拶を返す
    assert_equal('Hello from Ruby', hello_world)
  end
end

def hello_world
  'Hello from Ruby'
end
```

![ruby win hello
012](../../images/asciidoc/tdd_env/ruby-win-hello-012.png)

指定された名前で挨拶を返すようにします。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

  def test_簡単な挨拶を返す
    assert_equal('Hello from Ruby', hello_world)
  end

  def test_指定された名前で挨拶を返す
    assert_equal('Hello from VSCode', hello_world('VSCode'))
  end
end

def hello_world
  "Hello from Ruby"
end
```

![ruby win hello
013](../../images/asciidoc/tdd_env/ruby-win-hello-013.png)

関数に引数を追加します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

  def test_簡単な挨拶を返す
    assert_equal('Hello from Ruby', hello_world)
  end

  def test_指定された名前で挨拶を返す
    assert_equal('Hello from VSCode', hello_world('VSCode'))
  end
end

def hello_world(name)
  "Hello from #{name}"
end
```

![ruby win hello
014](../../images/asciidoc/tdd_env/ruby-win-hello-014.png)

`指定された名前で挨拶を返す` テストはパスしましたが今度は `簡単な挨拶を返す`
テストが失敗するようになりましたのでデフォルト引数を設定してテストをパスするようにします。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

  def test_簡単な挨拶を返す
    assert_equal('Hello from Ruby', hello_world)
  end

  def test_指定された名前で挨拶を返す
    assert_equal('Hello from VSCode', hello_world('VSCode'))
  end
end

def hello_world(name = 'Ruby')
  "Hello from #{name}"
end
```

![ruby win hello
015](../../images/asciidoc/tdd_env/ruby-win-hello-015.png)

仕上げに不要なテストを削除してテストケースの文言をわかりやすくしておきます。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何も指定されていない場合は既定の挨拶を返す
    assert_equal('Hello from Ruby', hello_world)
  end

  def test_指定された名前で挨拶を返す
    assert_equal('Hello from VSCode', hello_world('VSCode'))
  end
end

def hello_world(name = 'Ruby')
  "Hello from #{name}"
end
```

![ruby win hello
016](../../images/asciidoc/tdd_env/ruby-win-hello-016.png)

## プログラムをデバッグする

まず確認したいプログラムの行を左部分を押してブレークポイント（赤丸）を設定します。

![ruby win debug
001](../../images/asciidoc/tdd_env/ruby-win-debug-001.png)

ブレークポイントを設定したらF5を押してプログラムの実行します。そうするとブレークポイント部分でプログラムが停止して変数などの情報が確認できるようになります。

![ruby win debug
002](../../images/asciidoc/tdd_env/ruby-win-debug-002.png)

画面上の実行ボタンを押すと次のブレークポイントに移動します。

![ruby win debug
003](../../images/asciidoc/tdd_env/ruby-win-debug-003.png)

デバッガを終了するには終了ボタンを押します。

![ruby win debug
004](../../images/asciidoc/tdd_env/ruby-win-debug-004.png)

ブレークポイントを再度押すことで解除ができます。

![ruby win debug
005](../../images/asciidoc/tdd_env/ruby-win-debug-005.png)

## プログラムをレポジトリに保存する

ソース管理を選択して `リポジトリを初期化する` を押します。

![ruby win git 001](../../images/asciidoc/tdd_env/ruby-win-git-001.png)

`全ての変更をステージ` を選択します。

![ruby win git 002](../../images/asciidoc/tdd_env/ruby-win-git-002.png)

変更内容に `feat: HelloWorld` と入力して `コミット` を押します。

![ruby win git 003](../../images/asciidoc/tdd_env/ruby-win-git-003.png)

変更内容は `GitLens` から確認できます。

![ruby win git 004](../../images/asciidoc/tdd_env/ruby-win-git-004.png)