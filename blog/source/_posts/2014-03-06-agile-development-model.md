---
layout: post
title: "アジャイル開発モデル"
date: 2014-03-06 13:21:17 +0900
comments: true
categories: [マネジメント,エンジニアリング]
tags: [アジャイル開発]
published: true
---

<div style="position:relative;height:300px;width:640px;padding:1px;background:#333;"><a href="http://www.flickr.com/photos/seattlemunicipalarchives/4818952324/" target="_blank"><img src="http://farm5.static.flickr.com/4120/4818952324_a2cce9be1b_z.jpg?zz=1" alt="Engineering Department employees, 1962" style="position:absolute;clip:rect(102px 899px 402px -1px);margin:-102px 0 0 1px;padding-bottom:5px;" /></a><span style="position:absolute;bottom:0;right:0;background:#333;color:#DDD;font-size:10px;padding:3px;">Engineering Department employees, 1962 / Seattle Municipal Archives</span></div>
<hr>
アジャイル開発は２つの領域に分けられる。  
ひとつめは主にプロジェクトの計画・運営に関わるマネジメント領域。  
ふたつめは設計・開発に関わるエンジニアリング領域である。
<!-- more -->

## 構成 ##

+ [概要](#1)
+ [マネジメント](#2)
+ [エンジニアリング](#3)
+ [まとめ](#4)
+ [参考リンク](#5)
+ [参考文献](#6)

## <a name="1">概要</a> ##
## <a name="2">マネジメント</a> ##
### マネジメント領域概要 ###

<a href="http://www.flickr.com/photos/k2works/12945694205/" title="agile_adaption_02 by k2works, on Flickr"><img src="https://farm8.staticflickr.com/7337/12945694205_57475f777f.jpg" width="500" height="308" alt="agile_adaption_02"></a>

#### 方針 ####

##### インセプションデッキ #####

<a href="http://www.flickr.com/photos/k2works/12962680524/" title="inseption_deck_01 by k2works, on Flickr"><img src="https://farm8.staticflickr.com/7340/12962680524_52e6b611d1.jpg" width="500" height="290" alt="inseption_deck_01"></a>

##### 全体像を捉える #####

+ 我々はなぜここにいるのか？

+ エレベーターピッチを作る

+ パッケージデザインを作る

+ やらないことリストを作る

+ 「ご近所さん」を探せ

##### 具現化させる #####

+ 解決策を描く

+ 夜も眠れなくなるような問題は何だろう？

+ 期間を見極める

+ 何を諦めるのかはっきりさせる

+ 何がどれだけ必要なのか

##### 何を諦めるのかはっきりさせる #####

+ 時間
+ 予算
+ 品質
+ スコープ

##### 何がどれだけ必要なのか #####

+ いつ完了するのか？

+ いくらかかるのか？

#### 計画 ####
##### アジャイルな計画づくりとは #####

>チームの開発速度を測定して、その速度をもとに、いつ頃すべて完了させられるのかプロジェクトの完了時期を見通せるようにすることでしかない

>『アジャイルサムライ』

##### ユーザーストーリー #####

+ 顧客にとって何かしらの価値で書かれていること
  + 誰のためのストーリーで
  + 何をしたいか
  + なぜそうしたいのか

        <ユーザーの種類>として
        <達成したいゴール>をしたい
        なぜなら<理由>だからだ

+ INVEST
  + 独立していること
  + 交渉の余地がある
  + テストができる
  + 小さい、見積もれる

##### ストーリー収集ワークショップ #####

1. 大きくて見通しのよい部屋を用意する

1. 図をたくさん書く

1. ユーザーストーリーをたくさん書く

1. その他もろもろをプレインストーミング

1. リストを磨きあげる

##### 見積もり #####

+ 相対図を見積もる

+ ポイントで見積もる

+ 見積もり技法
  + 三角測量
  + プランニングポーカー

##### 計画の立て方 #####

+ 顧客にとって価値ある成果を届けられる計画

+ わかりやすくありのままを伝える誠実な計画

+ 約束したことを守り続けられる計画

+ 必要に応じて変更できる計画

##### 初回の計画づくり #####

1. リリースを定義する

1. プロジェクト規模を見極める

1. 優先順位をつける

1. チームのベロシティを見積もる

1. 期日を仮決めする

#### 運営 ####

<a href="http://www.flickr.com/photos/k2works/12962343063/" title="agile_operation_01 by k2works, on Flickr"><img src="https://farm8.staticflickr.com/7420/12962343063_5a93dab828.jpg" width="500" height="188" alt="agile_operation_01"></a>

##### 価値ある成果を毎週届ける #####

1. 分析と設計：作業の段取りをする
   + 「必要な分だけを、必要なときに」分析する
   + それからペルソナを作ろう
   + ペーパープロトタイプでいろんなデザインをどんどん作ろう
   + 受け入れテストを書いて、ストーリーの満足条件を定義しよう

1. 開発：作業する
   + 自動化されたテストを書く
   + 設計を継続的に発見させていき、改善し続ける
   + ちゃんと動くソフトウエアであり続けるために、コードを継続的にインテグレーションする
   + 顧客がシステムについて語る言葉に合わせてコードを書く

1. テスト：作業の結果を確認する
   + カンバン・・・仕掛り(WIP:Work In Progress)にできる作業の上限を設けていること
   + イテレーションのプレッシャーから開放される
   + １回のイテレーションに収まらない仕事にも取り組める
   + 期待をマネジメントしやすい

##### アジャイルな意思疎通の作戦 #####

+ 今回のイテレーションの作業に備える(ストーリー計画ミーティング)
+ 今回のイテレーションのフィードバックを得る(ショーケース)
+ 次回のイテレーション計画を立てる(イテレーション計画ミーティング)
+ 次回のイテレーションで改善できる余地を探す(ミニふりかえり)

##### 現場の状況を目に見えるようにする #####

+ ストーリーボード
+ リリースボード
+ ベロシティとバーンダウンチャート
+ インセプションデッキ(壁のスペースに余裕があれば)
+ チームの約束(Working Agreements)
+ チームが大事にすること(Shared Values)

#### 組織 ####

##### アジャイルチーム #####

+ きっちり区別しない役割分担。継続的な開発工程。チームで成果責任を果たそうする態度
+ チームをアジャイルにするためのコツ
  + 同じ仕事場で働く
  + 積極的に深く関わる顧客の存在
  + 自己組織化
  + 成果責任と権限移譲
  + 職能横断型チーム

+ 顧客
  + 何を作るか決める
  + 優先順位をつける
  + スコープについて厳しい決断を下す

+ 開発チーム
  + アナリスト
  + プログラム
  + テスター
  + UXデザイナ
  + プロジェクトマネージャー  

## <a name="3">エンジニアリング</a> ##
### エンジニアリング領域概要 ###

<a href="http://www.flickr.com/photos/k2works/12946099604/" title="agile_adaption_03 by k2works, on Flickr"><img src="https://farm3.staticflickr.com/2870/12946099604_9c44e46329.jpg" width="500" height="307" alt="agile_adaption_03"></a>

#### ユニットテスト ####

+ メソッドレベルの粒度で書く
+ 目的は変更の結果が期待通りになっていることをあきらかにすること
+ テスコードはプロダクトコードには含めない
+ メリット
  + 素早いフィードバックが得られる
  + 極めて低コストにリグレッションテストを実行できる
  + デバック時間を大幅に削減できる
  + 自身を持ってデプロイできる

#### リファクタリング ####

ソフトウエアの整合性を保ちながら、設計を少しずつ改善していける方法

+ 変数の名前変更
+ メソッドの名前変更
+ コードをシンプルに
+ メソッドの抽出
+ 変数のインライン化

#### テスト駆動開発 ####

以下のサイクルを回しながら、開発をすすめていく方法

1. レッド
1. グリーン
1. リファクタリング

ルールその１:失敗するテストをひとつ書くまでは、新しいコードを一切書かない

ルールその２:「危なっかしい所」をすべてテストする

>プログラマはまず、あたかもテスト対象のプロダクトコードが既に存在しているかのように考える。そして、それを呼び出して使うのに必要な、最低限のコードをテストコードとして表現する。

>『アジャイルサムライ』

#### 継続的インテグレーション ####

+ ソースコードリポジトリ
+ チェックイン手順
+ ビルドの自動化
+ 作業単位を小さくしようとする姿勢

## <a name="4">まとめ</a> ##
以上、２つの領域からアジャイル開発モデルを整理したがその目的は『毎週、価値のある成果を届ける』ことであり方法論はその目的を実現する手段にすぎない。目的を達成できなければいくら方法論をなぞったとしてそれはアジャイルでないし逆に方法論と違っていても目的を達成できればそれはアジャイルであるといえる。

## <a name="5">参考リンク</a> ##
+ [アジャイルソフトウエア開発宣言](http://www.agilemanifesto.org/iso/ja/)

+ [アジャイルソフトウェアの12の原則](http://www.agilemanifesto.org/iso/ja/principles.html)

## <a name="6">参考文献</a> ##
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?t=k2works0c-22&o=9&p=8&l=as1&asins=1934356581&ref=qf_sp_asin_til&fc1=000000&IS2=1&lt1=_blank&m=amazon&lc1=0000FF&bc1=000000&bg1=FFFFFF&f=ifr" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?t=k2works0c-22&o=9&p=8&l=as1&asins=4274068560&ref=qf_sp_asin_til&fc1=000000&IS2=1&lt1=_blank&m=amazon&lc1=0000FF&bc1=000000&bg1=FFFFFF&f=ifr" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>