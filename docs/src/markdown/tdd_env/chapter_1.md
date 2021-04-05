# 環境構築から始めるテスト駆動開発

## 6S

環境構築をするにあたっては **5S** + セキュリティの **6S** をベースに進めていきます。まず **5S**
について、それからセキュリティについて解説します。

### 5S

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
ですがそもそもいらないものが何なのかを決めなければなりません。プログラミングで扱う対象はモノではなく情報です。ではどうやって情報を扱っていけばよいでしょう？ここは、
**分類するな。ひたすら並べよ** の考えに従い一箇所に記録をまとめていきましょう。そのためのテクニックとして
**エンジニアリングデイブックス**
があります。これは何をやったか何を学んだかをノートに時系列に記録していくことです。

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

ノートは市販のものならどれでも構いませんがおすすめは
[ソフトリングノード](https://www.kokuyo-st.co.jp/stationery/softring-note/)
のB5サイズが手元に置いてもかさばらず使いやすいです。情報を一箇所に集めて必要なものと不要なものを分ける準備が出来ました。次は必要なものをすぐに取り出せるようにする
**整頓** をどのように実践していくかを解説します。

**整頓** の基本は **分類するな。ひたすら並べよ**
です。デジタルデータも一箇所に保存していきましょう。具体的に保存する場所は後で解説します。また、分類するなといっても分類をする必要は当然発生します。分類にあたっては一貫したネーミングルールを適用していきます。具体的な方法は都度解説していきます。

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

### セキュリティ(Security)

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

### ITリテラシ

以上がプログラミング環境構築にあたっての基本となる考えです。この記事では6Sを軸としたソフトウェア開発のための **ITリテラシ**
習得のベースとなる環境構築をすることを目的としています。

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

## アカウントの登録

まず各種サービスのアカウントを登録します。ここでは以下のアカウント設定で作業を進めていきますが各自作業の際は読み替えてください。

|          |                         |
| -------- | ----------------------- |
| Microsft | <newbie4649@outlook.jp> |
| Google   | <newbie4649@gmail.com>  |
| GitHub   | newbie4649              |
| Windows  | <newbie4649@outlook.jp> |
| WSL      | newbie4649              |

また、パスワードに関しては **セキュリティ**
を参考に設定してください。アカウントIDに関しては可能な限り共通のID名を設定すると管理しやすくなります。登録アカウントとパスワードは一箇所に記録していつでも確認できるようにして置いてください。理想はパスワードマネージャーの使用ですがクラウドストレージでもいいです。他人にみられることがないように注意して管理しましょう。クラウドストレージで安全に保存する自身が無い場合は
**エンジニアリングデイブックス**
に記録しておきましょう。その際、もし落として他人にみられてもわからないような工夫をしておきましょう。手段はどうあれ
**保存する場所は一箇所**
が原則です。

### Microsoftアカウントを作成する

[アカウントの作成](https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2fja-jp%2f&id=74335&aadredir=1&contextid=E56866F842F4E143&bk=1584685585&uiflavor=web&lic=1&mkt=JA-JP&lc=1041&uaid=491fc017de0f48c5c67a3833e7aca9ee)
から新しいメールアドレスを取得を選択します。

![ms 001](../../images/asciidoc/tdd_env/ms-001.png)

![ms 002](../../images/asciidoc/tdd_env/ms-002.png)

![ms 003](../../images/asciidoc/tdd_env/ms-003.png)

![ms 004](../../images/asciidoc/tdd_env/ms-004.png)

![ms 005](../../images/asciidoc/tdd_env/ms-005.png)

![ms 006](../../images/asciidoc/tdd_env/ms-006.png)

### Googleアカウントを作成する

[Google
アカウントの作成](https://support.google.com/accounts/answer/27441?hl=ja)
から `Googleアカウントを作成する` を選択します。

![ggl 001](../../images/asciidoc/tdd_env/ggl-001.png)

![ggl 002](../../images/asciidoc/tdd_env/ggl-002.png)

![ggl 003](../../images/asciidoc/tdd_env/ggl-003.png)

### GitHubアカウントを作成する

[GitHubに登録する](https://github.co.jp/) から `GitHubに登録する` を選択します。

![ghb 001](../../images/asciidoc/tdd_env/ghb-001.png)

![ghb 002](../../images/asciidoc/tdd_env/ghb-002.png)

Freeプランを選択します

![ghb 003](../../images/asciidoc/tdd_env/ghb-003.png)

### アカウントにサインインする

[Microsoft
アカウントにサインインする方法](https://support.microsoft.com/ja-jp/help/4028195)
を参考にしてローカルアカウントからMicrosoftアカウントに切り替えます。

![login 001](../../images/asciidoc/tdd_env/login-001.png)

![login 002](../../images/asciidoc/tdd_env/login-002.png)

![login 003](../../images/asciidoc/tdd_env/login-003.png)

![login 004](../../images/asciidoc/tdd_env/login-004.png)

![login 005](../../images/asciidoc/tdd_env/login-005.png)

![login 006](../../images/asciidoc/tdd_env/login-006.png)

![login 007](../../images/asciidoc/tdd_env/login-007.png)

## クラウドストレージのセットアップ

> Keep Knowledge in Plain Text
> 
> Plain text won’t become obsolete.It helps leverage your work and
> simplifies debugging and testing.
> 
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition 

[Office365](https://products.office.com/ja-jp/home?SilentAuth=1)
からOneDriveの設定を確認します。

![drive 001](../../images/asciidoc/tdd_env/drive-001.png)

![drive 002](../../images/asciidoc/tdd_env/drive-002.png)

![drive 003](../../images/asciidoc/tdd_env/drive-003.png)

アカウントのパスワードなど機密情報は [Personal Vault で OneDrive
ファイルを保護する](https://support.office.com/ja-jp/article/personal-vault-で-onedrive-ファイルを保護する-6540ef37-e9bf-4121-a773-56f98dce78c4)
を使って管理すると良いでしょう。もしくは [1Password](https://1password.com/jp/)
などパスワード管理ツールの導入を検討してください。

[PCのOneDrive](https://support.microsoft.com/ja-jp/help/17184/windows-10-onedrive)
にあるようにデータはローカルとクラウドの両方にあるので破損・紛失をしても復旧することが出来ます。

## 開発環境のセットアップ

### パッケージ管理ツールのインストール

アプリケーションの管理にはパッケージ管理ツール [Scoop](https://scoop.sh/) を使います。インストールの詳細は
[Scoopを使ったWindows環境構築のススメ -
Super\!\!](https://qiita.com/Dooteeen/items/12dc8fb14042888113d0)
を参照してください。

スタートメニューから `Windows PowerShell` を選択します。

![pkg 001](../../images/asciidoc/tdd_env/pkg-001.png)

以下のコマンドを入力します。

``` powershell
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
```

![pkg 002](../../images/asciidoc/tdd_env/pkg-002.png)

### gitのインストール

> Always Use Version Control
> 
> Vsersion control is a time machine for your work;you can go back.
> 
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition 

スタートメニューから `Windows PowerShell` を選択します。

![pkg 001](../../images/asciidoc/tdd_env/pkg-001.png)

以下のコマンドを入力します。

``` powershell
scoop install git
```

追加パッケージをインストールします

``` poershell
scoop bucket add extras
```

![git 001](../../images/asciidoc/tdd_env/git-001.png)

### PowerShellCoreのインストール

最新バージョンのセットアッププログラムをダウンロードします

[GitHub](https://github.com/PowerShell/PowerShell/tags)

Previewでない最新バージョンを選択します。

![pwsh 001](../../images/asciidoc/tdd_env/pwsh-001.png)

![pwsh 002](../../images/asciidoc/tdd_env/pwsh-002.png)

![pwsh 003](../../images/asciidoc/tdd_env/pwsh-003.png)

ダウンロードしたセットアッププログラムを実行します。

![pwsh 004](../../images/asciidoc/tdd_env/pwsh-004.png)

![pwsh 005](../../images/asciidoc/tdd_env/pwsh-005.png)

![pwsh 006](../../images/asciidoc/tdd_env/pwsh-006.png)

![pwsh 007](../../images/asciidoc/tdd_env/pwsh-007.png)

![pwsh 008](../../images/asciidoc/tdd_env/pwsh-008.png)

### Windows Terminalのインストール

> Use the Power of Command Shells
> 
> Use the shell when graphical user interfaces don’t cut it.
> 
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition 

画面左下のスタートメニューから `Microsft Store` を選択します。

![terminal 001](../../images/asciidoc/tdd_env/terminal-001.png)

検索欄に `terminal` と入力したら表示されられる候補の中から `Windows Terminal` を選択します。

![terminal 002](../../images/asciidoc/tdd_env/terminal-002.png)

### WSLのインストール

画面左下のスタートメニューから歯車のアイコンを選択してWindowsの設定画面を表示します。

![wsl 005](../../images/asciidoc/tdd_env/wsl-005.png)

`アプリ` を選択します。

![wsl 006](../../images/asciidoc/tdd_env/wsl-006.png)

`アプリと機能` から `プログラミングと機能` を選択します。

![wsl 007](../../images/asciidoc/tdd_env/wsl-007.png)

`Windows Subsystem for Linux` にチェックを入れてOKボタンを押します。

![wsl 008](../../images/asciidoc/tdd_env/wsl-008.png)

`今すぐ再起動` を押してWindowsを再起動します。

![wsl 009](../../images/asciidoc/tdd_env/wsl-009.png)

### Dockerのインストール

[Docker Desktop](https://www.docker.com/products/docker-desktop)
をインストールします。

![docker 001](../../images/asciidoc/tdd_env/docker-001.png)

OKを押します。

![docker 002](../../images/asciidoc/tdd_env/docker-002.png)

インストールが完了したら再起動します。

![docker 003](../../images/asciidoc/tdd_env/docker-003.png)

再起動後に以下の警告が表示されるのでリンクをクリックします。

![docker 004](../../images/asciidoc/tdd_env/docker-004.png)

Linxuカーネル更新プログラムパッケージをダウンロードして実行します。

![docker 005](../../images/asciidoc/tdd_env/docker-005.png)

![docker 006](../../images/asciidoc/tdd_env/docker-006.png)

![docker 007](../../images/asciidoc/tdd_env/docker-007.png)

完了したら、Restartを押します。

![docker 008](../../images/asciidoc/tdd_env/docker-008.png)

チュートリアルを実行して動作を確認しておきましょう。

![docker 009](../../images/asciidoc/tdd_env/docker-009.png)

### Ubuntuのインストール

スタートメニューから `Windows PowerShell` を選択します。

![pkg 001](../../images/asciidoc/tdd_env/pkg-001.png)

以下のコマンドを入力します。

``` powershell
wsl --set-default-version 2
```

画面左下のスタートメニューから `Microsft Store` を選択します。

![wsl 001](../../images/asciidoc/tdd_env/wsl-001.png)

続いて、検索欄に `ubuntu` と入力して候補の中から `Ubuntu` を選択します。

![wsl 002](../../images/asciidoc/tdd_env/wsl-002.png)

入手を押してアプリケーションをインストールします。

![wsl 003](../../images/asciidoc/tdd_env/wsl-003.png)

インストールが終わるとセットアップが始まるのでユーザーIDとパスワードを設定してください。

![wsl 011](../../images/asciidoc/tdd_env/wsl-011.png)

![wsl 012](../../images/asciidoc/tdd_env/wsl-012.png)

## エディタのセットアップ

> Achieve Editor Fluency
> 
> An editor is your most important tool. Know how to make it do what you
> need, quickly and accurately.
> 
> —  Pragmatic Programmer: your journey to mastery 20th Anniversary
> Edition 

### インストール

[Download Visual Studio Code Java Pack
Installer](https://aka.ms/vscode-java-installer-win)
からVSCodeをダウンロードしてセットアッププログラムを実行します。

![vscode 001](../../images/asciidoc/tdd_env/vscode-001.png)

![vscode 002](../../images/asciidoc/tdd_env/vscode-002.png)

![vscode 003](../../images/asciidoc/tdd_env/vscode-003.png)

### 設定

エディタが起動すると画面右下にWSL拡張機能インストールのポップアップが表示されるので `Install`
を押して拡張機能をインストールします。

![setting 001](../../images/asciidoc/tdd_env/setting-001.png)

続いて画面左下の歯車を選択してメニューから `Settings` を選択します。

![setting 002](../../images/asciidoc/tdd_env/setting-002.png)

検索欄に `trim` と入力します。

![setting 003](../../images/asciidoc/tdd_env/setting-003.png)

チェックをオンにします。

![setting 004](../../images/asciidoc/tdd_env/setting-004.png)

同様に検索欄に `format on save` と入力してチェックをオンにします。

![setting 005](../../images/asciidoc/tdd_env/setting-005.png)

必要に応じてキーバインドなども自分が使いやすいようにカスタマイズします。

  - [Visual Studio
    Codeで簡単にショートカットキーを変更する方法](https://qiita.com/kinchiki/items/dabb5c890d9c57907503)

  - [VSCode 内蔵ターミナルで ctrl-p
    などのショートカットキーを利用する方法](https://loumo.jp/wp/archive/20191125120000/)

### 拡張機能の追加

エディタのメニューが英語なので日本語に変更する拡張機能をインストールします。

[Japanese Language Pack for Visual Studio
Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)

画面左のExtensionアイコンを選択して検索欄に `japanese` と入力したら日本語拡張パッケージが表示されるので `Install`
を押します。

![package 001](../../images/asciidoc/tdd_env/package-001.png)

`Restart Now` を押してエディタを再起動します。

![package 002](../../images/asciidoc/tdd_env/package-002.png)

メニューが日本語になりました。

![package
    003](../../images/asciidoc/tdd_env/package-003.png)

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

### 設定の同期

エディタの設定をして拡張機能をインストールしました。再インストールなどでエディタを再インストールする場合に上記の作業を再度するのは手間なので設定をオンライに保存してすぐにセットアップできるようにしておきます。

サイドバーから設定の同期をオンにするを選択します。

![sync 001](../../images/asciidoc/tdd_env/sync-001.png)

`オンにする` を押します。

![sync 002](../../images/asciidoc/tdd_env/sync-002.png)

`サインインしてオンにする` を押します。

![sync 003](../../images/asciidoc/tdd_env/sync-003.png)

`GitHubでサインイン` を選択します。

![sync 004](../../images/asciidoc/tdd_env/sync-004.png)

ブラウザが起動するので `Continue` を押します。

![sync 005](../../images/asciidoc/tdd_env/sync-005.png)

GitHubのアカウントとパスワードを入力します。

![sync 006](../../images/asciidoc/tdd_env/sync-006.png)

`Authorize github` を押します。

![sync 007](../../images/asciidoc/tdd_env/sync-007.png)

もし、GitHub連携で以下のような画面になった場合は登録メールアドレスに認証コードが送られているので確認してください。

![sync 009](../../images/asciidoc/tdd_env/sync-009.png)

![sync 010](../../images/asciidoc/tdd_env/sync-010.png)

### Hello world

#### プログラムを作成する

エディタのセットアップが出来たのでかんたんなプログラムを作ってみましょう。 お題は [Hello
world](https://ja.wikipedia.org/wiki/Hello_world) です。
まず、プログラムを作成する場所ですが今回はディスクトップの直下に
`Projects` というフォルダを作成してその中に配置したいと思います。

![hello 001](../../images/asciidoc/tdd_env/hello-001.png)

`Projects` フォルダの中に `PowerShell` フォルダを作成します。

![hello 002](../../images/asciidoc/tdd_env/hello-002.png)

![hello 003](../../images/asciidoc/tdd_env/hello-003.png)

エディタを起動します。

![hello 004](../../images/asciidoc/tdd_env/hello-004.png)

エディタを起動したらエクスプローラアイコンから `フォルダを開く` を選択して作成したフォルダを開きます。

![hello 005](../../images/asciidoc/tdd_env/hello-005.png)

![hello 007](../../images/asciidoc/tdd_env/hello-007.png)

フォルダを開いたらファイルアイコンを選択して `HelloWorld.ps1` ファイルを作成します。

![hello 008](../../images/asciidoc/tdd_env/hello-008.png)

![hello 009](../../images/asciidoc/tdd_env/hello-009.png)

まず、以下のコードを入力してキーボードのF5を押します。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $false
    }
}
```

![hello 010](../../images/asciidoc/tdd_env/hello-010.png)

プログラムの実行と一緒にテストの実行結果が表示されます。

![hello 011](../../images/asciidoc/tdd_env/hello-011.png)

テストが通るように修正します。

``` powershell
Describe "HelloWorld" {
    It "何か便利なものだ" {
        $true | Should Be $true
    }
}
```

![hello 012](../../images/asciidoc/tdd_env/hello-012.png)

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

![hello 013](../../images/asciidoc/tdd_env/hello-013.png)

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

![hello
014](../../images/asciidoc/tdd_env/hello-014.png)

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

![hello 015](../../images/asciidoc/tdd_env/hello-015.png)

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

![hello 016](../../images/asciidoc/tdd_env/hello-016.png)

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

![hello 017](../../images/asciidoc/tdd_env/hello-017.png)

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

![hello 018](../../images/asciidoc/tdd_env/hello-018.png)

`HelloWorld`
プログラムの完成です。

#### プログラムをデバッグする

プログラムを作成していると思った通りに動かないことが多々あります。そのようなときにプログラムの動作を確認するにはエディタのデバッグ機能を使います。

まず確認したいプログラムの行を左部分を押してブレークポイント（赤丸）を設定します。

![hello
019](../../images/asciidoc/tdd_env/hello-019.png)

ブレークポイントを設定したらF5を押してプログラムの実行します。そうするとブレークポイント部分でプログラムが停止して変数などの情報が確認できるようになります。

![hello 020](../../images/asciidoc/tdd_env/hello-020.png)

画面上の実行ボタンを押すと次のブレークポイントに移動します。

![hello 021](../../images/asciidoc/tdd_env/hello-021.png)

![hello 022](../../images/asciidoc/tdd_env/hello-022.png)

![hello 023](../../images/asciidoc/tdd_env/hello-023.png)

デバッガを終了するには終了ボタンを押します。

![hello 024](../../images/asciidoc/tdd_env/hello-024.png)

ブレークポイントを再度押すことで解除ができます。

![hello 025](../../images/asciidoc/tdd_env/hello-025.png)

#### プログラムをレポジトリに保存する

作成したプログラムをレポジトリに保存します。まずソース管理アイコンを選択して `リポジトリを初期化する` を押します。

![hello 026](../../images/asciidoc/tdd_env/hello-026.png)

![hello 027](../../images/asciidoc/tdd_env/hello-027.png)

`変更をステージ` を選択します。

![hello 028](../../images/asciidoc/tdd_env/hello-028.png)

変更内容を入力します。ここでは `feat: HelloWorld` を入力しておきます。

![hello 029](../../images/asciidoc/tdd_env/hello-029.png)

`コミット` を押します。

![hello 030](../../images/asciidoc/tdd_env/hello-030.png)

初回登録時は以下の警告が表示されるので追加作業が必要になります。

![hello 031 1](../../images/asciidoc/tdd_env/hello-031-1.png)

![hello 031 2](../../images/asciidoc/tdd_env/hello-031-2.png)

以下のコマンドをターミナルに入力します。

    git config --global user.name "newbie4649"
    git config --global user.email newbie4649@outlook.jp

user.nameとuser.emailには自分のアカウント情報を登録すること。

![hello 032](../../images/asciidoc/tdd_env/hello-032.png)

再度 `コミット` を押してレポジトリに保存します。

![hello 033](../../images/asciidoc/tdd_env/hello-033.png)

レポジトリの記録内容は `ソース管理` から確認することが出来ます。

![hello 035](../../images/asciidoc/tdd_env/hello-035.png)

## 開発言語のセットアップ

Unresolved directive in chapter\_1.adoc -
include::episode\_0\_win.adoc\[\] Unresolved directive in
chapter\_1.adoc - include::episode\_0\_wsl.adoc\[\]

## 参照

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
