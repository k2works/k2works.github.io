---
layout: post
title: "ビヘイビア駆動開発"
date: 2014-04-09 19:27:00 +0900
comments: true
categories: [マネジメント,エンジニアリング]
tags: [アジャイル開発]
published: true
---
<div style="position:relative;height:300px;width:640px;padding:1px;background:#333;"><a href="http://www.flickr.com/photos/landrovermena/7955060152/" target="_blank"><img src="http://farm9.static.flickr.com/8036/7955060152_eac700f748_z.jpg?zz=1" alt="The All-New Range Rover | Test & Development" style="position:absolute;clip:rect(5px 902px 305px 2px);margin:-5px 0 0 -2px;padding-bottom:5px;" /></a><span style="position:absolute;bottom:0;right:0;background:#333;color:#DDD;font-size:10px;padding:3px;">The All-New Range Rover | Test & Development / landrovermena</span></div>
<hr>

>+ 十分といったら十分
>+ ステークホルダーに価値をもたらす
>+ すべては振る舞いから

<!-- more -->

# 構成 #
+ [ビヘイビア駆動開発(BDD)とは](#1)
+ [実装例](#2)

# 詳細 #

## <a name="1">ビヘイビア駆動開発(BDD)とは</a> ##

### テスト駆動開発(TDD)からビヘイビア駆動開発(BDD)へ

TDD・・・オブジェクトが何をするかではなく、オブジェクトが何であるか。構造に焦点を合わせる。

<a href="https://www.flickr.com/photos/k2works/13635473944" title="TDD by Katuyuki Kakigi, on Flickr"><img src="https://farm3.staticflickr.com/2938/13635473944_bb1b6b7d38_n.jpg" width="319" height="320" alt="TDD"></a>

TDD概念図

BDD・・・オブジェクトが何をするか。構造ではなく振る舞いに焦点を合わせる。

<a href="https://www.flickr.com/photos/k2works/13634941835" title="BDD by Katuyuki Kakigi, on Flickr"><img src="https://farm8.staticflickr.com/7176/13634941835_7bcc39f7f4_n.jpg" width="320" height="310" alt="BDD"></a>

BDD概念図


### BDDの概要
>BDDとは、ステークホルダーの視点に立って振る舞いを説明することにより、アプリケーションを実装するための手法である。

>『The RSpec Book』

### BDDサイクル  
1. Cucmberで始める
  1. １つのシナリオに焦点を合わせる
  1. 失敗するステップ定義を書く
  1. RSpecに進む
    1. 失敗するサンプルを書く
    1. サンプルを失敗させる
    1. リファクタリング
    1. ステップが成功するまで1-3を繰り返す
  1. リファクタリング
  1. シナリオが成功するまで1-5を繰り返す
1. シナリオが成功したら1に戻る


### BDDの原則
+ 十分といったら十分
+ ステークホルダーに価値をもたらす
+ すべては振る舞いから

### プロジェクトのインセプション
1. すべてのステークホルダーを集めて、プロジェクトのビジョンまたは目的を定める。
1. 定めたことを理解するためそのビジョンを持つコアステークホルダーと協力し、結果または目標を洗い出す。洗い出す対象はSMARTであることが望ましい。
1. 洗いだしたことを達成するソフトウエアで実行する必要があることを、フィーチャーセットまたはテーマ（レポートや顧客の登録など）として表現する。
1. 最後にこれらのテーマを構成する特定のフィーチャやストーリーについて話し合う

BDDは主にこの最後のレベルで適用される。また、ステークホルダーやビジネスアナリストといった用語は、個人ではなく役割を表す。

>SMARTな結果

>SMARTは、ある種の特性を持つ結果または目標を表現するために使われる頭文字です。その特性とは、Specific(具体的)、Measurable(測定可能)、Achievable(達成可能)、Relevant(適切)、Timeboxed(期限付き)の５つです。

>『The RSpec Book』

### リリースサイクル

1. ステークホルダーがビジネスアナリストと話し合い要件をフィーチャとして表現する。必要があればフィーチャを検証可能な小さなストーリーに分解する。
1. ステークホルダーとビジネスアナリストがテスト担当者と協力してストーリーの範囲を決定する。各ストーリーはどのように完結するかを意識する。
1. プログラマがストーリーの実装にとりかかる前の最後のタスクとして必要に応じてシナリオを自動化する。
1. 開発者はRSpecと「Coding by Example」に基づいてシナリオを実際に動かす。
  1. 必要な振る舞いを説明するサンプルコードを記述する
  1. そのサンプルを動作させるためのコードを実装する
  1. リファクタリングをおこなう
1. このシナリオを動かすのに十分なソフトウエアを完成させ、他のシナリオが動くようになるまでこの作業を繰り返す。
1. 一周して元に戻り、実際に動くシナリオをステークホルダーに見てもらいストーリーを完成させる。

BDDのもっとも重要な特徴の１つはシナリオを自動化するのが簡単で、しかもステークホルダーにとって理解しやすいこと。
これらのシナリオを定義し、自動化するのがCucumberが担当する。

>ストーリーイン、フィーチャアウト

>フィーチャは凝集された価値をステークホルダーに提供するものであり、ストーリーはほんの数日で実装できる機能を見てもらうためのものです。
>したがって、ステークホルダーにとって意味があるのはフィーチャのほうであり、フィーチャを提供するチームにとって意味があるのはストーリーのほうです。

>『The RSpec Book』

<a href="https://www.flickr.com/photos/k2works/13735080623" title="BDD_01 by Katuyuki Kakigi, on Flickr"><img src="https://farm4.staticflickr.com/3743/13735080623_1f7a591b55.jpg" width="500" height="188" alt="BDD_01"></a>

### ストーリーの構造
+ タイトル  
  どのストーリーについて説明するのかを明確にする。
+ ナラティブ  
  最低でもこのストーリーの**ステークホルダー**、ステークホルダーが望んでいる**フィーチャ**の説明、およびステークホルダーがそれを望んでいる理由を明らかにする。そしてこの振る舞いによりどのような**利益**を手にするのかを明らかにする。
+ 受け入れ基準  
  BDDの受け入れ基準は個々の**ステップ**で構成されるいくつかの**シナリオ**として定義される。

ナラティブの例
```
<ステークホルダー>として
<フィーチャ>をしたい
なぜなら<利益>だからだ
```

+ ビジネスアナリストはステークホルダーの使う言葉(ドメイン用語)をストーリーに使うことで全員が同じ用語を使うようにしなければならない
+ ドメイン用語はオブジェクト、メソッド、変数などコードベースにそのまま含まれる
+ ストーリーの「完了」を定義する受け入れい基準となるシナリオにおいて重要なのはステークホルダーが行うのとまったく同じ方法でアプリケーションとやりとりすること

### まとめ
+ BDDはTDDの枠組みを変化させ、本格的なアジャイル開発を理解しやすくする試みから発展した手法。  
+ BDDには３つの原則がある
  + 十分といったら十分
  + ステークホルダーに価値をもたらす
  + すべては振る舞いから


+ BDDのストーリーとシナリオは、自動化しやすく、ステークホルダーが明確に理解できることに重点を置いてた上で、一連の作業モデルをサポートするように設計されている。

## <a name="2">実装例</a> ##

[ビヘイビア駆動開発入門](https://github.com/k2works/bdd_introduction)を参照

# 参考文献 #
<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?t=k2works0c-22&o=9&p=8&l=as1&asins=4798121932&ref=qf_sp_asin_til&fc1=000000&IS2=1&lt1=_blank&m=amazon&lc1=0000FF&bc1=000000&bg1=FFFFFF&f=ifr" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>
