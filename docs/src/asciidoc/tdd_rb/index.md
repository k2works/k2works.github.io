これはとあるプログラマがどのような思考を経てテスト駆動開発でアプリケーションを構築していったかを解説した内容である。隣りに座って話を聞きながらコードを追いかけているイメージで読み進めてみてださい。

# エピソード0

## 環境構築から始めるテスト駆動開発

### 6S

環境構築をするにあたっては **5S** + セキュリティの **6S** をベースに進めていきます。まず **5S**
について、それからセキュリティについて解説します。

#### 5S

> 5S（ごエス、ごーエス）とは、製造業・サービス業などの職場環境の維持改善で用いられるスローガンである。各職場において徹底されるべき事項を5つにまとめたもので、4S運動に「躾」（習慣化の場合もある）を加えた5項。
>
> —  Wikipedia <https://ja.wikipedia.org/wiki/5S>

具体的には、

  - 整理（せいり、Seiri） いらないものを捨てる

  - 整頓（せいとん、Seiton） 決められた物を決められた場所に置き、いつでも取り出せる状態にしておく

  - 清掃（せいそう、Seisou） 常に掃除をする

  - 清潔（せいけつ、Seiketsu） 3S（上の整理・整頓・清掃）を維持し職場の衛生を保つ

  - 躾（しつけ、Shitsuke） 決められたルール・手順を正しく守る習慣をつける

これがプログラミング環境構築とどのように関係していくのでしょうか？まずは、いらないものを捨てるのが **整理**
ですがそもそもいらないものが何なのかを決めなければなりません。プログラミングで扱う対象はモノではなく情報です。ではどうやって情報を扱っていけばよいでしょう？ここは、**分類するな。ひたすら並べよ** の考えに従い一箇所に記録をまとめていきましょう。そのためのテクニックとして **エンジニアリングデイブックス** があります。これは何をやったか何を学んだかをノートに時系列に記録していくことです。

Engineering Dayboks

> Eventually Dave asked the obvious question. It turned out that they’d
> been trained to keep an engineering daybook, a kind of journal in
> which they recorded what they did, things they’d learned, sketches of
> ideas, readings from meters: basically anything to do with their work.
> When the notebook became full, they’d write the date range on the
> spine, then stick it on the shelf next to previous daybooks. …​
>
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition

