# 自動化から始めるテスト駆動開発

エピソード1ではテスト駆動開発のゴールが **動作するきれいなコード** であることを学びました。
では、良いコードを書き続けるためには何が必要になるでしょうか？それは
[ソフトウェア開発の三種の神器](https://t-wada.hatenablog.jp/entry/clean-code-that-works)
と呼ばれるものです。

> 今日のソフトウェア開発の世界において絶対になければならない3つの技術的な柱があります。
> 三本柱と言ったり、三種の神器と言ったりしていますが、それらは
> 
>   - バージョン管理
> 
>   - テスティング
> 
>   - 自動化
> 
> の3つです。
> 
> —  https://t-wada.hatenablog.jp/entry/clean-code-that-works 

**バージョン管理** と **テスティング** に関してはエピソード1で触れました。本エピソードでは最後の **自動化**
に関しての解説と次のエピソードに備えたセットアップ作業を実施しておきたいと思います。ですがその前に
**バージョン管理** で1つだけ解説しておきたいことがありますのでそちらから進めて行きたいと思います。

## コミットメッセージ

これまで作業の区切りにごとにレポジトリにコミットしていましたがその際に以下のような書式でメッセージを書いていました。

``` bash
$ git commit -m 'refactor: メソッドの抽出'
```

この書式は
[Angularルール](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#type)に従っています。具体的には、それぞれのコミットメッセージはヘッダ、ボディ、フッタで構成されています。ヘッダはタイプ、スコープ、タイトルというフォーマットで構成されています。

    <タイプ>(<スコープ>): <タイトル>
    <空行>
    <ボディ>
    <空行>
    <フッタ>

ヘッダは必須です。 ヘッダのスコープは任意です。 コミットメッセージの長さは50文字までにしてください。

(そうすることでその他のGitツールと同様にGitHub上で読みやすくなります。)

コミットのタイプは次を用いて下さい。

  - feat: A new feature (新しい機能)

  - fix: A bug fix (バグ修正)

  - docs: Documentation only changes (ドキュメント変更のみ)

  - style: Changes that do not affect the meaning of the code
    (white-space, formatting, missing semi-colons, etc) (コードに影響を与えない変更)

  - refactor: A code change that neither fixes a bug nor adds a feature
    (機能追加でもバグ修正でもないコード変更)

  - perf: A code change that improves performance (パフォーマンスを改善するコード変更)

  - test: Adding missing or correcting existing tests
    (存在しないテストの追加、または既存のテストの修正)

  - chore: Changes to the build process or auxiliary tools and libraries
    such as documentation generation
    (ドキュメント生成のような、補助ツールやライブラリやビルドプロセスの変更)

コミットメッセージにつけるプリフィックスに関しては [【今日からできる】コミットメッセージに 「プレフィックス」
をつけるだけで、開発効率が上がった話](https://qiita.com/numanomanu/items/45dd285b286a1f7280ed)
を参照ください。

## パッケージマネージャ

では **自動化** の準備に入りたいのですがそのためにはいくつかの外部プログラムを利用する必要があります。そのためのツールが
**RubyGems**
> です。

> RubyGemsとは、Rubyで記述されたサードパーティ製のライブラリを管理するためのツールで、RubyGemsで扱うライブラリをgemパッケージと呼びます。
> 
> —  かんたんRuby 

**RubyGems** はすでに何度か使っています。例えばエピソード1の初めの `minitest-reporters`
のインストールなどです。

``` bash
$ gem install minitest-reporters
```

では、これからもこのようにして必要な外部プログラムを一つ一つインストールしていくのでしょうか？また、開発用マシンを変えた時にも同じことを繰り返さないといけないのでしょうか？面倒ですよね。そのような面倒なことをしないで済む仕組みがRubyには用意されています。それが
**Bundler**
> です。

> Bundlerとは、作成したアプリケーションがどのgemパッケージに依存しているか、そしてインストールしているバージョンはいくつかという情報を管理するためのgemパッケージです。
> 
> —  かんたんRuby 

**Bundler** をインストールしてgemパッケージを束ねましょう。

``` bash
$ gem install bundler
$ bundle init
```

`Gemfile` が作成されます。

``` ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

# gem "rails"
```

`# gem "rails"` の部分を以下の様に書き換えます。

``` ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem 'rubocop', require: false
```

書き換えたら `bundle install` でgemパッケージをインストールします。

``` bash
$ bundle install
Fetching gem metadata from https://rubygems.org/....................
Resolving dependencies...
Using ast 2.4.0
Using bundler 2.1.4
Using jaro_winkler 1.5.4
Using parallel 1.19.1
Fetching parser 2.7.0.2
Installing parser 2.7.0.2
Using rainbow 3.0.0
Using ruby-progressbar 1.10.1
Fetching unicode-display_width 1.6.1
Installing unicode-display_width 1.6.1
Fetching rubocop 0.79.0
Installing rubocop 0.79.0
Bundle complete! 1 Gemfile dependency, 9 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
```

これで次の準備ができました。

## 静的コード解析

良いコードを書き続けるためにはコードの品質を維持していく必要があります。エピソード1では **テスト駆動開発**
によりプログラムを動かしながら品質の改善していきました。出来上がったコードに対する品質チェックの方法として
**静的コード解析** があります。Ruby用 **静的コード解析** ツール
[RuboCop](https://github.com/rubocop-hq/rubocop) を使って確認してみましょう。プログラムは先程
**Bundler** を使ってインストールしたので以下のコマンドを実行します。

``` bash
 $ rubocop
Inspecting 5 files
CCCWW

Offenses:

Gemfile:3:8: C: Style/StringLiterals: Prefer single-quoted strings when you don't need string interpolation or special symbols.
source "https://rubygems.org"
       ^^^^^^^^^^^^^^^^^^^^^^
Gemfile:5:21: C: Layout/SpaceInsideBlockBraces: Space between { and | missing.
git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }
                    ^^
...
```

なにかいろいろ出てきましたね。RuboCopの詳細に関しては [RuboCop is
何？](https://qiita.com/tomohiii/items/1a17018b5a48b8284a8b)を参照ください。`--lint`
オプションをつけて実施してみましょう。

``` bash
$ rubocop --lint
Inspecting 5 files
...W.

Offenses:

test/fizz_buzz_test.rb:109:7: : Parenthesize the param %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i } to make sure that the block will be associated with the %w[2 4 13 3 1 10].sort method call.
      assert_equal %w[1 2 3 4 10 13], ...
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test/fizz_buzz_test.rb:111:7: W: Lint/AmbiguousBlockAssociation: Parenthesize the param %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i } to make sure that the block will be associated with the %w[2 4 13 3 1 10].sort method call.
      assert_equal %w[13 10 4 3 2 1], ...
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5 files inspected, 2 offenses detected
```

また何やら出てきましたね。 [W:
Lint/AmbiguousBlockAssociation](https://rubocop.readthedocs.io/en/latest/cops_lint/#lintambiguousblockassociation)のメッセージを調べたところ、`fizz_buzz_test.rb`
の以下の学習用テストコードは書き方がよろしくないようですね。

``` ruby
...
      def test_指定した評価式で並び変えた配列を返す
        assert_equal %w[1 10 13 2 3 4], %w[2 4 13 3 1 10].sort
        assert_equal %w[1 2 3 4 10 13],
                     %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i }
        assert_equal %w[13 10 4 3 2 1],
                     %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i }
      end
...
```

**説明用変数の導入** を使ってテストコードをリファクタリングしておきましょう。

``` ruby
...
    def test_指定した評価式で並び変えた配列を返す
      result1 = %w[2 4 13 3 1 10].sort
      result2 = %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i }
      result3 = %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i }

      assert_equal %w[1 10 13 2 3 4], result1
      assert_equal %w[1 2 3 4 10 13], result2
      assert_equal %w[13 10 4 3 2 1], result3
    end
...
```

再度確認します。チェックは通りましたね。

``` bash
$ rubocop --lint
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

テストも実行して壊れていないかも確認しておきます。

``` bash
$ ruby test/fizz_buzz_test.rb
Started with run options --seed 42058

  19/19: [=========================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00257s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

いちいち調べるのも手間なので自動で修正できるところは修正してもらいましょう。

``` bash
$ rubocop --auto-correct
```

再度確認します。

``` bash
 $ rubocop
Inspecting 5 files
...CC

Offenses:

test/fizz_buzz_test.rb:15:11: C: Naming/MethodName: Use snake_case for method names.
      def test_3を渡したら文字列Fizzを返す
          ^^^^^^^^^^^^^^^^^^^^^
...
```

まだ、自動修正できなかった部分があるようですね。この部分はチェック対象から外すことにしましょう。

``` bash
$ rubocop --auto-gen-config
Added inheritance from `.rubocop_todo.yml` in `.rubocop.yml`.
Phase 1 of 2: run Layout/LineLength cop
Inspecting 5 files
.....

5 files inspected, no offenses detected
Created .rubocop_todo.yml.
Phase 2 of 2: run all cops
Inspecting 5 files
.C.CW

5 files inspected, 110 offenses detected
Created .rubocop_todo.yml.
```

生成された `.rubocop_todo.yml` の以下の部分を変更します。

``` yml
...
# Offense count: 32
# Configuration parameters: IgnoredPatterns.
# SupportedStyles: snake_case, camelCase
Naming/MethodName:
  EnforcedStyle: snake_case
  Exclude:
    - 'test/fizz_buzz_test.rb'
...
```

再度チェックを実行します。

``` bash
$ rubocop
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

セットアップができたのでここでコミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'chore: 静的コード解析セットアップ'
```

## コードフォーマッタ

良いコードであるためにはフォーマットも大切な要素です。

> 優れたソースコードは「目に優しい」ものでなければいけない。
> 
> —  リーダブルコード 

Rubyにはいくつかフォーマットアプリケーションはあるのですがここは `RuboCop`
の機能を使って実現することにしましょう。以下のコードのフォーマットをわざと崩してみます。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number)
          isFizz = number.modulo(3).zero?
    isBuzz = number.modulo(5).zero?

    return 'FizzBuzz' if isFizz && isBuzz
    return 'Fizz' if isFizz
    return 'Buzz' if isBuzz

    number.to_s
  end

  def self.generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

スタイルオプションをつけてチェックしてみます。

``` bash
$ rubocop --only Layout
Inspecting 5 files
.C...

Offenses:

lib/fizz_buzz.rb:7:3: C: Layout/IndentationWidth: Use 2 (not 8) spaces for indentation.
          isFizz = number.modulo(3).zero?
  ^^^^^^^^
lib/fizz_buzz.rb:8:5: C: Layout/IndentationConsistency: Inconsistent indentation detected.
    isBuzz = number.modulo(5).zero?
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:10:5: C: Layout/IndentationConsistency: Inconsistent indentation detected.
    return 'FizzBuzz' if isFizz && isBuzz
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:11:5: C: Layout/IndentationConsistency: Inconsistent indentation detected.
    return 'Fizz' if isFizz
    ^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:12:5: C: Layout/IndentationConsistency: Inconsistent indentation detected.
    return 'Buzz' if isBuzz
    ^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:14:5: C: Layout/IndentationConsistency: Inconsistent indentation detected.
    number.to_s
    ^^^^^^^^^^^

5 files inspected, 6 offenses detected
```

編集した部分が `Use 2 (not 8) spaces for indentation.` と指摘されています。
`--fix-layout` オプションで自動保存しておきましょう。

``` bash
$ rubocop --fix-layout
Inspecting 5 files
.C...

Offenses:

lib/fizz_buzz.rb:7:3: C: [Corrected] Layout/IndentationWidth: Use 2 (not 8) spaces for indentation.
          isFizz = number.modulo(3).zero?
  ^^^^^^^^
lib/fizz_buzz.rb:8:5: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
    isBuzz = number.modulo(5).zero?
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:8:11: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
          isBuzz = number.modulo(5).zero?
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:10:5: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
    return 'FizzBuzz' if isFizz && isBuzz
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:10:11: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
          return 'FizzBuzz' if isFizz && isBuzz
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:11:5: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
    return 'Fizz' if isFizz
    ^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:11:11: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
          return 'Fizz' if isFizz
          ^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:12:5: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
    return 'Buzz' if isBuzz
    ^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:12:11: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
          return 'Buzz' if isBuzz
          ^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:14:5: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
    number.to_s
    ^^^^^^^^^^^
lib/fizz_buzz.rb:14:11: C: [Corrected] Layout/IndentationConsistency: Inconsistent indentation detected.
          number.to_s
          ^^^^^^^^^^^

5 files inspected, 11 offenses detected, 11 offenses corrected
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number)
    isFizz = number.modulo(3).zero?
    isBuzz = number.modulo(5).zero?

    return 'FizzBuzz' if isFizz && isBuzz
    return 'Fizz' if isFizz
    return 'Buzz' if isBuzz

    number.to_s
  end

  def self.generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

``` bash
$ rubocop --only Layout
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

フォーマットが修正されたことが確認できましたね。ちなみに `--auto-correct`
オプションでもフォーマットをしてくれるので通常はこちらのオプションで問題ないと思います。

## コードカバレッジ

静的コードコード解析による品質の確認はできました。では動的なテストに関してはどうでしょうか？ **コードカバレッジ** を確認する必要あります。

> コード網羅率（コードもうらりつ、英: Code coverage
> ）コードカバレッジは、ソフトウェアテストで用いられる尺度の1つである。プログラムのソースコードがテストされた割合を意味する。この場合のテストはコードを見ながら行うもので、ホワイトボックステストに分類される。
> 
> —  ウィキペディア 

Ruby用 **コードカバレッジ** 検出プログラムとして
[SimpleCov](https://github.com/colszowka/simplecov)を使います。Gemfileに追加して
**Bundler** でインストールをしましょう。

``` ruby
# frozen_string_literal: true

source 'https://rubygems.org'

git_source(:github) { |repo_name| "https://github.com/#{repo_name}" }

gem 'minitest'
gem 'minitest-reporters'
gem 'rubocop', require: false
gem 'simplecov', require: false, group: :test
```

``` bash
$ bundle install
Fetching gem metadata from https://rubygems.org/..................
Resolving dependencies...
Fetching ansi 1.5.0
Installing ansi 1.5.0
Using ast 2.4.0
Fetching builder 3.2.4
Installing builder 3.2.4
Using bundler 2.1.4
Using docile 1.3.2
Using jaro_winkler 1.5.4
Using json 2.3.0
Fetching minitest 5.14.0
Installing minitest 5.14.0
Using ruby-progressbar 1.10.1
Fetching minitest-reporters 1.4.2
Installing minitest-reporters 1.4.2
Using parallel 1.19.1
Using parser 2.7.0.2
Using rainbow 3.0.0
Using unicode-display_width 1.6.1
Using rubocop 0.79.0
Using simplecov-html 0.10.2
Using simplecov 0.17.1
Bundle complete! 4 Gemfile dependencies, 17 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
```

サイトの説明に従ってテストコードの先頭に以下のコードを追加します。

``` ruby
# frozen_string_literal: true
require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'
...
```

テストを実施します。

``` bash
$ ruby test/fizz_buzz_test.rb
Started with run options --seed 10538

  19/19: [===============================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00297s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

テスト実行後に `coverage` というフォルダが作成されます。その中の `index.html`
を開くとカバレッジ状況を確認できます。セットアップが完了したらコミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'chore: コードカバレッジセットアップ'
```

## タスクランナー

ここまででテストの実行、静的コード解析、コードフォーマット、コードカバレッジを実施することができるようになりました。でもコマンドを実行するのにそれぞれコマンドを覚えておくのは面倒ですよね。例えばテストの実行は

``` bash
$ ruby test/fizz_buzz_test.rb
Started with run options --seed 21943

  19/19: [=======================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00261s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

このようにしていました。では静的コードの解析はどうやりましたか？フォーマットはどうやりましたか？調べるのも面倒ですよね。いちいち調べるのが面倒なことは全部
**タスクランナー** にやらせるようにしましょう。

> タスクランナーとは、アプリケーションのビルドなど、一定の手順で行う作業をコマンド一つで実行できるように予めタスクとして定義したものです。
> 
> —  かんたんRuby 

Rubyの **タスクランナー** は `Rake`
> です。

> RakeはRubyにおけるタスクランナーです。rakeコマンドと起点となるRakefileというタスクを記述するファイルを用意することで、タスクの実行や登録されたタスクの一覧表示を行えます。
> 
> —  かんたんRuby 

早速、テストタスクから作成しましょう。まず `Rakefile` を作ります。Mac/Linuxでは `touch`
コマンドでファイルを作れます。Windowsの場合は手作業で追加してください。

``` bash
$ touch Rakefile
```

``` ruby
require 'rake/testtask'

task default: [:test]

Rake::TestTask.new do |test|
  test.test_files = Dir['./test/fizz_buzz_test.rb']
  test.verbose = true
end
```

タスクが登録されたか確認してみましょう。

``` bash
$ rake -T
rake test  # Run tests
```

タスクが登録されたことが確認できたのでタスクを実行します。

``` bash
$ rake test
/Users/k2works/.rbenv/versions/2.5.5/bin/ruby -w -I"lib" -I"/Users/k2works/.rbenv/versions/2.5.5/lib/ruby/gems/2.5.0/gems/rake-13.0.1/lib" "/Users/k2works/.rbenv/versions/2.5.5/lib/ruby/gems/2.5.0/gems/rake-13.0.1/lib/rake/rake_test_loader.rb" "./test/fizz_buzz_test.rb"
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:79: warning: method redefined; discarding old test_特定の条件を満たす要素だけを配列に入れて返す
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:74: warning: previous definition of test_特定の条件を満たす要素だけを配列に入れて返す was here
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:94: warning: method redefined; discarding old test_新しい要素の配列を返す
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:89: warning: previous definition of test_新しい要素の配列を返す was here
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:104: warning: method redefined; discarding old test_配列の中から条件に一致する要素を取得する
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:99: warning: previous definition of test_配列の中から条件に一致する要素を取得する was here
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:138: warning: method redefined; discarding old test_畳み込み演算を行う
/Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/test/fizz_buzz_test.rb:133: warning: previous definition of test_畳み込み演算を行う was here
Started with run options --seed 5886

  19/19: [=======================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00271s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

テストは実施されたのですが警告メッセージが表示されるようになりました。メッセージの内容としては **学習用テスト**
のテストメソッド名が重複していることが理由のようです。せっかくなので修正しておきましょう。

``` ruby
class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
  ...
  end

  describe '配列や繰り返し処理を理解する' do
    def test_繰り返し処理
      $stdout = StringIO.new
      [1, 2, 3].each { |i| p i * i }
      output = $stdout.string

      assert_equal "1\n" + "4\n" + "9\n", output
    end

    def test_特定の条件を満たす要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].select(&:integer?)
      assert_equal [2, 4], result
    end

    def test_特定の条件を満たす要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].find_all(&:integer?)
      assert_equal [2, 4], result
    end

    def test_特定の条件を満たさない要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].reject(&:integer?)
      assert_equal [1.1, 3.3], result
    end

    def test_新しい要素の配列を返す
      result = %w[apple orange pineapple strawberry].map(&:size)
      assert_equal [5, 6, 9, 10], result
    end

    def test_新しい要素の配列を返す
      result = %w[apple orange pineapple strawberry].collect(&:size)
      assert_equal [5, 6, 9, 10], result
    end

    def test_配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry].find(&:size)
      assert_equal 'apple', result
    end

    def test_配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry].detect(&:size)
      assert_equal 'apple', result
    end

    def test_指定した評価式で並び変えた配列を返す
      result1 = %w[2 4 13 3 1 10].sort
      result2 = %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i }
      result3 = %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i }

      assert_equal %w[1 10 13 2 3 4], result1
      assert_equal %w[1 2 3 4 10 13], result2
      assert_equal %w[13 10 4 3 2 1], result3
    end

    def test_配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry apricot].grep(/^a/)
      assert_equal %w[apple apricot], result
    end

    def test_ブロック内の条件式が真である間までの要素を返す
      result = [1, 2, 3, 4, 5, 6, 7, 8, 9].take_while { |item| item < 6 }
      assert_equal [1, 2, 3, 4, 5], result
    end

    def test_ブロック内の条件式が真である以降の要素を返す
      result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].drop_while { |item| item < 6 }
      assert_equal [6, 7, 8, 9, 10], result
    end

    def test_畳み込み演算を行う
      result = [1, 2, 3, 4, 5].inject(0) { |total, n| total + n }
      assert_equal 15, result
    end

    def test_畳み込み演算を行う
      result = [1, 2, 3, 4, 5].reduce { |total, n| total + n }
      assert_equal 15, result
    end
  end
end
```

**メソッド名の変更** を適用してリファクタリングしましょう。

``` ruby
class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
  ...
  end

  describe '配列や繰り返し処理を理解する' do
    def test_繰り返し処理
      $stdout = StringIO.new
      [1, 2, 3].each { |i| p i * i }
      output = $stdout.string

      assert_equal "1\n" + "4\n" + "9\n", output
    end

    def test_selectメソッドで特定の条件を満たす要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].select(&:integer?)
      assert_equal [2, 4], result
    end

    def test_find_allメソッドで特定の条件を満たす要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].find_all(&:integer?)
      assert_equal [2, 4], result
    end

    def test_特定の条件を満たさない要素だけを配列に入れて返す
      result = [1.1, 2, 3.3, 4].reject(&:integer?)
      assert_equal [1.1, 3.3], result
    end

    def test_mapメソッドで新しい要素の配列を返す
      result = %w[apple orange pineapple strawberry].map(&:size)
      assert_equal [5, 6, 9, 10], result
    end

    def test_collectメソッドで新しい要素の配列を返す
      result = %w[apple orange pineapple strawberry].collect(&:size)
      assert_equal [5, 6, 9, 10], result
    end

    def test_findメソッドで配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry].find(&:size)
      assert_equal 'apple', result
    end

    def test_detectメソッドで配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry].detect(&:size)
      assert_equal 'apple', result
    end

    def test_指定した評価式で並び変えた配列を返す
      result1 = %w[2 4 13 3 1 10].sort
      result2 = %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i }
      result3 = %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i }

      assert_equal %w[1 10 13 2 3 4], result1
      assert_equal %w[1 2 3 4 10 13], result2
      assert_equal %w[13 10 4 3 2 1], result3
    end

    def test_配列の中から条件に一致する要素を取得する
      result = %w[apple orange pineapple strawberry apricot].grep(/^a/)
      assert_equal %w[apple apricot], result
    end

    def test_ブロック内の条件式が真である間までの要素を返す
      result = [1, 2, 3, 4, 5, 6, 7, 8, 9].take_while { |item| item < 6 }
      assert_equal [1, 2, 3, 4, 5], result
    end

    def test_ブロック内の条件式が真である以降の要素を返す
      result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].drop_while { |item| item < 6 }
      assert_equal [6, 7, 8, 9, 10], result
    end

    def test_injectメソッドで畳み込み演算を行う
      result = [1, 2, 3, 4, 5].inject(0) { |total, n| total + n }
      assert_equal 15, result
    end

    def test_reduceメソッドで畳み込み演算を行う
      result = [1, 2, 3, 4, 5].reduce { |total, n| total + n }
      assert_equal 15, result
    end
  end
end
```

テストを再実行して警告メッセージが消えたこと確認します。

``` bash
$ rake test
/home/gitpod/.rvm/rubies/ruby-2.6.3/bin/ruby -w -I"lib" -I"/home/gitpod/.rvm/rubies/ruby-2.6.3/lib/ruby/gems/2.6.0/gems/rake-12.3.2/lib" "/home/gitpod/.rvm/rubies/ruby-2.6.3/lib/ruby/gems/2.6.0/gems/rake-12.3.2/lib/rake/rake_test_loader.rb" "./test/fizz_buzz_test.rb"
Started with run options --seed 10674

  24/24: [=========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00396s
24 tests, 26 assertions, 0 failures, 0 errors, 0 skips
```

テストタスクが実行されたことが確認できたので引き続き静的コードの解析タスクを追加します。こちらも開発元がタスクを用意しているのでそちらを使うことにします。

``` ruby
require 'rake/testtask'
require 'rubocop/rake_task'
RuboCop::RakeTask.new

task default: [:test]

Rake::TestTask.new do |test|
  test.test_files = Dir['./test/fizz_buzz_test.rb']
  test.verbose = true
end
```

タスクが登録されたことを確認します。

``` bash
$ rake -T
rake rubocop               # Run RuboCop
rake rubocop:auto_correct  # Auto-correct RuboCop offenses
rake test                  # Run tests
```

続いてタスクを実行してみましょう。

``` bash
$ rake rubocop
Running RuboCop...
Inspecting 5 files
.C..C

Offenses:

Rakefile:1:1: C: Style/FrozenStringLiteralComment: Missing magic comment # frozen_string_literal: true.
require 'rake/testtask'
^
Rakefile:10:4: C: Layout/TrailingEmptyLines: Final newline missing.
end

test/fizz_buzz_test.rb:2:1: C: Layout/EmptyLineAfterMagicComment: Add an empty line after magic comments.
require 'simplecov'
^
test/fizz_buzz_test.rb:148:6: C: Layout/TrailingWhitespace: Trailing whitespace detected.
  end
     ^^

5 files inspected,
```

いろいろ出てきましたので自動修正しましょう。

``` bash
$ rake rubocop:auto_correct
Running RuboCop...
Inspecting 5 files
.C..C

Offenses:

Rakefile:1:1: C: [Corrected] Style/FrozenStringLiteralComment: Missing magic comment # frozen_string_literal: true.
require 'rake/testtask'
^
Rakefile:2:1: C: [Corrected] Layout/EmptyLineAfterMagicComment: Add an empty line after magic comments.
require 'rake/testtask'
^
Rakefile:10:4: C: [Corrected] Layout/TrailingEmptyLines: Final newline missing.
end

test/fizz_buzz_test.rb:2:1: C: [Corrected] Layout/EmptyLineAfterMagicComment: Add an empty line after magic comments.
require 'simplecov'
^
test/fizz_buzz_test.rb:148:6: C: [Corrected] Layout/TrailingWhitespace: Trailing whitespace detected.
  end
     ^^

5 files inspected, 5 offenses detected, 5 offenses corrected
```

``` ruby
$ rake rubocop
Running RuboCop...
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

うまく修正されたようですね。後、フォーマットコマンドもタスクとして追加しておきましょう。こちらは開発元が用意していないタスクなので以下のように追加します。

``` ruby
# frozen_string_literal: true

require 'rake/testtask'
require 'rubocop/rake_task'
RuboCop::RakeTask.new

task default: [:test]

Rake::TestTask.new do |test|
  test.test_files = Dir['./test/fizz_buzz_test.rb']
  test.verbose = true
end

desc "Run Format"
task :format do
  sh "rubocop --fix-layout"
end
```

``` bash
$ rake -T
rake format                # Run Format
rake rubocop               # Run RuboCop
rake rubocop:auto_correct  # Auto-correct RuboCop offenses
rake test                  # Run tests
```

``` bash
$ rake format
rubocop --fix-layout
Inspecting 5 files
.C...

Offenses:

Rakefile:17:4: C: [Corrected] Layout/TrailingEmptyLines: Final newline missing.
end


5 files inspected, 1 offense detected, 1 offense corrected
```

フォーマットは `rake rubocop:auto_correct`
で一緒にやってくれるので特に必要は無いのですがプログラムの開発元が提供していないタスクを作りたい場合はこのように追加します。セットアップができたのでコミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'chore: タスクランナーセットアップ'
```

## タスクの自動化

良いコードを書くためのタスクをまとめることができました。でも、どうせなら自動で実行できるようにしたいですよね。
タスクを自動実行するためのgemを追加します。
[Guard](https://github.com/guard/guard)とそのプラグインの
[Guard::Shell](https://github.com/guard/guard-shell)
[Guard::Minitest](https://github.com/guard/guard-minitest)
[guard-rubocop](https://github.com/yujinakayama/guard-rubocop)
をインストールします。それぞれの詳細は以下を参照してください。

  - [Ruby | Guard gem
    を利用してファイルの変更を検出し、任意のタスクを自動実行する](https://qiita.com/tbpgr/items/f5be21d8e19dd852d9b7)

  - [guard-shellでソースコードの変更を監視して自動でmake＆実行させる](https://qiita.com/emergent/items/0a38909206844265e0b5)

  - [Rails -
    Guardを使い、ファイル変更時にMinitestやRspecを自動実行する](https://forest-valley17.hatenablog.com/entry/2018/10/05/183521)

<!-- end list -->

``` ruby
# frozen_string_literal: true

source 'https://rubygems.org'

git_source(:github) { |repo_name| "https://github.com/#{repo_name}" }

gem 'guard'
gem 'guard-minitest'
gem 'guard-rubocop'
gem 'guard-shell'
gem 'minitest'
gem 'minitest-reporters'
gem 'rake'
gem 'rubocop', require: false
gem 'simplecov', require: false, group: :test
```

`bundle install` は `bundle` に省略できます。

``` bash
$ bundle
$ guard init
```

`Guardfile` が生成されるので以下の内容に変更します。

``` ruby
# frozen_string_literal: true

# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }
#
guard :shell do
  watch(%r{lib/(.*).rb}) { |_m| `rake test` }
end

guard :minitest do
  # with Minitest::Unit
  watch(%r{test\/*.rb})
end

guard :rubocop, cli: %w[--auto-correct --format fuubar --format html -o ./tmp/rubocop_results.html] do
  watch(/(.*).rb/)
end
```

`guard` が起動するか確認して一旦終了します。

``` bash
$ guard start
Warning: the running version of Bundler (2.1.3) is older than the version that created the lockfile (2.1.4). We suggest you to upgrade to the version that created the lockfile by running `gem install bundler:2.1.4`.
03:49:28 - INFO - Guard::Minitest 2.4.6 is running, with Minitest::Unit 5.14.0!
03:49:28 - INFO - Running: all tests
Coverage report generated for MiniTest to /workspace/tdd_rb/coverage. 4 / 11 LOC (36.36%) covered.
Started with run options --guard --seed 1256

  24/24: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00363s
24 tests, 26 assertions, 0 failures, 0 errors, 0 skips

03:49:28 - INFO - Inspecting Ruby code style of all files
Gemfile:15:46: C: [Corrected] Layout/TrailingEmptyLines: Final newline missing.
gem 'simplecov', require: false, group: :test

Guardfile:17:4: C: [Corrected] Layout/TrailingEmptyLines: Final newline missing.
end

 7/7 files |====================================== 100 =======================================>| Time: 00:00:00

7 files inspected, 2 offenses detected, 2 offenses corrected
03:49:30 - INFO - Guard is now watching at '/workspace/tdd_rb'
[1] guard(main)> exit

03:50:31 - INFO - Bye bye...
```

続いて `Rakefile` にguardタスクを追加します。あと、guardタスクをデフォルトにして `rake`
を実行すると呼び出されるようにしておきます。

``` ruby
# frozen_string_literal: true

require 'rake/testtask'
require 'rubocop/rake_task'
RuboCop::RakeTask.new

task default: [:guard]

Rake::TestTask.new do |test|
  test.test_files = Dir['./test/fizz_buzz_test.rb']
  test.verbose = true
end

desc 'Run Format'
task :format do
  sh 'rubocop --fix-layout'
end

desc 'Run Guard'
task :guard do
  sh 'guard start'
end
```

自動実行タスクを起動しましょう。

``` bash
$ rake
guard start
03:52:01 - INFO - Guard::Minitest 2.4.6 is running, with Minitest::Unit 5.14.0!
03:52:01 - INFO - Running: all tests
Coverage report generated for MiniTest to /workspace/tdd_rb/coverage. 4 / 11 LOC (36.36%) covered.
Started with run options --guard --seed 3219

  24/24: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00844s
24 tests, 26 assertions, 0 failures, 0 errors, 0 skips

03:52:01 - INFO - Inspecting Ruby code style of all files
 7/7 files |====================================== 100 =======================================>| Time: 00:00:00

7 files inspected, no offenses detected
03:52:03 - INFO - Guard is now watching at '/workspace/tdd_rb'
[1] guard(main)>
```

起動したら `fizz_buzz_test.rb` を編集してテストが自動実行されるか確認しましょう。

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
    def setup
      @fizzbuzz = FizzBuzz
    end

    describe '三の倍数の場合' do
      def test_3を渡したら文字列Fizzを返す
        assert_equal 'FizzFizz', @fizzbuzz.generate(3)
      end
    end
...
```

``` bash
05:00:34 - INFO - Running: all tests
Coverage report generated for MiniTest to /workspace/tdd_rb/coverage. 4 / 11 LOC (36.36%) covered.
Started with run options --guard --seed 16292

 FAIL["test_3を渡したら文字列Fizzを返す", #<Minitest::Reporters::Suite:0x000055640e99f080 @name="FizzBuzz::三の倍数の場合">, 0.005698626991943456]
 test_3を渡したら文字列Fizzを返す#FizzBuzz::三の倍数の場合 (0.01s)
        Expected: "FizzFizz"
          Actual: "Fizz"
        /workspace/tdd_rb/test/fizz_buzz_test.rb:18:in `test_3を渡したら文字列Fizzを返す'

  24/24: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00742s
24 tests, 26 assertions, 1 failures, 0 errors, 0 skips

05:00:35 - INFO - Inspecting Ruby code style: test/fizz_buzz_test.rb
 1/1 file |======================================= 100 =======================================>| Time: 00:00:00

1 file inspected, no offenses detected
05:00:36 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/border.png coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/controls.png
 0/0 files |====================================== 100 =======================================>| Time: 00:00:00

0 files inspected, no offenses detected
[1] guard(main)>
```

変更を感知してテストが実行されるた結果失敗していましました。コードを元に戻してテストをパスするようにしておきましょう。テストがパスすることが確認できたらコミットしておきましょう。このときターミナルでは
`guard` が動いているので別ターミナルを開いてコミットを実施すると良いでしょう。

``` bash
$ git add .
$ git commit -m 'chore: タスクの自動化'
```

これで
[ソフトウェア開発の三種の神器](https://t-wada.hatenablog.jp/entry/clean-code-that-works)の最後のアイテムの準備ができました。次回の開発からは最初にコマンドラインで
`rake`
を実行すれば良いコードを書くためのタスクを自動でやってくるようになるのでコードを書くことに集中できるようになりました。では、次のエピソードに進むとしましょう。
