import "./style.css";
import render from "@k2works/full-stack-lab";

const contents = `
## 機能名
## 仕様
## TODOリスト
`;

const mindmap = `
@startmindmap
+ root
++ right
+++ right right
*** right2
-- left
--- left left
-- left2

@endmindmap
`;

const usecase = `
@startuml
left to right direction
actor "Actor" as ac
rectangle Application {
  usecase "UseCase1" as UC1
  usecase "UseCase2" as UC2
  usecase "UseCase3" as UC3
}
ac --> UC1
ac --> UC2
ac --> UC3
@enduml
`;

const ui = `
@startsalt
{+
  コレクション画面
  {+
  {
  生徒
  教員
  組
  部
  イベント
  } |
  {
    == 生徒
    { + <&zoom-in> (          )}
    {T#
    + 田尻　智裕  | 3年B組    | 野球部 写真部
    + 山田　太郎  | 3年A組    | 野球部
    + 鈴木　花子  | 3年A組    | 写真部
    }
  }
  }
----------------
  シングル画面
  {+
  {
  生徒
  教員
  組
  部
  イベント
  } |
  {
    {
      <&person> <b>田尻 智裕
    }
    {
      名前
      田尻　智裕
      組
      3年B組
      部
      野球部 写真部
      関連する生徒
      田尻　智裕 山田　太郎　鈴木　花子
    }
  }
  }
}
@endsalt
`;

const uiModel = `
@startuml
  class 部 {
    名称
    カテゴリー
    生徒数
    印刷()
    新規()
    削除()
  }
  class 生徒 {
    氏名
    成績
    印刷()
    新規()
    削除()
  }
  class 組 {
    名称
    印刷()
    新規()
    削除()
  }
  class 教員 {
    氏名
    電話番号
    印刷()
    新規()
    削除()
  }
  class イベント {
    名称
    日付
    印刷()
    新規()
    削除()
  }
  部 *-* 生徒
  部 *-- 教員
  イベント *- 教員
  生徒 --* 組
`;

const uiInteraction = `
@startuml
  イベント_コレクション --> イベント_シングル
  イベント_シングル --> 教員_シングル
  教員_コレクション --> 教員_シングル
  教員_シングル --> 部_コレクション
  教員_シングル <-> 組_シングル
  組_コレクション --> 組_シングル
  組_シングル --> 生徒_コレクション
  生徒_コレクション --> 生徒_シングル
  生徒_シングル -> 組_シングル
  生徒_シングル --> 部_コレクション
  部_コレクション --> 部_シングル
  部_シングル --> 生徒_コレクション
@enduml
`;

const uml = `
@startuml
abstract class AbstractList
abstract AbstractCollection
interface List
interface Collection
List <|-- AbstractList
Collection <|-- AbstractCollection
Collection <|- List
AbstractCollection <|- AbstractList
AbstractList <|-- ArrayList
class ArrayList {
  Object[] elementData
  size()
}
enum TimeUnit {
  DAYS
  HOURS
  MINUTES
}
annotation SuppressWarnings
@enduml
`;

const erd = `
@startuml
' hide the spot
hide circle
' avoid problems with angled crows feet
skinparam linetype ortho
entity "Entity01" as e01 {
  *e1_id : number <<generated>>
  --
  *name : text
  description : text
}
entity "Entity02" as e02 {
  *e2_id : number <<generated>>
  --
  *e1_id : number <<FK>>
  other_details : text
}
entity "Entity03" as e03 {
  *e3_id : number <<generated>>
  --
  e1_id : number <<FK>>
  other_details : text
}
e01 ||..o{ e02
e01 |o..o{ e03
@enduml
`;

const mode = "APP"; // "UI" or "API" or "DOC"
render({ mindmap, contents, ui, uiModel, uiInteraction, usecase, uml, erd, mode });
