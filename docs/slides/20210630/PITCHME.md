---
marp: true
---

# 値オブジェクトの実装

---

## 構成

- 自己紹介
- 値オブジェクトとは
- マネーの実装
- まとめ

---

## 自己紹介

- カキギカツユキ
- ネット通販の会社で業務システムを開発運用しています
- あと、売掛金・買掛金管理の管理業務しています
- その前はシステムエンジニアとしていろんな会社のシステム開発をしていました

---

## 値オブジェクトとは

> IDに基づいた等価性を確保していない、MoneyやDate Rangeなどのシンプルな小型オブジェクト。
>
> エンタープライズアーキテクチャパターン

> 値の種類ごとに専用の型を用意するコードが安定し、コードの意図が明確になります。このように、値を扱うための専用クラスを作るやり方を値オブジェクト(Value Object)と呼びます。
>
> 現場で役立つシステム設計の原則

> エンティティの同一性を追跡するのは本質的なことだが、それ以外のオブジェクトに同一性を与えてしまうと、システムの性能を損なうことになり、分析作業が増え、さらに、すべてのオブジェクトの見た目が同じになってしまうことでモデルが台無しになりかねない。
>
> エリック・エヴァンスのドメイン駆動設計

---

## マネーの実装

```
import unittest
import hashlib


class Money:
    def __init__(self, amount, currency) -> None:
        self.__amount = amount
        self.__currency = currency

    def __str__(self) -> str:
        if self.__currency == 'JPY':
            return f'¥{self.__amount}'
        elif self.__currency == 'USD':
            return f'${self.__amount}'
        else:
            return f'{self.__amount}'

    def __eq__(self, other: object) -> bool:
        return(self.__amount == other.__amount and self.__currency == other.__currency)

    def __hash__(self) -> int:
        encoded_currency = int(hashlib.sha256(
            self.__currency.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        return hash(self.__amount + encoded_currency)

    def add(self, other: object) -> object:
        if self.__currency != other.__currency:
            raise ValueError('異なる通貨では計算できません')
        return Money(self.__amount + other.__amount, self.__currency)


class TestMoney(unittest.TestCase):
    def setUp(self) -> None:
        self.千円 = Money(1000, 'JPY')
        self.一万円 = Money(10000, 'JPY')
        self.千ドル = Money(1000, 'USD')

    def test_金額を表示する(self):
        self.assertEqual(str(self.千円), '¥1000')
        self.assertEqual(str(self.一万円), '¥10000')

    def test_外貨金額を表示する(self):
        self.assertEqual(str(self.千ドル), '$1000')

    def test_金額は等しい(self):
        self.assertEqual(self.千円, Money(1000, 'JPY'))
        self.assertNotEqual(self.千円, self.千ドル)

    def test_通貨を保持している(self):
        財布 = {self.千円}
        self.assertTrue(self.千円 in 財布)
        self.assertFalse(self.千ドル in 財布)

    def test_金額を合計する(self):
        二千円 = self.千円.add(Money(1000, 'JPY'))
        self.assertEqual(str(二千円), '¥2000')
        with self.assertRaises(ValueError, msg='異なる通貨では計算できません'):
            self.千ドル.add(Money(1000, 'JPY'))



unittest.main(argv=[''], verbosity=2, exit=False)
```

---

## まとめ

- 正直めんどくさい
- 慣れてくると普通に便利
- 基本形を指で覚える

---

## 参照

- エンタープライズアプリケーションアーキテクチャパターン マーチン・ファウラー  (著), 株式会社テクノロジックアート (翻訳), 長瀬嘉秀 (翻訳, 監修)
- 現場で役立つシステム設計の原則 〜変更を楽で安全にするオブジェクト指向の実践技法 増田 亨  (著) 
- エリック・エヴァンスのドメイン駆動設計 Eric Evans (著), 和智右桂  (翻訳), 牧野祐子 (翻訳), 今関剛 (監修)
