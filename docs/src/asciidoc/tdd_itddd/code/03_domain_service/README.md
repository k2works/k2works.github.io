# テスト駆動開発からはじめるドメイン駆動設計入門

## 概要

## 前提

| ソフトウェア   | バージョン | 備考 |
| :------------- | :--------- | :--- |
| ruby         | 2.7.0     |      |

### Quick Start

#### クラウドIDE使用の場合

##### 以下のリンクからクラウドIDEを起動する

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/k2works/tdd_itddd)

##### クラウドIDEが起動したらコマンドラインに以下のコマンドラインを入力してセットアップを開始する。

```bash
$ bundle
```

##### セットアップが完了したらテストが動くか確認する。

```bash
$ ruby test/hello_test.rb 
Started with run options --seed 40372

HelloTest
  test_greeting                                                   PASS (0.00s)

Finished in 0.00124s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
```

##### 自動化

`rake` コマンドを実行すると一連の操作が自動化さてファイルを編集するたびにテストが自動実行されるようになります。

```bash
$ rake
guard start
03:35:23 - INFO - Guard::Minitest 2.4.6 is running, with Minitest::Unit 5.14.0!
03:35:23 - INFO - Running: all tests
Started with run options --guard --seed 49364

HelloTest
  test_greeting                                                   PASS (0.00s)

Finished in 0.00157s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips

03:35:24 - INFO - Inspecting Ruby code style of all files
 1/1 file |============================== 100 ===============================>| Time: 00:00:00 

1 file inspected, no offenses detected
03:35:26 - INFO - Guard is now watching at '/workspace/tdd_itddd'
[1] guard(main)> 
```

詳細は [テスト駆動開発から始めるRuby入門 ~ソフトウェア開発の三種の神器を準備する~](https://qiita.com/k2works/items/385dc16333e065d69bd6) をご参照ください。