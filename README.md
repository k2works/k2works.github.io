# k2works Blog

## 概要

### 目的

### 前提

| ソフトウェア   | バージョン | 備考 |
| :------------- | :--------- | :--- |
| nodejs         | 10.16.3     |      |

## 構成

- [構築](#構築)
- [配置](#配置)
- [運用](#運用)
- [開発](#開発)

## 詳細

### 構築

以下の作業を最初の一回のみ実施する。構築後の定型的作業は配置・運用を参照する。

#### 開発パッケージのセットアップ

```
npm init -y
npm install --save-dev npm-run-all watch foreman cpx rimraf markdown-to-html
npm install --save-dev prettier
npm install --save-dev browser-sync connect-browser-sync nodemon
npx browser-sync init
touch Procfile
```

#### ブログのセットアップ

```
npm install hexo-cli
npx hexo init blog
cd blog
npm install
hexo generate
hexo server
```

**[⬆ back to top](#構成)**

### 配置

#### セットアップ

```
npm install
```

#### ブログのデプロイ

```
npm run blog:deploy
```

**[⬆ back to top](#構成)**

### 運用

#### ブログ記事の作成

```
npm run blog:new
```

**[⬆ back to top](#構成)**

### 開発

##### ブログのローカル起動

```
npm run blog:local
```

**[⬆ back to top](#構成)**

## 参照

- [hexo.io](https://hexo.io/)
- [hexo-theme-melody](https://molunerfinn.com/hexo-theme-melody-doc/#features)
- [AsciiDoc と PlantUML で Blog が書きたい](https://qiita.com/high-u/items/479ba757c028b9ad95f6)