ノートは市販のものならどれでも構いませんがおすすめは [ソフトリングノード](https://www.kokuyo-st.co.jp/stationery/softring-note/) のB5サイズが手元に置いてもかさばらず使いやすいです。情報を一箇所に集めて必要なものと不要なものを分ける準備が出来ました。次は必要なものをすぐに取り出せるようにする **整頓** をどのように実践していくかを解説します。

**整頓** の基本は **分類するな。ひたすら並べよ** です。デジタルデータも一箇所に保存していきましょう。具体的に保存する場所は後で解説します。また、分類するなといっても分類をする必要は当然発生します。分類にあたっては一貫したネーミングルールを適用していきます。具体的な方法は都度解説していきます。

> Name Well; Rename When Needed.
>
> Name to express your intent to readers, and rename as soon as that
> intent shifts.
>
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition
>

基本は実践しなければ意味がありません。そして習慣にすることで初めてものにできるものです。そのためには自ら躾けて習慣化していかなければなりません。

> 私がかつて発見した、そして多くの人に気づいてもらいたい効果とは、反復可能な振る舞いを規則にまで還元することで、規則の適用は機会的に反復可能になるということだ。
>
> —  テスト駆動開発

> ここで、Kent
> Beckが自ら語ったセリフを思い出しました。「僕は、偉大なプログラマなんかじゃない。偉大な習慣を身につけた少しましなプログラマなんだ」。
>
> —  リファクタリング(第2版)

#### セキュリティ(Security)

**5S** に続いてセキュリティに関してですがここで扱う内容は **情報セキュリティ** に関する内容です。

> 情報セキュリティ（じょうほうセキュリティ、英: information security）とは、情報の機密性、完全性、可用性を維持すること。
>
> —  Wikipedia
> <https://ja.wikipedia.org/wiki/%E6%83%85%E5%A0%B1%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3>
>

ここではパスワードに関する基本だけ抑えておいてください。

>   - 誕生日や電話番号など、親が見てパッと理解できる文字列はダメ
>
>   - 1単語で“読めてしまう”文字列はダメ
>
>   - 8文字以下の文字列は短すぎるからダメ
>
> —  子どもに「パスワード」の付け方を教えられますか？
> [子どもを守るITリテラシー学](https://www.itmedia.co.jp/pcuser/articles/1808/09/news035.html)
>

実際にパスワードを設定するときは

>   - サービスごとに、3単語以上の英文字を並べる（例：pekinese-optimal-start）
>
>   - なるべく長いパスワードを用意する（例：nagai-pasuwa-do-wo-youi-suru-amari-iirei-deha-naiga）
>
>   - 辞書に載っていないような文字列を用意する（例：Itags80vZyMp）
>
> —  子どもに「パスワード」の付け方を教えられますか？
> [子どもを守るITリテラシー学](https://www.itmedia.co.jp/pcuser/articles/1808/09/news035.html)
>

を参考にしてください。

#### ITリテラシ

以上がプログラミング環境構築にあたっての基本となる考えです。この記事では6Sを軸としたソフトウェア開発のための **ITリテラシ** 習得のベースとなる環境構築をすることを目的としています。

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

### アカウントの登録

まず各種サービスのアカウントを登録します。ここでは以下のアカウント設定で作業を進めていきますが各自作業の際は読み替えてください。

|          |                         |
| -------- | ----------------------- |
| Microsft | <newbie4649@outlook.jp> |
| Google   | <newbie4649@gmail.com>  |
| GitHub   | newbie4649              |
| Windows  | <newbie4649@outlook.jp> |
| WSL      | newbie4649              |

また、パスワードに関しては **セキュリティ** を参考に設定してください。アカウントIDに関しては可能な限り共通のID名を設定すると管理しやすくなります。登録アカウントとパスワードは一箇所に記録していつでも確認できるようにして置いてください。理想はパスワードマネージャーの使用ですがクラウドストレージでもいいです。他人にみられることがないように注意して管理しましょう。クラウドストレージで安全に保存する自身が無い場合は **エンジニアリングデイブックス** に記録しておきましょう。その際、もし落として他人にみられてもわからないような工夫をしておきましょう。手段はどうあれ **保存する場所は一箇所** が原則です。

#### Microsoftアカウントを作成する

[アカウントの作成](https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2fja-jp%2f&id=74335&aadredir=1&contextid=E56866F842F4E143&bk=1584685585&uiflavor=web&lic=1&mkt=JA-JP&lc=1041&uaid=491fc017de0f48c5c67a3833e7aca9ee) から新しいメールアドレスを取得を選択します。

![ms 001](../../images/article/episode_0/ms-001.png)

![ms 002](../../images/article/episode_0/ms-002.png)

![ms 003](../../images/article/episode_0/ms-003.png)

![ms 004](../../images/article/episode_0/ms-004.png)

![ms 005](../../images/article/episode_0/ms-005.png)

![ms 006](../../images/article/episode_0/ms-006.png)

#### Googleアカウントを作成する

[Google アカウントの作成](https://support.google.com/accounts/answer/27441?hl=ja) から `Googleアカウントを作成する` を選択します。

![ggl 001](../../images/article/episode_0/ggl-001.png)

![ggl 002](../../images/article/episode_0/ggl-002.png)

![ggl 003](../../images/article/episode_0/ggl-003.png)

#### GitHubアカウントを作成する

[GitHubに登録する](https://github.co.jp/) から `GitHubに登録する` を選択します。

![ghb 001](../../images/article/episode_0/ghb-001.png)

![ghb 002](../../images/article/episode_0/ghb-002.png)

Freeプランを選択します

![ghb 003](../../images/article/episode_0/ghb-003.png)

#### アカウントにサインインする

[Microsoft アカウントにサインインする方法](https://support.microsoft.com/ja-jp/help/4028195)を参考にしてローカルアカウントからMicrosoftアカウントに切り替えます。

![login 001](../../images/article/episode_0/login-001.png)

![login 002](../../images/article/episode_0/login-002.png)

![login 003](../../images/article/episode_0/login-003.png)

![login 004](../../images/article/episode_0/login-004.png)

![login 005](../../images/article/episode_0/login-005.png)

![login 006](../../images/article/episode_0/login-006.png)

![login 007](../../images/article/episode_0/login-007.png)

### クラウドストレージのセットアップ

> Keep Knowledge in Plain Text
>
> Plain text won’t become obsolete.It helps leverage your work and
> simplifies debugging and testing.
>
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition

[Office365](https://products.office.com/ja-jp/home?SilentAuth=1) からOneDriveの設定を確認します。

![drive 001](../../images/article/episode_0/drive-001.png)

![drive 002](../../images/article/episode_0/drive-002.png)

![drive 003](../../images/article/episode_0/drive-003.png)

アカウントのパスワードなど機密情報は [Personal Vault で OneDrive ファイルを保護する](https://support.office.com/ja-jp/article/personal-vault-で-onedrive-ファイルを保護する-6540ef37-e9bf-4121-a773-56f98dce78c4) を使って管理すると良いでしょう。もしくは [1Password](https://1password.com/jp/) などパスワード管理ツールの導入を検討してください。

[PCのOneDrive](https://support.microsoft.com/ja-jp/help/17184/windows-10-onedrive) にあるようにデータはローカルとクラウドの両方にあるので破損・紛失をしても復旧することが出来ます。

### 開発環境のセットアップ

#### パッケージ管理ツールのインストール

アプリケーションの管理にはパッケージ管理ツール [The Package Manager for Windows](https://chocolatey.org/) を使います。インストールの方法は [Chocolateyを使った環境構築の時のメモ](https://qiita.com/konta220/items/95b40b4647a737cb51aa) を参照してください。

`Get Started` を選択します。

![pkg 001](../../images/article/episode_0/pkg-001.png)

コードをコピーします。

![pkg 002](../../images/article/episode_0/pkg-002.png)

画面左下のスタートボタンを右クリックして `Windows PowerSHell(管理者)(A)` を起動してコピーしたコードを貼り付け実行します。

![pkg 003](../../images/article/episode_0/pkg-003.png)

![pkg 004](../../images/article/episode_0/pkg-004.png)

![pkg 005](../../images/article/episode_0/pkg-005.png)

![pkg 006](../../images/article/episode_0/pkg-006.png)

#### gitのインストール

> Always Use Version Control
>
> Vsersion control is a time machine for your work;you can go back.
>
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition

![git 001](../../images/article/episode_0/git-001.png)

画面左下のスタートボタンを右クリックして `Windows PowerSHell(管理者)(A)` を起動して以下のコマンドを入力します。質問には全てYを入力してください。

    choco install git

![git 002](../../images/article/episode_0/git-002.png)

#### PowerShellCoreのインストール

続いて、以下のコマンドを入力します。質問には全てYを入力してください。

    choco install powershell-core

![pwsh 001](../../images/article/episode_0/pwsh-001.png)

#### Windows Terminalのインストール

> Use the Power of Command Shells
>
> Use the shell when graphical user interfaces don’t cut it.
>
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition

画面左下のスタートメニューから `Microsft Store` を選択します。

![terminal 001](../../images/article/episode_0/terminal-001.png)

検索欄に `terminal` と入力したら表示されられる候補の中から `Windows Terminal` を選択します。

![terminal 002](../../images/article/episode_0/terminal-002.png)

`入手` を押してアプリケーションをインストールします。

![terminal 003](../../images/article/episode_0/terminal-003.png)

#### WSLのインストール

続いて、検索欄に `ubuntu` と入力して候補の中から `Ubuntu` を選択します。

![wsl 001](../../images/article/episode_0/wsl-001.png)

入手を押してアプリケーションをインストールします。

![wsl 002](../../images/article/episode_0/wsl-002.png)

インストール後に起動を実行しても必要な設定があるため実行できません。一旦アプリケーションを閉じます。

![wsl 003](../../images/article/episode_0/wsl-003.png)

画面左下のスタートメニューから歯車のアイコンを選択してWindowsの設定画面を表示します。

![wsl 004](../../images/article/episode_0/wsl-004.png)

`アプリ` を選択します。

![wsl 005](../../images/article/episode_0/wsl-005.png)

`アプリと機能` から `プログラミングと機能` を選択します。

![wsl 006](../../images/article/episode_0/wsl-006.png)

`Windows Subsystem for Linux` にチェックを入れてOKボタンを押します。

![wsl 007](../../images/article/episode_0/wsl-007.png)

`今すぐ再起動` を押してWindowsを再起動します。

![wsl 008 1](../../images/article/episode_0/wsl-008-1.png)

画面左下のスタートメニューから `Ubuntu` を選択します。

![wsl 008 2](../../images/article/episode_0/wsl-008-2.png)

セットアップが始まるのでユーザーIDとパスワードを設定してください。

![wsl 009](../../images/article/episode_0/wsl-009.png)

![wsl 010](../../images/article/episode_0/wsl-010.png)

### エディタのセットアップ

> Achieve Editor Fluency
>
> An editor is your most important tool. Know how to make it do what you
> need, quickly and accurately.
>
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition

#### インストール

[Download Visual Studio Code Java Pack Installer](https://aka.ms/vscode-java-installer-win) からVSCodeをダウンロードしてセットアッププログラムを実行します。

![vscode 001](../../images/article/episode_0/vscode-001.png)

![vscode 002](../../images/article/episode_0/vscode-002.png)

![vscode 003](../../images/article/episode_0/vscode-003.png)

#### 設定

エディタが起動すると画面右下にWSL拡張機能インストールのポップアップが表示されるので `Install` を押して拡張機能をインストールします。

![setting 001](../../images/article/episode_0/setting-001.png)

続いて画面左下の歯車を選択してメニューから `Settings` を選択します。

![setting 002](../../images/article/episode_0/setting-002.png)

検索欄に `trim` と入力します。

![setting 003](../../images/article/episode_0/setting-003.png)

チェックをオンにします。

![setting 004](../../images/article/episode_0/setting-004.png)

同様に検索欄に `format on save` と入力してチェックをオンにします。

![setting 005](../../images/article/episode_0/setting-005.png)

必要に応じてキーバインドなども自分が使いやすいようにカスタマイズします。

  - [Visual Studio
    Codeで簡単にショートカットキーを変更する方法](https://qiita.com/kinchiki/items/dabb5c890d9c57907503)

  - [VSCode 内蔵ターミナルで ctrl-p
    などのショートカットキーを利用する方法](https://loumo.jp/wp/archive/20191125120000/)

#### 拡張機能の追加

エディタのメニューが英語なので日本語に変更する拡張機能をインストールします。

[Japanese Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)

画面左のExtensionアイコンを選択して検索欄に `japanese` と入力したら日本語拡張パッケージが表示されるので `Install` を押します。

![package 001](../../images/article/episode_0/package-001.png)

`Restart Now` を押してエディタを再起動します。

![package 002](../../images/article/episode_0/package-002.png)

メニューが日本語になりました。

![package
    003](../../images/article/episode_0/package-003.png)

同様の手順で以下の拡張機能をインストールします。

1.  [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)

2.  [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

3.  [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

4.  [Git
    History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)

5.  [Bracket Pair
    Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)

6.  [Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)

7.  [TODO
    Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)

8.  [Path
    Autocomplete](https://marketplace.visualstudio.com/items?itemName=ionutvmi.path-autocomplete)

9.  [Rainbow
    CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)

10. [Partial
    Diff](https://marketplace.visualstudio.com/items?itemName=ryu1kn.partial-diff)

11. [Duplicate
    action](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-duplicate)

12. [GitHub Pull
    Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)

13. [gitignore](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore)

14. [Todo+](https://marketplace.visualstudio.com/items?itemName=fabiospampinato.vscode-todo-plus)

15. [Output
    Colorizer](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer)

16. [Trailing
    Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces)

#### 設定の同期

エディタの設定をして拡張機能をインストールしました。再インストールなどでエディタを再インストールする場合に上記の作業を再度するのは手間なので設定をオンライに保存してすぐにセットアップできるようにしておきます。

[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) をインストールすると以下の画面が表示されるので `LOGIN WITH GITHUB` を選択します。

![sync 001](../../images/article/episode_0/sync-001.png)

`アクセスを許可する` を押します。

![sync 002](../../images/article/episode_0/sync-002.png)

`開く` を押します。

![sync 003](../../images/article/episode_0/sync-003.png)

ブラウザが起動するので `Authorize` を押します。

![sync 004](../../images/article/episode_0/sync-004.png)

![sync 005](../../images/article/episode_0/sync-005.png)

`SKIP` を押します。

![sync 006](../../images/article/episode_0/sync-006.png)

エディタメニューの `表示` から `コマンドパレット` を選択して `Sync` と入力して入力候補の中から `アップデート・アップロードの設定` を選択します。

![sync 007](../../images/article/episode_0/sync-007.png)

`はい` を押して設定をアップロードします。

![sync 008](../../images/article/episode_0/sync-008.png)

エディタの設定を変更した際はアップロードすることで最新の設定を保存することができます。保存した設定を読み込む場合はコマンドパレットから `Sync: 設定をダウンロード` を選択します。

もし、GitHub連携で以下のような画面になった場合は登録メールアドレスに認証コードが送られているので確認してください。

![sync 009](../../images/article/episode_0/sync-009.png)

![sync 010](../../images/article/episode_0/sync-010.png)

#### Hello world

##### プログラムを作成する

エディタのセットアップが出来たのでかんたんなプログラムを作ってみましょう。 お題は [Hello world](https://ja.wikipedia.org/wiki/Hello_world) です。まず、プログラムを作成する場所ですが今回はディスクトップの直下 `Projects` というフォルダを作成してその中に配置したいと思います。

![hello 001](../../images/article/episode_0/hello-001.png)

`Projects` フォルダの中に `PowerShell` フォルダを作成します。

![hello 002](../../images/article/episode_0/hello-002.png)

![hello 003](../../images/article/episode_0/hello-003.png)

エディタを起動します。

![hello 004](../../images/article/episode_0/hello-004.png)

エディタを起動したらエクスプローラアイコンから `フォルダを開く` を選択して作成したフォルダを開きます。

![hello 005](../../images/article/episode_0/hello-005.png)

![hello 007](../../images/article/episode_0/hello-007.png)

フォルダを開いたらファイルアイコンを選択して `HelloWorld.ps1` ファイルを作成します。

![hello 008](../../images/article/episode_0/hello-008.png)

![hello 009](../../images/article/episode_0/hello-009.png)

まず、以下のコードを入力してキーボードのF5を押します。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $false
    }
}
```

![hello 010](../../images/article/episode_0/hello-010.png)

プログラムの実行と一緒にテストの実行結果が表示されます。

![hello 011](../../images/article/episode_0/hello-011.png)

テストが通るように修正します。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $true
    }
}
```

![hello 012](../../images/article/episode_0/hello-012.png)

テスティングフレームワークの動作が確認できたのでプログラム作成に入ります。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $true
    }
    It "簡単な挨拶を返す" {
        HelloWorld | Should Be "Hello from PowerShell"
    }
}
```

![hello 013](../../images/article/episode_0/hello-013.png)

`HelloWorld` 関数を追加します。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $true
    }
    It "簡単な挨拶を返す" {
        HelloWorld | Should Be "Hello from PowerShell"
    }
}

function HelloWorld {
    return "Hello from PowerShell"
}
```

![hello 014](../../images/article/episode_0/hello-014.png)

F5キーを押してテストが通ったことを確認したらテストケースを追加します。もしテストが失敗するようなら保存のタイミングあっていない場合があるので再度F5キーを押して実行してみてください。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $true
    }
    It "簡単な挨拶を返す" {
        HelloWorld | Should Be "Hello from PowerShell"
    }
    It "指定された名前で挨拶を返す" {
        HelloWorld "VSCode" | Should Be "Hello from VSCode"
    }
}

function HelloWorld {
    return "Hello from PowerShell"
}
```

![hello 015](../../images/article/episode_0/hello-015.png)

`HelloWorld` 関数は既定の挨拶しか返さないのでテストが失敗します。

    ...
    Describing HelloWorld
     [+] 何か便利なものだ 41ms
     [+] 簡単な挨拶を返す 12ms
     [-] 指定された名前で挨拶を返す 56ms
       Expected string length 17 but was 21. Strings differ at index 11.
       Expected: {Hello from VSCode}
       But was:  {Hello from PowerShell}
       ----------------------^
    ...

`HelloWorld` 関数に引数を追加して表示できるように変更します。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $true
    }
    It "簡単な挨拶を返す" {
        HelloWorld | Should Be "Hello from PowerShell"
    }
    It "指定された名前で挨拶を返す" {
        HelloWorld "VSCode" | Should Be "Hello from VSCode"
    }
}

function HelloWorld($name) {
    return "Hello from $name"
}
```

F5を押します。

![hello 016](../../images/article/episode_0/hello-016.png)

`指定された名前で挨拶を返す` テストは通りましたが今度は `簡単な挨拶を返す` テストが失敗してしまいました。

    Describing HelloWorld
     [+] 何か便利なものだ 39ms
     [-] 簡単な挨拶を返す 23ms
       Expected string length 21 but was 11. Strings differ at index 11.
       Expected: {Hello from PowerShell}
       But was:  {Hello from }
       ----------------------^
    ...
     [+] 指定された名前で挨拶を返す 29ms
    ...

`HelloWorld` 関数にデフォルト引数を設定してテストを通るようにします。

    Describe "HelloWorld" {
        It "何か便利なものだ" {
            $true | Should Be $true
        }
        It "簡単な挨拶を返す" {
            HelloWorld | Should Be "Hello from PowerShell"
        }
        It "指定された名前で挨拶を返す" {
            HelloWorld "VSCode" | Should Be "Hello from VSCode"
        }
    }

    function HelloWorld($name = "PowerShell") {
        return "Hello from $name"
    }

F5を押します。

![hello 017](../../images/article/episode_0/hello-017.png)

仕上げに不要なテストを削除してテストケースの文言をわかりやすくしておきます。

    Describe "HelloWorld" {
        It "何も指定されていない場合は既定の挨拶を返す" {
            HelloWorld | Should Be "Hello from PowerShell"
        }
        It "指定された名前で挨拶を返す" {
            HelloWorld "VSCode" | Should Be "Hello from VSCode"
        }
    }

    function HelloWorld($name = "PowerShell") {
        return "Hello from $name"
    }

![hello 018](../../images/article/episode_0/hello-018.png)

`HelloWorld` プログラムの完成です。

##### プログラムをデバッグする

プログラムを作成していると思った通りに動かないことが多々あります。そのようなときにプログラムの動作を確認するにはエディタのデバッグ機能を使います。

まず確認したいプログラムの行を左部分を押してブレークポイント（赤丸）を設定します。

![hello 019](../../images/article/episode_0/hello-019.png)

ブレークポイントを設定したらF5を押してプログラムの実行します。そうするとブレークポイント部分でプログラムが停止して変数などの情報が確認できるようになります。

![hello 020](../../images/article/episode_0/hello-020.png)

画面上の実行ボタンを押すと次のブレークポイントに移動します。

![hello 021](../../images/article/episode_0/hello-021.png)

![hello 022](../../images/article/episode_0/hello-022.png)

![hello 023](../../images/article/episode_0/hello-023.png)

デバッガを終了するには終了ボタンを押します。

![hello 024](../../images/article/episode_0/hello-024.png)

ブレークポイントを再度押すことで解除ができます。

![hello 025](../../images/article/episode_0/hello-025.png)

##### プログラムをレポジトリに保存する

作成したプログラムをレポジトリに保存します。まずソース管理アイコンを選択して `リポジトリを初期化する` を押します。

![hello 026](../../images/article/episode_0/hello-026.png)

![hello 027](../../images/article/episode_0/hello-027.png)

`変更をステージ` を選択します。

![hello 028](../../images/article/episode_0/hello-028.png)

変更内容を入力します。ここでは `feat: HelloWorld` を入力しておきます。

![hello 029](../../images/article/episode_0/hello-029.png)

`コミット` を押します。

![hello 030](../../images/article/episode_0/hello-030.png)

初回登録時は以下の警告が表示されるので追加作業が必要になります。

![hello 031 1](../../images/article/episode_0/hello-031-1.png)

![hello 031 2](../../images/article/episode_0/hello-031-2.png)

以下のコマンドをターミナルに入力します。

    git config --global user.name "newbie4649"
    git config --global user.email newbie4649@outlook.jp

![hello 032](../../images/article/episode_0/hello-032.png)

再度 `コミット` を押してレポジトリに保存します。

![hello 033](../../images/article/episode_0/hello-033.png)

レポジトリの記録内容は `GitLens` から確認することが出来ます。

![hello 034](../../images/article/episode_0/hello-034.png)

### 開発言語のセットアップ

#### Ruby環境のセットアップ(Windows版)

#### インストール

[RubyInstaller](https://rubyinstaller.org/downloads/)からWITH DEVKITをインストールします。

![ruby win install 001](../../images/article/episode_0/ruby-win-install-001.png)

インストラーの指示に従います。

![ruby win install 002](../../images/article/episode_0/ruby-win-install-002.png)

![ruby win install 003](../../images/article/episode_0/ruby-win-install-003.png)

![ruby win install 004](../../images/article/episode_0/ruby-win-install-004.png)

![ruby win install 005](../../images/article/episode_0/ruby-win-install-005.png)

3を入力してエンターキーを押します。

![ruby win install 006](../../images/article/episode_0/ruby-win-install-006.png)

#### 追加パッケージのインストール

[Ruby for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby)

[Ruby Solargraph](https://marketplace.visualstudio.com/items?itemName=castwide.solargraph)

[vscode-endwise](https://marketplace.visualstudio.com/items?itemName=kaiwood.endwise)

[ruby-rubocop](https://marketplace.visualstudio.com/items?itemName=misogi.ruby-rubocop)

[Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

[Ruby Test Explorer](https://marketplace.visualstudio.com/items?itemName=connorshea.vscode-ruby-test-adapter)

#### 設定

既定のシェルをPowerShell Coreに変更します。

![ruby win vscode 001](../../images/article/episode_0/ruby-win-vscode-001.png)

![ruby win vscode 002](../../images/article/episode_0/ruby-win-vscode-002.png)

新しいターミナルを開いて以下のコマンドを入力します。

``` bash
gem install rubocop
gem install debase
gem install ruby-debug-ide
gem install solargraph
```

![ruby win vscode 003](../../images/article/episode_0/ruby-win-vscode-003.png)

![ruby win vscode 004](../../images/article/episode_0/ruby-win-vscode-004.png)

#### Hello world

##### プログラムを作成する

`Projects` フォルダ内に `Ruby` フォルダを作成してエディタからフォルダを開きます。

![ruby win hello 001](../../images/article/episode_0/ruby-win-hello-001.png)

![ruby win hello 002](../../images/article/episode_0/ruby-win-hello-002.png)

![ruby win hello 003](../../images/article/episode_0/ruby-win-hello-003.png)

`新しいファイル` 作成アイコンを押します。

![ruby win hello 004](../../images/article/episode_0/ruby-win-hello-004.png)

ファイル名は `main.rb` とします。

![ruby win hello 005](../../images/article/episode_0/ruby-win-hello-005.png)

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

![ruby win hello 006](../../images/article/episode_0/ruby-win-hello-006.png)

`Debug Local File` を選択します。

![ruby win hello 007](../../images/article/episode_0/ruby-win-hello-007.png)

`launch.json` ファイルが作成されたら `main.rb` タブに戻ってF5キーを押します。

![ruby win hello 008](../../images/article/episode_0/ruby-win-hello-008.png)

デバッグコンソールに実行結果が表示されれば準備完了です。

![ruby win hello 009](../../images/article/episode_0/ruby-win-hello-009.png)

テストをパスするようにコードを修正してF5キーを押します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

end
```

![ruby win hello 010](../../images/article/episode_0/ruby-win-hello-010.png)

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

![ruby win hello 011](../../images/article/episode_0/ruby-win-hello-011.png)

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

![ruby win hello 012](../../images/article/episode_0/ruby-win-hello-012.png)

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

![ruby win hello 013](../../images/article/episode_0/ruby-win-hello-013.png)

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

![ruby win hello 014](../../images/article/episode_0/ruby-win-hello-014.png)

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

![ruby win hello 015](../../images/article/episode_0/ruby-win-hello-015.png)

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

![ruby win hello 016](../../images/article/episode_0/ruby-win-hello-016.png)

##### プログラムをデバッグする

まず確認したいプログラムの行を左部分を押してブレークポイント（赤丸）を設定します。

![ruby win debug 001](../../images/article/episode_0/ruby-win-debug-001.png)

ブレークポイントを設定したらF5を押してプログラムの実行します。そうするとブレークポイント部分でプログラムが停止して変数などの情報が確認できるようになります。

![ruby win debug 002](../../images/article/episode_0/ruby-win-debug-002.png)

画面上の実行ボタンを押すと次のブレークポイントに移動します。

![ruby win debug 003](../../images/article/episode_0/ruby-win-debug-003.png)

デバッガを終了するには終了ボタンを押します。

![ruby win debug 004](../../images/article/episode_0/ruby-win-debug-004.png)

ブレークポイントを再度押すことで解除ができます。

![ruby win debug 005](../../images/article/episode_0/ruby-win-debug-005.png)

##### プログラムをレポジトリに保存する

ソース管理を選択して `リポジトリを初期化する` を押します。

![ruby win git 001](../../images/article/episode_0/ruby-win-git-001.png)

`全ての変更をステージ` を選択します。

![ruby win git 002](../../images/article/episode_0/ruby-win-git-002.png)

変更内容に `feat: HelloWorld` と入力して `コミット` を押します。

![ruby win git 003](../../images/article/episode_0/ruby-win-git-003.png)

変更内容は `GitLens` から確認できます。

![ruby win git 004](../../images/article/episode_0/ruby-win-git-004.png)

#### Ruby環境のセットアップ(WSL版)

画面左下の `><` を押してメニューから `Remote-WSL: New Window` を選択します。

![ruby 001](../../images/article/episode_0/ruby-001.png)

`アクセスを許可する` を押します。

![ruby 002](../../images/article/episode_0/ruby-002.png)

新しいウィンドウが立ち上がったらExtensionメニューから `Install Local Extensions in "WSL: Ubuntu'…​"` を押します。

![ruby 003](../../images/article/episode_0/ruby-003.png)

全てにチェックをしてインストールします。

![ruby 004](../../images/article/episode_0/ruby-004.png)

拡張機能のインストールが終わったら `Reload Window` を押して拡張機能を読み込みます。

![ruby 005](../../images/article/episode_0/ruby-005.png)

#### プロビジョニングの実行

Ruby開発環境の自動構築をするため以下のレポジトリを自分のレポジトリにフォークします。

[テスト駆動開発から始めるRuby入門](https://github.com/hiroshima-arc/tdd_rb)

`Fork` を押します。

![provision 001](../../images/article/episode_0/provision-001.png)

`Fork` が完了して自分のレポジトリにコピーされたら `Clone or download` を押してレポジトリのURLをコピーします。

![provision 002](../../images/article/episode_0/provision-002.png)

エクスプローラアイコンメニューから `レポジトリをクローンする` を押します。

![provision 003](../../images/article/episode_0/provision-003.png)

先程コピーしたレポジトリのURLを貼り付けます。

![provision 004](../../images/article/episode_0/provision-004.png)

保存先はそのままで `OK` を押します。

![provision 005](../../images/article/episode_0/provision-005.png)

`開く` を押します。

![provision 006](../../images/article/episode_0/provision-006.png)

メニューから `ターミナル` `新しいターミナル` を選択します。

![provision 007 1](../../images/article/episode_0/provision-007-1.png)

![provision 007 2](../../images/article/episode_0/provision-007-2.png)

ターミナルに以下のコマンドを入力します。実行時にパスワード入力が求められるのでWSLで設定したパスワードを入力してください。

``` bash
$ sudo apt-get update -y
[sudo] password for newbie4649:
```

![provision 008](../../images/article/episode_0/provision-008.png)

続いて、ターミナルに以下のコマンドを入力します。

``` bash
$ sudo apt install ansible -y
```

続いて、エクスプローラから　`provisioning/vars/site.yml` をファイルを開いて `user:` の名前をWSLで設定したユーザーIDに変更します。

![provision 009](../../images/article/episode_0/provision-009.png)

変更を保存したらターミナルに以下のコマンドを入力します。

``` bash
$ cd provisioning/tasks/
$ sudo ansible-playbook --inventory=localhost, --connection=local site.yml
```

![provision 010](../../images/article/episode_0/provision-010.png)

セットアップが完了したらエディタを再起動してプロジェクトを開きます。

![provision 010 2](../../images/article/episode_0/provision-010-2.png)

以下のコマンドを入力してRubyがセットアップされていることを確認します。

``` bash
$ ruby -v
```

![provision 011](../../images/article/episode_0/provision-011.png)

続いて、ターミナルに以下のコマンドを入力します。

``` bash
$ code ~/.bashrc
```

表示されたファイルの一番最後に以下のコードを追加して保存します。

    ...
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_compl

![provision 012](../../images/article/episode_0/provision-012.png)

保存したら以下のコマンドを実行してNode.jsのバージョンが表示されたらセットアップ完了です。

``` bash
$ source ~/.bashrc
$ nvm install --lts
$ node -v
```

![provision 013](../../images/article/episode_0/provision-013.png)

#### 追加パッケージのインストール

[Ruby for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby)

[Ruby Solargraph](https://marketplace.visualstudio.com/items?itemName=castwide.solargraph)

[vscode-endwise](https://marketplace.visualstudio.com/items?itemName=kaiwood.endwise)

[ruby-rubocop](https://marketplace.visualstudio.com/items?itemName=misogi.ruby-rubocop)

[Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

[Ruby Test Explorer](https://marketplace.visualstudio.com/items?itemName=connorshea.vscode-ruby-test-adapter)

ターミナルに以下のコマンドを入力します。

``` bash
gem install rubocop
gem install debase
gem install ruby-debug-ide
gem install solargraph
```

#### Hello world

##### プログラムを作成する

`REAMD.md` を選択してから `新しいファイル` 作成アイコンを押します。

![ruby hello 001](../../images/article/episode_0/ruby-hello-001.png)

ファイル名は `main.rb` とします。

![ruby hello 002](../../images/article/episode_0/ruby-hello-002.png)

ファイルに以下のコードを入力したらRunアイコンを選択して `create a launch.json file` を押してメニューからRubyを選択します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, false)
  end
end
```

![ruby hello 003](../../images/article/episode_0/ruby-hello-003.png)

`Debug Local File` を選択します。

![ruby hello 004](../../images/article/episode_0/ruby-hello-004.png)

`launch.json` ファイルが作成されたら `main.rb` タブに戻ってF5キーを押します。

![ruby hello 005](../../images/article/episode_0/ruby-hello-005.png)

デバッグコンソールに実行結果が表示されれば準備完了です。

![ruby hello 006](../../images/article/episode_0/ruby-hello-006.png)

テストをパスするようにコードを修正してF5キーを押します。

``` ruby
require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_何か便利なもの
    assert_equal(true, true)
  end

end
```

![ruby hello 007](../../images/article/episode_0/ruby-hello-007.png)

テスティングフレームワークの動作が確認できたので `hello_world` 関数の作成に入ります。まず以下のコードを追加してF5キーを押してテストが失敗することを確認します。

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

![ruby hello 008](../../images/article/episode_0/ruby-hello-008.png)

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

![ruby hello 009](../../images/article/episode_0/ruby-hello-009.png)

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

![ruby hello 010](../../images/article/episode_0/ruby-hello-010.png)

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

![ruby hello 011](../../images/article/episode_0/ruby-hello-011.png)

`指定された名前で挨拶を返す` テストはパスしましたが今度は `簡単な挨拶を返す` テストが失敗するようになりましたのでデフォルト引数を設定してテストをパスするようにします。

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

![ruby hello 012](../../images/article/episode_0/ruby-hello-012.png)

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

![ruby hello 013](../../images/article/episode_0/ruby-hello-013.png)

##### プログラムをデバッグする

まず確認したいプログラムの行を左部分を押してブレークポイント（赤丸）を設定します。

![ruby debug
001](../../images/article/episode_0/ruby-debug-001.png)

ブレークポイントを設定したらF5を押してプログラムの実行します。そうするとブレークポイント部分でプログラムが停止して変数などの情報が確認できるようになります。

![ruby debug 002](../../images/article/episode_0/ruby-debug-002.png)

画面上の実行ボタンを押すと次のブレークポイントに移動します。

![ruby debug 003](../../images/article/episode_0/ruby-debug-003.png)

デバッガを終了するには終了ボタンを押します。

![ruby debug 004](../../images/article/episode_0/ruby-debug-004.png)

ブレークポイントを再度押すことで解除ができます。

![ruby debug 005](../../images/article/episode_0/ruby-debug-005.png)

##### プログラムをレポジトリに保存する

`全ての変更をステージ` を選択します。

![ruby git 001](../../images/article/episode_0/ruby-git-001.png)

変更内容に `feat: HelloWorld` と入力して `コミット` を押します。

![ruby git 002](../../images/article/episode_0/ruby-git-002.png)

変更内容は `GitLens` から確認できます。

![ruby git 003](../../images/article/episode_0/ruby-git-003.png)

### 参照

  - [Developer Roadmaps](https://roadmap.sh/)

  - [WEB DEVELOPER ROADMAP
    - 2020](https://github.com/kamranahmedse/developer-roadmap)

  - [「超」整理法の思想](https://note.com/yukionoguchi/n/n6fa36e6aff86)

  - [効率的な文書管理方法とは。保管方法、運用ルール作りの3ステップを紹介](https://at-jinji.jp/work/007)

  - [書類整理の基本は書類をためないこと！ 「『超』整理術」を簡単解説](https://at-jinji.jp/blog/11259/)

  - [The Pragmatic Programmer: your journey to mastery, 20th Anniversary
    Edition, 2nd
    Edition](https://www.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/)

  - [子どもを守るITリテラシー学](https://www.itmedia.co.jp/pcuser/articles/1808/09/news035.html)

  - [フォルダ管理の基本ルール5選！整理されていないデスクトップにさよならバイバイ！](https://jaminlifelog.com/notes/work/clean-desktop-files)

  - [新しい Microsoft
    アカウントを作成する方法](https://support.microsoft.com/ja-jp/help/4026324/microsoft-account-how-to-create)

  - [Java開発環境がすぐに作れる「Visual Studio Code Installer for
    Java」を試してみた](https://qiita.com/kikutaro/items/0e5deb36047d0137a767)

  - [Java in Visual Studio
    Code](https://code.visualstudio.com/docs/languages/java)

  - [WSL (Windows Subsystem for
    Linux)の基本メモ](https://qiita.com/rubytomato@github/items/fdfc0a76e848442f374e)

  - [Practical PowerShell Unit-Testing: Getting
    Started](https://www.red-gate.com/simple-talk/sysadmin/powershell/practical-powershell-unit-testing-getting-started/)

  - [日頃お世話になっているElectronのアプリ開発に入門してみる](https://qiita.com/y-tsutsu/items/179717ecbdcc27509e5a)

  - [VSCodeの拡張機能「GIST」が便利すぎてHackMDを使うのをやめた](https://qiita.com/kai_kou/items/ceeee47996339e5eecc4)

  - [VSCodeのオススメ拡張機能 24 選
    (とTipsをいくつか)](https://qiita.com/sensuikan1973/items/74cf5383c02dbcd82234)

  - [VScodeで保存時に自動で空白を削除しよう！](https://qiita.com/n_oshiumi/items/1ad3f55d58f2d9d48d1e)

  - [Visual Studio
    Codeで保存時自動整形の設定方法](https://qiita.com/mitashun/items/e2f118a9ca7b96b97840)

  - [VisualStudioCode
    でRubyの開発環境を作る](https://qiita.com/code2545Light/items/ca61673c42fb26fc2d28)

# エピソード1

## TODOリストから始めるテスト駆動開発

### TODOリスト

プログラムを作成するにあたってまず何をすればよいだろうか？私は、まず仕様の確認をして **TODOリスト** を作るところから始めます。

> TODOリスト
>
> 何をテストすべきだろうか----着手する前に、必要になりそうなテストをリストに書き出しておこう。
>
> —  テスト駆動開発

仕様

    1 から 100 までの数をプリントするプログラムを書け。
    ただし 3 の倍数のときは数の代わりに｢Fizz｣と、5 の倍数のときは｢Buzz｣とプリントし、
    3 と 5 両方の倍数の場合には｢FizzBuzz｣とプリントすること。

仕様の内容をそのままプログラムに落とし込むには少しサイズが大きいようですね。なので最初の作業は仕様を **TODOリスト** に分解する作業から着手することにしましょう。仕様をどのようにTODOに分解していくかは [50分でわかるテスト駆動開発](https://channel9.msdn.com/Events/de-code/2017/DO03?ocid=player)の26分あたりを参考にしてください。

TODOリスト

  - 数を文字列にして返す

  - 3 の倍数のときは数の代わりに｢Fizz｣と返す

  - 5 の倍数のときは｢Buzz｣と返す

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

まず `数を文字列にして返す`作業に取り掛かりたいのですがまだプログラミング対象としてはサイズが大きいようですね。もう少し具体的に分割しましょう。

  - 数を文字列にして返す

      - 1を渡したら文字列"1"を返す

これならプログラムの対象として実装できそうですね。

## テストファーストから始めるテスト駆動開発

### テストファースト

最初にプログラムする対象を決めたので早速プロダクトコードを実装・・・ではなく **テストファースト** で作業を進めていきましょう。まずはプログラムを実行するための準備作業を進める必要がありますね。

> テストファースト
>
> いつテストを書くべきだろうか----それはテスト対象のコードを書く前だ。
>
> —  テスト駆動開発

では、どうやってテストすればいいでしょうか？テスティングフレームワークを使って自動テストを書きましょう。

> テスト（名詞） どうやってソフトウェアをテストすればよいだろか----自動テストを書こう。
>
> —  テスト駆動開発

今回Rubyのテスティングフレームワークには [Minitest](http://docs.seattlerb.org/minitest/)を利用します。Minitestの詳しい使い方に関しては *Minitestの基本* [6](#pruby)を参照してください。では、まず以下の内容のテキストファイルを作成して `main.rb` で保存します。

``` ruby
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'

class HelloTest < Minitest::Test
  def test_greeting
    assert_equal 'hello world', greeting
  end
end

def greeting
  'hello world'
end
```

テストを実行します。

``` bash
$ ruby main.rb
Traceback (most recent call last):
        2: from main.rb:2:in `<main>'
        1: from /home/gitpod/.rvm/rubies/ruby-2.5.5/lib/ruby/site_ruby/2.5.0/rubygems/core_ext/kernel_require.rb:54:in `require'
/home/gitpod/.rvm/rubies/ruby-2.5.5/lib/ruby/site_ruby/2.5.0/rubygems/core_ext/kernel_require.rb:54:in `require': cannot load such file -- minitest/reporters (LoadError)
```

おおっと！いきなりエラーが出てきましたね。でも落ち着いてください。まず最初にやることはエラーメッセージの内容を読むことです。ここでは `require': cannot load such file — minitest/reporters (LoadError)` と表示されています。取っ掛かりとしては [エラーメッセージをキーワードに検索をする](https://www.google.com/search?sxsrf=ACYBGNTd6_rVoXXOBo2CHgs5vysIRIJaCQ%3A1579765868950&source=hp&ei=bFApXrCCN4Pg-Aa8v6vABw&q=%60require%27%3A+cannot+load+such+file&oq=%60require%27%3A+cannot+load+such+file&gs_l=psy-ab.3..0l2j0i30l6.1644.1644..2069…​2.0..0.116.116.0j1…​…​0…​.2j1..gws-wiz…​..10..35i362i39.-RXoHriCPZQ&ved=0ahUKEwiw6Ma7npnnAhUDMN4KHbzfCngQ4dUDCAg&uact=5) というのがあります。ちなみにここでは [minitest/reporters](https://github.com/kern/minitest-reporters) というGemがインストールされていなかったため読み込みエラーが発生していたようです。サイトのInstallationを参考にGemをインストールしておきましょう。

``` bash
$ gem install minitest-reporters
Fetching minitest-reporters-1.4.2.gem
Fetching ansi-1.5.0.gem
Fetching builder-3.2.4.gem
Successfully installed ansi-1.5.0
Successfully installed builder-3.2.4
Successfully installed minitest-reporters-1.4.2
Parsing documentation for ansi-1.5.0
Installing ri documentation for ansi-1.5.0
Parsing documentation for builder-3.2.4
Installing ri documentation for builder-3.2.4
Parsing documentation for minitest-reporters-1.4.2
Installing ri documentation for minitest-reporters-1.4.2
Done installing documentation for ansi, builder, minitest-reporters after 3 seconds
3 gems installed
```

Gemのインストールが完了したので再度実行してみましょう。今度はうまくいったようですね。Gemって何？と思ったかもしれませんがここではRubyの外部プログラム部品のようなものだと思っておいてください。`minitest-reporters` というのはテスト結果の見栄えを良くするための追加外部プログラムです。先程の作業ではそれを `gem install` コマンドでインストールしたのです。

``` bash
$ ruby main.rb
Started with run options --seed 9701

  1/1: [======================================================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00090s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
```

テストは成功しましたね。では続いてテストを失敗させてみましょう。`hello world` を `hello world!!!` に書き換えてテストを実行してみるとどうなるでしょうか。

``` ruby
...
class HelloTest < Minitest::Test
  def test_greeting
    assert_equal 'hello world!!!', greeting
  end
end
...
```

``` bash
$ ruby main.rb
Started with run options --seed 18217

 FAIL["test_greeting", #<Minitest::Reporters::Suite:0x00007f98a59194f8 @name="HelloTest">, 0.0007280000027094502]
 test_greeting#HelloTest (0.00s)
        Expected: "hello world!!!"
          Actual: "hello world"
        main.rb:11:in `test_greeting'

  1/1: [======================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00101s
1 tests, 1 assertions, 1 failures, 0 errors, 0 skips
```

オッケー、テスティングフレームワークが正常に読み込まれて動作することが確認できました。テストが正常に通るように戻しておきましょう。続いてバージョン管理システムのセットアップをしておきましょう。バージョン管理システム何それ？だって！？君はセーブしないでロールプレイングゲームをクリアできるのか？できないならまず [ここ](https://backlog.com/ja/git-tutorial/intro/01/)でGitを使ったバージョン管理の基本を学んでおきましょう。

``` bash
$ git init
$ git add .
$ git commit -m 'test: セットアップ'
```

これで[ソフトウェア開発の三種の神器](https://t-wada.hatenablog.jp/entry/clean-code-that-works)のうち **バージョン管理** と **テスティング** の準備が整いましたので **TODOリスト** の最初の作業に取り掛かかるとしましょう。

### 仮実装

TODOリスト

  - 数を文字列にして返す

      - **1を渡したら文字列"1"を返す**

  - 3 の倍数のときは数の代わりに｢Fizz｣と返す

  - 5 の倍数のときは｢Buzz｣と返す

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

**1を渡したら文字列"1"を返す** プログラムを `main.rb` に書きましょう。最初に何を書くのかって？
アサーションを最初に書きましょう。

> アサートファースト
>
> いつアサーションを書くべきだろうか----最初に書こう
>
>   - システム構築はどこから始めるべきだろうか。システム構築が終わったらこうなる、というストーリーを語るところからだ。
>
>   - 機能はどこから書き始めるべきだろうか。コードが書き終わったらこのように動く、というテストを書くところからだ。
>
>   - ではテストはどこから書き始めるべきだろうか。それはテストの終わりにパスすべきアサーションを書くところからだ。
>
> —  テスト駆動開発

まず、セットアッププログラムは不要なので削除しておきましょう。

``` ruby
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
```

テストコードを書きます。え？日本語でテストケースを書くの？ですかって。開発体制にもよりますが日本人が開発するのであれば無理に英語で書くよりドキュメントとしての可読性が上がるのでテストコードであれば問題は無いと思います。

> テストコードを読みやすくするのは、テスト以外のコードを読みやすくするのと同じくらい大切なことだ。
>
> —  リーダブルコード

``` ruby
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'

class FizzBuzzTest < Minitest::Test
  def test_1を渡したら文字列1を返す
    assert_equal '1', FizzBuzz.generate(1)
  end
end
```

テストを実行します。

``` bash
$ ruby main.rb
Started with run options --seed 678

ERROR["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x00007f956d8b6870 @name="FizzBuzzTest">, 0.0006979999998293351]
 test_1を渡したら文字列1を返す#FizzBuzzTest (0.00s)
NameError:         NameError: uninitialized constant FizzBuzzTest::FizzBuzz
        Did you mean?  FizzBuzzTest
            main.rb:10:in `test_1を渡したら文字列1を返す'

  1/1: [======================================================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00201s
1 tests, 0 assertions, 0 failures, 1 errors, 0 skips
```

`NameError: NameError: uninitialized constant FizzBuzzTest::FizzBuzz`…​FizzBuzzが定義されていない。そうですねまだ作ってないのだから当然ですよね。では`FizzBuzz::generate` メソッドを作りましょう。どんな振る舞いを書けばいいのでしょうか？とりあえず最初のテストを通すために **仮実装** から始めるとしましょう。

> 仮実装を経て本実装へ
>
> 失敗するテストを書いてから、最初に行う実装はどのようなものだろうか----ベタ書きの値を返そう。
>
> —  テスト駆動開発

`FizzBuzz` **クラス** を定義して **文字列リテラル** を返す `FizzBuzz::generate` **クラスメソッド** を作成しましょう。ちょっと何言ってるかわからないかもしれませんがとりあえずそんなものだと思って書いてみてください。

``` ruby
...
class FizzBuzz
  def self.generate(n)
    '1'
  end
end
```

テストが通ることを確認します。

``` bash
$ ruby main.rb
Started with run options --seed 60122

  1/1: [======================================================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00094s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
```

オッケー、これでTODOリストを片付けることができました。え？こんなベタ書きのプログラムでいいの？他に考えないといけないことたくさんあるんじゃない？ばかじゃないの？と思われるかもしませんが、この細かいステップに今しばらくお付き合いいただきたい。

TODOリスト

  - 数を文字列にして返す

      - **1を渡したら文字列"1"を返す**

  - 3 の倍数のときは数の代わりに｢Fizz｣と返す

  - 5 の倍数のときは｢Buzz｣と返す

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

### 三角測量

1を渡したら文字列1を返すようにできました。では、2を渡したらどうなるでしょうか？

TODOリスト

  - 数を文字列にして返す

      - ~~1を渡したら文字列"1"を返す~~

      - **2を渡したら文字列"2"を返す**

  - 3 の倍数のときは数の代わりに｢Fizz｣と返す

  - 5 の倍数のときは｢Buzz｣と返す

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

<!-- end list -->

``` ruby
...
class FizzBuzzTest < Minitest::Test
  def test_1を渡したら文字列1を返す
    assert_equal '1', FizzBuzz.generate(1)
  end

  def test_2を渡したら文字列2を返す
    assert_equal '2', FizzBuzz.generate(2)
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 62350

 FAIL["test_2を渡したら文字列2を返す", #<Minitest::Reporters::Suite:0x00007fa4968938d8 @name="FizzBuzzTest">, 0.0009390000013809185]
 test_2を渡したら文字列2を返す#FizzBuzzTest (0.00s)
        Expected: "2"
          Actual: "1"
        main.rb:17:in `test_2を渡したら文字列2を返す'

  2/2: [======================================================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00179s
2 tests, 2 assertions, 1 failures, 0 errors, 0 skips
```

テストが失敗しました。それは文字列1しか返さないプログラムなのだから当然ですよね。では1が渡されたら文字列1を返し、2を渡したら文字列2を返すようにプログラムを修正しましょう。**数値リテラル** を **文字列リテラル**　に変換する必要があります。公式リファレンスで調べてみましょう。

Rubyの公式リファレンスは <https://docs.ruby-lang.org/> です。[日本語リファレンス](https://docs.ruby-lang.org/ja/) から[るりまサーチ](https://docs.ruby-lang.org/ja/search/)を選択してキーワード検索してみましょう。[文字列 変換](https://docs.ruby-lang.org/ja/search/query:%E6%96%87%E5%AD%97%E5%88%97%E3%80%80%E5%A4%89%E6%8F%9B/)キーワードで検索すると `to_s` というキーワードが出てきました。今度は[to\_s](https://docs.ruby-lang.org/ja/search/query:to_s/)で検索すると色々出てきました、どうやら `to_s` を使えばいいみたいですね。

ちなみに検索エンジンから [Ruby 文字列 変換](https://www.google.com/search?hl=ja&sxsrf=ACYBGNRISq_mMHcQ1nGzgT3k_igW82f1Sg%3A1579494685196&source=hp&ei=HS0lXqnSCeeumAXN5ZigCg&q=Ruby+%E6%96%87%E5%AD%97%E5%88%97%E3%80%80%E5%A4%89%E6%8F%9B&oq=Ruby+%E6%96%87%E5%AD%97%E5%88%97%E3%80%80%E5%A4%89%E6%8F%9B&gs_l=psy-ab.3..0i4i37l2j0i8i30l6.1386.6456..6820…​2.0..0.139.2322.1j20…​…​0…​.1..gws-wiz…​…​.0i131i4j0i4j0i131j35i39j0j0i8i4i30.FfEPbOjPZcw&ved=0ahUKEwjp1IidrJHnAhVnF6YKHc0yBqQQ4dUDCAg&uact=5)で検索してもいろいろ出てくるのですがすべてのサイトが必ずしも正確な説明をしているまたは最新のバージョンに対応しているとは限らないので始めは公式リファレンスや市販の書籍から調べる癖をつけておきましょう。

``` ruby
...
class FizzBuzz
  def self.generate(n)
    n.to_s
  end
end
```

テストを実行します。

``` bash
$ ruby main.rb
Started with run options --seed 42479

  2/2: [======================================================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00098s
2 tests, 2 assertions, 0 failures, 0 errors, 0 skips
```

テストが無事通りました。このように２つ目のテストによって `FizzBuzz::generate` メソッドの一般化を実現することができました。このようなアプローチを **三角測量** と言います。

> 三角測量
>
> テストから最も慎重に一般化を引き出すやり方はどのようなものだろうか----２つ以上の例があるときだけ、一般化を行うようにしよう。
>
> —  テスト駆動開発

TODOリスト

  - **数を文字列にして返す**

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - 3 の倍数のときは数の代わりに｢Fizz｣と返す

  - 5 の倍数のときは｢Buzz｣と返す

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

たかが **数を文字列にして返す** プログラムを書くのにこんなに細かいステップを踏んでいくの？と思ったかもしれません。プログラムを書くということは細かいステップを踏んで行くことなのです。そして、細かいステップを踏み続けることが大切なことなのです。

> TDDで大事なのは、細かいステップを踏むことではなく、細かいステップを踏み続けられるようになることだ。
>
> —  テスト駆動開発


あと、テストケースの内容がアサーション一行ですがもっと検証するべきことがあるんじゃない？と思うでしょう。検証したいことがあれば独立したテストケースを追加しましょう。このような書き方はよろしくありません。

``` ruby
...
  def test_数字を渡したら文字列を返す
    assert_equal '1', FizzBuzz.generate(1)
    assert_equal '2', FizzBuzz.generate(2)
    assert_equal '3', FizzBuzz.generate(3)
    assert_equal '4', FizzBuzz.generate(4)
    assert_equal '5', FizzBuzz.generate(5)
  end
...
```

> テストの本質というのは、「こういう状況と入力から、こういう振る舞いと出力を期待する」のレベルまで要約できる。
>
> —  リーダブルコード

ここで一段落ついたので、これまでの作業内容をバージョン管理システムにコミットしておきましょう。

``` bash
$ git add main.rb
$ git commit -m 'test: 数を文字列にして返す'
```

## リファクタリングから始めるテスト駆動開発

### リファクタリング

ここでテスト駆動開発の流れを確認しておきましょう。

> 1.  レッド：動作しない、おそらく最初のうちはコンパイルも通らないテストを１つ書く。
>
> 2.  グリーン:そのテストを迅速に動作させる。このステップでは罪を犯してもよい。
>
> 3.  リファクタリング:テストを通すために発生した重複をすべて除去する。
>
> レッド・グリーン・リファクタリング。それがTDDのマントラだ。
>
> —  テスト駆動開発

コードはグリーンの状態ですが **リファクタリング** を実施していませんね。重複を除去しましょう。

> リファクタリング(名詞) 外部から見たときの振る舞いを保ちつつ、理解や修正が簡単になるように、ソフトウェアの内部構造を変化させること。
>
> —  リファクタリング(第2版)

> リファクタリングする(動詞) 一連のリファクタリングを適用して、外部から見た振る舞いの変更なしに、ソフトウェアを再構築すること。
>
> —  リファクタリング(第2版

#### メソッドの抽出

テストコードを見てください。テストを実行するにあたって毎回前準備を実行する必要があります。こうした処理は往々にして同じ処理を実行するものなので
**メソッドの抽出** を適用して重複を除去しましょう。

> メソッドの抽出
>
> ひとまとめにできるコードの断片がある。
>
> コードの断片をメソッドにして、それを目的を表すような名前をつける。
>
> —  新装版 リファクタリング

``` ruby
class FizzBuzzTest < Minitest::Test
  def test_1を渡したら文字列1を返す
    assert_equal '1', FizzBuzz.generate(1)
  end

  def test_2を渡したら文字列2を返す
    assert_equal '2', FizzBuzz.generate(2)
  end
end
```

テストフレームワークでは前処理にあたる部分を実行する機能がサポートされています。Minitestでは `setup` メソッドがそれに当たるので `FizzBuzz` オブジェクトを共有して共通利用できるようにしてみましょう。ここでは **インスタンス変数** に `FizzBuzz` **クラス** の参照を **代入** して各テストメソッドで共有できるようにしました。ちょっと何言ってるかわからないかもしれませんがここではそんなことをやってるぐらいのイメージで大丈夫です。

``` ruby
class FizzBuzzTest < Minitest::Test
  def setup
    @fizzbuzz = FizzBuzz
  end

  def test_1を渡したら文字列1を返す
    assert_equal '1', @fizzbuzz.generate(1)
  end

  def test_2を渡したら文字列2を返す
    assert_equal '2', @fizzbuzz.generate(2)
  end
end
```

テストプログラムを変更してしまいましたが壊れていないでしょうか？確認するにはどうすればいいでしょう？ テストを実行して確認すればいいですよね。

``` bash
$ ruby main.rb
Started with run options --seed 33356

  2/2: [======================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00083s
2 tests, 2 assertions, 0 failures, 0 errors, 0 skips
```

オッケー、前回コミットした時と同じグリーンの状態のままですよね。区切りが良いのでここでコミットしておきましょう。

``` bash
$ git add main.rb
$ git commit -m 'refactor: メソッドの抽出'
```

#### 変数名の変更

もう一つ気になるところがあります。

``` ruby
...
class FizzBuzz
  def self.generate(n)
    n.to_s
  end
end
```

引数の名前が `n` ですね。コンピュータにはわかるかもしれませんが人間が読むコードとして少し不親切です。特にRubyのような動的言語では型が明確に定義されないのでなおさらです。ここは **変数名の変更** を適用して人間にとって読みやすいコードにリファクタリングしましょう。

> コンパイラがわかるコードは誰にでも書ける。すぐれたプログラマは人間にとってわかりやすいコードを書く。
>
> —  リファクタリング(第2版)

> 名前は短いコメントだと思えばいい。短くてもいい名前をつければ、それだけ多くの情報を伝えることができる。
>
> —  リーダブルコード

``` ruby
...
class FizzBuzz
  def self.generate(number)
    number.to_s
  end
end
```

続いて、変更で壊れていないかを確認します。

``` bash
$ ruby main.rb
Started with run options --seed 33356

  2/2: [======================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00083s
2 tests, 2 assertions, 0 failures, 0 errors, 0 skips
```

オッケー、この時点でテストコードとプロダクトコードを変更しましたがその変更はすでに作成した自動テストによって壊れていないことを簡単に確認することができました。え、こんな簡単な変更でプログラムが壊れるわけないじゃん、ドジっ子なの？ですって。残念ながら私は絶対ミスしない完璧な人間ではないし、どちらかといえば注意力の足りないプログラマなのでこんな間違いも普通にやらかします。

``` ruby
...
class FizzBuzz
  def self.generate(number)
    numbr.to_s
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 59453

ERROR["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x0000564f6b1dfc70 @name="FizzBuzzTest">, 0.001019135997921694]
 test_1を渡したら文字列1を返す#FizzBuzzTest (0.00s)
NameError:         NameError: undefined local variable or method `numbr' for FizzBuzz:Class
        Did you mean?  number
            main.rb:21:in `generate'
            main.rb:11:in `test_1を渡したら文字列1を返す'

ERROR["test_2を渡したら文字列2を返す", #<Minitest::Reporters::Suite:0x0000564f6b1985f0 @name="FizzBuzzTest">, 0.003952859999117209]
 test_2を渡したら文字列2を返す#FizzBuzzTest (0.00s)
NameError:         NameError: undefined local variable or method `numbr' for FizzBuzz:Class
        Did you mean?  number
            main.rb:21:in `generate'
            main.rb:15:in `test_2を渡したら文字列2を返す'

  2/2: [====================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00746s
2 tests, 0 assertions, 0 failures, 2 errors, 0 skips
```

最初にプロダクトコードを書いて一通りの機能を作ってから動作を確認する進め方だとこの手の間違いはいつどこで作り込んだのかわからなくなるため原因の調査に時間がかかり残念な経験をしたドジっ子プログラマは変更なんてするもんじゃないと思いコードを変更することに不安を持つようになるでしょう。でも、テスト駆動開発ならそんなドジっ子プログラマでも自動テストと小さなステップのおかげで上記のようなしょうもない間違いもすぐに見つけてすぐに対応することができるのでコードを変更する勇気を持つことができるのです。

> テスト駆動開発は、プログラミング中の不安をコントロールする手法だ。
>
> —  テスト駆動開発

> リファクタリングでは小さなステップでプログラムを変更していく。そのため間違ってもバグを見つけるのは簡単である。
>
> —  リファクタリング(第2版)

このグリーンの状態にいつでも戻れるようにコミットして次の **TODOリスト** の内容に取り掛かるとしましょう。

``` bash
$ git add main.rb
$ git commit -m 'refactor: 変数名の変更'
```

> リファクタリングが成功するたびにコミットしておけば、たとえ壊してしまったとしても、動いていた状態に戻すことができます。変更をコミットしておき、意味のある単位としてまとまってから、共有のリポジトリに変更をプッシュすればよいのです。
>
> —  リファクタリング(第2版)

### 明白な実装

次は **3を渡したら文字列"Fizz"** を返すプログラムに取り組むとしましょう。

TODOリスト

  - *数を文字列にして返す*

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - 3 の倍数のときは数の代わりに｢Fizz｣と返す

      - **3を渡したら文字列"Fizz"を返す**

  - 5 の倍数のときは｢Buzz｣と返す

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

まずは、**テストファースト** **アサートファースト** で小さなステップで進めていくんでしたよね。

``` ruby
...
  def test_3を渡したら文字列Fizzを返す
    assert_equal 'Fizz', @fizzbuzz.generate(3)
  end
...
```

``` bash
$ ruby main.rb
Started with run options --seed 7095

 FAIL["test_3を渡したら文字列Fizzを返す", #<Minitest::Reporters::Suite:0x00007fbadf865f50 @name="FizzBuzzTest">, 0.017029999995429534]
 test_3を渡したら文字列Fizzを返す#FizzBuzzTest (0.02s)
        --- expected
        +++ actual
        @@ -1 +1,3 @@
        -"Fizz"
        +# encoding: US-ASCII
        +#    valid: true
        +"3"
        main.rb:19:in `test_3を渡したら文字列Fizzを返す'

  3/3: [======================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.05129s
3 tests, 3 assertions, 1 failures, 0 errors, 0 skips
```

さて、失敗するテストを書いたので次はテストを通すためのプロダクトコードを書くわけですがどうしましょうか？　**仮実装**　でベタなコードを書きますか？実現したい振る舞いは`もし3を渡したらならば文字列Fizzを返す` です。英語なら `If number is 3, result is Fizz`といったところでしょうか。ここは **明白な実装** で片付けた方が早いでしょう。

> 明白な実装
>
> シンプルな操作を実現するにはどうすればいいだろうか----そのまま実装しよう。
>
> 仮実装や三角測量は、細かく細かく刻んだ小さなステップだ。だが、ときには実装をどうすべきか既に見えていることが。
> そのまま進もう。例えば先ほどのplusメソッドくらいシンプルなものを仮実装する必要が本当にあるだろうか。
> 普通は、その必要はない。頭に浮かんだ明白な実装をただ単にコードに落とすだけだ。もしもレッドバーが出て驚いたら、あらためてもう少し歩幅を小さくしよう。
>
> —  テスト駆動開発

``` ruby
class FizzBuzz
  def self.generate(number)
    number.to_s
  end
end
```

ここでは **if式** と **演算子** を使ってみましょう。なんかプログラムっぽくなってきましたね。
3で割で割り切れる場合はFizzを返すということは **数値リテラル** 3で割った余りが0の場合は **文字列リテラル** Fizzを返すということなので余りを求める **演算子** を調べる必要がありますね。公式リファレンスで **算術演算子** をキーワードで検索したところ [いろいろ](https://docs.ruby-lang.org/ja/search/query:%E7%AE%97%E8%A1%93%E6%BC%94%E7%AE%97%E5%AD%90/)出てきました。 [%](https://docs.ruby-lang.org/ja/search/query:%E7%AE%97%E8%A1%93%E6%BC%94%E7%AE%97%E5%AD%90/query:%25/)を使えばいいみたいですね。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number % 3 == 0
       result = 'Fizz'
    end
    result
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 37722

  3/3: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00256s
3 tests, 3 assertions, 0 failures, 0 errors, 0 skips
```

テストがグリーンになったのでコミットしておきます。

``` bash
$ git add main.rb
$ git commit -m 'test: 3を渡したら文字列Fizzを返す'
```

#### アルゴリズムの置き換え

TODOリスト

  - ~~数を文字列にして返す~~

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - ~~3 の倍数のときは数の代わりに｢Fizz｣と返す~~

      - ~~3を渡したら文字列"Fizz"を返す~~

  - 5 の倍数のときは｢Buzz｣と返す

      - 5を渡したら文字列"Buzz"を返す

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

<!-- end list -->

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number % 3 == 0
       result = 'Fizz'
    end
    result
  end
end
```

レッド・グリーンときたので次はリファクタリングですね。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero?
       result = 'Fizz'
    end
    result
  end
end
```

ここでは **アルゴリズムの置き換え** を適用します。 **メソッドチェーンと述語メソッド** を使ってRubyらしい書き方にリファクタリングしてみました。

> アルゴリズムの取り替え
>
> アルゴリズムをよりわかりやすいものに置き換えたい。
>
> メソッドの本体を新たなアルゴリズムで置き換える。
>
> —  新装版 リファクタリング

> メソッドチェーンは言葉の通り、メソッドを繋げて呼び出す方法です。
>
> —  かんたんRuby

> 述語メソッドとはメソッド名の末尾に「？」をつけたメソッドのことを指します。
>
> —  かんたんRuby

リファクタリングによりコードが壊れていないかを確認したらコミットしておきましょう。

``` bash
$ ruby main.rb
Started with run options --seed 42180

  3/3: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00501s
3 tests, 3 assertions, 0 failures, 0 errors, 0 skips
```

``` bash
$ git add main.rb
$ git commit -m 'refactor: アルゴリズムの置き換え'
```

だんだんとリズムに乗ってきました。ここはギアを上げて **明白な実装** で引き続き **TODOリスト** の内容を片付けていきましょう。

TODOリスト

  - ~~数を文字列にして返す~~

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - ~~3の倍数のときは数の代わりに｢Fizz｣と返す~~

      - ~~3を渡したら文字列"Fizz"を返す~~

  - 5 の倍数のときは｢Buzz｣と返す

      - **5を渡したら文字列"Buzz"を返す**

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

**テストファースト** **アサートファースト** で最初に失敗するテストを書いて

``` ruby
...
  def test_5を渡したら文字列Buzzを返す
    assert_equal 'Buzz', @fizzbuzz.generate(5)
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 46876

 FAIL["test_5を渡したら文字列Buzzを返す", #<Minitest::Reporters::Suite:0x0000560f86b93700 @name="FizzBuzzTest">, 0.007562776008853689]
 test_5を渡したら文字列Buzzを返す#FizzBuzzTest (0.01s)
        --- expected
        +++ actual
        @@ -1 +1,2 @@
        -"Buzz"
        +# encoding: US-ASCII
        +"5"
        main.rb:23:in `test_5を渡したら文字列Buzzを返す'

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00849s
4 tests, 4 assertions, 1 failures, 0 errors, 0 skips
```

**if/elsif/else式** を使って条件分岐を追加しましょう。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero?
       result = 'Fizz'
    end
    result
  end
end
```

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end
    result
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 31468

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00158s
4 tests, 4 assertions, 0 failures, 0 errors, 0 skips
```

テストが通ったのでコミットしておきます。

``` bash
$ git add main.rb
$ git commit -m 'test: 5を渡したら文字列Buzzを返す'
```

#### メソッドのインライン化

TODOリスト

  - ~~数を文字列にして返す~~

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - ~~3の倍数のときは数の代わりに｢Fizz｣と返す~~

      - ~~3を渡したら文字列"Fizz"を返す~~

  - 5 の倍数のときは｢Buzz｣と返す

      - ~~5を渡したら文字列"Buzz"を返す~~

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

  - 1 から 100 までの数

  - プリントする

<!-- end list -->

``` ruby
class FizzBuzzTest < Minitest::Test
  def setup
    @fizzbuzz = FizzBuzz
  end

  def test_1を渡したら文字列1を返す
    assert_equal '1', @fizzbuzz.generate(1)
  end

  def test_2を渡したら文字列2を返す
    assert_equal '2', @fizzbuzz.generate(2)
  end

  def test_3を渡したら文字列Fizzを返す
    assert_equal 'Fizz', @fizzbuzz.generate(3)
  end

  def test_5を渡したら文字列Buzzを返す
    assert_equal 'Buzz', @fizzbuzz.generate(5)
  end
end
```

まずグループのアウトラインを作ってテストが壊れないかを確認します。

``` ruby
class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
    describe '三の倍数の場合' do
    end

    describe '五の倍数の場合' do
    end

    describe 'その他の場合' do
    end
  end

  def setup
    @fizzbuzz = FizzBuzz
  end

  def test_1を渡したら文字列1を返す
    assert_equal '1', @fizzbuzz.generate(1)
  end

  def test_2を渡したら文字列2を返す
    assert_equal '2', @fizzbuzz.generate(2)
  end

  def test_3を渡したら文字列Fizzを返す
    assert_equal 'Fizz', @fizzbuzz.generate(3)
  end

  def test_5を渡したら文字列Buzzを返す
    assert_equal 'Buzz', @fizzbuzz.generate(5)
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 39239

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00195s
4 tests, 4 assertions, 0 failures, 0 errors, 0 skips
```

壊れいないことを確認したらセットアップメソッドをまず移動してテストします。

``` ruby
class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
    def setup
      @fizzbuzz = FizzBuzz
    end

    describe '三の倍数の場合' do
    end

    describe '五の倍数の場合' do
    end

    describe 'その他の場合' do
    end
  end

  def test_1を渡したら文字列1を返す
    assert_equal '1', @fizzbuzz.generate(1)
  end

  def test_2を渡したら文字列2を返す
    assert_equal '2', @fizzbuzz.generate(2)
  end

  def test_3を渡したら文字列Fizzを返す
    assert_equal 'Fizz', @fizzbuzz.generate(3)
  end

  def test_5を渡したら文字列Buzzを返す
    assert_equal 'Buzz', @fizzbuzz.generate(5)
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 53111

ERROR["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x00005603cac658f8 @name="FizzBuzzTest">, 0.0027922230074182153]
 test_1を渡したら文字列1を返す#FizzBuzzTest (0.00s)
NoMethodError:         NoMethodError: undefined method `generate' for nil:NilClass
            main.rb:22:in `test_1を渡したら文字列1を返す'

ERROR["test_3を渡したら文字列Fizzを返す", #<Minitest::Reporters::Suite:0x00005603cac83e98 @name="FizzBuzzTest">, 0.00590475500212051]
 test_3を渡したら文字列Fizzを返す#FizzBuzzTest (0.01s)
NoMethodError:         NoMethodError: undefined method `generate' for nil:NilClass
            main.rb:30:in `test_3を渡したら文字列Fizzを返す'

ERROR["test_5を渡したら文字列Buzzを返す", #<Minitest::Reporters::Suite:0x00005603cac85ec8 @name="FizzBuzzTest">, 0.008002811024198309]
 test_5を渡したら文字列Buzzを返す#FizzBuzzTest (0.01s)
NoMethodError:         NoMethodError: undefined method `generate' for nil:NilClass
            main.rb:34:in `test_5を渡したら文字列Buzzを返す'

ERROR["test_2を渡したら文字列2を返す", #<Minitest::Reporters::Suite:0x00005603cac97e20 @name="FizzBuzzTest">, 0.010200971009908244]
 test_2を渡したら文字列2を返す#FizzBuzzTest (0.01s)
NoMethodError:         NoMethodError: undefined method `generate' for nil:NilClass
            main.rb:26:in `test_2を渡したら文字列2を返す'

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01247s
4 tests, 0 assertions, 0 failures, 4 errors, 0 skips
```

テストが失敗しました。これは **インスタンス変数** `@fizzbuzz` のスコープから外れたため
`FizzBuzz::generate` メソッド呼び出しに失敗したようです。テストメソッドを移動して変数のスコープ範囲に入れましょう。

``` ruby
class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
    def setup
      @fizzbuzz = FizzBuzz
    end

    describe '三の倍数の場合' do
      def test_3を渡したら文字列Fizzを返す
        assert_equal 'Fizz', @fizzbuzz.generate(3)
      end
    end

    describe '五の倍数の場合' do
      def test_5を渡したら文字列Buzzを返す
        assert_equal 'Buzz', @fizzbuzz.generate(5)
      end
    end

    describe 'その他の場合' do
      def test_1を渡したら文字列1を返す
        assert_equal '1', @fizzbuzz.generate(1)
      end

      def test_2を渡したら文字列2を返す
        assert_equal '2', @fizzbuzz.generate(2)
      end
    end
  end
end
```

すべてのメソッドを移動したら確認しましょう。

``` bash
$ ruby main.rb
Started with run options --seed 20627

  4/4: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00212s
4 tests, 4 assertions, 0 failures, 0 errors, 0 skips
```

ここでは、**メソッドのインライン化** を適用してしてテストコードを読みやすくすることにしました。テストコードの **自己文書化** により動作する仕様書にすることができました。

> メソッドのインライン化
>
> メソッドの本体が、名前をつけて呼ぶまでもなく明らかである。
>
> メソッド本体の呼び出し元にインライン化して、メソッドを除去する
>
> —  新装版 リファクタリング
>

> 混乱せずに読めるテストコードを目指すなら（コンピュータではなく人のためにテストを書いていることを忘れてはならない）、テストメソッドの長さは３行を目指そう。
>
> —  テスト駆動開発

> この関数名は「自己文書化」されている。関数名はいろんなところで使用されるのだから、優れたコメントよりも名前のほうが大切だ。
>
> —  リーダブルコード

テストも無事通るようになったのでコミットしておきます。

``` ruby
$ git add main.rb
$ git commit -m 'refactor: メソッドのインライン化'
```

さあ、**TODOリスト** もだいぶ消化されてきましたね。もうひと踏ん張りです。

TODOリスト

  - ~~数を文字列にして返す~~

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - ~~3の倍数のときは数の代わりに｢Fizz｣と返す~~

      - ~~3を渡したら文字列"Fizz"を返す~~

  - ~~5 の倍数のときは｢Buzz｣と返す~~

      - ~~5を渡したら文字列"Buzz"を返す~~

  - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

      - **15を渡したら文字列FizzBuzzを返す**

  - 1 から 100 までの数

  - プリントする

初めに失敗するテストを書きます。

``` ruby
...
    describe '三と五の倍数の場合' do
      def test_15を渡したら文字列FizzBuzzを返す
        assert_equal 'FizzBuzz', @fizzbuzz.generate(15)
      end
    end
...
```

``` bash
$ ruby main.rb
Started with run options --seed 16335

 FAIL["test_15を渡したら文字列FizzBuzzを返す", #<Minitest::Reporters::Suite:0x000056344a3be2a8 @name="FizzBuzz::三と五の倍数の場合">, 0.006737435003742576]
 test_15を渡したら文字列FizzBuzzを返す#FizzBuzz::三と五の倍数の場合 (0.01s)
        Expected: "FizzBuzz"
          Actual: "Fizz"
        main.rb:25:in `test_15を渡したら文字列FizzBuzzを返す'

  5/5: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01347s
5 tests, 5 assertions, 1 failures, 0 errors, 0 skips
```

続いて先程と同様に条件分岐を追加しましょう。

``` ruby
...
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    elsif number.modulo(15).zero?
      result = 'FizzBuzz'
    end
    result
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 45982

 FAIL["test_15を渡したら文字列FizzBuzzを返す", #<Minitest::Reporters::Suite:0x00007f822c00b2b0 @name="FizzBuzz::三と五の倍数の場合">, 0.00231200000
0529224]
 test_15を渡したら文字列FizzBuzzを返す#FizzBuzz::三と五の倍数の場合 (0.00s)
        Expected: "FizzBuzz"
          Actual: "Fizz"
        main.rb:25:in `test_15を渡したら文字列FizzBuzzを返す'

  4/4: [======================================================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00964s
4 tests, 4 assertions, 1 failures, 0 errors, 0 skips
```

おっと、調子に乗って **明白な実装** をしていたら怒られてしまいました。ここは一旦ギアを下げて小さなステップで何が問題かを調べることにしましょう。

> 明白な実装はセカンドギアだ。頭で考えていることがうまくコードに落とせないときは、ギアを下げる用意をしよう。
>
> —  テスト駆動開発

調べるにあたってコードを頭から読んでもいいのですが、問題が発生したのは `15を渡したら文字列FizzBuzzを返す` テストを追加したあとですよね？ということは原因は追加したコードにあるはずですよね？よって、追加部分をデバッグすれば原因をすぐ発見できると思いませんか？

今回はRubyのデバッガとしてByebugをインストールして使うことにしましょう。

``` bash
$ gem install byebug
```

インストールが完了したら早速Byebugからプログラムを起動して動作を確認してみましょう。

``` bash
$ byebug main.rb

[1, 10] in /Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/main.rb
=>  1: require 'minitest/reporters'
    2: Minitest::Reporters.use!
    3: require 'minitest/autorun'
    4:
    5: class FizzBuzzTest < Minitest::Test
    6:   describe 'FizzBuzz' do
    7:     def setup
    8:       @fizzbuzz = FizzBuzz
    9:     end
   10:
(byebug)
```

詳しい操作に関しては [printデバッグにさようなら！Ruby初心者のためのByebugチュートリアル](https://qiita.com/jnchito/items/5aaf323ab4f24b526a61)を参照してください。

では、問題の原因を調査するためbyebugメソッドでコード内にブレークポイントを埋め込んでデバッガを実行してみましょう。

``` ruby
...
    describe '三と五の倍数の場合' do
      def test_15を渡したら文字列FizzBuzzを返す
        require 'byebug'
        byebug
        assert_equal 'FizzBuzz', @fizzbuzz.generate(15)
      end
    end
...
```

``` bash
$ byebug main.rb

[1, 10] in /Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/main.rb
=>  1: require 'minitest/reporters'
    2: Minitest::Reporters.use!
    3: require 'minitest/autorun'
    4:
    5: class FizzBuzzTest < Minitest::Test
    6:   describe 'FizzBuzz' do
    7:     def setup
    8:       @fizzbuzz = FizzBuzz
    9:     end
   10:
```

ブレークポイントまで `continue` コマンドで処理を進めます。`continue` コマンドは `c` でもいけます。

``` bash
(byebug) c
   22:
   23:     describe '三と五の倍数の場合' do
   24:       def test_15を渡したら文字列FizzBuzzを返す
   25:         require 'byebug'
   26:         byebug
=> 27:         assert_equal 'FizzBuzz', @fizzbuzz.generate(15)
   28:       end
   29:     end
   30:
   31:     describe 'その他の場合' do
```

続いて問題が発生した `@fizzbuzz.generate(15)` メソッド内にステップインします。

``` bash
(byebug) s
   36:   end
   37: end
   38:
   39: class FizzBuzz
   40:   def self.generate(number)
=> 41:     result = number.to_s
   42:     if number.modulo(3).zero?
   43:       result = 'Fizz'
   44:     elsif number.modulo(5).zero?
   45:       result = 'Buzz'
```

引数の `number` は `15` だから `elsif number.modulo(15).zero?` の行で判定されるはず・・・

``` bash
(byebug) s
   37: end
   38:
   39: class FizzBuzz
   40:   def self.generate(number)
   41:     result = number.to_s
=> 42:     if number.modulo(3).zero?
   43:       result = 'Fizz'
   44:     elsif number.modulo(5).zero?
   45:       result = 'Buzz'
   46:     elsif number.modulo(15).zero?
(byebug) s
   38:
   39: class FizzBuzz
   40:   def self.generate(number)
   41:     result = number.to_s
   42:     if number.modulo(3).zero?
=> 43:       result = 'Fizz'
```

ファッ！？

``` bash
   44:     elsif number.modulo(5).zero?
   45:       result = 'Buzz'
   46:     elsif number.modulo(15).zero?
   47:       result = 'FizzBuzz'
(byebug) result
"15"
(byebug) q!
```

15は3で割り切れるから最初の判定で処理されますよね。まあ、常にコードに注意を払って頭の中で処理しながらコードを書いていればこんなミスすることは無いのでしょうが私はドジっ子プログラマなので計算機ができることは計算機にやらせて間違いがあれば原因を調べて解決するようにしています。とりあえず、テストを通るようにしておきましょう。

``` ruby
...
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero?
      result = 'Fizz'
      if number.modulo(15).zero?
        result = 'FizzBuzz'
      end
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end
    result
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 24862

  5/5: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00279s
5 tests, 5 assertions, 0 failures, 0 errors, 0 skips
```

テストが通ったのでコミットしておきます。コミットログにバグは残らないのですが作業の合間ではバグを作り込んでいましたよね。でも、テストがすぐに教えてくれるのですぐに修正することができました。結果として私のようなドジっ子プログラマでもバグの無いコードを書いているかのように見えるんですよ。

``` bash
$ git add main.rb
$ git commit -m 'test: 15を渡したら文字列FizzBuzzを返す'
```

> 私はテスト駆動開発を長年行っているので、他人にミスを気づかれる前に、自分の誤りを修正できるだけなのだ。
>
> —  テスト駆動開発

先程のコードですが・・・

``` ruby
...
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero?
      result = 'Fizz'
      if number.modulo(15).zero?
        result = 'FizzBuzz'
      end
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end
    result
  end
end
```

**if式** の中でさらに **if式** をネストしています。いわゆる **コードの不吉な臭い** がしますね。ここは仕様の文言にある `3と 5 両方の倍数の場合には｢FizzBuzz｣とプリントすること。` に沿った記述にするとともにネストした部分をわかりやすくするために **アルゴリズムの置き換え** を適用してリファクタリングをしましょう。

> ネストの深いコードは理解しにくい。
>
> —  リーダブルコード

``` ruby
...
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero? && number.modulo(5).zero?
      result = 'FizzBuzz'
    elsif number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end
    result
  end
end
```

テストして、

``` bash
$ ruby main.rb
Started with run options --seed 48529

  5/5: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00329s
5 tests, 5 assertions, 0 failures, 0 errors, 0 skips
```

コミットです。

``` bash
$ git add main.rb
$ git commit -m 'refactor: アルゴリズムの置き換え'
```

### 休憩

TODOリスト

  - ~~数を文字列にして返す~~

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - ~~3の倍数のときは数の代わりに｢Fizz｣と返す~~

      - ~~3を渡したら文字列"Fizz"を返す~~

  - ~~5 の倍数のときは｢Buzz｣と返す~~

      - ~~5を渡したら文字列"Buzz"を返す~~

  - ~~3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す~~

      - ~~15を渡したら文字列FizzBuzzを返す~~

  - **1 から 100 までの数**

  - プリントする

数を引数にして文字列を返す `FizzBuzz::generate` メソッドはできたみたいですね。次のやることは・・・新しいメソッドを追加する必要がありそうです。気分を切り替えるため少し休憩を取りましょう。

> 疲れたり手詰まりになったりしたときはどうすればいいだろうか----休憩を取ろう。
>
> —  テスト駆動開発

引き続き **TODOリスト** を片付けたいのですが `1から100までの数` を返すプログラムを書かないといけません。3を渡したらFizzのような **リテラル** を返すプログラムではなく 1から100までの **配列オブジェクト** を返すようなプログラムにする必要がありそうです。**TODOリスト** にするとこんな感じでしょうか。

TODOリスト

  - 1 から 100 までの数の配列を返す

      - 配列の初めは文字列の1を返す

      - 配列の最後は文字列の100を返す

  - プリントする

どうやら **配列オブジェクト** を返すプログラムを書かないといけないようですね。え？ **明白な実装** の実装イメージがわかない。そんな時はステップを小さくして **仮実装** から始めるとしましょう。

> 何を書くべきかわかっているときは、明白な実装を行う。わからないときには仮実装を行う。まだ正しい実装が見えてこないなら、三角測量を行う。それでもまだわからないなら、シャワーを浴びに行こう。
>
> —  テスト駆動開発

### 学習用テスト

#### 配列

**テストファースト** でまずRubyの **配列** の振る舞いを確認していきましょう。公式リファレンスによるとRubyでは[Arrayクラスとして定義されている](https://docs.ruby-lang.org/ja/latest/class/Array.html)ようですね。空の配列を作るには `[]` (配列リテラル)を使えばいいみたいですね。こんな感じかな？

``` ruby
...
    describe '1から100までの数の配列を返す' do
      def test_配列の初めは文字列の1を返す
        result = []
        assert_equal '1', result
      end
    end
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 54004

 FAIL["test_配列の初めは文字列の1を返す", #<Minitest::Reporters::Suite:0x00007fd0fb93d540 @name="FizzBuzz::1から
100までの数の配列を返す">, 0.0016740000028221402]
 test_配列の初めは文字列の1を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
        Expected: "1"
          Actual: []
        main.rb:37:in `test_配列の初めは文字列の1を返す'

  5/5: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00602s
5 tests, 5 assertions, 1 failures, 0 errors, 0 skips
```

これは同値ではないのはわかりますね。ではこうしたらどうなるでしょうか？

``` ruby
...
    describe '1から100までの数の配列を返す' do
      def test_配列の初めは文字列の1を返す
        result = ['1']
        assert_equal '1', result
      end
    end
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 32701

 FAIL["test_配列の初めは文字列の1を返す", #<Minitest::Reporters::Suite:0x00007fb36f096030 @name="FizzBuzz::1から100までの数の配列を返す">, 0.0018850000014936086]
 test_配列の初めは文字列の1を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
        Expected: "1"
          Actual: ["1"]
        main.rb:38:in `test_配列の初めは文字列の1を返す'

  5/5: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.04383s
5 tests, 5 assertions, 1 failures, 0 errors, 0 skips
```

**配列** には[要素を操作するメソッドが用意されており](https://docs.ruby-lang.org/ja/latest/class/Array.html)内容を色々操作できそうですね。でも、いちいちテストコードを編集してテストを実行させるのも面倒なのでここはデバッガを使ってみましょう。まずブレークポイントを設定して・・・

``` ruby
...
    describe '1から100までの数の配列を返す' do
      def test_配列の初めは文字列の1を返す
        require 'byebug'
        byebug
        result = ['1']
        assert_equal '1', result
      end
    end
  end
end
```

デバッガを起動します。

``` bash
$ byebug main.rb

[1, 10] in /Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/main.rb
=>  1: require 'minitest/reporters'
    2: Minitest::Reporters.use!
    3: require 'minitest/autorun'
    4:
    5: class FizzBuzzTest < Minitest::Test
    6:   describe 'FizzBuzz' do
    7:     def setup
    8:       @fizzbuzz = FizzBuzz
    9:     end
   10:
(byebug)
```

continueでブレークポイントまで進めます。

``` bash
(byebug) c
Started with run options --seed 15764

  /0: [=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=-] 0% Time: 00:00:00,  ETA: ??:??:??
[34, 43] in /Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/main.rb
   34:
   35:     describe '1から100までの数の配列を返す' do
   36:       def test_配列の初めは文字列の1を返す
   37:         require 'byebug'
   38:         byebug
=> 39:         result = ['1']
   40:         assert_equal '1', result
   41:       end
   42:     end
   43:   end
```

ステップインして `result` の中身を確認してみましょう。

``` bash
(byebug) s

[35, 44] in /Users/k2works/Projects/hiroshima-arc/tdd_rb/docs/src/article/code/main.rb
   35:     describe '1から100までの数の配列を返す' do
   36:       def test_配列の初めは文字列の1を返す
   37:         require 'byebug'
   38:         byebug
   39:         result = ['1']
=> 40:         assert_equal '1', result
   41:       end
   42:     end
   43:   end
   44: end
(byebug) result
["1"]
```

添字を指定して **配列** の最初の文字列を確認してみましょう。

``` bash
(byebug) result
["1"]
(byebug) result[1]
nil
```

おや？１番目は"1"では無いようですね。**配列** は0から始まるので1番目を指定するにはこうします。

``` bash
(byebug) result
["1"]
(byebug) result[1]
nil
(byebug) result[0]
"1"
```

続いて、複数の文字列から構成される **配列** を作ってみましょう。

``` bash
(byebug) result = ['1','2','3']
["1", "2", "3"]
(byebug) result[0]
"1"
(byebug) result[2]
"3"
```

ちなみにRubyだとこのように表記することができます。直感的でわかりやすくないですか？

``` bash
(byebug) result
["1", "2", "3"]
(byebug) result.first
"1"
(byebug) result.last
"3"
```

最後に追加、削除、変更をやってみましょう。

``` bash
(byebug) result = ['1','2','3']
["1", "2", "3"]
(byebug) result << '4'
["1", "2", "3", "4"]
(byebug) result.push('4')
["1", "2", "3", "4", "4"]
(byebug) result.delete_at(3)
"4"
(byebug) result
["1", "2", "3", "4"]
(byebug) result[2] = '30'
"30"
(byebug) result
["1", "2", "30", "4"]
```

**配列** の振る舞いもだいぶイメージできたのでデバッガを終了させてテストコードを少し変えてみましょう。

``` bash
(byebug) q
Really quit? (y/n) y
```

``` ruby
...
    describe '1から100までの数の配列を返す' do
      def test_配列の初めは文字列の1を返す
        result = ['1', '2', '3']
        assert_equal '1', result.first
        assert_equal '2', result[1]
        assert_equal '3', result.last
      end
    end
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 39118

  5/5: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00186s
5 tests, 7 assertions, 0 failures, 0 errors, 0 skips
```

**変数** `result` に配列を返すメソッドを作れば良さそうですね。とりあえずメソッド名は今の時点ではあまり考えずに・・・

``` ruby
...
    describe '1から100までの数の配列を返す' do
      def test_配列の初めは文字列の1を返す
        result = FizzBuzz.print_1_to_100
        assert_equal '1', result.first
      end
    end
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 19247

ERROR["test_配列の初めは文字列の1を返す", #<Minitest::Reporters::Suite:0x00007faaea925058 @name="FizzBuzz::1から
100までの数の配列を返す">, 0.0017889999980980065]
 test_配列の初めは文字列の1を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
NoMethodError:         NoMethodError: undefined method `print_1_to_100' for FizzBuzz:Class
            main.rb:37:in `test_配列の初めは文字列の1を返す'

  5/5: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00454s
5 tests, 4 assertions, 0 failures, 1 errors, 0 skips
```

ここまでくれば **仮実装** はできますね。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero? && number.modulo(5).zero?
      result = 'FizzBuzz'
    elsif number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end
    result
  end

  def self.print_1_to_100
    [1, 2, 3]
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 24564

 FAIL["test_配列の初めは文字列の1を返す", #<Minitest::Reporters::Suite:0x00007fefd8917060 @name="FizzBuzz::1から
100までの数の配列を返す">, 0.0011969999977736734]
 test_配列の初めは文字列の1を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
        Expected: "1"
          Actual: 1
        main.rb:38:in `test_配列の初めは文字列の1を返す'

  5/5: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00209s
5 tests, 5 assertions, 1 failures, 0 errors, 0 skips
```

ファッ！？、ああ、数字ではなく文字列で返すのだからこうですね。

``` ruby
...
  def self.print_1_to_100
    ['1', '2', '3']
  end
end
```

**%記法** を使うとよりRubyらしく書けます。

``` ruby
...
  def self.print_1_to_100
    %w[1 2 3]
  end
end
```

> %記法とは、文字列や正規表現などを定義する際に、%を使った特別な書き方をすることでエスケープ文字を省略するなど、可読性を高めることができる記法です。
>
> —  かんたんRuby

``` bash
$ ruby main.rb
Started with run options --seed 42995

  5/5: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00195s
5 tests, 5 assertions, 0 failures, 0 errors, 0 skips
```

**TODOリスト** の１つ目を **仮実装** で片づけことができました。ちなみにテストコードを使ってソフトウェアの振る舞いを検証するテクニックを **学習用テスト** と言います。

> 学習用テスト
>
> チーム外の誰かが書いたソフトウェアのテストを書くのはどのようなときか----そのソフトウェアの新機能を初めて使う際に書いてみよう。
>
> —  テスト駆動開発

TODOリスト

  - 1 から 100 までの数の配列を返す

      - ~~配列の初めは文字列の1を返す~~

      - 配列の最後は文字列の100を返す

  - プリントする

#### 繰り返し処理

`FizzBuzz::print_1_to_100` メソッドはまだ最後の要素が検証されていませんね。**三角測量** を使って小さなステップで進めていくことにしましょう。

``` ruby
...
    describe '1から100までの数の配列を返す' do
      def test_配列の初めは文字列の1を返す
        result = FizzBuzz.print_1_to_100
        assert_equal '1', result.first
      end

      def test_配列の最後は文字列の100を返す
        result = FizzBuzz.print_1_to_100
        assert_equal '100', result.last
      end
    end
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 12031

 FAIL["test_配列の最後は文字列の100を返す", #<Minitest::Reporters::Suite:0x00007fccc9828500 @name="FizzBuzz::1から100までの数の配列を返す">, 0.0018540000019129366]
 test_配列の最後は文字列の100を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
        Expected: "100"
          Actual: "3"
        main.rb:43:in `test_配列の最後は文字列の100を返す'

  6/6: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.02936s
```

配列は3までなので想定通りテストは失敗します。さて、1から100までの文字列で構成される配列をどうやって作りましょうか？ 先程は **if式** を使って **条件分岐** をプログラムで実行しました。今回は **繰り返し処理** をプログラムで実行する必要がありそうですね。Rubyの繰り返し処理には **for式** **while/until/loop** などがありますが実際のところ **eachメソッド** を使った繰り返し処理が主流です。とはいえ、実際に動かして振る舞いを確認しないとイメージは難しいですよね。 **学習用テスト** を書いてもいいのですが今回は *irb上で簡単なコードを動かしてみる*[6](#pruby)ことで振る舞いを検証してみましょう。まずコマンドラインで`irb`を起動します。

> Rubyにはfor文はあります。ですが、ほとんどのRubyプログラマはfor文を使いません。筆者も5〜6年Rubyを使っていますが、for文を書いたことは一度もありません。Rubyの場合はforのような構文で繰り返し処理をさせるのではなく、配列自身に対して「繰り返せ」という命令を送ります。ここで登場するのがeachメソッドです。
>
> —  プロを目指す人のためのRuby入門

``` bash
$ irb
irb(main):001:0>
```

まず先程デバッガで検証した配列の作成をやってみましょう。

``` bash
irb(main):001:0> result = %w[1 2 3]
=> ["1", "2", "3"]
```

配列のeachメソッドをつかって配列の中身を繰り返し処理で表示させてみましょう。`p` はプリントメソッドです。

``` bash
irb(main):003:0> result.each do |n| p n end
"1"
"2"
"3"
=> ["1", "2", "3"]
```

配列の中身を繰り返し処理で取り出す方法はわかりました。あとは100までの配列をどうやって作ればよいのでしょうか？`['1','2','3'…​'100']`と手書きで作りますか？100件ぐらいならまあできなくもないでしょうが1000件,10000件ならどうでしょうか？無理ですね。計算機にやってもらいましょう、調べてみるとRubyには **レンジオブジェクト(Range)** というもの用意されいるそうです。説明を読んでもピンと来ないので実際に動作を確認してみましょう。

> レンジオブジェクト（範囲オブジェクトとも呼ばれます）はRangeクラスのオブジェクトのことで、「..」や「…​」演算子を使って定義します。「1..3」のように定義し、主に整数値や文字列を使って範囲を表現します。
>
> —  かんたんRuby

``` bash
irb(main):008:0> (1..5).each do |n| p n end
1
2
3
4
5
=> 1..5
irb(main):009:0> (1...5).each do |n| p n end
1
2
3
4
```

100まで表示したいのでこうですね。

``` bash
irb(main):010:0> (1..100).each do |n| p n end
1
2
3
..
99
100
=> 1..100
```

`FizzBuzz::print_1_to_100` **メソッド** の **明白な実装** イメージができましたか？ `irb` を終了させてプロダクトコードを変更しましょう。

``` bash
irb(main):011:0> exit
```

``` ruby
...
  def self.print_1_to_100
    result = []
    (1..100).each do |n|
      result << n
    end
    result
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 38412

 FAIL["test_配列の初めは文字列の1を返す", #<Minitest::Reporters::Suite:0x00007f858480edf8 @name="FizzBuzz::1から
100までの数の配列を返す">, 0.0012219999989611097]
 test_配列の初めは文字列の1を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
        Expected: "1"
          Actual: 1
        main.rb:38:in `test_配列の初めは文字列の1を返す'

 FAIL["test_配列の最後は文字列の100を返す", #<Minitest::Reporters::Suite:0x00007f858480c8f0 @name="FizzBuzz::1から100までの数の配列を返す">, 0.0014040000023669563]
 test_配列の最後は文字列の100を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
        Expected: "100"
          Actual: 100
        main.rb:43:in `test_配列の最後は文字列の100を返す'

  6/6: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00218s
6 tests, 6 assertions, 2 failures, 0 errors, 0 skips
```

ファッ！？また、やらかしました。文字列に変換しなといけませんね。

``` ruby
...
  def self.print_1_to_100
    result = []
    (1..100).each do |n|
      result << n.to_s
    end
    result
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 40179

  6/6: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00196s
6 tests, 6 assertions, 0 failures, 0 errors, 0 skips
```

ちなみに、*do …​ endを使う代わりに、{}で囲んでもブロックを作れる*[6](#pruby)のでこのように書き換えることができます。

``` ruby
...
  def self.print_1_to_100
    result = []
    (1..100).each { |n| result << n.to_s }
    result
  end
end
```

変更したらテストして確認します。

``` bash
$ ruby main.rb
Started with run options --seed 59102

  7/7: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00236s
7 tests, 7 assertions, 0 failures, 0 errors, 0 skips
```

ここで、一旦コミットしておきましょう。

``` bash
$ git add main.rb
$ git commit -m 'test: 1から100までの数を返す'
```

TODOリスト

  - 1 から 100 までの数の配列を返す

      - ~~配列の初めは文字列の1を返す~~

      - ~~配列の最後は文字列の100を返す~~

  - プリントする

#### メソッド呼び出し

1から100までの数の配列を返すメソッドはできました。しかし、このプログラムは1から100までの数を `FizzBuzz::generate` した結果を返すのが正しい振る舞いですよね。 **TODOリスト** を追加してテストも追加します。

TODOリスト

  - 1 から 100 までの数の配列を返す

      - ~~配列の初めは文字列の1を返す~~

      - ~~配列の最後は文字列の100を返す~~

      - **配列の2番めは文字列のFizzを返す**

  - プリントする

<!-- end list -->

``` ruby
...
      def test_配列の2番目は文字列のFizzを返す
        result = FizzBuzz.print_1_to_100
        assert_equal 'Fizz', result[2]
      end
    end
  end
end
```

``` ruby
$ ruby main.rb
Started with run options --seed 50411

 FAIL["test_配列の2番目は文字列のFizzを返す", #<Minitest::Reporters::Suite:0x00007fe8a1917dc8 @name="FizzBuzz::1から100までの数の配列を返す">, 0.01608900000428548]
 test_配列の2番目は文字列のをFizz返す#FizzBuzz::1から100までの数の配列を返す (0.02s)
        --- expected
        +++ actual
        @@ -1 +1,3 @@
        -"Fizz"
        +# encoding: US-ASCII
        +#    valid: true
        +"3"
        main.rb:48:in `test_配列の2番目は文字列のFizzを返す'

  7/7: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.03112s
7 tests, 7 assertions, 1 failures, 0 errors, 0 skips
```

ですよね、ここは **繰り返し処理** の中で `FizzBuzz::generate` を呼び出すように変更しましょう。

``` ruby
...
  def self.print_1_to_100
    result = []
    (1..100).each { |n| result << generate(n) }
    result
  end
end
```

``` ruby
$ ruby main.rb
Started with run options --seed 15549

 FAIL["test_配列の最後は文字列の100を返す", #<Minitest::Reporters::Suite:0x00007ff80a907e28 @name="FizzBuzz::1から100までの数の配列を返す">, 0.001347000004898291]
 test_配列の最後は文字列の100を返す#FizzBuzz::1から100までの数の配列を返す (0.00s)
        Expected: "100"
          Actual: "Buzz"
        main.rb:43:in `test_配列の最後は文字列の100を返す'

  7/7: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00218s
7 tests, 7 assertions, 1 failures, 0 errors, 0 skips
```

新規に追加したテストはパスしたのですが２つ目のテストが失敗しています。これはテストケースが間違っていますね。

``` ruby
...
      def test_配列の最後は文字列のBuzzを返す
        result = FizzBuzz.print_1_to_100
        assert_equal 'Buzz', result.last
      end

      def test_配列の2番目は文字列のFizzを返す
        result = FizzBuzz.print_1_to_100
        assert_equal 'Fizz', result[2]
      end
    end
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 21247

  7/7: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00217s
7 tests, 7 assertions, 0 failures, 0 errors, 0 skips
```

他のパターンも明記しておきましょう。

``` ruby
...
    describe '1から100までのFizzBuzzの配列を返す' do
      def test_配列の初めは文字列の1を返す
        result = FizzBuzz.print_1_to_100
        assert_equal '1', result.first
      end

      def test_配列の最後は文字列のBuzzを返す
        result = FizzBuzz.print_1_to_100
        assert_equal 'Buzz', result.last
      end

      def test_配列の2番目は文字列のFizzを返す
        result = FizzBuzz.print_1_to_100
        assert_equal 'Fizz', result[2]
      end

      def test_配列の4番目は文字列のBuzzを返す
        result = FizzBuzz.print_1_to_100
        assert_equal 'Buzz', result[4]
      end

      def test_配列の14番目は文字列のFizzBuzzを返す
        result = FizzBuzz.print_1_to_100
        assert_equal 'FizzBuzz', result[14]
      end
    end
  end
end
```

**説明変数** への代入が重複しています。ついでに **メソッドの抽出** をして重複をなくしておきましょう。

> 最初のステップ「準備(Arrange)」は、テスト間で重複しがちだ。それとは対象的に「実行(Act)」「アサート(Assert)」は重複しないことが多い。
>
> —  テスト駆動開発

``` ruby
...
    describe '1から100までのFizzBuzzの配列を返す' do
      def setup
        @result = FizzBuzz.print_1_to_100
      end

      def test_配列の初めは文字列の1を返す
        assert_equal '1', @result.first
      end

      def test_配列の最後は文字列のBuzzを返す
        assert_equal 'Buzz', @result.last
      end

      def test_配列の2番目は文字列のFizzを返す
        assert_equal 'Fizz', @result[2]
      end

      def test_配列の4番目は文字列のBuzzを返す
        assert_equal 'Buzz', @result[4]
      end

      def test_配列の14番目は文字列のFizzBuzzを返す
        assert_equal 'FizzBuzz', @result[14]
      end
    end
  end
```

``` bash
$ ruby main.rb
Started with run options --seed 17460

  9/9: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00207s
9 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

とりあえず、現時点で仕様を満たすプログラムにはなったみたいですね。

``` bash
$ git add main.rb
$ git commit -m 'test: 1から100までのFizzBuzzの配列を返す'
```

TODOリスト

  - ~~1 から 100 までのFizzBuzzの配列を返す~~

      - ~~配列の初めは文字列の1を返す~~

      - ~~配列の最後は文字列の100を返す~~

      - ~~配列の2番めは文字列のFizzを返す~~

      - ~~配列の4番目は文字列のBuzzを返す~~

      - ~~配列の14番目は文字列のFizzBuzzを返す~~

  - プリントする

#### 配列や繰り返し処理の理解

まだリファクタリングが残っているのですがその前にRubyの配列メソッドの理解をもう少し深めたいので **学習用テスト** を追加しましょう。

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
      assert_equal %w[1 10 13 2 3 4], %w[2 4 13 3 1 10].sort
      assert_equal %w[1 2 3 4 10 13],
                   %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i }
      assert_equal %w[13 10 4 3 2 1],
                   %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i }
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

``` bash
$ ruby main.rb
Started with run options --seed 18136

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00307s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

``` bash
$ git add main.rb
$ git commit -m 'test: 学習用テスト'
```

### コードの不吉な臭い

終わりが見えてきましたがまだリファクタリングの必要がありそうです。

> 開発を終えるまでに考えつくまでに考えつく限りのテストを書き、テストに支えられたリファクタリングが、網羅性のあるテストに支えられてたリファクタリングになるようにしなければならない。
>
> —  テスト駆動開発

ここでプロダクトコードを眺めてみましょう。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero? && number.modulo(5).zero?
      result = 'FizzBuzz'
    elsif number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end
    result
  end

  def self.print_1_to_100
    result = []
    (1..100).each { |n| result << generate(n) }
    result
  end
end
```

**コードの不吉な臭い** が漂ってきませんか？私が感じた部分を解説していきますね。

#### 不思議な名前

> 不思議な名前
>
> 明快なコードにするために最も重要なのは、適切な名前付けです。
>
> —  リファクタリング(第2版)

> 変数や関数などの構成要素の名前は、抽象的ではなく具体的なものにしよう。
>
> —  リーダブルコード

まず、気になったのが `print_1_to_100` メソッドです。このメソッドはFizzBuzzの配列を返すメソッドであって1から100までを表示するメソッドではありませんよね。ここは **メソッド名の変更** を適用して処理の内容に沿った名前に変更しましょう。え？動いている処理をわざわざ変更してプログラムを壊す危険を犯す必要があるのかですって。確かに自動テストのない状況でドジっ子プログラマがそんなことをすればいずれ残念なことになるでしょうね。でも、すでに自動テストが用意されている今なら自信をもって動いている処理でも変更できますよね。

> リファクタリングに入る前に、しっかりとした一連のテスト群を用意しておくこと。これらのテストには自己診断機能が不可欠である。
>
> —  リファクタリング(第2版)

> テストは不安を退屈に変える賢者の石だ。
>
> —  テスト駆動開発

``` ruby
...
  def self.print_1_to_100
    result = []
    (1..100).each { |n| result << generate(n) }
    result
  end
end
```

``` ruby
...
  def self.generate_list
    result = []
    (1..100).each { |n| result << generate(n) }
    result
  end
end
```

変更で壊れていないか確認します。

``` bash
$ ruby main.rb
Started with run options --seed 47414

ERROR["test_配列の初めは文字列の1を返す", #<Minitest::Reporters::Suite:0x00007fe9e6858108 @name="FizzBuzz::1から
100までのFizzBuzzの配列を返す">, 0.0023099999998521525]
 test_配列の初めは文字列の1を返す#FizzBuzz::1から100までのFizzBuzzの配列を返す (0.00s)
NoMethodError:         NoMethodError: undefined method `print_1_to_100' for FizzBuzz:Class
            main.rb:37:in `setup'
...

ERROR["test_配列の最後は文字列のBuzzを返す", #<Minitest::Reporters::Suite:0x00007fe9f7097160 @name="FizzBuzz::1から100までのFizzBuzzの配列を返す">, 0.011574000000109663]
 test_配列の最後は文字列のBuzzを返す#FizzBuzz::1から100までのFizzBuzzの配列を返す (0.01s)
NoMethodError:         NoMethodError: undefined method `print_1_to_100' for FizzBuzz:Class
            main.rb:37:in `setup'

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01479s
19 tests, 16 assertions, 0 failures, 5 errors, 0 skips
```

いきなり失敗しちゃいました。でも、焦らずエラーメッセージを読みましょう。 ``NoMethodError: NoMethodError:undefined method `print_1_to_100' for FizzBuzz:Class`` メソッド名の変更したけどテストは以前のままでしたね。

``` ruby
...
    describe '1から100までのFizzBuzzの配列を返す' do
      def setup
        @result = FizzBuzz.print_1_to_100
      end
...
```

``` ruby
...
    describe '1から100までのFizzBuzzの配列を返す' do
      def setup
        @result = FizzBuzz.generate_list
      end
...
```

``` bash
$ ruby main.rb
Started with run options --seed 54699

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00351s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

プロダクトコードは壊れていなことが確認できたので自信を持ってコミットしておきましょう。

``` bash
$ git add main.rb
$ git commit -m 'refactor:　メソッド名の変更'
```

> TDDにおけるテストの考え方は実用主義に貫かれている。TDDにおいてテストは目的を達成するための手段であり、その目的は、大きなる自信を伴うコードだ。
>
> —  テスト駆動開発

#### 長い関数

> 長い関数
>
> 経験上、長く充実した人生を送るのは、短い関数を持ったプログラムです。
>
> —  リファクタリング(第2版)

次に気になったのが `FizzBuzz::generate` メソッド内のif分岐処理ですね。こうした条件分岐には仕様変更の際に追加ロジックが新たなif分岐として追加されてどんどん長くなって読みづらいコードに成長する危険性があります。そういうコードは早めに対策を打っておくのが賢明です。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s
    if number.modulo(3).zero? && number.modulo(5).zero?
      result = 'FizzBuzz'
    elsif number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end
    result
  end

  def self.generate_list
    result = []
    (1..100).each { |n| result << generate(n) }
    result
  end
end
```

まずコードをもう少し読みやすくしましょう。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s

    if number.modulo(3).zero? && number.modulo(5).zero?
      result = 'FizzBuzz'
    elsif number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end

    result
  end

  def self.generate_list
    result = []

    (1..100).each { |n| result << generate(n) }

    result
  end
end
```

`FizzBuzz` の **メソッド** は大きく分けて **変数** の初期化 **条件分岐** **繰り返し処理** による判断、計算そして結果の **代入** を行い最後に **代入** された **変数** を返す流れになっています。 そこで各単位ごとにスペースを挿入してコードの可読性を上げておきましょう。

> 人間の脳はグループや階層を１つの単位として考える。コードの概要をすばやく把握してもらうには、このような「単位」を作ればいい。
>
> —  リーダブルコード

処理の単位ごとに区切りをつけました。次はif分岐ですがこうします。

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s

    if number.modulo(3).zero? && number.modulo(5).zero?
      result = 'FizzBuzz'
    elsif number.modulo(3).zero?
      result = 'Fizz'
    elsif number.modulo(5).zero?
      result = 'Buzz'
    end

    result
  end
...
```

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s

    return 'FizzBuzz' if number.modulo(3).zero? && number.modulo(5).zero?
    return 'Fizz' if number.modulo(3).zero?
    return 'Buzz' if number.modulo(5).zero?

    result
  end
...
```

``` bash
$ ruby main.rb
Started with run options --seed 62095

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00296s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

条件に該当した場合は処理を最後まで進めずその場で終了させる書き方を **ガード節** と言います。このように書くことで追加ロジックが発生しても既存のコードを編集することなく追加することができるので安全に簡単に変更できるコードにすることができます。

> ガード節による入れ子条件記述の置き換え
>
> メソッド内に正常ルートが不明確な条件つき振る舞いがある。
>
> 特殊ケースすべてに対してガード節を使う。
>
> —  新装版 リファクタリング

> 関数で複数のreturn文を使ってはいけないと思っている人がいる。アホくさ。関数から早く返すのはいいことだ。むしろ望ましいときもある。
>
> —  リーダブルコード

``` bash
$ git add main.rb
$ git commit -m 'refactor: ガード節による入れ子条件の置き換え'
```

どの条件にも該当しない場合は数字を文字列してかえすのですが **一時変数** の `result` は最後でしか使われていませんね。このような場合は **変数のインライン化** を適用しましょう。

> 一時変数のインライン化
>
> 簡単な式によって一度だけ代入される一時変数があり、それが他のリファクタリングの障害となっている。
>
> その一時変数への参照をすべて式で置き換える。
>
> —  新装版 リファクタリング

``` ruby
class FizzBuzz
  def self.generate(number)
    result = number.to_s

    return 'FizzBuzz' if number.modulo(3).zero? && number.modulo(5).zero?
    return 'Fizz' if number.modulo(3).zero?
    return 'Buzz' if number.modulo(5).zero?

    result
  end
...
```

``` ruby
class FizzBuzz
  def self.generate(number)
    return 'FizzBuzz' if number.modulo(3).zero? && number.modulo(5).zero?
    return 'Fizz' if number.modulo(3).zero?
    return 'Buzz' if number.modulo(5).zero?

    number.to_s
  end
...
```

``` bash
$ ruby main.rb
Started with run options --seed 2528

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00255s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

変更によって壊れていないことが確認できたのでコミットします。

``` bash
$ git add main.rb
$ git commit -m 'refactor:　変数のインライン化'
```

続いて、FizzBuzzを判定する部分ですがもう少しわかりやすくするため **説明用変数の導入** を適用します。

> 説明用変数の導入
>
> 複雑な式がある。
>
> その式の結果または部分的な結果を、その目的を説明する名前をつけた一時変数に代入する。
>
> —  リファクタリング(第2版)

``` ruby
class FizzBuzz
  def self.generate(number)
    return 'FizzBuzz' if number.modulo(3).zero? && number.modulo(5).zero?
    return 'Fizz' if number.modulo(3).zero?
    return 'Buzz' if number.modulo(5).zero?

    number.to_s
  end
...
```

``` ruby
class FizzBuzz
  def self.generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if number.modulo(3).zero? && number.modulo(5).zero?
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end
...
```

３で割り切れる場合の結果を `isFizz` 変数に 5で割り切れる場合の結果 `isBuzz` 変数に代入して使えるようにしました。このような変数を **説明変数** と呼びます。また似たようなパターンに **要約変数** というものがあります。FizzBuzzを返す判定部分にこの **説明変数** を適用しました。壊れていないか確認しておきましょう。

> 説明変数
>
> 式を簡単に分割するには、式を表す変数を使えばいい。この変数を「説明変数」と呼ぶこともある。
>
> —  リーダブルコード

> 要約変数
>
> 大きなコードの塊を小さな名前に置き換えて、管理や把握を簡単にする変数のことを要約変数と呼ぶ。
>
> —  リーダブルコード

``` ruby
class FizzBuzz
  def self.generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end
...
```

``` bash
$ ruby main.rb
Started with run options --seed 4314

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00262s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

壊れていませんね。ではコミットしておきましょう。

``` bash
$ git add main.rb
$ git commit -m 'refactor:　変数の抽出'
```

#### ループと変更可能なデータ

> ループ
>
> プログラミング言語の黎明期から、ループは中心的な存在でした。しかし今ではベルボトムのジーンズやペナントのお土産のように、あまり重要でなくなりつつあります。
>
> —  リファクタリング(第2版)

`FizzBuzz::generate` メソッドのリファクタリングはできたので続いて `FizzBuzz::generate_list` メソッドを見ていきましょう。

``` ruby
...
  def self.generate_list
    result = []

    (1..100).each { |n| result << generate(n) }

    result
  end
end
```

空の **配列** を変数に代入してその変数に `FizzBuzz::generate` メソッドの結果を追加して返す処理ですがもしこのような変更をしてしまったらどうなるでしょうか？

``` ruby
...
  def self.generate_list
    result = []

    (1..100).each { |n| result << generate(n) }

    result = []
    result
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 19180

 FAIL["test_配列の14番目は文字列のをFizzBuzz返す", #<Minitest::Reporters::Suite:0x00007fa72805c018 @name="FizzBuzz::1から100までのFizzBuzzの配列を返す">, 0.0021289999967848416]
 test_配列の14番目は文字列のをFizzBuzz返す#FizzBuzz::1から100までのFizzBuzzの配列を返す (0.00s)
        Expected: "FizzBuzz"
          Actual: nil
        main.rb:57:in `test_配列の14番目は文字列のをFizzBuzz返す'
...

Finished in 0.03063s
19 tests, 21 assertions, 5 failures, 0 errors, 0 sk
```

せっかく作った配列を初期化して返してしまいましたね。このようにミュータブルな変数はバグを作り込む原因となる傾向があります。まず一時変数を使わないように変更しましょう。

> 変更可能なデータ
>
> データの変更はしばしば予期せぬ結果や、厄介なバグを引き起こします。
>
> —  リファクタリング(第2版)

> 「永続的に変更されない」変数は扱いやすい。
>
> —  リーダブルコード

``` ruby
...
  def self.generate_list
    return (1..100).each { |n| result << generate(n) }
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 56578

ERROR["test_配列の4番目は文字列のをBuzz返す", #<Minitest::Reporters::Suite:0x00007fe705854af0 @name="FizzBuzz::1から100までのFizzBuzzの配列を返す">, 0.001975000002857996]
 test_配列の4番目は文字列のをBuzz返す#FizzBuzz::1から100までのFizzBuzzの配列を返す (0.00s)
NameError:         NameError: undefined local variable or method `result' for FizzBuzz:Class
            main.rb:153:in `block in generate_list'
            main.rb:153:in `each'
            main.rb:153:in `generate_list'
            main.rb:37:in `setup'
...
  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01032s
19 tests, 16 assertions, 0 failures, 5 errors, 0 skips
```

一時変数 `result` は使わないので

``` ruby
...
  def self.generate_list
    return (1..100).each { |n| generate(n) }
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 35137

ERROR["test_配列の4番目は文字列のをBuzz返す", #<Minitest::Reporters::Suite:0x00007f7f1384ff78 @name="FizzBuzz::1から100までのFizzBuzzの配列を返す">, 0.0014560000017809216]
 test_配列の4番目は文字列のをBuzz返す#FizzBuzz::1から100までのFizzBuzzの配列を返す (0.00s)
NoMethodError:         NoMethodError: undefined method `[]' for 1..100:Range
            main.rb:53:in `test_配列の4番目は文字列のをBuzz返す'
...
  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.03285s
19 tests, 18 assertions, 2 failures, 3 errors, 0 skips
```

結果を配列にして返したいのですが **eachメソッド** ではうまくできませんね。Rubyには新しい配列を作成する **mapメソッド** が用意されいるのでそちらを使いましょう。

> mapは配列の要素を画する際によく利用されるメソッドで、ブロックの最後の要素（メモ）で新しい配列を作ります。
>
> —  かんたんRuby

``` ruby
...
  def self.generate_list
    return (1..100).map { |n| generate(n) }
  end
end
```

``` bash
 $ ruby main.rb
Started with run options --seed 44043

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00261s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

うまくいきましたね。あと、Rubyではreturnを省略できるので

``` ruby
...
  def self.generate_list
    (1..100).map { |n| generate(n) }
  end
end
```

``` bash
$ ruby main.rb
Started with run options --seed 7994

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00238s
```

**パイプラインによるループの置き換え** の適用により **eachメソッド** による繰り返し処理を **mapメソッド** を使ったイミュータブルなコレクションパイプライン処理に変えることができました。

> パイプラインによるループの置き換え
>
> 多くのプログラマと同様に、私もオブジェクトの集合の反復処理にはループを使うように教えられました。しかし言語環境は、よりすぐれた仕組みとしてコレクションのパイプラインを提供するようになりました。
>
> —  リファクタリング(第2版)
>

> Rubyに限らず、プログラミングの世界ではしばしばミュータブル（mutable)とイミュータブル（imutable）と言う言葉が登場します。ミュータブルは「変更可能な」という意味で、反対にイミュータブルは「変更できない、不変の」という意味です。
>
> —  プロを目指す人のためのRuby入門

``` bash
$ git add main.rb
$ git commit -m 'refactor: パイプラインによるループの置き換え'
```

#### マジックナンバー

最大値は100にしていますが変更することもあるので **マジックナンバーの置き換え** を適用してわかりやすくしておきましょう。

> シンボル定数によるマジックナンバーの置き換え
>
> 特別な意味を持った数字のリテラルがある。
>
> 定数を作り、それにふさわしい名前をつけて、そのリテラルを置き換える。
>
> —  新装版 リファクタリング

Rubyでは定数は英字の大文字で始まる名前をつけると自動的に定数として扱われます。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

...

  def self.generate_list
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

意味のわかる定数として宣言しました。コードに直接記述された `100` をといった **数値リテラル** はマジックナンバーと呼ばれ往々にして後で何を意味するものかわからなくなり変更を難しくする原因となります。早めに意味を表す定数にしておきましょう。

> 名前付けされずにプログラム内に直接記述されている数値をマジックナンバーと呼び、一般的には極力避けるようにします。
>
> —  かんたんRuby

> いい名前というのは、変数の目的や値を表すものだ。
>
> —  リーダブルコード

``` bash
$ ruby main.rb
Started with run options --seed 32408

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00241s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

テストは通りました。でもこのコードは初見の人には分かりづらいのでコメントを入れておきましょう。Rubyの **単一行コメントアウト** のやり方は行頭に `#` を使います。

``` ruby
...
  def self.generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

ここではなぜこのような処理を選択したかをコメントしましたが何でもコメントすればよいというわけではありません。

> コメント
>
> ここでコメントについて言及しているのは、コメントが消臭剤として使われることがあるからです。コメントが非常に丁寧に書かれているのは、実はわかりにくいコードを補うためだったとうことがよくあるのです。
>
> —  リファクタリング(第2版)
>

> コメントを書くのであれば、正確に書くべきだ（できるだけ明確で詳細に）。また、コメントには画面の領域を取られるし、読むのにも時間がかかるので、簡潔なものでなければいけない。
>
> —  リーダブルコード

``` bash
$ git add main.rb
$ git commit -m 'refactor: マジックナンバーの置き換え'
```

### 動作するきれいなコード

TODOリスト

  - ~~数を文字列にして返す~~

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - ~~3の倍数のときは数の代わりに｢Fizz｣と返す~~

      - ~~3を渡したら文字列"Fizz"を返す~~

  - ~~5 の倍数のときは｢Buzz｣と返す~~

      - ~~5を渡したら文字列"Buzz"を返す~~

  - ~~13 と 5 両方の倍数の場合には｢FizzBuzz｣と返す~~

      - ~~15を渡したら文字列FizzBuzzを返す~~

  - ~~1 から 100 までのFizzBuzzの配列を返す~~

      - ~~配列の初めは文字列の1を返す~~

      - ~~配列の最後は文字列の100を返す~~

      - ~~配列の2番めは文字列のFizzを返す~~

      - ~~配列の4番目は文字列のBuzzを返す~~

      - ~~配列の14番目は文字列のFizzBuzzを返す~~

  - プリントする

**TODOリスト** も残すところあと１つとなりました。これまで `main.rb` ファイル１つだけで開発を行ってきましたがリリースするにはもうひと手間かけたほうがいいでしょうね。libディレクトリを作成したあと `main.rb` ファイルを `fizz_buzz.rb` ファイルに名前を変更してlibディレクトリに移動します。

    /
    |--lib/
        |
         -- fizz_buzz.rb

続いてテストコードをテストディレクトリに保存してプログラム本体とテストコードを分離します

    /
    |--lib/
        |
         -- fizz_buzz.rb
    |--test/
        |
         -- fizz_buzz_test.rb

分離したテストが動くか確認しておきましょう。

``` bash
$ ruby test/fizz_buzz_test.rb
Started with run options --seed 17134

ERROR["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x00007fc07a085060 @name="FizzBuzz::その他の場合">, 0.001282999997783918]
 test_1を渡したら文字列1を返す#FizzBuzz::その他の場合 (0.00s)
NameError:         NameError: uninitialized constant FizzBuzzTest::FizzBuzz
        Did you mean?  FizzBuzzTest
            test/fizz_buzz_test.rb:8:in `setup'
...
  19/19: [===============================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.03717s
19 tests, 12 assertions, 0 failures, 9 errors, 0 skips
```

テストファイルからFizzBuzzクラスを読み込めるようにする必要があります。

``` ruby
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzTest < Minitest::Test
...
```

Rubyで別のファイルを読み込むには **require** を使います。

> requireを使う用途は主に三つあります。
>
>   - 標準添付ライブラリを読み込む
>
>   - 第三者が作成しているライブラリを読み込む
>
>   - 別ファイルに定義した自分のファイルを読み込む
>
> —  かんたんRuby

また、**require\_relative**
> という方法も用意されています。どう違うのでしょうか？

> require\_relativeは$LOAD\_PATHの参照は行わず「relative」という名称の通り相対的なパスでファイルの読み込みを行います。
>
> —  かんたんRuby

ちょっと何言ってるかわからないうちは **require** を上記のフォルダ構成で使っていてください。一応以下の使い分けがありますが今は頭の隅に留めるだけでいいと思います。

> requireは標準添付ライブラリなどの自分が書いていないコードを読み込む時に使い、こちらのrequire\_relativeは自分の書いたコードを読み込む時に使うように使い分けるのが良いでしょう。
>
> —  かんたんRuby

``` bash
$ ruby test/fizz_buzz_test.rb
Started with run options --seed 44438

  19/19: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00279s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

では最後に `main.rb` ファイルを追加して `FizzBuzz:generate_list` を呼び出すようにします。

    /main.rb
      |--lib/
          |
           -- fizz_buzz.rb
      |--test/
          |
           -- fizz_buzz_test.rb

``` ruby
require './lib/fizz_buzz.rb'

puts FizzBuzz.generate_list
```

**puts** は結果を画面に出力するメソッドです。 先程は **p** メソッドを使って画面に **配列** の中身を１件ずつ表示していましたが今回は **配列** 自体を改行して画面に出力するため **puts** メソッドを使います。機能的にはほどんど変わらないのですが以下の様に使い分けるそうです。

> まず、用途としてはputsメソッドとprintメソッドは一般ユーザ向け、pメソッドは開発者向け、というふうに別かれます。
>
> —  プロを目指す人のためのRuby入門

``` bash
$ ruby main.rb
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
Buzz
```

ちなみに **print** メソッドを使った場合はこのように出力されます。

``` bash
$ ruby main.rb
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz", "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz", "31", "32", "Fizz", "34", "Buzz", "Fizz", "37", "38", "Fizz", "Buzz", "41", "Fizz", "43", "44", "FizzBuzz", "46", "47", "Fizz", "49", "Buzz", "Fizz", "52", "53", "Fizz", "Buzz", "56", "Fizz", "58", "59", "FizzBuzz", "61", "62", "Fizz", "64", "Buzz", "Fizz", "67", "68", "Fizz", "Buzz", "71", "Fizz", "73", "74", "FizzBuzz", "76", "77", "Fizz", "79", "Buzz", "Fizz", "82", "83", "Fizz", "Buzz", "86", "Fizz", "88", "89", "FizzBuzz", "91", "92", "Fizz", "94", "Buzz", "Fizz", "97", "98", "Fizz", "Buzz"] $
```

プログラムの完成です。コミットしておきましょう。

``` bash
$ git commit -m 'feat: プリントする'
```

TODOリスト

  - ~~数を文字列にして返す~~

      - ~~1を渡したら文字列"1"を返す~~

      - ~~2を渡したら文字列"2"を返す~~

  - ~~3の倍数のときは数の代わりに｢Fizz｣と返す~~

      - ~~3を渡したら文字列"Fizz"を返す~~

  - ~~5 の倍数のときは｢Buzz｣と返す~~

      - ~~5を渡したら文字列"Buzz"を返す~~

  - ~~13 と 5 両方の倍数の場合には｢FizzBuzz｣と返す~~

      - ~~15を渡したら文字列FizzBuzzを返す~~

  - ~~1 から 100 までのFizzBuzzの配列を返す~~

      - ~~配列の初めは文字列の1を返す~~

      - ~~配列の最後は文字列の100を返す~~

      - ~~配列の2番めは文字列のFizzを返す~~

      - ~~配列の4番目は文字列のBuzzを返す~~

      - ~~配列の14番目は文字列のFizzBuzzを返す~~

  - ~~プリントする~~

#### ふりかえり

`FizzBuzz` プログラムの最初のバージョンをリリースすることができたのでこれまでのふりかえりをしておきましょう。

まず **TODOリスト** を作成して **テストファースト** で１つずつ小さなステップで開発を進めていきました。 **仮実装を経て本実装へ** の過程で Rubyの **クラス** を定義して **文字列リテラル** を返す **メソッド** を作成しました。この時点でRubyの **オブジェクトとメソッド** という概念に触れています。

> Rubyの世界では、ほぼどのような値もオブジェクトという概念で表されます。オブジェクトという表現はかなり範囲の広い表現方法で、クラスやインスタンスを含めてオブジェクトと称します。
>
> —  かんたんRuby

> プログラミング言語においてメソッド、あるいは関数と呼ばれるものを簡単に説明すると処理をひとかたまりにまとめたものと言って良いでしょう。
>
> —  かんたんRuby

ちょっと何言ってるかわからないかもしれませんが、今はそういう概念があってこうやって書くのねという程度の理解で十分です。

その後 **リファクタリング** を通じて多くの概念に触れることになりました。 まず **変数名の変更** でRubyにおける **変数**の概念と操作を通じて名前付けの重要性を学びました。

> Rubyでは変数を扱うために特別な宣言やキーワードは必要ありません。「=」 の左辺に任意の変数名を記述するだけで変数宣言となります。
>
> —  かんたんRuby

続いて **明白な実装** を通して **制御構造** のうち **条件分岐** のための **if式** と **演算子** を使いプログラムを制御し判定・計算をする方法を学びました。また、**アルゴリズムの置き換え** を適用してコードをよりわかりやすくしました。

> Rubyではプログラムを構成する最小の要素を式と呼びます。変数やリテラル、制御構文、演算子などが式として扱われます。
>
> —  かんたんRuby

そして、 **学習用テスト** を通して新しい問題を解決するために **配列オブジェクト** **レンジオブジェクト** といった **文字列リテラル** **数値リテラル** 以外の **データ構造** の使い方を学習して、**配列** を操作するための **制御構造** として **繰り返し処理** を **eachメソッド** を使って実現しました。

> これら「100」や「3.14」といった部分を数値リテラルと呼びます。
>
> —  かんたんRuby

> このように文字列をシングルクオートやダブルクオートで括っている表記を文字列リテラルと呼びます。
>
> —  かんたんRuby

仕上げは、**コードの不吉な臭い** からさらなる改善を実施しました。 **不思議な名前** の **メソッド** を **自動的テスト**を用意することで自信を持って **リファクタリング** を実施し、**長い関数** に対して **ガード節** を導入し **一時変数** **説明変数** など **変数** バリエーションの取り扱いを学びました。そして、**ループ** と **変更可能なデータ** から **コレクションパイプライン** の使い方と **ミュータブル** **イミュータブル** の概念を学び、**コメント** のやり方と **定数** と **マジックナンバー** の問題を学びました。

最後に、**require** の使い方を通してファイルの分割方法を学ぶことができました。

ちょっと何言ってるかわからない単語ばかり出てきたかもしれませんがこれでRubyの基本の半分は抑えています。自分でFizzBuzzコードが書けて用語の意味が説明できるようになれば技能・学科第一段階の半分ぐらいといったところでしょうか。仮免許取得にはまだ習得しなければならない技術と知識がありますので。

#### 良いコード

以下のコードを作成しました。

**/main.rb.**

``` ruby
require './lib/fizz_buzz.rb'

puts FizzBuzz.generate_list
```

**/lib/fizz\_buzz.rb.**

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end

  def self.generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

**/test/fizz\_buzz\_test.rb.**

``` ruby
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
    def setup
      @fizzbuzz = FizzBuzz
    end

    describe '三の倍数の場合' do
      def test_3を渡したら文字列Fizzを返す
        assert_equal 'Fizz', @fizzbuzz.generate(3)
      end
    end

    describe '五の倍数の場合' do
      def test_5を渡したら文字列Buzzを返す
        assert_equal 'Buzz', @fizzbuzz.generate(5)
      end
    end

    describe '三と五の倍数の場合' do
      def test_15を渡したら文字列FizzBuzzを返す
        assert_equal 'FizzBuzz', @fizzbuzz.generate(15)
      end
    end

    describe 'その他の場合' do
      def test_1を渡したら文字列1を返す
        assert_equal '1', @fizzbuzz.generate(1)
      end

      def test_2を渡したら文字列2を返す
        assert_equal '2', @fizzbuzz.generate(2)
      end
    end

    describe '1から100までのFizzBuzzの配列を返す' do
      def setup
        @result = FizzBuzz.generate_list
      end

      def test_配列の初めは文字列の1を返す
        assert_equal '1', @result.first
      end

      def test_配列の最後は文字列のBuzzを返す
        assert_equal 'Buzz', @result.last
      end

      def test_配列の2番目は文字列のFizzを返す
        assert_equal 'Fizz', @result[2]
      end

      def test_配列の4番目は文字列のBuzzを返す
        assert_equal 'Buzz', @result[4]
      end

      def test_配列の14番目は文字列のFizzBuzzを返す
        assert_equal 'FizzBuzz', @result[14]
      end
    end
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
      assert_equal %w[1 10 13 2 3 4], %w[2 4 13 3 1 10].sort
      assert_equal %w[1 2 3 4 10 13],
                   %w[2 4 13 3 1 10].sort { |a, b| a.to_i <=> b.to_i }
      assert_equal %w[13 10 4 3 2 1],
                   %w[2 4 13 3 1 10].sort { |b, a| a.to_i <=> b.to_i }
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

どうでしょう、学習用テストは除くとしてプロダクトコードに対して倍以上のテストコードを作っていますよね。テストコードを作らず一発で `fizz_buzz.rb` のようなコードを書くことはできますか？ たしかに [fizz buzz ruby](https://www.google.com/search?hl=ja&sxsrf=ACYBGNTdUEAzXtUgi9nlBCK6fnpac2rtIg%3A1579588091710&source=hp&ei=-5kmXs7SKIPnwQO9rYbgBA&q=fizz+buzz+ruby&oq=fizz&gs_l=psy-ab.3.0.35i39l3j0l3j0i131j0.636.1384..2671...1.0..0.205.540.1j2j1......0....1..gws-wiz.......0i4j0i131i4.du79cnj-Ge4) といったキーワードで検索すればサンプルコードは見つかるのでコピーして同じ振る舞いをするコードをすぐに書くことはできるでしょう。でも仕様が追加された場合はどうしましょう。

仕様

    1 から 100 までの数をプリントするプログラムを書け。
    ただし 3 の倍数のときは数の代わりに｢Fizz｣と、5 の倍数のときは｢Buzz｣とプリントし、
    3 と 5 両方の倍数の場合には｢FizzBuzz｣とプリントすること。
    タイプごとに出力を切り替えることができる。
    タイプ１は通常、タイプ２は数字のみ、タイプ３は FizzBuzz の場合のみをプリントする。

また同じようなコードサンプルを探しますか？私ならば **TODOリスト** に以下の項目を追加することから始めます。

TODOリスト

  - タイプ1の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

次に何をやるかはもうわかりますよね。テスト駆動開発とはただ失敗するテストを１つずつ書いて通していくことではありません。

> TDDは分析技法であり、設計技法であり、実際には開発のすべてのアクティビティを構造化する技法なのだ。
>
> —  テスト駆動開発

ではテストファーストで書けば質の高い良いコードがかけるようになるのでしょうか？以下のコードを見てください。

``` ruby
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'

class FizzBuzz
  # fizz_buzzメソッドを実行する
  def self.fizz_buzz(n)
  a = n.to_s
    if n % 3 == 0
      a = 'Fizz'
    if n % 15 == 0
      a = 'FizzBuzz'
    end
        elsif n % 5 == 0
          a = 'Buzz'
        end
           a
  end

# 1から100までをプリントする
  def self.print_1_to_100
              n = []
    (1..100).each do |i|
  n << fizz_buzz(i)
                        end
  n
  end
end

class FizzBuzzTest < Minitest::Test
  describe 'FizzBuzz' do
    def setup
      @p = FizzBuzz
    end

      def test_15を渡したら文字列pを返す
        assert_equal 'FizzBuzz', FizzBuzz.fizz_buzz(15)
      end
      def test_3を渡したら文字列3を返す
        assert_equal 'Fizz', FizzBuzz.fizz_buzz(3)
      end
      def test_1を渡したら文字列1を返す
        assert_equal '1', @p.fizz_buzz(1)
      end
      def test_5を渡したら文字列Buzzを返す
        assert_equal 'Buzz', FizzBuzz.fizz_buzz(5)
      end

    describe '1から100までプリントする' do
  def setup
    @x = FizzBuzz.print_1_to_100
  end

  def test_配列の4番目は文字列のをBuzz返す
    assert_equal 'Buzz', @x[4]
  end

      def test_配列の初めは文字列の1を返す
        assert_equal '1', @x.first
      end

      def test_配列の最後は文字列のBuzzを返す
        assert_equal 'Buzz', FizzBuzz.print_1_to_100.last
      end

def test_配列の14番目は文字列のFizzBuzz返す
  assert_equal 'FizzBuzz', @x[14]
end
  def test_配列の2番目は文字列の2を返す
    assert_equal 'Fizz', @x[2]
  end

    end
  end
end
```

``` bash
$ ruby test/fizz_buzz_tfd_test.rb
Started with run options --seed 43131

  9/9: [===================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00135s
9 tests, 9 assertions, 0 failures, 0 errors, 0 skips
```

プログラムは動くしテストも通ります。でもこれはテスト駆動開発で作られたと言えるでしょうか？質の高い良いコードでしょうか？何が足りないかはわかりますよね。

> テスト駆動開発における質の向上の手段は、リファクタリングによる継続的でインクリメンタルな設計であり、「単なるテストファースト」と「テスト駆動開発」の違いはそこにあります。
>
> —  テスト駆動開発 付録C 訳者解説

そもそも良いコードは何なのでしょうか？いくつかの見解があるようです。

> TDDは「より良いコードを書けば、よりうまくいく」という素朴で奇妙な仮設によって成り立っている
>
> —  テスト駆動開発
>

> 「動作するきれいなコード」。RonJeffriesのこの簡潔な言葉が、テスト駆動開発(TDD)のゴールだ。動作するきれいなコードはあらゆる意味で価値がある。
>
> —  テスト駆動開発

> 良いコードかどうかは、変更がどれだけ容易なのかで決まる。
>
> —  リファクタリング(第2版)

> コードは理解しやすくなければいけない。
>
> —  リーダブルコード

> コードは他の人が最短時間で理解できるように書かなければいけない。
>
> —  リーダブルコード

> 優れたソースコードは「目に優しい」ものでなければいけない。
>
> —  リーダブルコード


少なくともテスト駆動開発のゴールに良いコードがあるということはいえるでしょう。え？どうやったら良いコードを書けるようになるかって？私が教えてほしいのですがただ言えることは他の分野と同様に規律の習得と絶え間ない練習と実践の積み重ねのむこうにあるのだろうということだけです。

> 私がかつて発見した、そして多くの人に気づいてもらいたい効果とは、反復可能な振る舞いを規則にまで還元することで、規則の適用は機会的に反復可能になるということだ。
>
> —  テスト駆動開発

>ここで、Kent Beckが自ら語ったセリフを思い出しました。「僕は、偉大なプログラマなんかじゃない。偉大な習慣を身につけた少しましなプログラマなんだ」。
>
> —  リファクタリング(第2版)

# エピソード2

## 自動化から始めるテスト駆動開発

エピソード1ではテスト駆動開発のゴールが **動作するきれいなコード** であることを学びました。では、良いコードを書き続けるためには何が必要になるでしょうか？それは[ソフトウェア開発の三種の神器](https://t-wada.hatenablog.jp/entry/clean-code-that-works)と呼ばれるものです。

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

**バージョン管理** と **テスティング** に関してはエピソード1で触れました。本エピソードでは最後の **自動化** に関しての解説と次のエピソードに備えたセットアップ作業を実施しておきたいと思います。ですがその前に **バージョン管理** で1つだけ解説しておきたいことがありますのでそちらから進めて行きたいと思います。

### コミットメッセージ

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

コミットメッセージにつけるプリフィックスに関しては [【今日からできる】コミットメッセージに 「プレフィックス」をつけるだけで、開発効率が上がった話](https://qiita.com/numanomanu/items/45dd285b286a1f7280ed)を参照ください。

### パッケージマネージャ

では **自動化** の準備に入りたいのですがそのためにはいくつかの外部プログラムを利用する必要があります。そのためのツールが **RubyGems** です。

> RubyGemsとは、Rubyで記述されたサードパーティ製のライブラリを管理するためのツールで、RubyGemsで扱うライブラリをgemパッケージと呼びます。
>
> —  かんたんRuby

**RubyGems** はすでに何度か使っています。例えばエピソード1の初めの `minitest-reporters`
のインストールなどです。

``` bash
$ gem install minitest-reporters
```

では、これからもこのようにして必要な外部プログラムを一つ一つインストールしていくのでしょうか？また、開発用マシンを変えた時にも同じことを繰り返さないといけないのでしょうか？面倒ですよね。そのような面倒なことをしないで済む仕組みがRubyには用意されています。それが **Bundler** です。

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

### 静的コード解析

良いコードを書き続けるためにはコードの品質を維持していく必要があります。エピソード1では **テスト駆動開発** によりプログラムを動かしながら品質の改善していきました。出来上がったコードに対する品質チェックの方法として **静的コード解析** があります。Ruby用 **静的コード解析** ツール[RuboCop](https://github.com/rubocop-hq/rubocop) を使って確認してみましょう。プログラムは先程 **Bundler** を使ってインストールしたので以下のコマンドを実行します。

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

なにかいろいろ出てきましたね。RuboCopの詳細に関しては [RuboCop is 何？](https://qiita.com/tomohiii/items/1a17018b5a48b8284a8b)を参照ください。`--lint` オプションをつけて実施してみましょう。

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

また何やら出てきましたね。 [W:Lint/AmbiguousBlockAssociation](https://rubocop.readthedocs.io/en/latest/cops_lint/#lintambiguousblockassociation)のメッセージを調べたところ、`fizz_buzz_test.rb` の以下の学習用テストコードは書き方がよろしくないようですね。

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

### コードフォーマッタ

良いコードであるためにはフォーマットも大切な要素です。

> 優れたソースコードは「目に優しい」ものでなければいけない。
>
> —  リーダブルコード

Rubyにはいくつかフォーマットアプリケーションはあるのですがここは `RuboCop` の機能を使って実現することにしましょう。以下のコードのフォーマットをわざと崩してみます。

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

編集した部分が `Use 2 (not 8) spaces for indentation.` と指摘されています。`--fix-layout` オプションで自動保存しておきましょう。

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

フォーマットが修正されたことが確認できましたね。ちなみに `--auto-correct` オプションでもフォーマットをしてくれるので通常はこちらのオプションで問題ないと思います。

### コードカバレッジ

静的コードコード解析による品質の確認はできました。では動的なテストに関してはどうでしょうか？ **コードカバレッジ** を確認する必要あります。

> コード網羅率（コードもうらりつ、英: Code coverage
> ）コードカバレッジは、ソフトウェアテストで用いられる尺度の1つである。プログラムのソースコードがテストされた割合を意味する。この場合のテストはコードを見ながら行うもので、ホワイトボックステストに分類される。
>
> —  ウィキペディア

Ruby用 **コードカバレッジ** 検出プログラムとして [SimpleCov](https://github.com/colszowka/simplecov)を使います。Gemfileに追加して **Bundler** でインストールをしましょう。

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

テスト実行後に `coverage` というフォルダが作成されます。その中の `index.html` を開くとカバレッジ状況を確認できます。セットアップが完了したらコミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'chore: コードカバレッジセットアップ'
```

### タスクランナー

ここまででテストの実行、静的コード解析、コードフォーマット、コードカバレッジを実施することができるようになりました。でもコマンドを実行するのにそれぞれコマンドを覚えておくのは面倒ですよね。例えばテストの実行は

``` bash
$ ruby test/fizz_buzz_test.rb
Started with run options --seed 21943

  19/19: [=======================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00261s
19 tests, 21 assertions, 0 failures, 0 errors, 0 skips
```

このようにしていました。では静的コードの解析はどうやりましたか？フォーマットはどうやりましたか？調べるのも面倒ですよね。いちいち調べるのが面倒なことは全部 **タスクランナー** にやらせるようにしましょう。

> タスクランナーとは、アプリケーションのビルドなど、一定の手順で行う作業をコマンド一つで実行できるように予めタスクとして定義したものです。
>
> —  かんたんRuby

Rubyの **タスクランナー** は `Rake` です。

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

テストは実施されたのですが警告メッセージが表示されるようになりました。メッセージの内容としては **学習用テスト** のテストメソッド名が重複していることが理由のようです。せっかくなので修正しておきましょう。

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

フォーマットは `rake rubocop:auto_correct` で一緒にやってくれるので特に必要は無いのですがプログラムの開発元が提供していないタスクを作りたい場合はこのように追加します。セットアップができたのでコミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'chore: タスクランナーセットアップ'
```

### タスクの自動化

良いコードを書くためのタスクをまとめることができました。でも、どうせなら自動で実行できるようにしたいですよね。タスクを自動実行するためのgemを追加します。[Guard](https://github.com/guard/guard)とそのプラグインの [Guard::Shell](https://github.com/guard/guard-shell) [Guard::Minitest](https://github.com/guard/guard-minitest) [guard-rubocop](https://github.com/yujinakayama/guard-rubocop) をインストールします。それぞれの詳細は以下を参照してください。

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

続いて `Rakefile` にguardタスクを追加します。あと、guardタスクをデフォルトにして `rake` を実行すると呼び出されるようにしておきます。

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

変更を感知してテストが実行されるた結果失敗していましました。コードを元に戻してテストをパスするようにしておきましょう。テストがパスすることが確認できたらコミットしておきましょう。このときターミナルでは `guard` が動いているので別ターミナルを開いてコミットを実施すると良いでしょう。

``` bash
$ git add .
$ git commit -m 'chore: タスクの自動化'
```

これで [ソフトウェア開発の三種の神器](https://t-wada.hatenablog.jp/entry/clean-code-that-works) の最後のアイテムの準備ができました。次回の開発からは最初にコマンドラインで `rake` を実行すれば良いコードを書くためのタスクを自動でやってくるようになるのでコードを書くことに集中できるようになりました。では、次のエピソードに進むとしましょう。

# エピソード3

## オブジェクト指向から始めるテスト駆動開発

### テスト駆動開発

エピソード1ので作成したプログラムに以下の仕様を追加します。

仕様

    1 から 100 までの数をプリントするプログラムを書け。
    ただし 3 の倍数のときは数の代わりに｢Fizz｣と、5 の倍数のときは｢Buzz｣とプリントし、
    3 と 5 両方の倍数の場合には｢FizzBuzz｣とプリントすること。
    タイプごとに出力を切り替えることができる。
    タイプ１は通常、タイプ２は数字のみ、タイプ３は FizzBuzz の場合のみをプリントする。

早速開発に取り掛かりましょう。エピソード2で開発環境の自動化をしているので以下のコマンドを実行するだけで開発を始めることができます。

``` bash
$ rake
```

`guard` が起動するとコンソールが使えなくなるのでもう一つコンソールを開いておきましょう。もしくは `.` を使うことで `guard` 内でコンソールのコマンドを呼び出すことができます。

``` bash
[1] guard(main)> . ls
coverage  Gemfile.lock  lib      provisioning  README.md  tmp
Gemfile   Guardfile     main.rb  Rakefile      test       Vagrantfile
[2] guard(main)> . pwd
/workspace/tdd_rb
[3] guard(main)> . git status
```

#### TODOリスト作成

まずは追加仕様を **TODOリスト** に落とし込んでいきます。

TODOリスト

  - タイプ1の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

#### タイプ1の場合

**テストファースト** **アサートファースト** で最初に失敗するテストから始めます。テストを追加しましょう。

ここでは既存の `FizzBuzz.generate` メソッドにタイプを **引数** として追加することで対応できるように変更してみたいと思います。まず、 `fizz_buzz_test.rb` ファイルに以下のテストコードを追加します。

``` ruby
...
  end

  describe 'タイプごとに出力を切り替えることができる' do
    describe 'タイプ1の場合' do
      def test_1を渡したら文字列1を返す
        assert_equal '1', FizzBuzz.generate(1, 1)
      end
    end
  end

  describe '配列や繰り返し処理を理解する' do
...
```

``` bash
...
05:32:51 - INFO - Running: all tests
Coverage report generated for MiniTest to /workspace/tdd_rb/coverage. 4 / 11 LOC (36.36%) covered.
Started with run options --guard --seed 37049

ERROR["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x00005623e6a24260 @name="タイプごとに出力を切り替えることができる::タイプ1の場合">, 0.0019176720088580623]
 test_1を渡したら文字列1を返す#タイプごとに出力を切り替えることができる::タイプ1の場合 (0.00s)
Minitest::UnexpectedError:         ArgumentError: wrong number of arguments (given 2, expected 1)
            /workspace/tdd_rb/lib/fizz_buzz.rb:6:in `generate'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:74:in `test_1を渡したら文字列1を返す'

  25/25: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00796s
25 tests, 26 assertions, 0 failures, 1 errors, 0 skips
...
```

`ArgumentError: wrong number of arguments (given 2, expected 1)` **引数** が違うと指摘されていますね。 `FizzBuzz.generate` メソッドの引数の変更したいのですが既存のテストを壊したくないのでここは **デフォルト引数** 使ってみましょう。

> メソッドの引数にはデフォルト値を指定する定義方法があります。これは、メソッドの引数を省略した場合に割り当てられる値です。
>
> —  かんたんRuby

``` bash
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end
...
```

``` bash
...
05:32:52 - INFO - Inspecting Ruby code style: test/fizz_buzz_test.rb Guardfile
 2/2 files |====================================== 100 =======================================>| Time: 00:00:00

2 files inspected, no offenses detected
05:32:54 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png
 0/0 files |====================================== 100 =======================================>| Time: 00:00:00

0 files inspected, no offenses detected
05:37:29 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
lib/fizz_buzz.rb:6:29: W: [Corrected] Lint/UnusedMethodArgument: Unused method argument - type. If it's necessary, use _ or _type as an argument name to indicate that it won't be used.
  def self.generate(number, type = 1)
                            ^^^^
 1/1 file |======================================= 100 =======================================>| Time: 00:00:00

1 file inspected, 1 offense detected, 1 offense corrected
05:37:31 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
 1/1 file |======================================= 100 =======================================>| Time: 00:00:00

1 file inspected, no offenses detected
[1] guard(main)>
05:39:37 - INFO - Run all
05:39:37 - INFO - Running: all tests
Coverage report generated for MiniTest to /workspace/tdd_rb/coverage. 4 / 11 LOC (36.36%) covered.
Started with run options --guard --seed 8607

  25/25: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00723s
25 tests, 27 assertions, 0 failures, 0 errors, 0 skips
...
```

ちなみにここでは 引数に `type=1` と入力したのですがコードフォーマットによって以下のように自動修正されます。

``` bash
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, _type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end
...
```

**case式** を使って **引数** を判定できるように変更しましょう。ちなみに `_type` をメソッド内で変数として使うと警告されるので `type` に変更しています。

``` ruby
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    case type
    when 1
      is_fizz = number.modulo(3).zero?
      is_buzz = number.modulo(5).zero?

      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    end
  end
...
```

``` bash
...
Started with run options --seed 51330


Progress: |=============================================================|

Finished in 0.00828s
25 tests, 27 assertions, 0 failures, 0 errors, 0 skips
04:27:12 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
 1/1 file |=================== 100 ====================>| Time: 00:00:00

1 file inspected, no offenses detected
04:27:13 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png
 0/0 files |=================== 100 ===================>| Time: 00:00:00

0 files inspected, no offenses detected
...
```

テストは無事通りました。ここでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: タイプ1の場合'
```

追加仕様の取っ掛かりができました。既存のテストを流用したいので先程作成したテストを削除して以下のように新しいグループ内に既存テストコードを移動しましょう。

``` ruby
...

class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列Fizzを返す
          assert_equal 'Fizz', @fizzbuzz.generate(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列Buzzを返す
          assert_equal 'Buzz', @fizzbuzz.generate(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.generate(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1)
        end
      end

      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          @result = FizzBuzz.generate_list
        end

        def test_配列の初めは文字列の1を返す
          assert_equal '1', @result.first
        end

        def test_配列の最後は文字列のBuzzを返す
          assert_equal 'Buzz', @result.last
        end

        def test_配列の2番目は文字列のFizzを返す
          assert_equal 'Fizz', @result[2]
        end

        def test_配列の4番目は文字列のBuzzを返す
          assert_equal 'Buzz', @result[4]
        end

        def test_配列の14番目は文字列のFizzBuzzを返す
          assert_equal 'FizzBuzz', @result[14]
        end
      end
    end
  end
...
```

テストコードが壊れていないことを確認したらコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: メソッドのインライン化'
```

TODOリスト

  - タイプ1の場合

      - 数を文字列にして返す

          - ~~1を渡したら文字列"1"を返す~~

      - 3 の倍数のときは数の代わりに｢Fizz｣と返す\_

          - ~~3を渡したら文字列"Fizz"を返す~~

      - 5 の倍数のときは｢Buzz｣と返す\_

          - ~~5を渡したら文字列"Buzz"を返す~~

      - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す\_

          - ~~15を渡したら文字列"FizzBuzz"を返す~~

  - タイプ2の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

      - 3 の倍数のときは数を文字列にして返す

          - 3を渡したら文字列"3"を返す

      - 5 の倍数のときは数を文字列にして返す

          - 5を渡したら文字列"5"を返す

      - 3 と 5 両方の倍数の場合には数を文字列にして返す

          - 15を渡したら文字列"15"を返す

  - タイプ3の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

      - 3 の倍数のときは数を文字列にして返す

          - 3を渡したら文字列"3"を返す

      - 5 の倍数のときは数を文字列にして返す

          - 5を渡したら文字列"5"を返す

      - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

          - 15を渡したら文字列"FizzBuzz"を返す

#### タイプ2の場合

TODOリスト

  - ~~タイプ1の場合~~

  - タイプ2の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

      - 3 の倍数のときは数を文字列にして返す

          - 3を渡したら文字列"3"を返す

      - 5 の倍数のときは数を文字列にして返す

          - 5を渡したら文字列"5"を返す

      - 3 と 5 両方の倍数の場合には数を文字列にして返す

          - 15を渡したら文字列"15"を返す

  - タイプ3の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

      - 3 の倍数のときは数を文字列にして返す

          - 3を渡したら文字列"3"を返す

      - 5 の倍数のときは数を文字列にして返す

          - 5を渡したら文字列"5"を返す

      - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

          - 15を渡したら文字列"FizzBuzz"を返す

続いて、タイプ2の場合に取り掛かりましょう。

``` ruby
...
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1, 2)
        end
      end
    end
...
```

``` bash
...
FAIL["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x00005555ec747100 @name="数を文字列にして返す::タイプ2の場合::その他の場合">, 0.002283181995153427]
 test_1を渡したら文字列1を返す#数を文字列にして返す::タイプ2の場合::その他の場合 (0.00s)
        Expected: "1"
          Actual: nil
        /workspace/tdd_rb/test/fizz_buzz_test.rb:75:in `test_1を渡したら文字列1を返す'

  24/24: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00437s
24 tests, 26 assertions, 1 failures, 0 errors, 0 skips
...
```

まだ **引数** に2を渡した場合は何もしないので **case式** に2を渡した場合の処理を追加します。

``` ruby
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    case type
    when 1
      is_fizz = number.modulo(3).zero?
      is_buzz = number.modulo(5).zero?

      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    end
  end
...
```

``` bash
...
Started with run options --seed 19625


Progress: |=============================================================================|

Finished in 0.00894s
24 tests, 26 assertions, 0 failures, 0 errors, 0 skips
...
```

テストが通ったのでテストケースを追加します。ここはタイプ1の場合をコピーして編集すれば良いでしょう。

``` ruby
...
   end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.generate(3, 2)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.generate(5, 2)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列15を返す
          assert_equal '15', @fizzbuzz.generate(15, 2)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1, 2)
        end
      end
    end
  end
...
```

``` bash
...
Coverage report generated for MiniTest to /workspace/tdd_rb/coverage. 4 / 13 LOC (30.77%) covered.
Started with run options --guard --seed 898

  27/27: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00900s
27 tests, 29 assertions, 0 failures, 0 errors, 0 skips

06:27:40 - INFO - Inspecting Ruby code style of all files
test/fizz_buzz_test.rb:11:3: C: Metrics/BlockLength: Block has too many lines. [70/62]
  describe '数を文字列にして返す' do ...
  ^^^^^^^^^^^^^^^^^^^^^^^^
 7/7 files |====================================== 100 =======================================>| Time: 00:00:00

7 files inspected, 1 offense detected
...
```

テストは通りましたが何やら警告が表示されるようになりました。　
[Metrics/BlockLength:Block has too many lines.](https://rubocop.readthedocs.io/en/latest/cops\_metrics/\#metricsblocklength) これは `数を文字列にして返す` テストケースのコードブロックが長いという警告のようですがテストコードはチェックの対象から外しておきたいので `.rubocop_todo.yml` に以下コードを追加してチェック対象から外しておきます。

``` yml
...
# Offense count: 2
# Configuration parameters: CountComments, ExcludedMethods.
# ExcludedMethods: refine
Metrics/BlockLength:
  Max: 62
  Exclude:
    - 'test/fizz_buzz_test.rb'
...
```

ちなみに `guard(main)>` にカーソルを合わせてエンターキーを押すと自動化タスクが実行されます。

``` bash
[1] guard(main)>
02:03:15 - INFO - Run all
/home/gitpod/.rvm/rubies/ruby-2.6.3/bin/ruby -w -I"lib" -I"/workspace/.rvm/gems/rake-13.0.1/lib" "/workspace/.rvm/gems/rake-13.0.1/lib/rake/rake_test_loader.rb" "./test/fizz_buzz_test.rb"
/home/gitpod/.rvm/rubies/ruby-2.6.3/bin/ruby -w -I"lib" -I"/workspace/.rvm/gems/rake-13.0.1/lib" "/workspace/.rvm/gems/rake-13.0.1/lib/rake/rake_test_loader.rb" "./test/fizz_buzz_test.rb"
Started with run options --seed 47335


Progress: |==============================================================================|

Finished in 0.00781s
27 tests, 29 assertions, 0 failures, 0 errors, 0 skips
Started with run options --seed 47825


Progress: |==============================================================================|

Finished in 0.00761s
27 tests, 29 assertions, 0 failures, 0 errors, 0 skips
02:03:17 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 13 / 13 LOC (100.0%) covered.
Started with run options --guard --seed 17744

  27/27: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00789s
27 tests, 29 assertions, 0 failures, 0 errors, 0 skips

02:03:17 - INFO - Inspecting Ruby code style of all files
 7/7 files |=========================== 100 ============================>| Time: 00:00:00

7 files inspected, no offenses detected
02:03:19 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/border.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/loading_background.png
 0/0 files |=========================== 100 ============================>| Time: 00:00:00

0 files inspected, no offenses detected
[1] guard(main)>
```

警告は消えたのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: タイプ2の場合'
```

TODOリスト

  - ~~タイプ1の場合~~

  - タイプ2の場合

      - 数を文字列にして返す

          - ~~1を渡したら文字列"1"を返す~~

      - 3 の倍数のときは数を文字列にして返す

          - ~~3を渡したら文字列"3"を返す~~

      - 5 の倍数のときは数を文字列にして返す

          - ~~5を渡したら文字列"5"を返す~~

      - 3 と 5 両方の倍数の場合には数を文字列にして返す

          - ~~15を渡したら文字列"15"を返す~~

  - タイプ3の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

      - 3 の倍数のときは数を文字列にして返す

          - 3を渡したら文字列"3"を返す

      - 5 の倍数のときは数を文字列にして返す

          - 5を渡したら文字列"5"を返す

      - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

          - 15を渡したら文字列"FizzBuzz"を返す

#### タイプ3の場合

TODOリスト

  - ~~タイプ1の場合~~

  - ~~タイプ2の場合~~

  - タイプ3の場合

      - 数を文字列にして返す

          - 1を渡したら文字列"1"を返す

      - 3 の倍数のときは数を文字列にして返す

          - 3を渡したら文字列"3"を返す

      - 5 の倍数のときは数を文字列にして返す

          - 5を渡したら文字列"5"を返す

      - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

          - 15を渡したら文字列"FizzBuzz"を返す

続いて、タイプ3の場合ですがやることは同じなので今回は一気にテストを書いてみましょう。

``` ruby
...
    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.generate(3, 3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.generate(5, 3)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.generate(15, 3)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1, 3)
        end
      end
    end
  end
...
```

``` bash
...
 FAIL["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x00005642171ea5a0 @name="数を文字列にして返す::タイプ3の場合::その他の場合">, 0.003375133004738018]
 test_1を渡したら文字列1を返す#数を文字列にして返す::タイプ3の場合::その他の場合 (0.00s)
        Expected: "1"
          Actual: nil
        /workspace/tdd_rb/test/fizz_buzz_test.rb:123:in `test_1を渡したら文字列1を返す'

 FAIL["test_5を渡したら文字列5を返す", #<Minitest::Reporters::Suite:0x000056421723af78 @name="数を文字列にして返す::タイプ3の場合::五の倍数の場合">, 0.003832244998193346]
 test_5を渡したら文字列5を返す#数を文字列にして返す::タイプ3の場合::五の倍数の場合 (0.00s)
        Expected: "5"
          Actual: nil
        /workspace/tdd_rb/test/fizz_buzz_test.rb:111:in `test_5を渡したら文字列5を返す'

 FAIL["test_3を渡したら文字列3を返す", #<Minitest::Reporters::Suite:0x0000564217297340 @name="数を文字列にして返す::タイプ3の場合::三の倍数の場合">, 0.0043466729985084385]
 test_3を渡したら文字列3を返す#数を文字列にして返す::タイプ3の場合::三の倍数の場合 (0.00s)
        Expected: "3"
          Actual: nil
        /workspace/tdd_rb/test/fizz_buzz_test.rb:105:in `test_3を渡したら文字列3を返す'

 FAIL["test_15を渡したら文字列FizzBuzzを返す", #<Minitest::Reporters::Suite:0x00005642174dec98 @name="数を文字列にして返す::タイプ3の場合::三と五の倍数の場合">, 0.006096020006225444]
 test_15を渡したら文字列FizzBuzzを返す#数を文字列にして返す::タイプ3の場合::三と五の倍数の場合 (0.01s)
        Expected: "FizzBuzz"
          Actual: nil
        /workspace/tdd_rb/test/fizz_buzz_test.rb:117:in `test_15を渡したら文字列FizzBuzzを返す'

  31/31: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00650s
31 tests, 33 assertions, 4 failures, 0 errors, 0 skips
...
```

**case式** に処理を追加します。

``` ruby
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    case type
    when 1
      is_fizz = number.modulo(3).zero?
      is_buzz = number.modulo(5).zero?

      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      is_fizz = number.modulo(3).zero?
      is_buzz = number.modulo(5).zero?

      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    end
  end
...
```

``` bash
...
Started with run options --seed 12137


Progress: |=============================================================================|

Finished in 0.01662s
31 tests, 33 assertions, 0 failures, 0 errors, 0 skips
05:06:44 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png lib/fizz_buzz.rb
lib/fizz_buzz.rb:6:3: C: Metrics/CyclomaticComplexity: Cyclomatic complexity for generate is too high. [10/8]
  def self.generate(number, type = 1) ...
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:6:3: C: Metrics/PerceivedComplexity: Perceived complexity for generate is too high. [8/7]
  def self.generate(number, type = 1) ...
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 1/1 file |=========================== 100 ============================>| Time: 00:00:00

1 file inspected, 2 offenses detected
...
```

テストは通りましたが新しい警告が表示されるようになりました。とりあえずコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: タイプ3の場合'
```

処理の追加により一部重複が発生しました。ここは、 **ステートメントのスライド** を適用して重複をなくしておきましょう。

> ステートメントのスライド
>
> 旧：重複した条件記述の断片の統合
>
> —  リファクタリング(第2版)

> 重複した条件記述の断片の統合
>
> 条件式のすべて分岐に同じコードの断片がある。
>
> それを式の外側に移動する。
>
> —  新装版 リファクタリング

``` ruby
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    case type
    when 1
      is_fizz = number.modulo(3).zero?
      is_buzz = number.modulo(5).zero?

      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      is_fizz = number.modulo(3).zero?
      is_buzz = number.modulo(5).zero?

      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    end
  end
...
```

``` ruby
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case type
    when 1
      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    end
  end
...
```

警告は消えていませんがプログラムは壊れていないことが確認できたのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: ステートメントのスライド'
```

TODOリスト

  - ~~タイプ1の場合~~

  - ~~タイプ2の場合~~

  - タイプ3の場合

      - 数を文字列にして返す

          - ~~1を渡したら文字列"1"を返す~~

      - 3 の倍数のときは数を文字列にして返す

          - ~~3を渡したら文字列"3"を返す~~

      - 5 の倍数のときは数を文字列にして返す

          - ~~5を渡したら文字列"5"を返す~~

      - 3 と 5 両方の倍数の場合には｢FizzBuzz｣と返す

          - ~~15を渡したら文字列"FizzBuzz"を返す~~

#### それ以外のタイプの場合

追加仕様には対応しましたがタイプ1,2,3以外の値が **引数** として渡された場合はどうしましょうか？ 現状では `nil` を返しますがこのような例外ケースも考慮する必要があります。

TODOリスト

  - ~~タイプ1の場合~~

  - ~~タイプ2の場合~~

  - ~~タイプ3の場合~~

  - それ以外のタイプの場合

**例外処理** を追加します。まず、例外のテストですが以下の様に書きます。

> 例外とは記述したプログラムが想定していない値を受け取ったり、何らかの障害が発生した場合に処理を中断して、例外オブジェクトを生成して呼び出し元のメソッドに処理を戻す機構です。
>
> —  かんたんRuby

``` ruby
    describe 'タイプ3の場合' do
...
    end

    describe 'それ以外のタイプの場合' do
      def setup
        @fizzbuzz = FizzBuzz
      end

      def test_例外を返す
        e = assert_raises RuntimeError do
          @fizzbuzz.generate(1, 4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
...
```

``` bash
...
 FAIL["test_例外を返す", #<Minitest::Reporters::Suite:0x0000558a26888e60 @name="数を文字列にして返す::それ以外のタイプの場合">, 0.003033002998563461]
 test_例外を返す#数を文字列にして返す::それ以外のタイプの場合 (0.00s)
        RuntimeError expected but nothing was raised.
        /workspace/tdd_rb/test/fizz_buzz_test.rb:134:in `test_例外を返す'

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00609s
32 tests, 34 assertions, 1 failures, 0 errors, 0 skips
...
```

**case式** に該当しないタイプが指定された場合は **例外を発生させる** ようにします。

> 例外を明示的に発生させるには「raise」を使います。raiseには発生させたい例外クラスを指定するのですが、何も指定しない場合はRuntimeErrorオブジェクトが生成されます。
>
> —  かんたんRuby

``` ruby
...
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case type
    when 1
      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    else
      raise '該当するタイプは存在しません'
    end
  end
...
```

``` bash
...
07:04:53 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 16 / 16 LOC (100.0%) covered.
Started with run options --guard --seed 32508

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00600s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
...
```

テストが通ったのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'test: それ以外のタイプの場合'
```

TODOリスト

  - *タイプ1の場合*

  - *タイプ2の場合*

  - *タイプ3の場合*

  - *それ以外のタイプの場合*

**TODOリスト**
をすべて完了しました。追加仕様を満たすプログラムは出来ましたがまだ改善の余地がありそうですね。以降ではオブジェクト指向アプローチによるコードのリファクタリングを解説していきたいと思います。

### オブジェクト指向

#### 手続き型プログラム

**オブジェクト指向** の解説の前に以下のコードを御覧ください。いわゆる **手続き型** で書かれたコードですが、これも追加仕様を満たしています。

``` ruby
MAX_NUMBER = 100
type = 1
list = []

MAX_NUMBER.times do |i|
  r = ''
  i += 1
  case type
  when 1
    if i % 3 == 0 && i % 5 == 0
      r = 'FizzBuzz'
    elsif i % 3 == 0
      r = 'Fizz'
    elsif i % 5 == 0
      r = 'Buzz'
    else
      r = i.to_s
    end
  when 2
    r = i.to_s
  when 3
    if i % 3 == 0 && i % 5 == 0
      r = 'FizzBuzz'
    else
      r = i.to_s
    end
  else
    r = '該当するタイプは存在しません'
  end

  list.push(r)
end

puts list
```

処理の流れをフローチャートにしたものです、実態はコードに記述されている内容を記号に置き換えて人間が読めるようにしたものです。

    start

    repeat

      if (タイプ1) then (yes)
        if (カウンタが3と5で割り切れる) then (yes)
          :変数にFizzBuzzをセットする;
        else if (カウンタが3で割り切れる) then (yes)
          :変数にFizzをセットする;
        else if (カウンタが5で割り切れる) then (yes)
          :変数にBuzzをセットする;
        else
          :変数にカウンタをセットする;
        endif
      else if (タイプ2) then (yes)
        :変数にカウンタをセットする;
      else if (タイプ3) then (yes)
        if (カウンタが3と5で割り切れる) then (yes)
          :変数にFizzBuzzをセットする;
        else
          :変数にカウンタを文字列にしてセットする;
        endif
      else (no)
       :変数に該当するタイプは存在しませんをセットする;
      endif

      :カウンタを1増やす;
    repeat while (カウンタが100になるまで)

    stop

#### オブジェクト指向プログラム

続いて、これまでに作ってきたコードがこちらになります。上記の **手続き型コード** との大きな違いとして `class` というキーワードでくくられている部分があります。

> クラスとは、大まかに説明すると何らかの値と処理（メソッド）をひとかたまりにしたものです。
>
> —  かんたんRuby

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case type
    when 1
      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    else
      raise '該当するタイプは存在しません'
    end
  end

  def self.generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

[UML](https://ja.wikipedia.org/wiki/%E7%B5%B1%E4%B8%80%E3%83%A2%E3%83%87%E3%83%AA%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E) を使って上記のコードの構造をクラス図として表現しました。

    class FizzBuzz {
        MAX_NUMBER = 100
        {static} generate(number)
        {static} generate_list()
    }

更にシーケンス図を使って上記のコードの振る舞いを表現しました。

    participant "Main" as A
    participant "FizzBuzz" as B

    A -> B : generate_list()
    activate B

    loop 100 times
      B -> B : generate()
    end loop

    A <<-- B : list
    deactivate B

**手続き型コード** のフローチャートと比べてどう思われましたか？具体的な記述が少なくデータや処理の概要だけを表現しているけどFizzBuzzのルールを知っている人であれば何をやろうとしているかのイメージはつかみやすいのではないでしょうか？だから何？と思われるかもしれませんが現時点では **オブジェクト指向** において **抽象化** がキーワードだという程度の認識で十分です。

オブジェクト指向の理解を深める取り掛かりにはこちらの記事を参照してください。

  - [オブジェクト指向のいろは](https://qiita.com/nrslib/items/73bf176147192c402049)

オブジェクト指向の詳細は控えるとして、ここでは **カプセル化** **ポリモフィズム** **継承** というオブジェクト指向プログラムで原則とされる概念をリファクタリングを通して体験してもらい、オブジェクト指向プログラムの感覚を掴んでもらうことを目的に解説を進めていきたいと思います。

### カプセル化

#### フィールドのカプセル化

    class FizzBuzz {
        MAX_NUMBER = 100
        {static} generate(number)
        {static} generate_list()
    }

まず、データとロジックを１つのクラスにまとめていくためのリファクタリングを実施していくとします。`FizzBuzz` クラスにFizzBuzz配列を保持できるようして以下のように取得できるようにしたいと思います。

``` ruby
...
          fizzbuzz.generate_list
          @result = fizzbuzz.list
...
```

まず、 **インスタンス変数** 追加します。次に `self` キーワードを外して **クラスメソッド** から **インスタンスメソッド** に変更します。

> クラスメソッドはいくつか定義方法がありますが、どの方法を使ってもクラスメソッドとして定義されれば「クラス名.メソッド名」という形で呼び出せます。
>
> —  かんたんRuby

> インスタンスメソッドはコンストラクタと同じようにクラス内でdefキーワードを使ってメソッドを定義するだけで作成できます。
>
> —  かんたんRuby

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

  def self.generate(number, type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case type
    when 1
      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    else
      raise '該当するタイプは存在しません'
    end
  end

  def self.generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

  def list
    @list
  end

  def generate(number, type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case type
    when 1
      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    else
      raise '該当するタイプは存在しません'
    end
  end

  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

``` bash
...

ERROR["test_15を渡したら文字列FizzBuzzを返す", #<Minitest::Reporters::Suite:0x00005613555ed120 @name="数を文字列にして返す::タイプ3の場合::三と五の倍数の場合">, 0.0041351839900016785]
 test_15を渡したら文字列FizzBuzzを返す#数を文字列にして返す::タイプ3の場合::三と五の倍数の場合 (0.00s)
Minitest::UnexpectedError:         NoMethodError: undefined method `generate' for FizzBuzz:Class
            /workspace/tdd_rb/test/fizz_buzz_test.rb:117:in `test_15を渡したら文字列FizzBuzzを返す'
...
```

FizzBuzz配列を **インスタンス変数** `@list` に **代入** して **インスタンス変数** 経由で取得できるように変更しました。変更にあたり **クラスメソッド** `FizzBuzz.generate` と `FizzBuzz.generate_list` を **インスタンスメソッド** に変更しています。それに伴ってテストが失敗して ``NoMethodError: undefined method `generate'`` と表示されるようになってしまいました。**インスタンスメソッド** が使えるようにするため　`new` メソッドを使ってFizzBuzzクラスの **インスタンス** を作りFizzBuzz配列を **インスタンス変数** 経由で取得するようにテストコードを変更します。

> クラスとして定義された情報を元に具体的な値を伴ったオブジェクトを作成することをインスタンス化と呼び、生成されたオブジェクトのことをインスタンスと呼びます。
>
> —  かんたんRuby

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new
      end
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end
...
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new
      end
...
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new
      end
...
    end

    describe 'それ以外のタイプの場合' do
      def setup
        @fizzbuzz = FizzBuzz.new
      end
...
    end
  end
...
```

``` bash
...
07:17:36 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 5 / 17 LOC (29.41%) covered.
Started with run options --guard --seed 7701

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00616s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
...
```

テストが直りました。**クラスメソッド** **インスタンスメソッド** **インスタンス変数** **インスタンス** などいろんな単語が出てきて戸惑ってしまったかもしれませんが、ピンとこないうちは **クラス** に値や状態を保持させるためには **インスタンス化** する必要があってそのためには `new` メソッドを使わないといけないのね程度の理解で十分です。大概のことは手を動かしているうちにピンと来るようになります。

**インスタンス変数** に直接アクセスしているのでここは **アクセッサメソッド** を使って **フィールドのカプセル化** を適用しておきます。

> オブジェクト指向ではクラス内の値をカプセル化することが重要ですが、時には内部で保持しているインスタンス変数を参照や更新できる方が良い場合もあります。複雑な処理ではなく、単にインスタンス変数にアクセスするためのメソッドのことを、アクセッサメソッドと呼びます。
>
> —  かんたんRuby

> フィールドのカプセル化
>
> 公開フィールドがある。
>
> それを非公開にして、そのアクセサを用意する。
>
> —  新装版 リファクタリング

自動実行の結果、以下のように書き換えられている部分を変更します。

``` ruby
class FizzBuz、
  MAX_NUMBER = 100
　attr_reader :list
...
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_accessor :list
...
```

テストが動作して既存のコードが壊れていないことが確認できたのでここでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: フィールドのカプセル化'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        generate(number)
        generate_list()
    }

引き続き、FizzBuzz配列は保持できるようになりましたがタイプごとに出力される配列のパターンは違います。FizzBuzzクラスにタイプを持たる必要があります。ここでは **コンストラクタ** を使って **インスタンス化** する際に **インスタンス変数** に **代入** するようにします。Rubyでは **initialize** というメソッドを使って初期化処理を実行します。

> クラスをインスタンス化した時に初期化処理を行うシチュエーションはよくあります。このような初期化処理を行うメソッドをコンストラクタと呼び、Rubyではinitializeという特別なメソッドを用意することで実現できます。
>
> —  かんたんRuby

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_accessor :list

  def initialize(type)
    @type = type
  end
...
```

``` bash
...
ERROR["test_3を渡したら文字列3を返す", #<Minitest::Reporters::Suite:0x00005564e21e85b0 @name="数を文字列にして返す::タイプ3の場合::三の倍数の場合">, 0.004276092993677594]
 test_3を渡したら文字列3を返す#数を文字列にして返す::タイプ3の場合::三の倍数の場合 (0.00s)
Minitest::UnexpectedError:         ArgumentError: wrong number of arguments (given 0, expected 1)
            /workspace/tdd_rb/lib/fizz_buzz.rb:7:in `initialize'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:101:in `new'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:101:in `setup'
...
```

テストが失敗して引数が違うというエラーが表示される用になりました。`new` メソッドの **引数** にタイプを渡すようにテストを変更します。

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(1)
      end
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(1)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end
...
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(2)
      end
...
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(3)
      end
...
    end

    describe 'それ以外のタイプの場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(4)
      end
...
    end
  end
...
```

``` bash
...
07:28:38 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 6 / 19 LOC (31.58%) covered.
Started with run options --guard --seed 46661

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00793s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
...
```

テストは直りましたがまだ **インスタンス変数** のタイプが使われていないので使うようにプロダクトコードを変更します。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_accessor :list

  def initialize(type)
    @type = type
  end

  def generate(number, _type = 1)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case @type
...
```

`FizzBuzz.gnerate` メソッドの **引数** から `type` を削除します。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_accessor :list

  def initialize(type)
    @type = type
  end

  def generate(number)
...
```

``` bash
...
ERROR["test_15を渡したら文字列FizzBuzzを返す", #<Minitest::Reporters::Suite:0x0000564e16c14200 @name="数を文字列にして返す::タイプ3の場合::三と五の倍数の場合">, 0.01706391001062002]
 test_15を渡したら文字列FizzBuzzを返す#数を文字列にして返す::タイプ3の場合::三と五の倍数の場合 (0.02s)
Minitest::UnexpectedError:         ArgumentError: wrong number of arguments (given 2, expected 1)
            /workspace/tdd_rb/lib/fizz_buzz.rb:11:in `generate'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:118:in `test_15を渡したら文字列FizzBuzzを返す'
...
```

続いて、`FizzBuzz#generate` メソッドから不要になった **引数** `type`
を削除したところテストが壊れたのでテストコードを修正します。

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
  ...
    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(2)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.generate(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.generate(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列15を返す
          assert_equal '15', @fizzbuzz.generate(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1)
        end
      end
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(3)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.generate(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.generate(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.generate(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1)
        end
      end
    end

    describe 'それ以外のタイプの場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(4)
      end

      def test_例外を返す
        e = assert_raises RuntimeError do
          @fizzbuzz.generate(1)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
...
```

``` bash
...
07:34:57 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 15 / 19 LOC (78.95%) covered.
Started with run options --guard --seed 59116

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00700s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
...
```

**インスタンス変数** の `@type` も **アクセッサメソッド** を使って **フィールドのカプセル化** を適用しておきます。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_accessor :list

  def initialize(type)
    @type = type
  end
...
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_accessor :list
  attr_accessor :type

  def initialize(type)
    @type = type
  end
...
```

``` bash
...
Started with run options --guard --seed 56315

  32/32: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01069s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
...
```

コミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: フィールドのカプセル化'
```

#### setterの削除

FizzBuzz配列を取得する **アクセッサメソッド** は現在このように定義されています。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_accessor :list
  attr_accessor :type
...
```

以下のようにテストコードを変更したらどうなるでしょうか？

``` ruby
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(1)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end
...
```

``` ruby
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(1)
          fizzbuzz.generate_list
          fizzbuzz.list = []
          @result = fizzbuzz.list
        end
...
```

``` bash
...
 FAIL["test_配列の2番目は文字列のFizzを返す", #<Minitest::Reporters::Suite:0x0000563c29a8a8c0 @name="数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す">, 0.005137628992088139]
 test_配列の2番目は文字列のFizzを返す#数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す (0.01s)
        Expected: "Fizz"
          Actual: nil
        /workspace/tdd_rb/test/fizz_buzz_test.rb:58:in `test_配列の2番目は文字列のFizzを返す'
...
```

FizzBuzz配列が初期化されてしまいました。**アクセッサメソッド** に参照のための **getter** と 更新するための **setter** が許可されているため　**カプセル化** が破られてしまいました。ここは **setterの削除** を適用して外部からの更新を出来ないようにしておきましょう。

> getterを定義するには、「attr\_reader」を使います。このメソッドにインスタンス変数の「@」を除いた名称をシンボル表現にしたものを列挙します。複数ある場合はカンマで区切って複数の値を指定することができます。
>
> —  かんたんRuby
>

> setterを定義するには、「attr\_writer」を使います。このメソッドもattr\_readerと同じくインスタンス変数名の「@」を除いた名称をシンボル表現にしたものを列挙します。複数ある場合はカンマで区切って複数の値を指定することができます。
>
> —  かんたんRuby
>

> getter/setterの両方を定義する場合、そのインスタンスは属しているクラス外から自由に参照や更新ができてしまいます。これはカプセル化の観点には反した挙動なので、できる限りattr\_readerだけで済ませられないか検討しましょう。
>
> —  かんたんRuby
>

> setterの削除
>
> setterが用意されているということは、フィールドが変更される可能性があることを意味します。オブジェクトを生成した後でフィールドを変更したくないなら、setterは用意しません（加えて、フィールドを変更不可にします）。そうすることで、フィールドはコンストラクタでのみで設定され、変更させないという意図が明確になって、フィールドが変更される可能性を、たいていは排除できます。
>
> —  リファクタリング(第2版)

Rubyでは以下のようにして **インスタンス変数** を読み取り専用にします。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_accessor :type
...
```

``` bash
ERROR["test_配列の2番目は文字列のFizzを返す", #<Minitest::Reporters::Suite:0x000055b32efd75f0 @name="数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す">, 0.008614362974185497]
 test_配列の2番目は文字列のFizzを返す#数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す (0.01s)
Minitest::UnexpectedError:         NoMethodError: undefined method `list=' for #<FizzBuzz:0x000055b32ee8c678>
        Did you mean?  list
            /workspace/tdd_rb/test/fizz_buzz_test.rb:45:in `setup'
```

更新メソッドは存在しませんというエラーに変わったことが確認できたのでテストを元にもどします。

同様に **インスタンス変数** の `@type` も読み取り専用にします。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type
...
```

``` bash
...
04:32:06 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 22 / 22 LOC (100.0%) covered.
Started with run options --guard --seed 20902

  32/32: [===========================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00920s
...
```

テストが壊れていないことを確認したらコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: setterの削除'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }

### ポリモーフィズム

#### ポリモーフィズムによる条件記述の置き換え 1

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }

リファクタリングによりデータとロジックを１つのクラスにまとめて **カプセル化** を進めることが出来ました。しかし、以下の警告メッセージが表示されたままです。**ポリモーフィズム** を使ったロジックのリファクタリングを実施していきましょう。

``` bash
...
07:53:29 - INFO - Inspecting Ruby code style: test/fizz_buzz_test.rb lib/fizz_buzz.rb
lib/fizz_buzz.rb:11:3: C: Metrics/CyclomaticComplexity: Cyclomatic complexity for generate is too high. [10/8]
  def generate(number) ...
  ^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:11:3: C: Metrics/PerceivedComplexity: Perceived complexity for generate is too high. [8/7]
  def generate(number) ...
  ^^^^^^^^^^^^^^^^^^^^
 2/2 files |====================================== 100 =======================================>| Time: 00:00:00

2 files inspected, 2 offenses detected
...
```

[循環的複雑度](https://ja.wikipedia.org/wiki/%E5%BE%AA%E7%92%B0%E7%9A%84%E8%A4%87%E9%9B%91%E5%BA%A6) が高く可読性が低く複雑なコードと警告されているようです。対象となっている　`FizzBuzz#generate` を確認してみましょう。

  - [Metrics/CyclomaticComplexity](https://rubocop.readthedocs.io/en/latest/cops_metrics/#metricscyclomaticcomplexity)

  - [Metrics/PerceivedComplexity](https://rubocop.readthedocs.io/en/latest/cops_metrics/#metricsperceivedcomplexity)

<!-- end list -->

``` ruby
...
  def generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case @type
    when 1
      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    else
      raise '該当するタイプは存在しません'
    end
  end
...
```

コードの不吉な臭いである **スイッチ文** に該当するコードのようなのでここはリファクタリングカタログに従って **ポリモーフィズムによる条件記述の置き換え** を適用していきましょう。比較的大きなリファクタリングなのでいくつかのステップに分けて進めていきます。

> スイッチ文
>
> オブジェクト指向プログラミングのメリットして、スイッチ文が従来にくらべて少なくなるということがあります。スイッチ文は重複したコードを生み出す問題児です。コードのあちらこちらに同じようなスイッチ文が見られることがあります。これでは新たな分岐を追加したときに、すべてのスイッチ文を探して似たような変更をしていかなければなりません。オブジェクト指向ではポリモーフィズムを使い、この問題をエレガントに解決できます。
>
> —  新装版 リファクタリング
>

> 重複したスイッチ文
>
> 最近はポリモーフィズムも一般的となり、15年前に比べるとswitch文が単純に赤信号というわけでもなくなりました。また、多くのプログラミング言語が、基本データ型以外をサポートする、より洗練されたswitch文を提供してきています。そこで、今後問題とするのは、重複したswitch文のみとします。switch/case文や、ネストしたif/else文の形で、コードのさまざまな箇所に同じ条件分岐ロジックが書かれていれば、それは「不吉な臭い」です。重複した条件分岐が問題なのは、新たな分岐を追加したら、すべての重複した条件分岐を探して更新指定かなけれけならないからです。ポリモーフィズムは、そうした単調な繰り返しに誘うダークフォースに対抗するための、洗練された武器です。コードベースをよりモダンにしていきましょう。
>
> —  リファクタリング(第2版)

> ポリモーフィズムによる条件記述の置き換え
>
> オブジェクトのタイプによって異なる振る舞いを選択する条件記述がある。
>
> 条件記述の各アクション部をサブクラスでオーバーライドするメソッドに移動する。元のメソッドはabstractにする。
>
> —  新装版 リファクタリング

``` ruby
class FizzBuzz
...
end

class FizzBuzzType01; end
class FizzBuzzType02; end
class FizzBuzzType03; end
```

まず、タイプごとのクラスを定義します。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = type
  end

  def self.create(type)
    case type
    when 1
      FizzBuzzType01.new
    when 2
      FizzBuzzType02.new
    when 3
      FizzBuzzType03.new
    else
      raise '該当するタイプは存在しません'
    end

...
```

次に、タイプごとのクラスを **インスタンス化** する **ファクトリメソッド** をFizzBuzzクラスに追加します。この時点では新しいクラスとメソッドの追加だけなのでテストは壊れていないはずです（警告は出ていますが・・・）。ここでコミットしておきますがリファクタリング作業としては [仕掛](https://ja.wikipedia.org/wiki/%E4%BB%95%E6%8E%9B%E5%93%81) なのでWIP(Work In Progress)をメッセージに追加してコミットします。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): ポリモーフィズムによる条件記述の置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    FizzBuzz -> FizzBuzzType01
    FizzBuzz -> FizzBuzzType02
    FizzBuzz -> FizzBuzzType03

#### ポリモーフィズムによる条件記述の置き換え 2

続いて、各タイプクラスに **インスタンスメソッド** を実装します。ここでは **case式** の各処理をコピー&ペーストしています。カット&ペーストするとプロダクトコードが壊れたままリファクタリングを進めることになるのでここは慎重に進めていきます。

``` ruby
class FizzBuzz
...
end

class FizzBuzzType01; end
class FizzBuzzType02; end
class FizzBuzzType03; end
```

``` ruby
...
class FizzBuzzType01
  def generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end
end
...
```

``` ruby
...
class FizzBuzzType02
  def generate(number)
    number.to_s
  end
end
...
```

``` ruby
...
class FizzBuzzType03
  def generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz

    number.to_s
  end
end
```

警告は出ますがテストは壊れていないのでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): ポリモーフィズムによる条件記述の置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create()
        generate(number)
        generate_list()
    }
    class FizzBuzzType01 {
        generate()
    }
    class FizzBuzzType02 {
        generate()
    }
    class FizzBuzzType03 {
        generate()
    }
    FizzBuzz -> FizzBuzzType01
    FizzBuzz -> FizzBuzzType02
    FizzBuzz -> FizzBuzzType03

#### ポリモーフィズムによる条件記述の置き換え 3

これで準備は整いましたのでテストコードの `setup` メソッドを **ファクトリメソッド** の呼び出しに変更します。以下の部分は変更してはいけません。理由はわかりますか？

``` ruby
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(1)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end
...
```

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz.create(1)
      end
...
    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.create(2)
      end
...
    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.create(3)
      end
...
    describe 'それ以外のタイプの場合' do
      def setup
        @fizzbuzz = FizzBuzz.create(4)
      end

      def test_例外を返す
        e = assert_raises RuntimeError do
          @fizzbuzz.generate(1)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
```

``` bash
...
08:14:14 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 26 / 42 LOC (61.9%) covered.
Started with run options --guard --seed 37585

ERROR["test_例外を返す", #<Minitest::Reporters::Suite:0x000056317940fa28 @name="数を文字列にして返す::それ以外のタイプの場合">, 0.0037079370085848495]
 test_例外を返す#数を文字列にして返す::それ以外のタイプの場合 (0.00s)
Minitest::UnexpectedError:         RuntimeError: 該当するタイプは存在しません
            /workspace/tdd_rb/lib/fizz_buzz.rb:20:in `create'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:132:in `setup'

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00685s
32 tests, 33 assertions, 0 failures, 1 errors, 0 skips
...
```

失敗するテストがありますね、該当するコードを確認したところ例外が発生するタイミングが変わってしまったので以下のように変更します。

``` ruby
...
    describe 'それ以外のタイプの場合' do
      def setup
        @fizzbuzz = FizzBuzz.create(4)
      end

      def test_例外を返す
        e = assert_raises RuntimeError do
          @fizzbuzz.generate(1)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
...
```

``` ruby
...
    describe 'それ以外のタイプの場合' do
      def test_例外を返す
        e = assert_raises RuntimeError do
          FizzBuzz.create(4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
...
```

``` bash
...
08:18:08 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 37 / 42 LOC (88.1%) covered.
Started with run options --guard --seed 40171

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00559s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
...
```

コミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): ポリモーフィズムによる条件記述の置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzz -> FizzBuzzType01
    FizzBuzz -> FizzBuzzType02
    FizzBuzz -> FizzBuzzType03

#### ポリモーフィズムによる条件記述の置き換え 4

タイプごとにFizzBuzzを生成するクラスを用意したのでFizzBuzzクラスから呼び出せるようにしましょう。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = type
  end
...
  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

まず、**コンストラクタ** から **クラスメソッド** の **ファクトリメソッド** を呼び出して **インスタンス変数** の `type` にタイプクラスの **参照** を **代入** します。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = FizzBuzz.create(type)
  end
...
  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

``` bash
ERROR["test_配列の14番目は文字列のFizzBuzzを返す", #<Minitest::Reporters::Suite:0x000055670a343110 @name="数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す">, 0.006740843993611634]
 test_配列の14番目は文字列のFizzBuzzを返す#数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す (0.01s)
Minitest::UnexpectedError:         RuntimeError: 該当するタイプは存在しません
            /workspace/tdd_rb/lib/fizz_buzz.rb:42:in `generate'
            /workspace/tdd_rb/lib/fizz_buzz.rb:48:in `block in generate_list'
            /workspace/tdd_rb/lib/fizz_buzz.rb:48:in `each'
            /workspace/tdd_rb/lib/fizz_buzz.rb:48:in `map'
            /workspace/tdd_rb/lib/fizz_buzz.rb:48:in `generate_list'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:44:in `setup'
```

テストが失敗して沢山エラーが表示するようになりましたが落ち着いてください。次に **インスタンスメソッド** `FizzBuzz#generate_list` 内の `FizzBuzz#generate` メソッド呼び出しを **インスタンス変数** `type` が参照するタイプクラスのメソッド `FizzBuzzTypeXX#generate` を呼び出すように変更します。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = FizzBuzz.create(type)
  end
...
  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| @type.generate(n) }
  end
end
```

``` bash
Started with run options --seed 13878


Progress: |=====================================================================================================|

Finished in 0.00960s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
05:54:49 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
lib/fizz_buzz.rb:24:3: C: Metrics/CyclomaticComplexity: Cyclomatic complexity for generate is too high. [10/8]
  def generate(number) ...
  ^^^^^^^^^^^^^^^^^^^^
lib/fizz_buzz.rb:24:3: C: Metrics/PerceivedComplexity: Perceived complexity for generate is too high. [8/7]
  def generate(number) ...
  ^^^^^^^^^^^^^^^^^^^^
 1/1 file |======================================= 100 ========================================>| Time: 00:00:00

1 file inspected, 2 offenses detected
```

再びテストが通るようになりました。始めのうちはコードを少し変更しただけでなんで動くようになったの？と思うかもしれませんがこれが **ポリモーフィズム** の威力です。この概念を感覚としてつかんで使いこなせるようになることがオブジェクト指向プログラミングの第一歩です。感覚は意識して手を動かしていればそのうちつかめます（多分）。

**ポリモーフィズムによる条件記述の置き換え** が完了したのでWIPを外してコミットします。

``` bash
$ git add .
$ git commit -m 'refactor ポリモーフィズムによる条件記述の置き換え'
```

#### State/Strategyによるタイプコードの置き換え

仕上げは　**State/Strategyによるタイプコードの置き換え** を適用して、警告メッセージを消すとしましょう。

> State/Strategyによるタイプコードの置き換え
>
> クラスの振る舞いに影響するタイプコードがあるが、サブクラス化はできない。
>
> 状態オブジェクトでタイプコードを置き換える
>
> —  新装版 リファクタリング

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzz *- FizzBuzzType01
    FizzBuzz *- FizzBuzzType02
    FizzBuzz *- FizzBuzzType03

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = FizzBuzz.create(type)
  end

  def self.create(type)
    case type
    when 1
      FizzBuzzType01.new
    when 2
      FizzBuzzType02.new
    when 3
      FizzBuzzType03.new
    else
      raise '該当するタイプは存在しません'
    end
  end

  def generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    case @type
    when 1
      return 'FizzBuzz' if is_fizz && is_buzz
      return 'Fizz' if is_fizz
      return 'Buzz' if is_buzz

      number.to_s
    when 2
      number.to_s
    when 3
      return 'FizzBuzz' if is_fizz && is_buzz

      number.to_s
    else
      raise '該当するタイプは存在しません'
    end
  end

  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| @type.generate(n) }
  end
end
...
```

まず、`FizzBuzz#generate` のメソッド呼び出しを **インスタンス変数** `type` が参照するタイプクラスのメソッド `FizzBuzzTypeXX#generate` に **委譲** するように変更します。

``` ruby
...
  def generate(number)
    @type.generate(number)
  end

  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| @type.generate(n) }
  end
end
...
```

``` bash
...
Started with run options --seed 49543


Progress: |=====================================================================================================|

Finished in 0.00925s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
06:34:27 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
 1/1 file |======================================= 100 ========================================>| Time: 00:00:00

1 file inspected, no offenses detected
06:34:29 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png
 0/0 files |======================================= 100 =======================================>| Time: 00:00:00

0 files inspected, no offenses detecte
...
```

警告が消えました。しかもテストは壊れていないようです。実は `FizzBuzz#generate` メソッドはどこからも使われていないためテストも壊れることが無いのですがこれでは不要なメソッドになってしまうので **移譲の隠蔽** を実施して、ロジックを **カプセル化** します。

> 委譲の隠蔽
>
> オブジェクト指向について最初に教わる時、カプセル化とはフィールドを隠すことだと習うでしょう。しかし経験を積むにつれて、他にもカプセル化できるものがあることに気づきます。
>
> —  リファクタリング(第2版)

``` ruby
...
  def generate(number)
    @type.generate(number)
  end

  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
...
```

テストもFizzBuzzインスタンス経由で実行するように修正しておきます。これですべての呼び出しが `new` メソッド経由となりテストコードに一貫性を取り戻すことが出来ました。

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(1)
      end
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(1)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end
...
    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(2)
      end
...
    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(3)
      end
...
    describe 'それ以外のタイプの場合' do
      def test_例外を返す
        e = assert_raises RuntimeError do
          FizzBuzz.new(4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
...
```

``` bash
...
08:32:17 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 32 / 32 LOC (100.0%) covered.
Started with run options --guard --seed 63863

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00564s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips

08:32:18 - INFO - Inspecting Ruby code style of all files
 7/7 files |====================================== 100 =======================================>| Time: 00:00:00

7 files inspected, no offenses detected
...
```

**ポリモーフィズム** の感覚がつかめないうちは `FizzBuzz#generate` のコードが一行になったのに既存のテストも壊れず動いていることが不思議に思うかもしれません。しかしコードとしてはFizzBuzzクラスの `generate` メソッドは任意のタイプクラスの `generate` メソッドを呼び出しているだけで処理の詳細は理解しなくても振る舞いを理解できる **抽象化** された読みやすいコードになりました。静的コード解析も可読性が高くシンプルなコードとみなしてくれているようです。さて、警告メッセージもなくなり、テストも壊れていないのでコミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'refactor: State/Strategyによるタイプコードの置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzz *- FizzBuzzType01
    FizzBuzz *- FizzBuzzType02
    FizzBuzz *- FizzBuzzType03

### 継承

分割したタイプクラスのメソッドに重複する処理があるので **継承** を使ってリファクタリングしましょう。ここでは **スーパークラスの抽出**を適用します。

> スーパークラスの抽出
>
> 似通った特性を持つ２つのクラスがある。
>
> スーパークラスを作成して、共通の特性を移動する。
>
> —  新装版 リファクタリング

#### スーパークラスの抽出

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzz *- FizzBuzzType01
    FizzBuzz *- FizzBuzzType02
    FizzBuzz *- FizzBuzzType03

まずは、タイプクラスのスーパークラスとなる `FizzBuzzType` クラスを作成して各タイプクラスに継承させます。

> クラスベースのオブジェクト指向言語の多くはクラスの継承機能を有しています。クラスの継承とはあるクラスを元として、新しいクラスを定義することです。この時、継承元となるクラスを親クラスやスーパークラスと呼び、継承したクラスのことを子クラスやサブクラスと呼びます。
>
> —  かんたんRuby

Rubyの **クラスの継承** は以下のように書きます。

``` ruby
class FizzBuzz
...
end

class FizzBuzzType; end

class FizzBuzzType01
...
```

``` ruby
...
class FizzBuzzType; end

class FizzBuzzType01 < FizzBuzzType
...
end

class FizzBuzzType02 < FizzBuzzType
...
end

class FizzBuzzType03 < FizzBuzzType
...
end
```

スーパークラス `FizzBuzzType` を定義して各サブクラスに継承させます。

``` bash
08:42:24 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 33 / 33 LOC (100.0%) covered.
Started with run options --guard --seed 43548

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00860s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips

08:42:25 - INFO - Inspecting Ruby code style of all files
 7/7 files |====================================== 100 =======================================>| Time: 00:00:00

7 files inspected, no offenses detected
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz -> FizzBuzzType

次に `is_fizz` `is_buzz` 部分を共通メソッドとしてスーパークラスに定義して各タイプクラスで呼び出すように変更します。

``` ruby
...
class FizzBuzzType; end

class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz
    return 'Fizz' if is_fizz
    return 'Buzz' if is_buzz

    number.to_s
  end
end

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    number.to_s
  end
end

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    is_fizz = number.modulo(3).zero?
    is_buzz = number.modulo(5).zero?

    return 'FizzBuzz' if is_fizz && is_buzz

    number.to_s
  end
end
```

``` ruby
...
class FizzBuzzType
  def is_fizz(number)
    number.modulo(3).zero?
  end

  def is_buzz(number)
    number.modulo(5).zero?
  end
end

class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if is_fizz(number) && is_buzz(number)
    return 'Fizz' if is_fizz(number)
    return 'Buzz' if is_buzz(number)

    number.to_s
  end
end

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    number.to_s
  end
end

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if is_fizz(number) && is_buzz(number)

    number.to_s
  end
end
```

``` bash
08:50:16 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 33 / 33 LOC (100.0%) covered.
Started with run options --guard --seed 45685

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01073s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips

08:50:17 - INFO - Inspecting Ruby code style of all files
lib/fizz_buzz.rb:35:7: C: Naming/PredicateName: Rename is_fizz to fizz?.
  def is_fizz(number)
      ^^^^^^^
lib/fizz_buzz.rb:39:7: C: Naming/PredicateName: Rename is_buzz to buzz?.
  def is_buzz(number)
      ^^^^^^^
 7/7 files |====================================== 100 =======================================>| Time: 00:00:00

7 files inspected, 2 offenses detected
```

テストが壊れていないことが確認できたのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: スーパークラスの抽出'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
      is_fizz(number)
      is_buzz(number)
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz -> FizzBuzzType

#### メソッド名の変更

**スーパークラスの抽出** を実施したところまた警告メッセージが表示されるようになりました。

``` bash
08:50:19 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png lib/fizz_buzz.rb
lib/fizz_buzz.rb:35:7: C: Naming/PredicateName: Rename is_fizz to fizz?.
  def is_fizz(number)
      ^^^^^^^
lib/fizz_buzz.rb:39:7: C: Naming/PredicateName: Rename is_buzz to buzz?.
  def is_buzz(number)
      ^^^^^^^
 1/1 file |======================================= 100 =======================================>| Time: 00:00:00

1 file inspected, 2 offenses detected
```

[Naming/PredicateName](https://rubocop.readthedocs.io/en/latest/cops_naming/#namingpredicatename) Rubyのネーミングとしてはよろしくないようなので指示に従って **メソッド名の変更** を実施しましょう。

``` ruby
...
class FizzBuzzType
  def is_fizz(number)
    number.modulo(3).zero?
  end

  def is_buzz(number)
    number.modulo(5).zero?
  end
end

class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if is_fizz(number) && is_buzz(number)
    return 'Fizz' if is_fizz(number)
    return 'Buzz' if is_buzz(number)

    number.to_s
  end
end

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    number.to_s
  end
end

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if is_fizz(number) && is_buzz(number)

    number.to_s
  end
end
```

``` ruby
...
class FizzBuzzType
  def fizz?(number)
    number.modulo(3).zero?
  end

  def buzz?(number)
    number.modulo(5).zero?
  end
end

class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if fizz?(number) && buzz?(number)
    return 'Fizz' if fizz?(number)
    return 'Buzz' if buzz?(number)

    number.to_s
  end
end

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    number.to_s
  end
end

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if fizz?(number) && buzz?(number)

    number.to_s
  end
end
```

``` bash
Progress: |====================================================================================================|

Finished in 0.01144s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
08:53:35 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
 1/1 file |======================================= 100 =======================================>| Time: 00:00:00

1 file inspected, no offenses detected
```

作業としては難しくないのでミスタイプしないように（まあ、ミスタイプしてもテストが教えてくれますが・・・）変更してコミットしましょう。

``` bash
$ git add .
$ git commit -m 'refactor: メソッド名の変更'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        {static} create(type)
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz -> FizzBuzzType

#### メソッドの移動

`FizzBuzz` クラスの **ファクトリメソッド** ですが **特性の横恋慕** の臭いがするので **メソッドの移動** を実施します。

> 特性の横恋慕
>
> オブジェクト指向には、処理および処理に必要なデータを１つにまとめてしまうという重要な考え方があります。あるメソッドが、自分のクラスより他のクラスに興味を持つような場合には、古典的な誤りを犯しています。
>
> —  新装版 リファクタリング
>

> メソッドの移動
>
> あるクラスでメソッドが定義されているが、現在または将来において、そのクラスの特性よりも他のクラスの特性の方が、そのメソッドを使ったり、そのメソッドから使われたりすることが多い。
>
> 同様の本体を持つ新たなメソッドを、それを最も多用するクラスに作成する。元のメソッドは、単純な委譲とするか、またはまるごと取り除く。
>
> —  新装版 リファクタリング

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list

  def initialize(type)
    @type = FizzBuzz.create(type)
  end

  def self.create(type)
    case type
    when 1
      FizzBuzzType01.new
    when 2
      FizzBuzzType02.new
    when 3
      FizzBuzzType03.new
    else
      raise '該当するタイプは存在しません'
    end
  end

  def generate(number)
    @type.generate(number)
  end

  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| generate(n) }
  end
end

class FizzBuzzType
  def fizz?(number)
    number.modulo(3).zero?
  end

  def buzz?(number)
    number.modulo(5).zero?
  end
end
...
```

**クラスメソッド** `FizzBuzz.create` をカット&ペーストして `FizzBuzzType.create` に移動します。 `FizzBuzz` の **コンストラクタ** で呼び出している **クラスメソッド** を `FizzBuzzType.create` に変更します。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list

  def initialize(type)
    @type = FizzBuzzType.create(type)
  end

  def generate(number)
    @type.generate(number)
  end

  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| generate(n) }
  end
end

class FizzBuzzType
  def self.create(type)
    case type
    when 1
      FizzBuzzType01.new
    when 2
      FizzBuzzType02.new
    when 3
      FizzBuzzType03.new
    else
      raise '該当するタイプは存在しません'
    end
  end

  def fizz?(number)
    number.modulo(3).zero?
  end

  def buzz?(number)
    number.modulo(5).zero?
  end
end
...
```

``` bash
08:59:27 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 33 / 33 LOC (100.0%) covered.
Started with run options --guard --seed 19583

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00688s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips

08:59:28 - INFO - Inspecting Ruby code style of all files
 7/7 files |====================================== 100 =======================================>| Time: 00:00:00

7 files inspected, no offenses detected
```

テストが壊れていないことを確認したらコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: メソッドの移動'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz -> FizzBuzzType

### 値オブジェクト

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz -> FizzBuzzType

#### オブジェクトによるプリミティブの置き換え

`FizzBuzz` クラスを **インスタンス化** するには以下のように書きます。

``` ruby
fizz_buzz = FizzBuzz.new(1)
```

> クラスとして定義された情報を元に具体的な値を伴ったオブジェクトを作成することをインスタンス化と呼び、生成されたオブジェクトのことをインスタンスと呼びます。
>
> —  かんたんRuby

**コンストラクタ** の **引数** に渡される `1` は何を表しているのでしょうか？もちろんタイプですが初めてこのコードを見る人にはわからないでしょう。このような整数、浮動小数点、文字列などの基本データ（プリミティブ）型の使い方からは **基本データ型への執着**の臭いがします。 **オブジェクトによるプリミティブの置き換え** を実施してコードの意図を明確にしましょう。

> 基本データ型への執着
>
> オブジェクト指向のメリットとして、基本データ型とそれより大きなクラスとの境界を取り除くということがあります。プログラミング言語の組み込み（built-in）型と区別できないような小さなクラスを自分で定義することが容易です。
>
> —  新装版 リファクタリング

> 基本データ型への執着
>
> 興味深いことに、多くのプログラマは、対象としているドメインに役立つ、貨幣、座標、範囲などの基本的な型を導入するのを嫌がる傾向があります。
>
> —  リファクタリング(第2版)

> オブジェクトによるデータ値の置き換え
>
> 追加のデータや振る舞いが必要なデータ項目がある。
>
> そのデータ項目をオブジェクトに変える。
>
> —  新装版 リファクタリング

> オブジェクトによるプリミティブの置き換え
>
> 旧：オブジェクトによるデータ値の置き換え
>
> 旧：クラスによるタイプコードの置き換え
>
> —  リファクタリング(第2版)

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = FizzBuzzType.create(type)
  end
...
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = type
  end
...
```

**コンストラクタ** で引き渡されるタイプは整数ではなくタイプクラスの **インスタンス** に変更します。

``` bash
...

ERROR["test_1を渡したら文字列1を返す", #<Minitest::Reporters::Suite:0x00005654f32602c0 @name="数を文字列にして返す::タイプ3の場合::その他の場合">, 0.00241121300496161]
 test_1を渡したら文字列1を返す#数を文字列にして返す::タイプ3の場合::その他の場合 (0.00s)
Minitest::UnexpectedError:         NoMethodError: undefined method `generate' for 3:Integer
            /workspace/tdd_rb/lib/fizz_buzz.rb:12:in `generate'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:125:in `test_1を渡したら文字列1を返す'
...
```

テストが失敗しました。 **コンストラクタ** の引数を整数からタイプクラスの **インスタンス** に変更します。

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(1)
      end
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(1)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end
...
    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(2)
      end
...
    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(3)
      end
...
    describe 'それ以外のタイプの場合' do
      def test_例外を返す
        e = assert_raises RuntimeError do
          FizzBuzz.new(4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
```

ここで注意するのは `それ以外のタイプの場合` ですが例外を投げなくなります。静的に型付けされた言語なら型チェックエラーになるのですがRubyは動的に型付けされる言語のため `FizzBuzz#generate` メソッド実行までエラーになりません。そこで例外を投げる `FizzBuzzType#create` メソッドに変更しておきます。

``` ruby
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(FizzBuzzType01.new)
      end
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(FizzBuzzType01.new)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end
...
    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(FizzBuzzType02.new)
      end
...
    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(FizzBuzzType03.new)
      end
...
    describe 'それ以外のタイプの場合' do
      def test_例外を返す
        e = assert_raises RuntimeError do
          FizzBuzzType.create(4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
```

それ以外のタイプの場合は **ファクトリメソッド** 経由でないと **例外** を出さなくなるので注意してください。

``` bash
09:09:40 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 30 / 33 LOC (90.91%) covered.
Started with run options --guard --seed 17452

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00687s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
```

初めてコードを見る人でもテストコードを見ればコードの意図が読み取れるようになりましたのでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: オブジェクトによるプリミティブの置き換え'
```

   class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType

#### マジックナンバーの置き換え

まだプリミティグ型を使っている部分があります。ここは **マジックナンバーの置き換え** を実施して可読性を上げておきましょう。

``` ruby
...
class FizzBuzzType
  def self.create(type)
    case type
    when 1
      FizzBuzzType01.new
    when 2
      FizzBuzzType02.new
    when 3
      FizzBuzzType03.new
    else
      raise '該当するタイプは存在しません'
    end
 end
...
```

``` ruby
...
class FizzBuzzType
  TYPE_01 = 1
  TYPE_02 = 2
  TYPE_03 = 3

  def self.create(type)
    case type
    when FizzBuzzType::TYPE_01
      FizzBuzzType01.new
    when FizzBuzzType::TYPE_02
      FizzBuzzType02.new
    when FizzBuzzType::TYPE_03
      FizzBuzzType03.new
    else
      raise '該当するタイプは存在しません'
    end
  end
...
```

``` bash
09:18:51 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 33 / 36 LOC (91.67%) covered.
Started with run options --guard --seed 41124

  32/32: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00909s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips
```

テストは壊れていないのでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: マジックナンバーの置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
        generate(number)
    }
    class FizzBuzzType02 {
        generate(number)
    }
    class FizzBuzzType03 {
        generate(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType

#### オブジェクトによるプリミティブの置き換え

次に **基本データ型への執着** の臭いがする箇所として `FizzBuzz#generate` メソッドが返すFizzBuzzの値が文字型である点です。文字列の代わりに **値オブジェクト** `FizzBuzzValue` クラスを定義します。

> 値の種類ごとに専用の型を用意するとコードが安定し、コードの意図が明確になります。このように、値を扱うための専用クラスを作るやり方を値オブジェクト（ValueObject）と呼びます。
>
> —  現場で役立つシステム設計の原則

``` ruby
...
class FizzBuzzValue
  attr_reader :number, :value

  def initialize(number, value)
    @number = number
    @value = value
  end

  def to_s
    "#{@number}:#{@value}"
  end

  def ==(other)
    @number == other.number && @value == other.value
  end

  alias eql? ==
end
```

各タイプクラスの `generate` メソッドが文字列のプリミティブ型を返しているので **値オブジェクト** `FizzBuzzValue` を返すように変更します。

``` ruby
...
class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if fizz?(number) && buzz?(number)
    return 'Fizz' if fizz?(number)
    return 'Buzz' if buzz?(number)

    number.to_s
  end
end

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    number.to_s
  end
end

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    return 'FizzBuzz' if fizz?(number) && buzz?(number)

    number.to_s
  end
end
...
```

``` ruby
...
class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    return FizzBuzzValue.new(number, 'FizzBuzz') if fizz?(number) && buzz?(number)
    return FizzBuzzValue.new(number, 'Fizz') if fizz?(number)
    return FizzBuzzValue.new(number, 'Buzz') if buzz?(number)

    FizzBuzzValue.new(number, number.to_s)
  end
end

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, number.to_s)
  end
end

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    return FizzBuzzValue.new(number, 'FizzBuzz') if fizz?(number) && buzz?(number)

    FizzBuzzValue.new(number, number.to_s)
  end
end
...
```

``` bash
...
 FAIL["test_配列の2番目は文字列のFizzを返す", #<Minitest::Reporters::Suite:0x000055feccc65ab8 @name="数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す">, 0.012104410998290405]
 test_配列の2番目は文字列のFizzを返す#数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す (0.01s)
        --- expected
        +++ actual
        @@ -1 +1 @@
        -"Fizz"
        +#<FizzBuzzValue:0xXXXXXX @number=3, @value="Fizz">
        /workspace/tdd_rb/test/fizz_buzz_test.rb:57:in `test_配列の2番目は文字列のFizzを返す'
...
```

変更によりテストが失敗しました。エラー内容を見てみると文字列からオブジェクトを返しているためアサーションが失敗しているようです。ここは、**値オブジェクト** の **アクセッサメソッド** を経由して取得した値をアサーション対象に変更しましょう。

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(FizzBuzzType01.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列Fizzを返す
          assert_equal 'Fizz', @fizzbuzz.generate(3).value
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列Buzzを返す
          assert_equal 'Buzz', @fizzbuzz.generate(5).value
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.generate(15).value
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1).value
        end
      end

      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(FizzBuzzType01.new)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end

        def test_配列の初めは文字列の1を返す
          assert_equal '1', @result.first.value
        end

        def test_配列の最後は文字列のBuzzを返す
          assert_equal 'Buzz', @result.last.value
        end

        def test_配列の2番目は文字列のFizzを返す
          assert_equal 'Fizz', @result[2].value
        end

        def test_配列の4番目は文字列のBuzzを返す
          assert_equal 'Buzz', @result[4].value
        end

        def test_配列の14番目は文字列のFizzBuzzを返す
          assert_equal 'FizzBuzz', @result[14].value
        end
      end
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(FizzBuzzType02.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.generate(3).value
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.generate(5).value
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列15を返す
          assert_equal '15', @fizzbuzz.generate(15).value
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1).value
        end
      end
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzz.new(FizzBuzzType03.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.generate(3).value
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.generate(5).value
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.generate(15).value
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.generate(1).value
        end
      end
    end

    describe 'それ以外のタイプの場合' do
      def test_例外を返す
        e = assert_raises RuntimeError do
          FizzBuzzType.create(4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
...
```

``` bash
08:49:28 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 41 / 46 LOC (89.13%) covered.
Started with run options --guard --seed 25972

  32/32: [==================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00619s
32 tests, 35 assertions, 0 failures, 0 errors, 0 skips

08:49:29 - INFO - Inspecting Ruby code style of all files
 7/7 files |======================================= 100 =======================================>| Time: 00:00:00

7 files inspected, no offenses detected
08:49:30 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png
 0/0 files |======================================= 100 =======================================>| Time: 00:00:00

0 files inspected, no offenses detected
```

テストコードをそれほど変更することなく **値オブジェクト** を返すリファクタリングが出来ました。コミットしておきましょう。

``` bash
$ git add .
$ git commit -m 'refactor: オブジェクトによるプリミティブの置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType
    FizzBuzzType -> FizzBuzzValue

#### 学習用テスト

**値オブジェクト** の理解を深めるために **学習用テスト** を追加します。

``` ruby
...
  describe 'FizzBuzzValue' do
    def setup
      @fizzbuzz = FizzBuzz.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
    end

    def test_同じで値である
      value1 = @fizzbuzz.generate(1)
      value2 = @fizzbuzz.generate(1)

      assert value1.eql?(value2)
    end

    def test_to_stringメソッド
      value = @fizzbuzz.generate(3)

      assert_equal '3:Fizz', value.to_s
    end
  end
end
```

``` bash
$ git add .
$ git commit -m 'test: 学習用テスト'
```

### ファーストクラスコレクション

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType
    FizzBuzzType -> FizzBuzzValue

#### コレクションのカプセル化

**値オブジェクト** を扱うFizzBuzzリストですが **コレクションのカプセル化** を適用して **ファーストクラスコレクション** オブジェクトを追加しましょう。

> コレクションのカプセル化
>
> メソッドがコレクションを返している。
>
> 読み取り専用のビューを返して、追加と削除のメソッドを提供する。
>
> —  新装版 リファクタリング
>

> このように、コレクション型のデータとロジックを特別扱いにして、コレクションを１つだけ持つ専用クラスを作るやり方をコレクションオブジェクトあるいはファーストクラスコレクションと呼びます。
>
> —  現場で役立つシステム設計の原則

まず、 **ファーストクラスコレクション** クラスを追加します。

``` ruby
...
class FizzBuzzList
  attr_reader :value

  def initialize(list)
    @value = list
  end

  def to_s
    @value.to_s
  end

  def add(value)
    FizzBuzzList.new(@value + value)
  end
end
```

FizzBuzz配列を **ファーストクラスコレクション** から取得するように変更します。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = type
  end
...
  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = (1..MAX_NUMBER).map { |n| generate(n) }
  end
end
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = type
    @list = FizzBuzzList.new([])
  end

...
  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = @list.add((1..MAX_NUMBER).map { |n| @type.generate(n) })
  end
end
```

なんだか紛らわしい書き方になってしましました。配列を作るのに以前の配列を元に新しい配列を作るとか回りくどいことをしないで既存の配列を使い回せばいいじゃんと思うかもしれませんが **変更可能なデータ** はバグの原因となる傾向があります。変更可能な **ミュータブル** な変数ではなく 永続的に変更されない **イミュータブル** な変数を使うように心がけましょう。

> 変更可能なデータ
>
> データの変更はしばし予期せぬ結果結果や、厄介なバグを引き起こします。他で違う値を期待していることに気づかないままに、ソフトウェアのある箇所で値を変更してしまえば、それだけで動かなくなってしまいます。これは値が変わる条件がまれにしかない場合、特に見つけにくいバグとなります。そのため、ソフトウェア開発の一つの潮流である関数型プログラミングは、データは不変であるべきで、更新時は常に元にデータ構造のコピーを返すようにし、元データには手を触れないという思想に基づいています。
>
> —  リファクタリング(第2版)

> 値オブジェクトと同じようにコレクションオブジェクトも、できるだけ「不変」スタイルで設計します。そのほうがプログラムが安定します。
>
> —  現場で役立つシステム設計の原則

``` bash
...
ERROR["test_配列の14番目は文字列のFizzBuzzを返す", #<Minitest::Reporters::Suite:0x00005561331b7940 @name="FizzBuzz::数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す">, 0.011710233025951311]
 test_配列の14番目は文字列のFizzBuzzを返す#FizzBuzz::数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す (0.01s)
Minitest::UnexpectedError:         NoMethodError: undefined method `[]' for #<FizzBuzzList:0x0000556133198ba8 @value=[]>
            /workspace/tdd_rb/test/fizz_buzz_test.rb:66:in `test_配列の14番目は文字列のFizzBuzzを返す'
...
```

**ファーストクラスコレクション** 経由で取得するようになったので **アクセッサメソッド** を変更する必要があります。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = type
  end
...
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :list
  attr_reader :type

  def initialize(type)
    @type = type
    @list = FizzBuzzList.new([])
  end
...
```

``` ruby
class FizzBuzz
  MAX_NUMBER = 100
  attr_reader :type

  def list
    @list.value
  end

  def initialize(type)
    @type = type
    @list = FizzBuzzList.new([])
  end
....
```

``` bash
09:12:46 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 53 / 56 LOC (94.64%) covered.
Started with run options --guard --seed 61051

  34/34: [==================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01285s
34 tests, 37 assertions, 0 failures, 0 errors, 0 skips

09:12:47 - INFO - Inspecting Ruby code style of all files
 7/7 files |======================================= 100 =======================================>| Time: 00:00:00

7 files inspected, no offenses detected
09:12:48 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png
 0/0 files |======================================= 100 =======================================>| Time: 00:00:00

0 files inspected, no offenses detected
```

テストが直ったのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: コレクションのカプセル化'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType
    FizzBuzzType -> FizzBuzzValue
    FizzBuzzList *-- FizzBuzzValue
    FizzBuzz -> FizzBuzzList

#### 学習用テスト

**ファーストクラスコレクション** を理解するため **学習用テスト** を追加しておきましょう。

``` ruby
...
  describe 'FizzBuzzValueList' do
    def setup
      @fizzbuzz = FizzBuzz.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
    end

    def test_新しいインスタンスが作られる
      list1 = @fizzbuzz.generate_list
      list2 = list1.add(list1.value)

      assert_equal 100, list1.value.count
      assert_equal 200, list2.value.count
    end
  end
end
```

``` bash
$ git add .
$ git commit -m 'refactor: 学習用テスト'
```

### オブジェクト指向設計

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType
    FizzBuzzType -> FizzBuzzValue
    FizzBuzzList *-- FizzBuzzValue
    FizzBuzz -> FizzBuzzList

**値オブジェクト** 及び **ファーストクラスコレクション** の適用で **基本データ型への執着** の臭いはなくなりました。今度は設計の観点から全体を眺めてみましょう。ここで気になるのが `FizzBuzz` クラスです。このクラスは他のクラスと比べてやることが多いようです。このようなクラスは **単一責任の原則** に違反している可能性があります。そこで **デザインパターン** の１つである **Commandパターン** を使ったリファクタリングである **メソッドオブジェクトによるメソッドの置き換え** 適用してみようと思います。

> SRP:
> 単一責任の原則
>
> かつて単一責任の原則(SRP)は、以下のように語られてきた。
>
>     モジュールを変更する理由はたったひとつだけであるべきである
>
> ソフトウェアシステムに手を加えるのは、ユーザーやステークホルダーを満足させるためだ。この「ユーザーやステークホルダー」こそが、単一責任の原則（SRP）を指す「変更する理由」である。つまり、この原則は以下のように言い換えられる。
>
>     モジュールはたったひとりのユーザーやステークホルダーに対して責任を負うべきである。
>
> 残念ながら「たったひとりのユーザーやステークホルダー」という表現は適切ではない。複数のユーザーやステークホルダーがシステムを同じように変更したいと考えることもある。ここでは、変更を望む人たちをひとまとめにしたグループとして扱いたい。このグループのことをアクターと呼ぶことにしよう。
> これを踏まえると、最終的な単一責任の原則（SRP）は以下のようになる。
>
>     モジュールはたったひとつのアクターに対して責任を負うべきである。
>
> さて、ここでいう「モジュール」とは何のことだろう？端的に言えば、モジュールとはソースファイルのことである。たいていの場合は、この定義で問題ないだろう。だが、ソースファイル以外のところにコードを格納する言語や開発環境も存在する。そのような場合の「モジュール」は、いくつかの関数やデータをまとめた凝集性のあるものだと考えよう。
>
> 「凝集性のある」という言葉が単一責任の原則（SRP）を匂わせる。凝集性が、ひとつのアクターに対する責務を負うコードをまとめるフォースとなる。
>
> —  Clean Architecture 達人に学ぶソフトウェアの構造と設計
>

> Commandパターン
>
> 処理の呼び出しが、シンプルなメソッド呼び出しよりも複雑になってきたときはどうすればよいだろうか---処理のためのオブジェクトを作成し、それを起動するようにしよう。
>
> —  テスト駆動開発
>

> メソッドオブジェクトによるメソッドの置き換え
>
> 長いメソッドで、「メソッドの抽出」を適用できないようなローカル変数の使い方をしている。
>
> メソッド自身をオブジェクトとし、すべてのローカル変数をそのオブジェクトのフィールドとする。そうすれば、そのメソッドを同じオブジェクト中のメソッド群に分解できる。
>
> —  新装版 リファクタリング

#### メソッドオブジェクトによるメソッドの置き換え

まず、**値オブジェクト** の `FizzBuzzValue` を返す責務だけを持った **メソッドオブジェクト** を抽出します。Rubyのような動的言語では必要が無いのですが **Commandパターン** の説明のため **インターフェイス** にあたるスーパークラスを継承した **メソッドオブジェクト** を定義します。

``` ruby
...
class FizzBuzzCommand
  def execute; end
end

class FizzBuzzValueCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    @type.generate(number).value
  end
end
```

テストコードを `FizzBuzzValueCommand` を呼び出すように変更します。

``` ruby
...
class FizzBuzzTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType01.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列Fizzを返す
          assert_equal 'Fizz', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列Buzzを返す
          assert_equal 'Buzz', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end

      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzz.new(FizzBuzzType01.new)
          fizzbuzz.generate_list
          @result = fizzbuzz.list
        end

        def test_配列の初めは文字列の1を返す
          assert_equal '1', @result.first.value
        end

        def test_配列の最後は文字列のBuzzを返す
          assert_equal 'Buzz', @result.last.value
        end

        def test_配列の2番目は文字列のFizzを返す
          assert_equal 'Fizz', @result[2].value
        end

        def test_配列の4番目は文字列のBuzzを返す
          assert_equal 'Buzz', @result[4].value
        end

        def test_配列の14番目は文字列のFizzBuzzを返す
          assert_equal 'FizzBuzz', @result[14].value
        end
      end
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType02.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列15を返す
          assert_equal '15', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType03.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'それ以外のタイプの場合' do
      def test_例外を返す
        e = assert_raises RuntimeError do
          FizzBuzzType.create(4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
...
```

``` bash
...
09:56:19 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 60 / 63 LOC (95.24%) covered.
Started with run options --guard --seed 27353

  35/35: [==================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00692s
35 tests, 39 assertions, 0 failures, 0 errors, 0 skips

09:56:20 - INFO - Inspecting Ruby code style of all files
 7/7 files |======================================= 100 =======================================>| Time: 00:00:00

7 files inspected, no offenses detected
09:56:21 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/loading_background.png coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/border.png
 0/0 files |======================================= 100 =======================================>| Time: 00:00:00
 ...
```

`FizzBuzzValueCommand` の抽出ができたのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: メソッドオブジェクトによるメソッドの置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType
    FizzBuzzType -> FizzBuzzValue
    FizzBuzzList *-- FizzBuzzValue
    FizzBuzz -> FizzBuzzList
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzValueCommand *- FizzBuzzType

#### メソッドオブジェクトによるメソッドの置き換え

続いて、**ファーストクラスコレクション** を扱う `FizzBuzzList` を返す責務だけを持った **メソッドオブジェクト** を抽出します。

``` ruby
...
class FizzBuzzListCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    FizzBuzzList.new((1..number).map { |i| @type.generate(i) }).value
  end
end
```

テストコードを **FizzBuzzListCommand** 経由から実行するように変更します

``` ruby
...
        describe '1から100までのFizzBuzzの配列を返す' do
          def setup
            fizzbuzz = FizzBuzz.new(FizzBuzzType01.new)
            fizzbuzz.generate_list
            @result = fizzbuzz.list
          end
...
```

``` ruby
...
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzzListCommand.new(FizzBuzzType01.new)
          @result = fizzbuzz.execute(100)
        end
...
```

``` bash
01:27:54 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 61 / 66 LOC (92.42%) covered.
Started with run options --guard --seed 62253

  35/35: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00652s
35 tests, 39 assertions, 0 failures, 0 errors, 0 skips
```

テストが通ったのでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: メソッドオブジェクトによるメソッドの置き換え'
```

    class FizzBuzz {
        MAX_NUMBER = 100
        list
        type
        generate(number)
        generate_list()
    }
    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      type
      execute(number)
    }
    class FizzBuzzListCommand {
      type
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzz *- FizzBuzzType
    FizzBuzzType -> FizzBuzzValue
    FizzBuzzList *-- FizzBuzzValue
    FizzBuzz -> FizzBuzzList
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzCommand *- FizzBuzzType
    FizzBuzzListCommand -> FizzBuzzList

#### デッドコードの削除

`FizzBuzz` クラスの責務は各 **メソッドオブジェクト** が実行するようになったので削除しましょう。

``` ruby
class FizzBuzz
  MAX_NUMBER = 100

  def initialize(type)
    @type = type
    @list = FizzBuzzList.new([])
  end

  def list
    @list.value
  end

  def generate(number)
    @type.generate(number)
  end

  def generate_list
    # 1から最大値までのFizzBuzz配列を1発で作る
    @list = @list.add((1..MAX_NUMBER).map { |n| @type.generate(n) })
  end
end

class FizzBuzzType
...
```

``` ruby
class FizzBuzzType
...
```

``` bash
...
ERROR["test_同じで値である", #<Minitest::Reporters::Suite:0x0000562fd34f7848 @name="FizzBuzzValue">, 0.008059715997660533]
 test_同じで値である#FizzBuzzValue (0.01s)
Minitest::UnexpectedError:         NameError: uninitialized constant FizzBuzzTest::FizzBuzz
            /workspace/tdd_rb/test/fizz_buzz_test.rb:225:in `setup'

ERROR["test_to_stringメソッド", #<Minitest::Reporters::Suite:0x0000562fd37694a0 @name="FizzBuzzValue">, 0.01728590900893323]
 test_to_stringメソッド#FizzBuzzValue (0.02s)
Minitest::UnexpectedError:         NameError: uninitialized constant FizzBuzzTest::FizzBuzz
            /workspace/tdd_rb/test/fizz_buzz_test.rb:225:in `setup'

ERROR["test_新しいインスタンスが作られる", #<Minitest::Reporters::Suite:0x0000562fd39be070 @name="FizzBuzzValueList">, 0.028008958004647866]
 test_新しいインスタンスが作られる#FizzBuzzValueList (0.03s)
Minitest::UnexpectedError:         NameError: uninitialized constant FizzBuzzTest::FizzBuzz
            /workspace/tdd_rb/test/fizz_buzz_test.rb:244:in `setup'

========================================|

Finished in 0.03539s
35 tests, 35 assertions, 0 failures, 3 errors, 0 skips
...
```

テストが失敗しました。これは **学習用テスト** で `FizzBuzz` クラスを使っている箇所があるからですね。 **メソッドオブジェクト** 呼び出しに変更しておきましょう。

``` ruby
  describe 'FizzBuzzValue' do
    def setup
      @fizzbuzz = FizzBuzz.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
    end

    def test_同じで値である
      value1 = @fizzbuzz.generate(1)
      value2 = @fizzbuzz.generate(1)

      assert value1.eql?(value2)
    end

    def test_to_stringメソッド
      value = @fizzbuzz.generate(3)

      assert_equal '3:Fizz', value.to_s
    end
  end

  describe 'FizzBuzzValueList' do
    def setup
      @fizzbuzz = FizzBuzz.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
    end

    def test_新しいインスタンスが作られる
      list1 = @fizzbuzz.generate_list
      list2 = list1.add(list1.value)

      assert_equal 100, list1.value.count
      assert_equal 200, list2.value.count
    end
  end
end
```

``` ruby
...
  describe 'FizzBuzzValue' do
    def test_同じで値である
      value1 = FizzBuzzValue.new(1, '1')
      value2 = FizzBuzzValue.new(1, '1')

      assert value1.eql?(value2)
    end

    def test_to_stringメソッド
      value = FizzBuzzValue.new(3, 'Fizz')

      assert_equal '3:Fizz', value.to_s
    end
  end

  describe 'FizzBuzzValueList' do
    def test_新しいインスタンスが作られる
      command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
      array = command.execute(100)
      list1 = FizzBuzzList.new(array)
      list2 = list1.add(array)

      assert_equal 100, list1.value.count
      assert_equal 200, list2.value.count
    end
  end
end
```

``` bash
...
01:35:22 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 50 / 56 LOC (89.29%) covered.
Started with run options --guard --seed 10411

  35/35: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00704s
35 tests, 39 assertions, 0 failures, 0 errors, 0 skips
...
```

不要なコードを残しておくとメンテナンスの時に削除していいのかわからなくなり可読性を落とし原因となります。削除できる時に削除しておきましょう。後で必要になったとしてもバージョン管理システムを使えば問題ありません。ということでコミットします。

> デッドコードの削除
>
> コードが使用されなくなったら削除すべきです。そのコードが将来必要になるかもしれないなどという心配はしません。必要になったらいつでも、バージョン管理システムから再び掘り起こせるからです。
>
> （中略）
>
> デッドコードのコメントアウトは、かつては一般的な習慣でした。それは、バージョン管理システムが広く使用される以前の時代や、使いづらかった時代には有用でした。現在では、とても小さなコードベースでもバージョン管理システムに置けるため、もはや必要のない習慣です。
>
> —  リファクタリング(第2版)

``` bash
$ git add .
$ git commit -m 'refactor: デッドコードの削除'
```

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      type
      execute(number)
    }
    class FizzBuzzListCommand {
      type
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

#### デザインパターン

**メソッドオブジェクトによるメソッドの置き換え** リファクタリングの結果として **Commandパターン** という **デザインパターン** を適用しました。実はこれまでにも **オブジェクトによるプリミティブの置き換え** では **Value Objectパターン** を **ポリモーフィズムによる条件記述の置き換え** では **Factory Methodパターン** をそして、 **委譲の隠蔽** の実施による **State/Strategyによるタイプコードの置き換え** では **Strategyパターン** を適用しています。

[Command パターン](https://ja.wikipedia.org/wiki/Command_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)

    interface Command {
      execute()
    }
    class Invoker {
    }
    class ConcreateCommand {
      execute()
    }
    class Receiver {
      Action()
    }
    class Client {
    }
    Invoker o-> Command
    Command <|-- ConcreateCommand
    Receiver <- ConcreateCommand
    Client -> Receiver
    Client -> ConcreateCommand

> Value Objectパターン
>
> 広く共有されるものの、同一インスタンスであることはさほど重要でないオブジェクトを設計するにはどうしたらよいだろうか----オブジェクト作成時に状態を設定したら、その後決して変えないようにする。オブジェクトへの操作は必ず新しいオブジェクトを返すようにしよう。
>
> —  テスト駆動開発

> Factory Methodパターン
>
> オブジェクト作成に柔軟性をもたせたいときは、どうすればよいだろうか---単にコンストラクタで作るのではなく、メソッドを使ってオブジェクトを作成しよう。
>
> —  テスト駆動開発

[Strategy
パターン](https://ja.wikipedia.org/wiki/Strategy_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)

    class Context {
      ContextInterface()
    }
    interface Strategy {
      AlgorithmInterface()
    }
    class ConcreateStrategyA {
      AlgorithmInterface()
    }
    class ConcreateStrategyB {
      AlgorithmInterface()
    }
    Context o- Strategy
    Strategy <|-- ConcreateStrategyA
    Strategy <|-- ConcreateStrategyB

作成したコードはパターンと完全に一致しているわけではありませんし、Rubyのような動的言語ではもっと簡単な実現方法もありますがここでは先人の考えた設計パターンというものがありオブジェクト指向設計の [イデオム](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%87%E3%82%A3%E3%82%AA%E3%83%A0) として使えること。そしてテスト駆動開発では一般的な設計アプローチとは異なる形で導かれているということくらいを頭に残しておけば結構です。どのパターンをいつ適用するかはリファクタリングを繰り返しているうちに思いつくようになってきます（多分）。

> ただ、書籍『デザインパターン』（通称Gof本）の大ヒットは、その反面、それらパターンを表現する方法の多様性を奪ってしまった。Gof本には、設計をフェーズとして扱うという暗黙の前提があるように見受けられる。つまり、リファクタリングを設計行為として捉えていない。TDDにおける設計は、デザインパターンを少しだけ違う側面から捉えなければならない。
>
> —  テスト駆動開発

あと、設計の観点から今回 **単一責任の原則** に従って `FizzBuzz` クラスを **メソッドオブジェクト** に分割して削除しました。

    Interface FizzBuzzCommand {
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzCommand *- FizzBuzzType

もし、新しい処理を追加する必要が発生した場合はどうしましょうか？ `FizzBuzzCommand` インターフェイスを実装した **メソッドオブジェクト** を追加しましょう。

    Interface FizzBuzzCommand {
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzCommand <|-- FizzBuzzSomethingSpecialCommand
    FizzBuzzCommand *- FizzBuzzType

もし、新しいタイプが必要になったらどうしましょうか？ `FizzBuzzType` クラスを継承した新しいタイプクラスを追加しましょう。

    Interface FizzBuzzCommand {
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType <|-- FizzBuzzTypeXX
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzCommand *- FizzBuzzType

このように既存のコードを変更することなく振る舞いを変更できるので **オープン・クローズドの原則** を満たした設計といえます。

> OCP:オープン・クローズドの原則
>
> 「オープン・クローズドの原則（OCP）」は、1988年にBertrand Maeerが提唱した以下のような原則だ。
>
>     ソフトウェアの構成要素は拡張に対しては開いていて、修正に対しては閉じていなければならない。
>     　　　　　　　　　　　　『アジャイルソフトウェア開発の奥義　第2版』（SBクリエイティブ）より引用
>
> 言い換えれば、ソフトウェアの振る舞いは、既存の成果物を変更せず拡張できるようにすべきである、ということだ。
>
> —  Clean Architecture 達人に学ぶソフトウェアの構造と設計

### 例外

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      type
      execute(number)
    }
    class FizzBuzzListCommand {
      type
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

ここまでは、正常系をリファクタリングして設計を改善してきました。しかし、アプリケーションは例外系も考慮する必要があります。続いて、**アサーションの導入** を適用した例外系のリファクタリングに取り組むとしましょう。

> アサーションの導入
>
> 前提を明示するためのすぐれたテクニックとして、アサーションを記述する方法があります。
>
> —  リファクタリング(第2版)

#### アサーションの導入

まず、 **メソッドオブジェクト** の `FizzBuzzValueCommand` にマイナスの値が渡された場合の振る舞いをどうするか考えます。ここでは正の値のみ許可する振る舞いにしたいので以下のテストコードを追加します。

``` ruby
class FizzBuzzTest < Minitest::Test
...
  describe '例外ケース' do
    def test_値は正の値のみ許可する
      assert_raises Assertions::AssertionFailedError do
        FizzBuzzValueCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(-1)
      end
    end
  end
end
```

``` bash
...
ERROR["test_値は正の値のみ許可する", #<Minitest::Reporters::Suite:0x00007fadf30c45d8 @name="例外ケース">, 0.006546000000525964]
 test_値は正の値のみ許可する#例外ケース (0.01s)
Minitest::UnexpectedError:         NameError: uninitialized constant FizzBuzzTest::Assertions
            /Users/k2works/Projects/sandbox/tdd_rb/test/fizz_buzz_test.rb:249:in `test_値は正の値のみ許可する'

  36/36: [=========================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.03159s
36 tests, 39 assertions, 0 failures, 1 errors, 0 skips
...
```

テストを通すためアサーションモジュールを追加します。Rubyでは **モジュール** を使います。

> モジュールはクラスと非常によく似ていますが、以下の二点が異なります。
>
>   - モジュールはインスタンス化できない
>
>   - 本章後半可能なのは include や extend が可能なのはモジュールだけ
>
> それ以外のクラスメソッドや定数の定義などはクラスと同じように定義することができます。
>
> —  かんたんRuby

``` ruby
...
module Assertions
  class AssertionFailedError < StandardError; end

  def assert(&condition)
    raise AssertionFailedError, 'Assertion Failed' unless condition.call
  end
end

class FizzBuzzValue
...
```

アサーションモジュールを追加してエラーはなくなりましたがテストは失敗したままです。

``` bash
...
 FAIL["test_値は正の値のみ許可する", #<Minitest::Reporters::Suite:0x00007fdcfc0c2548 @name="例外ケース">, 0.005800000000817818]
 test_値は正の値のみ許可する#例外ケース (0.01s)
        Assertions::AssertionFailedError expected but nothing was raised.
        /Users/k2works/Projects/sandbox/tdd_rb/test/fizz_buzz_test.rb:249:in `test_値は正の値のみ許可する'

============================================================================================================|

Finished in 0.00621s
36 tests, 40 assertions, 1 failures, 0 errors, 0 skips
...
```

追加したモジュールを `FizzBuzzValue` クラスをに **Mix-in** します。そして、**コンストラクタ** 実行時に数値は0以上であるアサーションを追加します。

> Rubyでの継承は一種類、単一継承しか実行できませんが、複数のクラスを継承する多重継承の代わりにMix-inというメソッドの共有方法を提供します。
>
> —  かんたんRuby

``` ruby
class FizzBuzzValue
  attr_reader :number, :value

  def initialize(number, value)
    @number = number
    @value = value
  end
...
end
```

``` ruby
class FizzBuzzValue
  include Assertions
  attr_reader :number, :value

  def initialize(number, value)
    assert { number >= 0 }
    @number = number
    @value = value
  end
...
end
```

``` bash
...
Started with run options --seed 37354


Progress: |====================================================================================================|

Finished in 0.01433s
36 tests, 40 assertions, 0 failures, 0 errors, 0 skips
...
```

アサーションが機能するようになりました、コミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: アサーションの導入'
```

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      type
      execute(number)
    }
    class FizzBuzzListCommand {
      type
      execute(number)
    }
    class Assertions {
      assert(&condition)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType
    FizzBuzzValue --|> Assertions

次は、**メソッドオブジェクト** の `FizzBuzzListCommand` の実行時に100件以上指定された場合の振る舞いをどうするか考えます。ここでは100までを許可する振る舞いにします。

``` ruby
...
  describe '例外ケース' do
    def test_値は正の値のみ許可する
      assert_raises Assertions::AssertionFailedError do
        FizzBuzzValueCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(-1)
      end
    end

    def test_100より多い数を許可しない
      assert_raises Assertions::AssertionFailedError do
        FizzBuzzListCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(101)
      end
    end
  end
end
```

`FizzBuzzList` にアサーションモジュールを **Mix-in** します。**コンストラクタ** 実行時に配列のサイズは100までというアサーションを追加します。

``` ruby
...
class FizzBuzzList
  include Assertions
  attr_reader :value

  def initialize(list)
    assert { list.count <= 100 }
    @value = list
  end
...
```

``` bash
...
ERROR["test_新しいインスタンスが作られる", #<Minitest::Reporters::Suite:0x00005558ca6e8e80 @name="FizzBuzzValueList">, 0.010412617004476488]
 test_新しいインスタンスが作られる#FizzBuzzValueList (0.01s)
Minitest::UnexpectedError:         Assertions::AssertionFailedError: Assertion Failed
            /workspace/tdd_rb/lib/fizz_buzz.rb:58:in `assert'
            /workspace/tdd_rb/lib/fizz_buzz.rb:88:in `initialize'
            /workspace/tdd_rb/lib/fizz_buzz.rb:97:in `new'
            /workspace/tdd_rb/lib/fizz_buzz.rb:97:in `add'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:259:in `test_新しいインスタンスが作られる'

====================================================================================================|

Finished in 0.01238s
36 tests, 38 assertions, 0 failures, 1 errors, 0 skips
...
```

追加したテストはパスするようになりましたが既存のテストコードでエラーが出るようになりました。該当するテストコードを見たところ100件より多い **学習用テスト** で **ファーストクラスコレクション** を作ろうとしたため `AssertionFailedError` を発生させたようです。テストコードを修正しておきましょう。

``` ruby
...
  describe 'FizzBuzzValueList' do
    def test_新しいインスタンスが作られる
      command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
      array = command.execute(100)
      list1 = FizzBuzzList.new(array)
      list2 = list1.add(array)

      assert_equal 100, list1.value.count
      assert_equal 200, list2.value.count
    end
  end
...
```

最初は50件作るように変更します。

``` ruby
...
  describe 'FizzBuzzValueList' do
    def test_新しいインスタンスが作られる
      command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
      array = command.execute(50)
      list1 = FizzBuzzList.new(array)
      list2 = list1.add(array)

      assert_equal 100, list1.value.count
      assert_equal 200, list2.value.count
    end
  end
...
```

アサーションエラーはなくなりましたが期待した値と違うと指摘されています。テストコードのアサーションを修正します。

``` bash
 FAIL["test_新しいインスタンスが作られる", #<Minitest::Reporters::Suite:0x0000556b5137c780 @name="FizzBuzzValueList">, 0.003735148988198489]
 test_新しいインスタンスが作られる#FizzBuzzValueList (0.00s)
        Expected: 100
          Actual: 50
        /workspace/tdd_rb/test/fizz_buzz_test.rb:261:in `test_新しいインスタンスが作られる'

  36/36: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00837s
36 tests, 39 assertions, 1 failures, 0 errors, 0 skips
```

``` ruby
...
  describe 'FizzBuzzValueList' do
    def test_新しいインスタンスが作られる
      command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
      array = command.execute(50)
      list1 = FizzBuzzList.new(array)
      list2 = list1.add(array)

      assert_equal 50, list1.value.count
      assert_equal 200, list2.value.count
    end
  end
...
```

２つ目のアサーションに引っかかってしまいました。こちらも修正します。

``` bash
 FAIL["test_新しいインスタンスが作られる", #<Minitest::Reporters::Suite:0x0000563a0c4fc2b0 @name="FizzBuzzValueList">, 0.005684088013367727]
 test_新しいインスタンスが作られる#FizzBuzzValueList (0.01s)
        Expected: 200
          Actual: 100
        /workspace/tdd_rb/test/fizz_buzz_test.rb:262:in `test_新しいインスタンスが作られる'

  36/36: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00809s
36 tests, 40 assertions, 1 failures, 0 errors, 0 skips
```

``` ruby
...
  describe 'FizzBuzzValueList' do
    def test_新しいインスタンスが作られる
      command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
      array = command.execute(50)
      list1 = FizzBuzzList.new(array)
      list2 = list1.add(array)

      assert_equal 50, list1.value.count
      assert_equal 100, list2.value.count
    end
  end
...
```

``` bash
...
01:58:57 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 61 / 64 LOC (95.31%) covered.
Started with run options --guard --seed 44956

  36/36: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00717s
36 tests, 40 assertions, 0 failures, 0 errors, 0 skips
...
```

仕様変更による反映が出来たのでコミットしましょう。

``` bash
$ git add .
$ git commit -m 'refactor: アサーションの導入'
```

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      execute(number)
    }
    class FizzBuzzListCommand {
      execute(number)
    }
    class Assertions {
      assert(&condition)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType
    FizzBuzzValue --|> Assertions
    FizzBuzzList --|> Assertions

**アサーションの導入** とは別のアプローチとして **例外** を返す方法もあります。 **例外によるエラーコードの置き換え** を適用してアサーションモジュールを削除しましょう。

> 例外によるエラーコードの置き換え
>
> エラーを示す特別なコードをメソッドがリターンしている。
>
> 代わりに例外を発生させる。
>
> —  新装版 リファクタリング

#### 例外によるエラーコードの置き換え

アサーションモジュールを削除してアサーション部分を **例外** に変更します。

``` ruby
...
module Assertions
  class AssertionFailedError < StandardError; end

  def assert(&condition)
    raise AssertionFailedError, 'Assertion Failed' unless condition.call
  end
end

class FizzBuzzValue
  include Assertions
  attr_reader :number, :value

  def initialize(number, value)
    assert { number >= 0 }
    @number = number
    @value = value
  end
...
end

class FizzBuzzList
  include Assertions
  attr_reader :value

  def initialize(list)
    assert { list.count <= 100 }
    @value = list
  end
...
end
...
```

``` ruby
...
class FizzBuzzValue
  attr_reader :number, :value

  def initialize(number, value)
    raise '正の値のみ有効です' if number < 0

    @number = number
    @value = value
  end
...
end

class FizzBuzzList
  attr_reader :value

  def initialize(list)
    raise '上限は100件までです' if list.count > 100

    @value = list
  end
...
end
```

``` bash
...
ERROR["test_値は正の値のみ許可する", #<Minitest::Reporters::Suite:0x000055d30f0b8a50 @name="FizzBuzz::数を文字列にして返す::例外ケース">, 0.004186890990240499]
 test_値は正の値のみ許可する#FizzBuzz::数を文字列にして返す::例外ケース (0.00s)
Minitest::UnexpectedError:         NameError: uninitialized constant FizzBuzzTest::Assertions
            /workspace/tdd_rb/test/fizz_buzz_test.rb:143:in `test_値は正の値のみ許可する'

ERROR["test_100より多い数を許可しない", #<Minitest::Reporters::Suite:0x000055d30f114210 @name="FizzBuzz::数を文字列にして返す::例外ケース">, 0.008254560001660138]
 test_100より多い数を許可しない#FizzBuzz::数を文字列にして返す::例外ケース (0.01s)
Minitest::UnexpectedError:         NameError: uninitialized constant FizzBuzzTest::Assertions
            /workspace/tdd_rb/test/fizz_buzz_test.rb:151:in `test_100より多い数を許可しない'

  37/37: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01731s
37 tests, 39 assertions, 0 failures, 2 errors, 0 skips
...
```

アサーションモジュールを削除したのでエラーが発生しています。テストコードを修正しましょう。

``` ruby
...
  describe '例外ケース' do
    def test_値は正の値のみ許可する
      assert_raises Assertions::AssertionFailedError do
        FizzBuzzValueCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(-1)
      end
    end

    def test_100より多い数を許可しない
      assert_raises Assertions::AssertionFailedError do
        FizzBuzzListCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(101)
      end
    end
  end
end
```

``` ruby
...
  describe '例外ケース' do
    def test_値は正の値のみ許可する
      e = assert_raises RuntimeError do
        FizzBuzzValueCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(-1)
      end

      assert_equal '正の値のみ有効です', e.message
    end

    def test_100より多い数を許可しない
      e = assert_raises RuntimeError do
        FizzBuzzListCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(101)
      end

      assert_equal '上限は100件までです', e.message
    end
  end
end
```

``` bash
...
02:13:46 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 55 / 58 LOC (94.83%) covered.
Started with run options --guard --seed 55179

  37/37: [=================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00738s
37 tests, 43 assertions, 0 failures, 0 errors, 0 skips
...
```

再びテストが通るようになったのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor:  例外によるエラーコードの置き換え'
```

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      execute(number)
    }
    class FizzBuzzListCommand {
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

#### アルゴリズムの置き換え

``` bash
02:13:46 - INFO - Inspecting Ruby code style: test/fizz_buzz_test.rb lib/fizz_buzz.rb
lib/fizz_buzz.rb:58:26: C: Style/NumericPredicate: Use number.negative? instead of number < 0.
    raise '正の値のみ有効です' if number < 0
                         ^^^^^^^^^^
 2/2 files |====================================== 100 =======================================>| Time: 00:00:00

2 files inspected, 1 offense detected
```

テストは通りますが警告が表示されるようになりました。 `Style/NumericPredicate: Use number.negative? instead of number < 0.` とのことなので **アルゴリズムの置き換え** を適用しておきましょう。

> アルゴリズムの取り替え
>
> アルゴリズムをよりわかりやすいものに置き換えたい
>
> メソッドの本体を新たなアルゴリズムで置き換える。
>
> —  新装版 リファクタリング

``` ruby
...
class FizzBuzzValue
  attr_reader :number, :value

  def initialize(number, value)
    raise '正の値のみ有効です' if number < 0
...
```

``` ruby
...

class FizzBuzzValue
  attr_reader :number, :value

  def initialize(number, value)
    raise '正の値のみ有効です' if number.negative?
...
```

``` bash
02:18:31 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
 1/1 file |======================================= 100 =======================================>| Time: 00:00:00

1 file inspected, no offenses detected
```

警告が消えたのでコミットします。

``` bash
$ git add .
$ git commit -m 'refactor: アルゴリズムの置き換え'
```

#### マジックナンバーの置き換え

件数に **リテラル** を使っています。ここは **マジックナンバーの置き換え** を適用するべきですね。

> シンボリック定数によるマジックナンバーの置き換え
>
> 特別な意味を持った数字のリテラルがある。
>
> 定数を作り、それにふさわしい名前をつけて、そのリテラルを置き換える。
>
> —  新装版 リファクタリング

``` ruby
...
class FizzBuzzList
  attr_reader :value

  def initialize(list)
    raise '上限は100件までです' if list.count > 100

    @value = list
  end
...
```

**式展開** を使ってメッセージ内容も定数から参照するようにしましょう。

> 式展開
>
> 式展開とは、「\#{}」の書式で文字列中に何らかの変数や式を埋め込むことが可能な機能です。これは、ダブルクオートを使用した場合のみの機能です。
>
> —  かんたんRuby

``` ruby
class FizzBuzzList
  MAX_COUNT = 100
  attr_reader :value

  def initialize(list)
    raise "上限は#{MAX_COUNT}件までです" if list.count > MAX_COUNT

    @value = list
  end
...
```

テストは壊れていないようですが `MAX_COUNT` を変更したらテストが失敗するか確認しておきましょう。

``` ruby
class FizzBuzzList
  MAX_COUNT = 10
...
```

``` bash
...
ERROR["test_配列の14番目は文字列のFizzBuzzを返す", #<Minitest::Reporters::Suite:0x000055942ab5e230 @name="FizzBuzz::数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す">, 0.008073228993453085]
 test_配列の14番目は文字列のFizzBuzzを返す#FizzBuzz::数を文字列にして返す::タイプ1の場合::1から100までのFizzBuzzの配列を返す (0.01s)
Minitest::UnexpectedError:         RuntimeError: 上限は10件までです
            /workspace/tdd_rb/lib/fizz_buzz.rb:80:in `initialize'
            /workspace/tdd_rb/lib/fizz_buzz.rb:112:in `new'
            /workspace/tdd_rb/lib/fizz_buzz.rb:112:in `execute'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:45:in `setup'
...
```

想定通りのエラーが発生したのでコードを元に戻してコミットしましょう。

``` ruby
class FizzBuzzList
  MAX_COUNT = 100
...
```

``` bash
...
Started with run options --seed 5525


Progress: |====================================================================================================|

Finished in 0.01262s
37 tests, 43 assertions, 0 failures, 0 errors, 0 skips
...
```

``` bash
$ git add .
$ git commit -m 'refactor: マジックナンバーの置き換え'
```

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       MAX_COUNT = 100
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      execute(number)
    }
    class FizzBuzzListCommand {
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

#### 特殊ケースの導入

最後に **ポリモーフィズム** の応用としてタイプクラスが未定義の場合に **例外** ではなく未定義のタイプクラスを返す **特殊ケースの導入** を適用してみましょう。

> ヌルオブジェクトの導入
>
> null値のチェックが繰り返し現れる。
>
> そのnull値をヌルオブジェクトで置き換える。
>
> —  新装版 リファクタリング
>

> 特殊ケースの導入
>
> 旧：ヌルオブジェクトの導入
>
> 特殊ケースの処理を要する典型的な値がnullなので、このパターンをヌルオブジェクトパターンと呼ぶことがあります、しかし、通常の特殊ケースとアプローチは同じです。いわばヌルオブジェクトは「特殊ケース」の特殊ケースです。
>
> —  リファクタリング(第2版)

まず、それ以外のタイプの場合の振る舞いを変更します。

``` ruby
...
    describe 'それ以外のタイプの場合' do
      def test_例外を返す
        e = assert_raises RuntimeError do
          FizzBuzzType.create(4)
        end

        assert_equal '該当するタイプは存在しません', e.message
      end
    end
  end
...
```

``` ruby
...
   describe 'それ以外のタイプの場合' do
      def test_未定義のタイプを返す
        fizzbuzz = FizzBuzzType.create(4)

        assert_equal '未定義', fizzbuzz.to_s
      end
    end
  end
...
```

``` bash
...
ERROR["test_未定義のタイプを返す", #<Minitest::Reporters::Suite:0x00005593e21297d0 @name="数を文字列にして返す::それ以外のタイプの場合">, 0.0065623498521745205]
 test_未定義のタイプを返す#数を文字列にして返す::それ以外のタイプの場合 (0.01s)
Minitest::UnexpectedError:         RuntimeError: 該当するタイプは存在しません
            /workspace/tdd_rb/lib/fizz_buzz.rb:17:in `create'
            /workspace/tdd_rb/test/fizz_buzz_test.rb:131:in `test_未定義のタイプを返す'

  37/37: [==================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00780s
37 tests, 41 assertions, 0 failures, 1 errors, 0 skips
...
```

現時点では **例外** を投げるので未定義タイプ `FizzBuzzTypeNotDefined` を作成して **ファクトリメソッド** を変更します。

``` ruby
class FizzBuzzType
  TYPE_01 = 1
  TYPE_02 = 2
  TYPE_03 = 3

  def self.create(type)
    case type
    when FizzBuzzType::TYPE_01
      FizzBuzzType01.new
    when FizzBuzzType::TYPE_02
      FizzBuzzType02.new
    when FizzBuzzType::TYPE_03
      FizzBuzzType03.new
    else
      raise '該当するタイプは存在しません'
    end
  end

  def fizz?(number)
    number.modulo(3).zero?
  end

  def buzz?(number)
    number.modulo(5).zero?
  end
end

class FizzBuzzType01 < FizzBuzzType
...
```

``` ruby
class FizzBuzzType
  TYPE_01 = 1
  TYPE_02 = 2
  TYPE_03 = 3

  def self.create(type)
    case type
    when FizzBuzzType::TYPE_01
      FizzBuzzType01.new
    when FizzBuzzType::TYPE_02
      FizzBuzzType02.new
    when FizzBuzzType::TYPE_03
      FizzBuzzType03.new
    else
      FizzBuzzTypeNotDefined.new
    end
  end
...
class FizzBuzzTypeNotDefined < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, '')
  end

  def to_s
    '未定義'
  end
end

class FizzBuzzValue
...
```

``` bash
...
Started with run options --seed 33939


Progress: |=====================================================================================================|

Finished in 0.01193s
37 tests, 42 assertions, 0 failures, 0 errors, 0 skips
06:46:48 - INFO - Inspecting Ruby code style: lib/fizz_buzz.rb
 1/1 file |======================================= 100 ========================================>| Time: 00:00:00

1 file inspected, no offenses detected
06:46:49 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/border.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/loading_background.png
 0/0 files |======================================= 100 =======================================>| Time: 00:00:00

0 files inspected, no offenses detected
...
```

テストが通るようになりました。 **メソッドオブジェクト** から実行された場合の振る舞いも明記しておきましょう。

``` ruby
...
    describe 'それ以外のタイプの場合' do
      def test_未定義のタイプを返す
        fizzbuzz = FizzBuzzType.create(4)

        assert_equal '未定義', fizzbuzz.to_s
      end

      def test_空の文字列を返す
        type = FizzBuzzType.create(4)
        command = FizzBuzzValueCommand.new(type)

        assert_equal '', command.execute(3)
      end
    end
  end
...
```

``` bash
...
06:48:54 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 62 / 65 LOC (95.38%) covered.
Started with run options --guard --seed 18202

  38/38: [==================================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00747s
38 tests, 43 assertions, 0 failures, 0 errors, 0 skips
...
```

`FizzBuzzTypeNotDefined` オブジェクトは **Null Objectパターン** を適用したものです。

> Null Objectパターン
>
> 特殊な状況をオブジェクトで表現するにはどうすればよいだろうか---その特殊な状況を表現するオブジェクトを作り、通常のオブジェクトと同じプロトコル（メソッド群）を実装しよう。
>
> —  テスト駆動開発

**オープン・クローズドの原則** に従って未定義のタイプである **Null Object** を安全に追加することができたのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor: 特殊ケースの導入'
```

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzTypeNotDefined {
       generate(number)
       to_s()
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       MAX_COUNT = 100
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      execute(number)
    }
    class FizzBuzzListCommand {
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType <|-- FizzBuzzTypeNotDefined
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzTypeNotDefined --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

### モジュール分割

    class FizzBuzzType {
        TYPE_01 = 1
        TYPE_02 = 2
        TYPE_03 = 3
        {static} create(type)
        fizz?(number)
        buzz?(number)
    }
    class FizzBuzzType01 {
       generate(number)
    }
    class FizzBuzzType02 {
       generate(number)
    }
    class FizzBuzzType03 {
       generate(number)
    }
    class FizzBuzzTypeNotDefined {
       generate(number)
       to_s()
    }
    class FizzBuzzValue {
       number
       value
       to_s()
       eql?(other)
    }
    class FizzBuzzList {
       MAX_COUNT = 100
       value
       to_s()
       add(value)
    }
    Interface FizzBuzzCommand {
      execute()
    }
    class FizzBuzzValueCommand {
      execute(number)
    }
    class FizzBuzzListCommand {
      execute(number)
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType <|-- FizzBuzzTypeNotDefined
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzTypeNotDefined --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

クラスモジュールの抽出によってアプリケーションの構造が **抽象化** された結果、視覚的に把握できるようになりました。ここでアプリケーションを実行してみましょう。

``` bash
$ ruby main.rb
Traceback (most recent call last):
main.rb:5:in `<main>': uninitialized constant FizzBuzz (NameError)
Did you mean?  FizzBuzzType
```

エラーが出ています、これはアプリケーションの構成が変わったためです。クライアントプログラムをアプリケーションの変更に合わせて修正します。

``` ruby
# frozen_string_literal: true

require './lib/fizz_buzz.rb'

puts FizzBuzz.generate_list
```

``` bash
# frozen_string_literal: true

require './lib/fizz_buzz.rb'

command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
command.execute(100).each { |i| puts i.value }
```

``` bash
$ ruby main.rb
1
2
Fizz
4
Buzz
...
Fizz
```

クライアントプログラムが直ったのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'fix: プリントする'
```

#### ドメインモデル

`fizz_buzz.rb` ファイル内のクラスモジュールをファイルとして分割していきます。まずは **ドメインオブジェクト** を抽出して **ドメインモデル** として整理しましょう。既存のテストを壊さないように１つづつコピー&ペーストしていきます。

> 関連する業務データと業務ロジックを１つにまとめたこのようなオブジェクトをドメインオブジェクトと呼びます。
>
> 「ドメイン」とは、対象領域とか問題領域という意味です。業務アプリケーションの場合、そのアプリケーションが対象となる業務活動全体がドメインです。業務活動という問題領域（ドメイン）で扱うデータと業務ロジックを、オブジェクトとして表現したものドメインオブジェクトです。ドメインオブジェクトは、業務データと業務ロジックを密接に関係づけます。
>
> —  現場で役立つシステム設計の原則

> このように業務アプリケーションの対象領域（ドメイン）をオブジェクトのモデルとして整理したものをドメインモデルと呼びます。
>
> —  現場で役立つシステム設計の原則

    /main.rb
      |--lib/
          |
           -- fizz_buzz.rb
      |--test/
          |
           -- fizz_buzz_test.rb

    /main.rb
      |--lib/
          |
          domain/
               |
               model/
                   |
                   -- fizz_buzz_value.rb
                   -- fizz_buzz_list.rb
               type/
                   |
                   -- fizz_buzz_type.rb
                   -- fizz_buzz_type_01.rb
                   -- fizz_buzz_type_02.rb
                   -- fizz_buzz_type_03.rb
                   -- fizz_buzz_type_not_defined.rb
           -- fizz_buzz.rb
      |--test/
          |
           -- fizz_buzz_test.rb

**値オブジェクトクラス** と **タイプクラス** を `domain` フォルダ以下に配置します。

``` ruby
# frozen_string_literal: true

class FizzBuzzValue
  attr_reader :number, :value

  def initialize(number, value)
    raise '正の値のみ有効です' if number.negative?

    @number = number
    @value = value
  end

  def to_s
    "#{@number}:#{@value}"
  end

  def ==(other)
    @number == other.number && @value == other.value
  end

  alias eql? ==
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzList
  MAX_COUNT = 100
  attr_reader :value

  def initialize(list)
    raise "上限は#{MAX_COUNT}件までです" if list.count > MAX_COUNT

    @value = list
  end

  def to_s
    @value.to_s
  end

  def add(value)
    FizzBuzzList.new(@value + value)
  end
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzType
  TYPE_01 = 1
  TYPE_02 = 2
  TYPE_03 = 3

  def self.create(type)
    case type
    when FizzBuzzType::TYPE_01
      FizzBuzzType01.new
    when FizzBuzzType::TYPE_02
      FizzBuzzType02.new
    when FizzBuzzType::TYPE_03
      FizzBuzzType03.new
    else
      FizzBuzzTypeNotDefined.new
    end
  end

  def fizz?(number)
    number.modulo(3).zero?
  end

  def buzz?(number)
    number.modulo(5).zero?
  end
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    return FizzBuzzValue.new(number, 'FizzBuzz') if fizz?(number) && buzz?(number)
    return FizzBuzzValue.new(number, 'Fizz') if fizz?(number)
    return FizzBuzzValue.new(number, 'Buzz') if buzz?(number)

    FizzBuzzValue.new(number, number.to_s)
  end
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, number.to_s)
  end
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    return FizzBuzzValue.new(number, 'FizzBuzz') if fizz?(number) && buzz?(number)

    FizzBuzzValue.new(number, number.to_s)
  end
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzTypeNotDefined < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, '')
  end

  def to_s
    '未定義'
  end
end
```

``` bash
...
07:29:03 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/border.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/loading_background.png lib/domain/type/fizz_buzz_type_not_defined.rb lib/domain/type/fizz_buzz_type_03.rb lib/domain/type/fizz_buzz_type_02.rb lib/domain/type/fizz_buzz_type_01.rb lib/domain/type/fizz_buzz_type.rb lib/domain/model/fizz_buzz_list.rb lib/domain/model/fizz_buzz_value.rb
lib/domain/type/fizz_buzz_type_not_defined.rb:3:1: C: Style/Documentation: Missing top-level class documentation comment.
class FizzBuzzTypeNotDefined < FizzBuzzType
^^^^^
lib/domain/type/fizz_buzz_type_03.rb:3:1: C: Style/Documentation: Missing top-level class documentation comment.
class FizzBuzzType03 < FizzBuzzType
^^^^^
lib/domain/type/fizz_buzz_type_02.rb:3:1: C: Style/Documentation: Missing top-level class documentation comment.
class FizzBuzzType02 < FizzBuzzType
^^^^^
lib/domain/type/fizz_buzz_type_01.rb:3:1: C: Style/Documentation: Missing top-level class documentation comment.
class FizzBuzzType01 < FizzBuzzType
^^^^^
lib/domain/type/fizz_buzz_type.rb:3:1: C: Style/Documentation: Missing top-level class documentation comment.
class FizzBuzzType
^^^^^
lib/domain/model/fizz_buzz_list.rb:3:1: C: Style/Documentation: Missing top-level class documentation comment.
class FizzBuzzList
^^^^^
lib/domain/model/fizz_buzz_value.rb:3:1: C: Style/Documentation: Missing top-level class documentation comment.
class FizzBuzzValue
^^^^^
 7/7 files |======================== 100 =========================>| Time: 00:00:00

7 files inspected, 7 offenses detected
...
```

テストは壊れていないようですが警告が出るようになりました。まだ仕掛ですが一旦コミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): モジュール分割'
```

    package "Domain" {
      package "Model" {
        class FizzBuzzValue {
        }
        class FizzBuzzList {
        }
      }
      package "Type" {
        class FizzBuzzType {
        }
        class FizzBuzzType01 {
        }
        class FizzBuzzType02 {
        }
        class FizzBuzzType03 {
        }
        class FizzBuzzTypeNotDefined {
        }
      }
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType <|-- FizzBuzzTypeNotDefined
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzTypeNotDefined --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue

#### アプリケーション

続いて **アプリケーション層** の分割を行います。

> データクラスと機能クラスを分ける手続き型の設計では、アプリケーション層のクラスに業務ロジックの詳細を記述します。
>
> —  現場で役立つシステム設計の原則

    /main.rb
      |--lib/
          |
          domain/
               |
               model/
                   |
                   -- fizz_buzz_value.rb
                   -- fizz_buzz_list.rb
               type/
                   |
                   -- fizz_buzz_type.rb
                   -- fizz_buzz_type_01.rb
                   -- fizz_buzz_type_02.rb
                   -- fizz_buzz_type_03.rb
           -- fizz_buzz.rb
      |--test/
          |
           -- fizz_buzz_test.rb

    /main.rb
      |--lib/
          |
         application/
               |
               -- fizz_buzz_command.rb
               -- fizz_buzz_value_command.rb
               -- fizz_buzz_list_command.rb
         domain/
               |
               model/
                   |
                   -- fizz_buzz_value.rb
                   -- fizz_buzz_list.rb
               type/
                   |
                   -- fizz_buzz_type.rb
                   -- fizz_buzz_type_01.rb
                   -- fizz_buzz_type_02.rb
                   -- fizz_buzz_type_03.rb
           -- fizz_buzz.rb
      |--test/
          |
           -- fizz_buzz_test.rb

ここでは **ドメインオブジェクト** を操作する **メソッドオブジェクト** を `application` フォルダ以下に配置します。

``` ruby
# frozen_string_literal: true

class FizzBuzzCommand
  def execute; end
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzValueCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    @type.generate(number).value
  end
end
```

``` ruby
# frozen_string_literal: true

class FizzBuzzListCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    FizzBuzzList.new((1..number).map { |i| @type.generate(i) }).value
  end
end
```

テストは壊れていないのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): モジュール分割'
```

    package "Application" {
      class FizzBuzzCommand {
      }
      class FizzBuzzValueCommand {
      }
      class FizzBuzzListCommand {
      }
    }
    package "Domain" {
      package "Model" {
        class FizzBuzzValue {
        }
        class FizzBuzzList {
        }
      }
      package "Type" {
        class FizzBuzzType {
        }
        class FizzBuzzType01 {
        }
        class FizzBuzzType02 {
        }
        class FizzBuzzType03 {
        }
        class FizzBuzzTypeNotDefined {
        }
      }
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType <|-- FizzBuzzTypeNotDefined
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzTypeNotDefined --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

#### テスト

アプリケーションのメイン部分は分割できました。続いてテストも分割しましょう。

    /main.rb
      |--lib/
          |
         application/
               |
               -- fizz_buzz_command.rb
               -- fizz_buzz_value_command.rb
               -- fizz_buzz_list_command.rb
         domain/
               |
               model/
                   |
                   -- fizz_buzz_value.rb
                   -- fizz_buzz_list.rb
               type/
                   |
                   -- fizz_buzz_type.rb
                   -- fizz_buzz_type_01.rb
                   -- fizz_buzz_type_02.rb
                   -- fizz_buzz_type_03.rb
           -- fizz_buzz.rb
      |--test/
          |
           -- fizz_buzz_test.rb

    /main.rb
      |--lib/
          |
         application/
               |
               -- fizz_buzz_command.rb
               -- fizz_buzz_value_command.rb
               -- fizz_buzz_list_command.rb
         domain/
               |
               model/
                   |
                   -- fizz_buzz_value.rb
                   -- fizz_buzz_list.rb
               type/
                   |
                   -- fizz_buzz_type.rb
                   -- fizz_buzz_type_01.rb
                   -- fizz_buzz_type_02.rb
                   -- fizz_buzz_type_03.rb
           -- fizz_buzz.rb
      |--test/
          |
          application/
               |
               -- fizz_buzz_value_command_test.rb
               -- fizz_buzz_list_command_test.rb
          domain/
               |
               model/
                     |
                     -- fizz_buzz_value_test.rb
                     -- fizz_buzz_list_test.rb
          |
           -- learning_test.rb

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzValueCommandTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType01.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列Fizzを返す
          assert_equal 'Fizz', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列Buzzを返す
          assert_equal 'Buzz', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType02.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列15を返す
          assert_equal '15', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType03.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'それ以外のタイプの場合' do
      def test_未定義のタイプを返す
        fizzbuzz = FizzBuzzType.create(4)

        assert_equal '未定義', fizzbuzz.to_s
      end

      def test_空の文字列を返す
        type = FizzBuzzType.create(4)
        command = FizzBuzzValueCommand.new(type)

        assert_equal '', command.execute(3)
      end
    end
  end

  describe '例外ケース' do
    def test_値は正の値のみ許可する
      e = assert_raises RuntimeError do
        FizzBuzzValueCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(-1)
      end

      assert_equal '正の値のみ有効です', e.message
    end
  end
end
```

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzListCommandTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzzListCommand.new(FizzBuzzType01.new)
          @result = fizzbuzz.execute(100)
        end

        def test_配列の初めは文字列の1を返す
          assert_equal '1', @result.first.value
        end

        def test_配列の最後は文字列のBuzzを返す
          assert_equal 'Buzz', @result.last.value
        end

        def test_配列の2番目は文字列のFizzを返す
          assert_equal 'Fizz', @result[2].value
        end

        def test_配列の4番目は文字列のBuzzを返す
          assert_equal 'Buzz', @result[4].value
        end

        def test_配列の14番目は文字列のFizzBuzzを返す
          assert_equal 'FizzBuzz', @result[14].value
        end
      end
    end
  end

  describe '例外ケース' do
    def test_100より多い数を許可しない
      e = assert_raises RuntimeError do
        FizzBuzzListCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(101)
      end

      assert_equal '上限は100件までです', e.message
    end
  end
end
```

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzValueTest < Minitest::Test
  def test_同じで値である
    value1 = FizzBuzzValue.new(1, '1')
    value2 = FizzBuzzValue.new(1, '1')

    assert value1.eql?(value2)
  end

  def test_to_stringメソッド
    value = FizzBuzzValue.new(3, 'Fizz')

    assert_equal '3:Fizz', value.to_s
  end
end
```

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzListTest < Minitest::Test
  def test_新しいインスタンスが作られる
    command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
    array = command.execute(50)
    list1 = FizzBuzzList.new(array)
    list2 = list1.add(array)

    assert_equal 50, list1.value.count
    assert_equal 100, list2.value.count
  end
end
```

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

class LearningTest < Minitest::Test
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

ファイル分割でテストは壊れていないようですが警告がたくさん出てきました。

``` bash
...
test/learning_test.rb:70:14: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_ブロック内の条件式が真である間までの要素を返す
             ^^^^^^^^^^^^^^^^^^^^^^^
test/learning_test.rb:75:9: C: Naming/MethodName: Use snake_case for method names.
    def test_ブロック内の条件式が真である以降の要素を返す
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
test/learning_test.rb:75:14: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_ブロック内の条件式が真である以降の要素を返す
             ^^^^^^^^^^^^^^^^^^^^^^
test/learning_test.rb:80:9: C: Naming/MethodName: Use snake_case for method names.
    def test_injectメソッドで畳み込み演算を行う
        ^^^^^^^^^^^^^^^^^^^^^^^^^
test/learning_test.rb:80:20: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_injectメソッドで畳み込み演算を行う
                   ^^^^^^^^^^^^^^
test/learning_test.rb:85:9: C: Naming/MethodName: Use snake_case for method names.
    def test_reduceメソッドで畳み込み演算を行う
        ^^^^^^^^^^^^^^^^^^^^^^^^^
test/learning_test.rb:85:20: C: Naming/AsciiIdentifiers: Use only ascii symbols in identifiers.
    def test_reduceメソッドで畳み込み演算を行う
                   ^^^^^^^^^^^^^^
 15/15 files |======================= 100 ========================>| Time: 00:00:00

15 files inspected, 87 offenses detected
...
```

これらはテストコードに関する警告がほとんどなので `.rubocop.yml` を編集してチェック対象から外しておきましょう。

``` yml
inherit_from: .rubocop_todo.yml

Naming/AsciiIdentifiers:
  Exclude:
    - 'test/**/*'

Naming/MethodName:
  EnforcedStyle: snake_case
  Exclude:
    - 'test/**/*'

Metrics/BlockLength:
  Max: 62
  Exclude:
    - 'test/**/*'

Documentation:
  Enabled: false
```

``` bash
...
08:21:55 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 144 / 215 LOC (66.98%) covered.
Started with run options --guard --seed 55977

  70/70: [=====================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01518s
70 tests, 79 assertions, 0 failures, 0 errors, 0 skips

08:21:56 - INFO - Inspecting Ruby code style of all files
/workspace/tdd_rb/.rubocop.yml: Warning: no department given for Documentation.
 22/22 files |======================= 100 ========================>| Time: 00:00:00

22 files inspected, no offenses detected
08:21:58 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/border.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/loading_background.png
/workspace/tdd_rb/.rubocop.yml: Warning: no department given for Documentation.
 0/0 files |======================== 100 =========================>| Time: 00:00:00

0 files inspected, no offenses detected
...
```

警告は消えました、仕上げに `fizz_buzz_test.rb` ファイルを削除します。

``` bash
...
08:24:12 - INFO - Running: all tests
Coverage report generated for MiniTest, Unit Tests to /workspace/tdd_rb/coverage. 135 / 201 LOC (67.16%) covered.
Started with run options --guard --seed 40104

  32/32: [=====================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00601s
32 tests, 36 assertions, 0 failures, 0 errors, 0 skips

08:24:13 - INFO - Inspecting Ruby code style of all files
/workspace/tdd_rb/.rubocop.yml: Warning: no department given for Documentation.
 21/21 files |======================= 100 ========================>| Time: 00:00:00

21 files inspected, no offenses detected
08:24:14 - INFO - Inspecting Ruby code style: coverage/assets/0.10.2/colorbox/controls.png coverage/assets/0.10.2/colorbox/border.png coverage/assets/0.10.2/colorbox/loading.gif coverage/assets/0.10.2/colorbox/loading_background.png
/workspace/tdd_rb/.rubocop.yml: Warning: no department given for Documentation.
 0/0 files |======================== 100 =========================>| Time: 00:00:00

0 files inspected, no offenses detected
...
```

テストの分割も完了したのでコミットしておきます。

``` bash
$ git add .
$ git commit -m 'refactor(WIP): モジュール分割'
```

#### エントリーポイント

仕上げはクラスモジュールのエントリーポイント作成とテストヘルパーの追加です。

    /main.rb
      |--lib/
          |
         application/
               |
               -- fizz_buzz_command.rb
               -- fizz_buzz_value_command.rb
               -- fizz_buzz_list_command.rb
         domain/
               |
               model/
                   |
                   -- fizz_buzz_value.rb
                   -- fizz_buzz_list.rb
               type/
                   |
                   -- fizz_buzz_type.rb
                   -- fizz_buzz_type_01.rb
                   -- fizz_buzz_type_02.rb
                   -- fizz_buzz_type_03.rb
           -- fizz_buzz.rb
      |--test/
          |
          application/
               |
               -- fizz_buzz_value_command_test.rb
               -- fizz_buzz_list_command._test.rb
          domain/
               |
               model/
                     |
                     -- fizz_buzz_value_test.rb
                     -- fizz_buzz_list_test.rb
          |
           -- learning_test.rb

    /main.rb
      |--lib/
          |
         application/
               |
               -- fizz_buzz_command.rb
               -- fizz_buzz_value_command.rb
               -- fizz_buzz_list_command.rb
         domain/
               |
               model/
                   |
                   -- fizz_buzz_value.rb
                   -- fizz_buzz_list.rb
               type/
                   |
                   -- fizz_buzz_type.rb
                   -- fizz_buzz_type_01.rb
                   -- fizz_buzz_type_02.rb
                   -- fizz_buzz_type_03.rb
           -- fizz_buzz.rb
      |--test/
          |
          application/
               |
               -- fizz_buzz_value_command_test.rb
               -- fizz_buzz_list_command._test.rb
          domain/
               |
               model/
                     |
                     -- fizz_buzz_value_test.rb
                     -- fizz_buzz_list_test.rb
          |
           -- learning_test.rb
           -- test_helper.rb

`fizz_buzz.rb` ファイルの内容をクラスモジュール読み込みに変更します。

``` ruby
require './lib/application/fizz_buzz_command.rb'
require './lib/application/fizz_buzz_value_command.rb'
require './lib/application/fizz_buzz_list_command.rb'
require './lib/domain/model/fizz_buzz_value.rb'
require './lib/domain/model/fizz_buzz_list.rb'
require './lib/domain/type/fizz_buzz_type.rb'
require './lib/domain/type/fizz_buzz_type_01.rb'
require './lib/domain/type/fizz_buzz_type_02.rb'
require './lib/domain/type/fizz_buzz_type_03.rb'
require './lib/domain/type/fizz_buzz_type_not_defined.rb'
```

``` bash
...
08:34:32 - INFO - Running: all tests
Coverage report generated for MiniTest to /workspace/tdd_rb/coverage. 119 / 211 LOC (56.4%) covered.
Started with run options --guard --seed 18696

  32/32: [=====================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00561s
32 tests, 36 assertions, 0 failures, 0 errors, 0 skips
....
```

コードカバレッジがうまく機能していないようなので、`test_helper.rb` を追加して共通部分を各テストファイルから読み込むように変更します。

``` ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
```

``` ruby
require 'simplecov'
SimpleCov.start
require 'minitest/reporters'
Minitest::Reporters.use!
require 'minitest/autorun'
require './lib/fizz_buzz'

...
```

``` ruby
require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

...
```

テストタスクを実行したところ動作しなくなりました。

``` bash
$ rake test
```

テスト対象をテストディレクトリ内のすべてのテストコードに変更します。

``` ruby
...
Rake::TestTask.new do |test|
  test.test_files = Dir['./test/fizz_buzz_test.rb']
  test.verbose = true
end
...
```

``` ruby
...
Rake::TestTask.new do |test|
  test.test_files = Dir['./test/**/*_test.rb']
  test.verbose = true
end
...
```

``` bash
$ rake test
Started with run options --seed 46929

  32/32: [=====================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.00800s
32 tests, 36 assertions, 0 failures, 0 errors, 0 skips
```

テストも壊れていないし警告も出ていません。モジュール分割完了です。

``` bash
$ git add .
$ git commit -m 'refactor: モジュール分割'
```

    package "lib" {
      package "Application" {
        class FizzBuzzCommand {
        }
        class FizzBuzzValueCommand {
        }
        class FizzBuzzListCommand {
        }
      }
      package "Domain" {
        package "Model" {
          class FizzBuzzValue {
          }
          class FizzBuzzList {
          }
        }
        package "Type" {
          class FizzBuzzType {
          }
          class FizzBuzzType01 {
          }
          class FizzBuzzType02 {
          }
          class FizzBuzzType03 {
          }
          class FizzBuzzTypeNotDefined {
          }
        }
      }
    }
    package "test" {
      class FizzBuzzValueCommandTest {
      }
      class FizzBuzzListCommandTest {
      }
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType <|-- FizzBuzzTypeNotDefined
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzTypeNotDefined --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

### ふりかえり

今回、 **オブジェクト指向プログラム** から **オブジェクト指向設計** そして **モジュール分割** を **テスト駆動開発**を通じて実践しました。各トピックを振り返ってみましょう。

#### オブジェクト指向プログラム

エピソード1で作成したプログラムの追加仕様を **テスト駆動開発** で実装しました。 次に **手続き型コード** との比較から **オブジェクト指向プログラム** を構成する **カプセル化** **ポリモフィズム** **継承** という概念をコードベースの **リファクタリング** を通じて解説しました。

具体的には **フィールドのカプセル** から **setterの削除** を適用することにより **カプセル化** を実現しました。続いて、 **ポリモーフィズムによる条件記述の置き換え** から **State/Strategyによるタイプコードの置き換え** を適用することにより **ポリモーフィズム** の効果を体験しました。そして、 **スーパークラスの抽出** から **メソッド名の変更** **メソッドの移動** の適用を通して **継承** の使い方を体験しました。さらに **値オブジェクト** と **ファーストクラス** というオブジェクト指向プログラミングに必要なツールの使い方も学習しました。

#### オブジェクト指向設計

次に設計の観点から **単一責任の原則** に違反している `FizzBuzz` クラスを **デザインパターン** の1つである **Commandパターン** を使ったリファクタリングである **メソッドオブジェクトによるメソッドの置き換え** を適用してクラスの責務を分割しました。オブジェクト指向設計のイデオムである **デザインパターン** として **Commandパターン** 以外に **Value Objectパターン** **Factory Methodパターン** **Strategyパターン** を **リファクタリング** を適用する過程ですでに実現していたことを説明しました。そして、**オープン・クローズドの原則** を満たすコードに **リファクタリング** されたことで既存のコードを変更することなく振る舞いを変更できるようになりました。

加えて、正常系の設計を改善した後 **アサーションの導入** **例外によるエラーコードの置き換え** といった例外系の **リファクタリング** を適用しました。最後に **ポリモーフィズム** の応用として **特殊ケースの導入** の適用による **Null Objectパターン** を使った **オープン・クローズドの原則** に従った安全なコードの追加方法を解説しました。

#### モジュールの分割

仕上げに、**モノリシック** なファイルから個別のクラスモジュールへの分割を **ドメインオブジェクト** の抽出を通して **ドメインモデル** へと整理することにより **モジュール分割** を実現しました。最終的にプログラムからアプリケーションへと体裁を整えることが出来ました。以下が最終的なモジュール構造とコードです。

    package "lib" {
      package "Application" {
        class FizzBuzzCommand {
        }
        class FizzBuzzValueCommand {
        }
        class FizzBuzzListCommand {
        }
      }
      package "Domain" {
        package "Model" {
          class FizzBuzzValue {
          }
          class FizzBuzzList {
          }
        }
        package "Type" {
          class FizzBuzzType {
          }
          class FizzBuzzType01 {
          }
          class FizzBuzzType02 {
          }
          class FizzBuzzType03 {
          }
          class FizzBuzzTypeNotDefined {
          }
        }
      }
    }
    package "test" {
      class FizzBuzzValueCommandTest {
      }
      class FizzBuzzListCommandTest {
      }
    }
    FizzBuzzType <|-- FizzBuzzType01
    FizzBuzzType <|-- FizzBuzzType02
    FizzBuzzType <|-- FizzBuzzType03
    FizzBuzzType <|-- FizzBuzzTypeNotDefined
    FizzBuzzType01 --> FizzBuzzValue
    FizzBuzzType02 --> FizzBuzzValue
    FizzBuzzType03 --> FizzBuzzValue
    FizzBuzzTypeNotDefined --> FizzBuzzValue
    FizzBuzzList *- FizzBuzzValue
    FizzBuzzCommand <|-- FizzBuzzValueCommand
    FizzBuzzCommand <|-- FizzBuzzListCommand
    FizzBuzzListCommand --> FizzBuzzList
    FizzBuzzCommand *- FizzBuzzType

  - Application

**/main.rb.**

``` ruby
# frozen_string_literal: true

require './lib/fizz_buzz.rb'

command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
command.execute(100).each { |i| puts i.value }
```

**/lib/application/fizz\_buzz\_command.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzCommand
  def execute; end
end
```

**/lib/application/fizz\_buzz\_value\_command.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzValueCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    @type.generate(number).value
  end
end
```

**/lib/application/fizz\_buzz\_list\_command.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzListCommand < FizzBuzzCommand
  def initialize(type)
    @type = type
  end

  def execute(number)
    FizzBuzzList.new((1..number).map { |i| @type.generate(i) }).value
  end
end
```

  - Domain

**/lib/domain/model/fizz\_buzz\_value.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzValue
  attr_reader :number, :value

  def initialize(number, value)
    raise '正の値のみ有効です' if number.negative?

    @number = number
    @value = value
  end

  def to_s
    "#{@number}:#{@value}"
  end

  def ==(other)
    @number == other.number && @value == other.value
  end

  alias eql? ==
end
```

**/lib/domain/model/fizz\_buzz\_list.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzList
  MAX_COUNT = 100
  attr_reader :value

  def initialize(list)
    raise "上限は#{MAX_COUNT}件までです" if list.count > MAX_COUNT

    @value = list
  end

  def to_s
    @value.to_s
  end

  def add(value)
    FizzBuzzList.new(@value + value)
  end
end
```

**/lib/domain/type/fizz\_buzz\_type.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzType
  TYPE_01 = 1
  TYPE_02 = 2
  TYPE_03 = 3

  def self.create(type)
    case type
    when FizzBuzzType::TYPE_01
      FizzBuzzType01.new
    when FizzBuzzType::TYPE_02
      FizzBuzzType02.new
    when FizzBuzzType::TYPE_03
      FizzBuzzType03.new
    else
      FizzBuzzTypeNotDefined.new
    end
  end

  def fizz?(number)
    number.modulo(3).zero?
  end

  def buzz?(number)
    number.modulo(5).zero?
  end
end
```

**/lib/domain/type/fizz\_buzz\_type\_01.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzType01 < FizzBuzzType
  def generate(number)
    return FizzBuzzValue.new(number, 'FizzBuzz') if fizz?(number) && buzz?(number)
    return FizzBuzzValue.new(number, 'Fizz') if fizz?(number)
    return FizzBuzzValue.new(number, 'Buzz') if buzz?(number)

    FizzBuzzValue.new(number, number.to_s)
  end
end
```

**/lib/domain/type/fizz\_buzz\_type\_02.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzType02 < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, number.to_s)
  end
end
```

**/lib/domain/type/fizz\_buzz\_type\_03.rb.**

``` ruby
# frozen_string_literal: true

class FizzBuzzType03 < FizzBuzzType
  def generate(number)
    return FizzBuzzValue.new(number, 'FizzBuzz') if fizz?(number) && buzz?(number)

    FizzBuzzValue.new(number, number.to_s)
  end
end
```

**/lib/domain/type/fizz\_buzz\_type\_not\_defined.b.**

``` ruby
# frozen_string_literal: true

class FizzBuzzTypeNotDefined < FizzBuzzType
  def generate(number)
    FizzBuzzValue.new(number, '')
  end

  def to_s
    '未定義'
  end
end
```

  - Test

**/test/application/fizz\_buzz\_value\_command\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzValueCommandTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType01.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列Fizzを返す
          assert_equal 'Fizz', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列Buzzを返す
          assert_equal 'Buzz', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'タイプ2の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType02.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列15を返す
          assert_equal '15', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'タイプ3の場合' do
      def setup
        @fizzbuzz = FizzBuzzValueCommand.new(FizzBuzzType03.new)
      end

      describe '三の倍数の場合' do
        def test_3を渡したら文字列3を返す
          assert_equal '3', @fizzbuzz.execute(3)
        end
      end

      describe '五の倍数の場合' do
        def test_5を渡したら文字列5を返す
          assert_equal '5', @fizzbuzz.execute(5)
        end
      end

      describe '三と五の倍数の場合' do
        def test_15を渡したら文字列FizzBuzzを返す
          assert_equal 'FizzBuzz', @fizzbuzz.execute(15)
        end
      end

      describe 'その他の場合' do
        def test_1を渡したら文字列1を返す
          assert_equal '1', @fizzbuzz.execute(1)
        end
      end
    end

    describe 'それ以外のタイプの場合' do
      def test_未定義のタイプを返す
        fizzbuzz = FizzBuzzType.create(4)

        assert_equal '未定義', fizzbuzz.to_s
      end

      def test_空の文字列を返す
        type = FizzBuzzType.create(4)
        command = FizzBuzzValueCommand.new(type)

        assert_equal '', command.execute(3)
      end
    end
  end

  describe '例外ケース' do
    def test_値は正の値のみ許可する
      e = assert_raises RuntimeError do
        FizzBuzzValueCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(-1)
      end

      assert_equal '正の値のみ有効です', e.message
    end
  end
end
```

**/test/application/fizz\_buzz\_list\_command\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzListCommandTest < Minitest::Test
  describe '数を文字列にして返す' do
    describe 'タイプ1の場合' do
      describe '1から100までのFizzBuzzの配列を返す' do
        def setup
          fizzbuzz = FizzBuzzListCommand.new(FizzBuzzType01.new)
          @result = fizzbuzz.execute(100)
        end

        def test_配列の初めは文字列の1を返す
          assert_equal '1', @result.first.value
        end

        def test_配列の最後は文字列のBuzzを返す
          assert_equal 'Buzz', @result.last.value
        end

        def test_配列の2番目は文字列のFizzを返す
          assert_equal 'Fizz', @result[2].value
        end

        def test_配列の4番目は文字列のBuzzを返す
          assert_equal 'Buzz', @result[4].value
        end

        def test_配列の14番目は文字列のFizzBuzzを返す
          assert_equal 'FizzBuzz', @result[14].value
        end
      end
    end
  end

  describe '例外ケース' do
    def test_100より多い数を許可しない
      e = assert_raises RuntimeError do
        FizzBuzzListCommand.new(
          FizzBuzzType.create(FizzBuzzType::TYPE_01)
        ).execute(101)
      end

      assert_equal '上限は100件までです', e.message
    end
  end
end
```

**/test/domain/model/fizz\_buzz\_value\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzValueTest < Minitest::Test
  def test_同じで値である
    value1 = FizzBuzzValue.new(1, '1')
    value2 = FizzBuzzValue.new(1, '1')

    assert value1.eql?(value2)
  end

  def test_to_stringメソッド
    value = FizzBuzzValue.new(3, 'Fizz')

    assert_equal '3:Fizz', value.to_s
  end
end
```

**/test/domain/model/fizz\_buzz\_list\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class FizzBuzzListTest < Minitest::Test
  def test_新しいインスタンスが作られる
    command = FizzBuzzListCommand.new(FizzBuzzType.create(FizzBuzzType::TYPE_01))
    array = command.execute(50)
    list1 = FizzBuzzList.new(array)
    list2 = list1.add(array)

    assert_equal 50, list1.value.count
    assert_equal 100, list2.value.count
  end
end
```

**/test/learning\_test.rb.**

``` ruby
# frozen_string_literal: true

require './test/test_helper'
require 'minitest/autorun'
require './lib/fizz_buzz'

class LearningTest < Minitest::Test
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

#### 良い設計

エピソード1では **良いコード** について考えました。

> TDDは「より良いコードを書けば、よりうまくいく」という素朴で奇妙な仮設によって成り立っている
>
> —  テスト駆動開発
>

> 「動作するきれいなコード」。RonJeffriesのこの簡潔な言葉が、テスト駆動開発(TDD)のゴールだ。動作するきれいなコードはあらゆる意味で価値がある。
>
> —  テスト駆動開発

> 良いコードかどうかは、変更がどれだけ容易なのかで決まる。
>
> —  リファクタリング(第2版)

> コードは理解しやすくなければいけない。
>
> —  リーダブルコード

本エピソードでは **テスト駆動開発** による **オブジェクト指向プログラミング** の **リファクタリング** を経てコードベースを改善してきました。そして **オブジェクト指向設計** により **良いコード** のプログラムを **良い設計** のアプリケーションへと進化させることができました。

> どこに何が書いてあるかをわかりやすくし、変更の影響を狭い範囲に閉じ込め、安定して動作する部品を柔軟に組み合わせながらソフトウェアを構築する技法がオブジェクト指向設計です。
>
> —  現場で役立つシステム設計の原則
>

> 設計の良し悪しは、ソフトウェアを変更するときにはっきりします。
>
> 構造が入り組んだわかりづらいプログラムは内容の理解に時間がかかります。重複したコードをあちこちで修正する作業が増え、変更の副作用に悩まされます。
>
> 一方、うまく設計されたプログラムは変更が楽で安全です。変更すべき箇所がかんたんにわかり、変更するコード量が少なく、変更の影響を狭い範囲に限定できます。
>
> プログラムの修正に３日かかるか、それとも半日で済むか。その違いを生むのが「設計」なのです。
>
> —  現場で役立つシステム設計の原則

では、いつ設計をしていたのでしょうか？ わかりますよね、このエピソードの始まりから終わりまで常に設計をしていたのです。

> TDDは分析技法であり、設計技法であり、実際には開発のすべてのアクティビティを構造化する技法なのだ。
>
> - テスト駆動開発

# エピソード4

## クライアント開発から始めるテスト駆動開発

### APIサービスを作る

### APIサービスと連携する

### UIを作る

### UIとAPIサービスを連携する

# エピソード5

## 継続的インテグレーションから始めるテスト駆動開発

### E2Eテストのセットアップ

### クライアントモジュールの分割

### 本番環境と開発環境で表示を切り返る

### クライアントタスクの自動化

### コードレビュー

# エピソードx

## パフォーマンスチューニングから始めるテスト駆動開発

### 概要

[フィボナッチ数](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0) を計算するプログラムを **テスト駆動開発** で作ります。

初めに **TODOリスト** をプログラミング作業をリストアップします。次に、最初に失敗するテストを作成します。 その後 **仮実装**でベタ書き値を返すテストを実行します。 それから **三角測量** を使って慎重にアルゴリズムを一般化していきます。そして、 **明白な実装** によりアルゴリズムを完成させます。

アルゴリズムが完成したら **リファクタリング** を実施してコードベースを **動作するきれいなコード** に洗練していきます。

**動作するきれいなコード** になったらパフォーマンスの検証をするためパフォーマンスチューニングを実施します。 パフォーマンスチューニングでは **プロファイラ** を使ったプログラムのボトルネック調査を実施します。アルゴリズムのパフォーマンスを改善したら別途追加したアルゴリズムと **ベンチマーク** を実施してどのアルゴリズムを採用するかを決定します。

仕上げは、 **モジュール分割** によりRubyアプリケーションとしてリリースします。

### 仕様

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
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  | 8  | 9  | 10 | 11 | 12  | 13  | 14  | 15  | 16  | 18   | 19   | …​ |
| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | …​ |

### TODOリスト

> TODOリスト
>
> 何をテストすべきだろうか----着手する前に、必要になりそうなテストをリストに書き出しておこう。
>
> —  テスト駆動開発

**TODOリスト** を書き出す取っ掛かりとして仕様で定義されている内容からプログラムで実施できる内容に分解してきましょう。仕様では以下のように定義されているので。

|   |   |   |   |   |   |   |    |    |    |    |    |     |     |     |     |     |      |      |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  | 8  | 9  | 10 | 11 | 12  | 13  | 14  | 15  | 16  | 18   | 19   | …​ |
| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | …​ |

最初のタスクは `0を渡したら0を返す` 振る舞いをするプログラムを作ることにしましょう。

|   |    |
| --- | --- |
| 0 | …​ |
| 0 | …​ |

同様のパターンで他のタスクも切り出してみましょう。

|   |   |    |
| --- | --- | --- |
| 0 | 1 | …​ |
| 0 | 1 | …​ |

|   |   |   |    |
| --- | --- | --- | --- |
| 0 | 1 | 2 | …​ |
| 0 | 1 | 1 | …​ |

とりあえず、３件ほどタスクとして切り出したので **TODOリスト** の作成は一旦終了してプログラミング作業に入るとしましょう。

  - 0を渡したら0を返す

  - 1を渡したら1を返す

  - 2を渡したら1を返す

### 仮実装

> 仮実装を経て本実装へ
>
> 失敗するテストを書いてから、最初に行う実装はどのようなものだろうか----ベタ書きの値を返そう。
>
> —  テスト駆動開発

#### 0を渡したら0を返す

早速、 **TODOリスト**
の１つ目から片付けていくとしましょう。

  - **0を渡したら0を返す**

  - 1を渡したら1を返す

  - 2を渡したら1を返す

まずは最初に失敗するテストを書きますがまずは以下のサンプルコードを使ってテスティングフレームワークの動作確認をしておきましょう。今回利用するRubyのテスティングフレームワークは [minitest](https://github.com/seattlerb/minitest) です。 `test` フォルダ以下に `fibonacci_test.rb` ファイルを追加して以下のコードを入力します。

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

gemインストールが完了したらコマンドラインに `ruby test/fibonacci_test.rb` コマンドを入力してテストを実施します。

``` bash
$ ruby test/fibonacci_test.rb
Started with run options --seed 28548

  1/1: [==========================================================] 100% Time: 00:00:00, Time: 00:00:00

Finished in 0.01040s
1 tests, 1 assertions, 0 failures, 0 errors, 0 skips
...
```

テストは無事実行されたようですね。続いてテストが失敗するか確認しておきましょう。 `greeting` メソッドの `hello world` を `hello world!` に変更してテストを実行します。

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

テスティングフレームワークのセットアップと動作確認が終了したので最初の失敗するテストを書きます。まずは **アサーションファースト**　でサンプルコードを削除して以下のコードにします。

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

  - ~~0を渡したら0を返す~~

  - 1を渡したら1を返す

  - 2を渡したら1を返す

### 三角測量

> 三角測量
>
> テストから最も慎重に一般化を引き出すやり方はどのようなものだろうか----２つ以上の例があるときだけ、一般化を行うようにしよう。
>
> —  テスト駆動開発

#### 1を渡したら1を返す

１つ目の **TODOリスト** を片付けたので２つ目の **TODOリスト** に取り掛かるとしましょう。

  - ~~0を渡したら0を返す~~

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

#### リファクタリング

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - 2を渡したら1を返す

次の **TODOリスト** に着手する前にテストケース内の重複が気になり始めたので、共通部分をアサーションからくくり出して、入力値と期待値の組でテストを回すようにテストコードを **リファクタリング** します。

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

#### 1を渡したら2を返す

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - **2を渡したら1を返す**

テストコードの　**リファクタリング** を実施したので続いて　**TODOリスト** の３つ目に着手します。まずは **アサーション** の追加ですね。

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

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - ~~2を渡したら1を返す~~

### 明白な実装

> 明白な実装
>
> シンプルな操作を実現するにはどうすればいいだろうか----そのまま実装しよう。
>
> 仮実装や三角測量は、細かく細かく刻んだ小さなステップだ。だが、ときには実装をどうすべきか既に見えていることが。
> そのまま進もう。例えば先ほどのplusメソッドくらいシンプルなものを仮実装する必要が本当にあるだろうか。
> 普通は、その必要はない。頭に浮かんだ明白な実装をただ単にコードに落とすだけだ。もしもレッドバーが出て驚いたら、あらためてもう少し歩幅を小さくしよう。
>
> —  テスト駆動開発

#### 3を渡したら2を返す

最初に定義した **TODOリスト** の内容は完了しましたがプログラムの一般化にはまだテストケースが足りないでしょう。3を渡した場合のテストケースを追加します。

|   |   |   |   |    |
| --- | --- | ----| --- | --- |
| 0 | 1 | 2 | 3 | …​ |
| 0 | 1 | 1 | 2 | …​ |

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - ~~2を渡したら1を返す~~

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

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - ~~2を渡したら1を返す~~

  - ~~3を渡したら2を返す~~

#### フィボナッチ数計算

そろそろゴールが見えてきました。**TODOリスト** を追加してフィボナッチ数計算アルゴリズムを完成させましょう。

|   |   |   |   |   |    |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | …​ |
| 0 | 1 | 1 | 2 | 3 | …​ |

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - ~~2を渡したら1を返す~~

  - ~~3を渡したら2を返す~~

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

ここでコミット...しないで今回は更に進めます。 **TODOリスト** を追加します。

|   |   |   |   |   |   |    |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | …​ |
| 0 | 1 | 1 | 2 | 3 | 5 | …​ |

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - ~~2を渡したら1を返す~~

  - ~~3を渡したら2を返す~~

  - ~~4を渡したら3を返す~~

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

  - ~~0を渡したら0を返す~~

  - ~~1を渡したら1を返す~~

  - ~~2を渡したら1を返す~~

  - ~~3を渡したら2を返す~~

  - ~~4を渡したら3を返す~~

  - ~~5を渡したら5を返す~~

### リファクタリング

> リファクタリング(名詞) 外部から見たときの振る舞いを保ちつつ、理解や修正が簡単になるように、ソフトウェアの内部構造を変化させること。
>
> —  リファクタリング(第2版)

> リファクタリングする(動詞) 一連のリファクタリングを適用して、外部から見た振る舞いの変更なしに、ソフトウェアを再構築すること。
>
> —  リファクタリング(第2版

アルゴリズムの実装は出来ましたがアプリケーションとしては不十分なので **リファクタリング** を適用してコードを **動作するきれいなコード** に洗練していきます。

#### クラスの抽出

まず、テストケース内でメソッドを定義していますがこれでは一つのクラスでアルゴリズムの実行とテストの実行という２つの責務を `FibonacciTest` クラスが担当しています。 **単一責任の原則** に違反しているので **クラスの抽出** を実施して責務を分担させましょう。

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

テストが壊れていないことを確認したら `FibonacciTest` クラス内の **クラスメソッド** `FIbonacciTest.fib` を削除して **フィクスチャー** `setup` メソッドを作成して **インスタンス変数** `@fib` に `Fibonacci` クラスの参照を代入します。

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

#### 変数名の変更

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

#### メソッド名の変更

`Fibonacci` クラスの **クラスメソッド** `Fibonacci.fib` はフィボナッチ数を計算するメソッドですが名前が紛らわしいので **メソッド名の変更** を適用します。

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

**インスタンスメソッド** を `fib` から `calc` に変更します。今回は呼び出し先の `FibonacciTest` のテストコードも修正する必要があります。

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

### パフォーマンスチューニング

> 心がけるべきことは、他のパフォーマンス分析とおなじように、実際のデータを使い、リアルな利用パターンを試し、プロファイリングを行ってからでないと、パフォーマンスを問題にする資格はない、ということだ。
>
> —  テスト駆動開発

これまでのテストケースでは小さな値を使ってきましたが大きな値の場合のプログラムの挙動が問題無いか確認しておく必要があります [１００番目までのフィボナッチ数列](http://www.suguru.jp/Fibonacci/Fib100.html) を参考に大きな値の場合のテストケースを追加してアプリケーションのパフォーマンスを検証しましょう。

#### メモ化によるパフォーマンス改善

**TODOリスト** に新しいタスクを追加します。

|   |   |    |          |          |           |    |
| --- | --- | --- | --- | --- | --- | --- |
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

テストが完了するのが随分遅くなってしまいました。これはアルゴリズムを改善する必要がありそうです。 まずは **プロファイラ** を使って実行状況を確認します。今回は [profileライブラリ](https://docs.ruby-lang.org/ja/latest/library/profile.html) を使います。

``` bash
$ ruby -r profile test/fibonacci_test.rb
Started with run options --seed 42383

  2/1: [======================                      ] 50% Time: 00:00:00,  ETA: 00:00:00
```

処理が終わらないようなら `ctr-c` で強制終了すれば結果が出力されます。出力内容の `Fibonacci.calc` がフィボナッチ数計算メソッド実行部分です。

``` bash
...
  %   cumulative   self              self     total
 time   seconds   seconds    calls  ms/call  ms/call  name
192.39    25.50     25.50        2 12750.69 12750.69  Thread::Queue#pop
 75.32    35.49      9.98   246940     0.04     1.65  Fibonacci.calc
....
```

再帰呼び出しが何度も実行された結果パフォーマンスを低下させているようです。ここは [メモ化](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%A2%E5%8C%96) を使ってパフォーマンスを改善させましょう。

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

### ベンチマーク

続いて、異なるフィボナッチ数計算アルゴリズムを実装してどのアルゴリズムを採用するべきかを [ベンチマーク](https://ja.wikipedia.org/wiki/%E3%83%99%E3%83%B3%E3%83%81%E3%83%9E%E3%83%BC%E3%82%AF) を取って判断したいと思います。

#### ループ処理による実装

まずはループ処理によるフィボナッチ数計算のアルゴリズムを実装します。以下が **テストファースト** **アサートファースト** で作成したコードです。

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

#### 一般項による実装

[フィボナッチ数列の一般項](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0#%E4%B8%80%E8%88%AC%E9%A0%85) で定義されているのでこれを **テストファースト** **アサートファースト** で実装します。

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

#### メソッド名の変更

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

まず、最初に実装した再帰呼び出しアルゴリズムのメソッド名を `Fibonacci.calc` から `Fibonacci.recursive` に変更します。

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

最後に、一般項アルゴリズムのメソッド名を `Fibonacci.calc3` から `Fibonacci.general_term` に変更します。

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

#### サブクラスによるタイプコードの置き換え 1

現在の `Fibonacci` クラスはアルゴリズムを追加する場合クラスを編集する必要があります。その際に既存のアルゴリズムを壊してしまう可能性があります。これは **オープン・クローズド原則** に違反しているので **サブクラスによるタイプコードの置き換え** を適用してアルゴリズムを **カプセル化** して、安全に追加・変更できる設計に **リファクタリング** します。

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

まず、**クラスの抽出** により再帰呼び出しアルゴリズムの **メソッドオブジェクト** `FibonacciRecursive` クラスを作成して テスト **フィクスチャー** で **インスタンス化** して **インスタンス変数** にオブジェクトの参照を代入します。ここではメソッドの呼び出しが `exec` に変更されているのでテストコードもそれに合わせて変更します。

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

#### サブクラスによるタイプコードの置き換え 2

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

#### サブクラスによるタイプコードの置き換え 3

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

#### サブクラスによるタイプコードの置き換え 4

最後に、 `Fibonacci` クラスに **Strategyパターン** を適用して各アルゴリズムの実行を **委譲** します。

[Strategy パターン](https://ja.wikipedia.org/wiki/Strategy_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)

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

#### ファイル分割

続いてテストとアプリケーションを分割します。 `lib` ディレクトリを作成して `fibonacci.rb` ファイルを追加してアプリケーションコード部分をカット＆ペーストします。

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

続いて、分割した `fibonacci.rb` ファイル内に定義されたクラスを読み込むようにテストクラスを修正します。 ファイルの読み込みには `require` を使います。

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

#### ベンチマークの実施

**ベンチマーク** を実施する準備が出来たので `test` ディレクトリに以下の `fibonacci_benchmark.rb` ファイルを追加します。

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

### モジュール分割

#### アプリケーションのリリース

**動作するきれいなコード** をリリースするにあたってクラスモジュールごとにファイル分割して **エントリーポイント** からアプリケーションを実行できるようにしたいと思います。

    /
      |--lib/
          |
           -- fibonacci.rb
      |--test/
          |
           -- fibonacci_test.rb
           -- fibonacci_benchmark.rb

まず、 `lib` に `fibonacci` フォルダを追加します。クラスモジュールは `Fibonacci` の **名前空間** で管理するようにします。

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

仕上げはコマンドラインから実行できるようにします。 ルート直下に `main.rb` を追加して以下のコードを追加します。 ここでは **ベンチマーク** で一番良い結果の出た一般項のアルゴリズムを使うことにします。

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

#### アプリケーションの構成

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

# 参照

## 参考サイト

  - [50
    分でわかるテスト駆動開発](https://channel9.msdn.com/Events/de-code/2017/DO03?ocid=player)

  - [サルでもわかるGit入門〜バージョン管理を使いこなそう〜](https://backlog.com/ja/git-tutorial/)

  - [プログラミング言語 Ruby リファレンスマニュアル](https://docs.ruby-lang.org/ja/)

  - [検索結果を要チェック！Rubyの公式リファレンスは docs.ruby-lang.org です
    〜公式な情報源を調べるクセを付けよう〜](https://qiita.com/jnchito/items/2dc760ee0716ea12bbf0)

  - [動作するきれいなコード: SeleniumConf Tokyo 2019
    基調講演文字起こし+α](https://t-wada.hatenablog.jp/entry/clean-code-that-works)

  - [RuboCop](https://github.com/rubocop-hq/rubocop)

  - [RuboCop is
    何？](https://qiita.com/tomohiii/items/1a17018b5a48b8284a8b)

  - [ruby rake の使い方](https://qiita.com/abcb2/items/9905449ab3fcf5d27ace)

  - [RuboCopのrake
    taskを使う](https://qiita.com/tbpgr/items/443fe45f0dbe02aa768a)

  - [オブジェクト指向のいろは](https://qiita.com/nrslib/items/73bf176147192c402049)

## 参考図書

# References

  - \[\] テスト駆動開発 Kent Beck (著), 和田 卓人 (翻訳): オーム社; 新訳版 (2017/10/14)

  - \[\] 新装版 リファクタリング―既存のコードを安全に改善する― (OBJECT TECHNOLOGY SERIES) Martin
    Fowler (著), 児玉 公信 (翻訳), 友野 晶夫 (翻訳), 平澤 章 (翻訳), その他: オーム社; 新装版
    (2014/7/26)

  - \[\] リファクタリング(第2版): 既存のコードを安全に改善する (OBJECT TECHNOLOGY SERIES) Martin
    Fowler (著), 児玉 公信 (翻訳), 友野 晶夫 (翻訳), 平澤 章 (翻訳), その他: オーム社; 第2版
    (2019/12/1)

  - \[\] リーダブルコード ―より良いコードを書くためのシンプルで実践的なテクニック (Theory in practice)
    Dustin Boswell (著), Trevor Foucher (著), 須藤 功平 (解説), 角 征典 (翻訳):
    オライリージャパン; 初版八刷版 (2012/6/23)

  - \[\] Clean Code　アジャイルソフトウェア達人の技 (アスキードワンゴ) Ｒｏｂｅｒｔ Ｃ．Ｍａｒｔｉｎ (著), 花井
    志生 (著) ドワンゴ (2017/12/28)

  - \[\] 現場で役立つシステム設計の原則 〜変更を楽で安全にするオブジェクト指向の実践技法 増田 亨 (著) 技術評論社
    (2017/7/5)

  - \[\] かんたん Ruby (プログラミングの教科書) すがわらまさのり (著) 技術評論社 (2018/6/21)

  - \[\] プロを目指す人のためのRuby入門 言語仕様からテスト駆動開発・デバッグ技法まで (Software Design
    plusシリーズ) 伊藤 淳一 (著): 技術評論社 (2017/11/25)

  -  The Pragmatic Programmer: your journey to mastery, 20th Anniversary Edition David Thomas (著), Andrew Hunt (著):
     Addison-Wesley Professional; 2版 (2019/7/30)