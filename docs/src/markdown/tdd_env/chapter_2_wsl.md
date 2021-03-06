# Ruby環境のセットアップ(WSL版)

画面左下の `><` を押してメニューから `Remote-WSL: New Window` を選択します。

![ruby 001](../../images/asciidoc/tdd_env/ruby-001.png)

`アクセスを許可する` を押します。

![ruby 002](../../images/asciidoc/tdd_env/ruby-002.png)

新しいウィンドウが立ち上がったらExtensionメニューから `Install Local Extensions in "WSL:
Ubuntu'…​"` を押します。

![ruby 003](../../images/asciidoc/tdd_env/ruby-003.png)

全てにチェックをしてインストールします。

![ruby 004](../../images/asciidoc/tdd_env/ruby-004.png)

拡張機能のインストールが終わったら `Reload Window` を押して拡張機能を読み込みます。

![ruby 005](../../images/asciidoc/tdd_env/ruby-005.png)

# プロビジョニングの実行

Ruby開発環境の自動構築をするため以下のレポジトリを自分のレポジトリにフォークします。

[テスト駆動開発から始めるRuby入門](https://github.com/hiroshima-arc/tdd_rb)

`Fork` を押します。

![provision 001](../../images/asciidoc/tdd_env/provision-001.png)

`Fork` が完了して自分のレポジトリにコピーされたら `Clone or download` を押してレポジトリのURLをコピーします。

![provision 002](../../images/asciidoc/tdd_env/provision-002.png)

エクスプローラアイコンメニューから `レポジトリをクローンする` を押します。

![provision 003](../../images/asciidoc/tdd_env/provision-003.png)

先程コピーしたレポジトリのURLを貼り付けます。

![provision 004](../../images/asciidoc/tdd_env/provision-004.png)

保存先はそのままで `OK` を押します。

![provision 005](../../images/asciidoc/tdd_env/provision-005.png)

`開く` を押します。

![provision 006](../../images/asciidoc/tdd_env/provision-006.png)

メニューから `ターミナル` `新しいターミナル` を選択します。

![provision 007 1](../../images/asciidoc/tdd_env/provision-007-1.png)

![provision 007 2](../../images/asciidoc/tdd_env/provision-007-2.png)

ターミナルに以下のコマンドを入力します。実行時にパスワード入力が求められるのでWSLで設定したパスワードを入力してください。

``` bash
$ sudo apt-get update -y
[sudo] password for newbie4649:
```

![provision 008](../../images/asciidoc/tdd_env/provision-008.png)

続いて、ターミナルに以下のコマンドを入力します。

``` bash
$ sudo apt install ansible -y
```

続いて、エクスプローラから　`provisioning/vars/site.yml` をファイルを開いて `user:`
の名前をWSLで設定したユーザーIDに変更します。

![provision 009](../../images/asciidoc/tdd_env/provision-009.png)

変更を保存したらターミナルに以下のコマンドを入力します。

``` bash
$ cd provisioning/tasks/
$ sudo ansible-playbook --inventory=localhost, --connection=local site.yml
```

![provision 010](../../images/asciidoc/tdd_env/provision-010.png)

セットアップが完了したらエディタを再起動してプロジェクトを開きます。

![provision 010 2](../../images/asciidoc/tdd_env/provision-010-2.png)

以下のコマンドを入力してRubyがセットアップされていることを確認します。

``` bash
$ ruby -v
```

![provision 011](../../images/asciidoc/tdd_env/provision-011.png)

続いて、ターミナルに以下のコマンドを入力します。

``` bash
$ code ~/.bashrc
```

表示されたファイルの一番最後に以下のコードを追加して保存します。

    ...
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_compl

![provision 012](../../images/asciidoc/tdd_env/provision-012.png)

保存したら以下のコマンドを実行してNode.jsのバージョンが表示されたらセットアップ完了です。

``` bash
$ source ~/.bashrc
$ nvm install --lts
$ node -v
```

![provision 013](../../images/asciidoc/tdd_env/provision-013.png)

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

ターミナルに以下のコマンドを入力します。

``` bash
gem install rubocop
gem install debase
gem install ruby-debug-ide
gem install solargraph
```

# Hello world

## プログラムを作成する

`REAMD.md` を選択してから `新しいファイル` 作成アイコンを押します。

![ruby hello 001](../../images/asciidoc/tdd_env/ruby-hello-001.png)

ファイル名は `main.rb` とします。

![ruby hello 002](../../images/asciidoc/tdd_env/ruby-hello-002.png)

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

![ruby hello 003](../../images/asciidoc/tdd_env/ruby-hello-003.png)

`Debug Local File` を選択します。

![ruby hello 004](../../images/asciidoc/tdd_env/ruby-hello-004.png)

`launch.json` ファイルが作成されたら `main.rb` タブに戻ってF5キーを押します。

![ruby hello 005](../../images/asciidoc/tdd_env/ruby-hello-005.png)

デバッグコンソールに実行結果が表示されれば準備完了です。

![ruby hello 006](../../images/asciidoc/tdd_env/ruby-hello-006.png)

テストをパスするようにコードを修正してF5キーを押します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

end
```

![ruby hello 007](../../images/asciidoc/tdd_env/ruby-hello-007.png)

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

![ruby hello 008](../../images/asciidoc/tdd_env/ruby-hello-008.png)

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

![ruby hello 009](../../images/asciidoc/tdd_env/ruby-hello-009.png)

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

![ruby hello 010](../../images/asciidoc/tdd_env/ruby-hello-010.png)

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

![ruby hello 011](../../images/asciidoc/tdd_env/ruby-hello-011.png)

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

![ruby hello 012](../../images/asciidoc/tdd_env/ruby-hello-012.png)

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

![ruby hello 013](../../images/asciidoc/tdd_env/ruby-hello-013.png)

## プログラムをデバッグする

まず確認したいプログラムの行を左部分を押してブレークポイント（赤丸）を設定します。

![ruby debug
001](../../images/asciidoc/tdd_env/ruby-debug-001.png)

ブレークポイントを設定したらF5を押してプログラムの実行します。そうするとブレークポイント部分でプログラムが停止して変数などの情報が確認できるようになります。

![ruby debug 002](../../images/asciidoc/tdd_env/ruby-debug-002.png)

画面上の実行ボタンを押すと次のブレークポイントに移動します。

![ruby debug 003](../../images/asciidoc/tdd_env/ruby-debug-003.png)

デバッガを終了するには終了ボタンを押します。

![ruby debug 004](../../images/asciidoc/tdd_env/ruby-debug-004.png)

ブレークポイントを再度押すことで解除ができます。

![ruby debug 005](../../images/asciidoc/tdd_env/ruby-debug-005.png)

## プログラムをレポジトリに保存する

`全ての変更をステージ` を選択します。

![ruby git 001](../../images/asciidoc/tdd_env/ruby-git-001.png)

変更内容に `feat: HelloWorld` と入力して `コミット` を押します。

![ruby git 002](../../images/asciidoc/tdd_env/ruby-git-002.png)

変更内容は `GitLens` から確認できます。

![ruby git 003](../../images/asciidoc/tdd_env/ruby-git-003.png)
