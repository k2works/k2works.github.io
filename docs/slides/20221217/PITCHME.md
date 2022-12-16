---
marp: true
---

### ExcelでJavaScriptが使えるようになったからってぜんぜん活用する気ないんだからねっ！

---

### 構成

* 自己紹介
* Excel JavaScript API
* デモ

---

### 自己紹介

* カキギカツユキ
* ぼっち・ざ・情シス
* ネット通販の会社で業務システムを開発運用しています
* あと、売掛金・買掛金管理の管理業務しています
* その前はシステムエンジニアとしていろんな会社のシステム開発をしていました
* 最近はシステムトレードの個人開発やってます

---

### Excel JavaScript API

> An Excel add-in interacts with objects in Excel by using the Office JavaScript API, which includes two JavaScript object models:
>
> * **Excel JavaScript API**: These are the [application-specific APIs](https://learn.microsoft.com/en-us/office/dev/add-ins/develop/application-specific-api-model) for Excel. Introduced with Office 2016, the [Excel JavaScript API](https://learn.microsoft.com/en-us/javascript/api/excel) provides strongly-typed objects that you can use to access worksheets, ranges, tables, charts, and more.
> * **Common APIs**: Introduced with Office 2013, the [Common API](https://learn.microsoft.com/en-us/javascript/api/office) can be used to access features such as UI, dialogs, and client settings that are common across multiple types of Office applications.
>
---

### Excel JavaScript API
#### Excel add-ins

> An Excel add-in allows you to extend Excel application functionality across multiple platforms including Windows, Mac, iPad, and in a browser. Use Excel add-ins within a workbook to:
---

### Excel JavaScript API

#### Script Lab , a Microsoft Garage project

> ## What is Script Lab?
>
> Wouldn't it be crazy if you could launch Excel, click to open a small code window, and then instantly start writing and executing JavaScript that interacts with your spreadsheet?
>
> Script lab is a tool for anyone who wants to learn about writing Office Add-ins for Excel, Outlook, Word, or PowerPoint. The focus is the Office JavaScript API, which is the technology you need for building Office Add-ins that run across platforms. Maybe you're an experienced Office developer and you want to quickly prototype a feature for your add-in. Or maybe you've never tried writing code for Office and you just want to play with a sample and tweak it to learn more. Either way, Script Lab is for you.

---

### デモ

#### SQLぽく使えるからってぜんぜん活用する気ないんだからねっ!

```JavaScript
async function runSql() {
  await Excel.run(async (context) => {
    selectAll(context, data);
    selectAllScore(context, data);
    selectByGender(context, data, "女");
    selectByAgeGrater(context, data, 10);
    selectByScoreLessEqual(context, data, 50);

    await context.sync();
  });
}

/**
 * 全件選択
 * SELECT * FROM Student;
 * @param context コンテキスト
 * @param data データ
 */
const selectAll = (context: Excel.RequestContext, data: student[]) => {
  const select = (data) => data.map((i) => i);
  console.log(select(data));
  context.workbook.worksheets.getItemOrNullObject("全選択").delete();
  const sheet = context.workbook.worksheets.add("全選択");
  display(sheet, "成績表", select(data));
};

....

/**
 * 成績を条件に選択
 * SELECT * FROM Student WHERE test_score<=50;
 * @param context コンテキスト
 * @param data データ
 * @param score 点数
 */
const selectByScoreLessEqual = (context: Excel.RequestContext, data: student[], score: number) => {
  const select_test_score_grater_less_equal = (data, test_score) => data.filter((i) => i.test_score <= test_score);
  console.log(select_test_score_grater_less_equal(data, 50));
  context.workbook.worksheets.getItemOrNullObject("点数選択").delete();
  const sheet = context.workbook.worksheets.add("点数選択");
  display(sheet, "点数成績表", select_test_score_grater_less_equal(data, score));
};
```

---

### デモ

#### ストレージに保存できるからってぜんぜん活用する気ないんだからねっ！

```YAML
https://cdnjs.cloudflare.com/ajax/libs/dexie/3.2.2/dexie.min.js
```

```JavaScript
type friend = {
  id: number;
  name: string;
  age: number;
};

async function runDB() {
  await Excel.run(async (context) => {
    const db = localDB(context);
    const result: friend[] = await db.selectAll();
    renderDBSheet(context, result)
    await context.sync();
  });
}
```

---

### デモ

#### 外部サービスとAPI連携できるからってぜんぜん活用する気ないんだからねっ！

```YAML
https://cdnjs.cloudflare.com/ajax/libs/axios/1.2.1/axios.min.js
```

---

```JavaScript
type reservableRoom = {
  meetingRoom: {
    roomId: { value: string };
    roomName: string;
  };
};

type reservableRoomList = {
  list: reservableRoom[];
};

async function runAPI() {
  await Excel.run(async (context) => {
    const authService = new AuthService();
    await authService.login("U000001", "pAssw0rd");
    const roomService = new RoomService();
    const result = await roomService.list(new Date());
    renderApiSheet(context, result.data);
    authService.logout();
    await context.sync();
  });
}
```

---

### デモ

#### テスト駆動開発ができるからってぜんぜん活用する気ないんだからねっ！


```YAML
https://cdnjs.cloudflare.com/ajax/libs/mocha/2.2.1/mocha.min.css
https://cdnjs.cloudflare.com/ajax/libs/mocha/2.2.1/mocha.min.js
@types/mocha
https://unpkg.com/expect@%3C21/umd/expect.min.js
@types/jest
```

```HTML
<div id="mocha">
</div>

<script class="mocha-init">
	mocha.setup('bdd');
	//mocha.checkLeaks();
</script>
<script src="test.array.js"></script>
<script src="test.object.js"></script>
<script src="test.xhr.js"></script>
<script class="mocha-exec">
	mocha.run();
</script>
```

---

```JavaScript
(() => {
  describe("FizzBuzz", () => {
    let fizzBuzz;
    beforeEach(() => {
      fizzBuzz = FizzBuzz;
    });

    describe("三の倍数の場合", () => {
      it("3を渡したときは文字列Fizzを返す", () => {
        expect(fizzBuzz.generate(3)).toEqual("Fizz");
      });
    });
    describe("五の倍数の場合", () => {
      it("5を渡したときは文字列Buzzを返す", () => {
        expect(fizzBuzz.generate(5)).toEqual("Buzz");
      });
    });

    describe("三と五の倍数の場合", () => {
      it("15を渡したら文字列FizzBuzzを返す", () => {
        expect(fizzBuzz.generate(15)).toEqual("FizzBuzz");
      });
    });
...
  });
})();
```

---

```JavaScript
class FizzBuzz {
  static get MAX_NUMBER() {
    return 100;
  }
  static get FIZZ() {
    return "Fizz";
  }
  static get BUZZ() {
    return "Buzz";
  }

  static generate(number): string {
    const isFizzBuzz = number % 3 === 0 && number % 5 === 0;
    const isFizz = number % 3 === 0;
    const isBuzz = number % 5 === 0;

    if (isFizzBuzz) return `${this.FIZZ}${this.BUZZ}`;
    if (isFizz) return this.FIZZ;
    if (isBuzz) return this.BUZZ;

    return number.toString();
  }

  static generateList(): string[] {
    let array = [];
    for (let i = 0; i < this.MAX_NUMBER; i++) {
      array.push(FizzBuzz.generate(i + 1));
    }
    return array;
  }
}

async function runTDD() {
  await Excel.run(async (context) => {
    const result = FizzBuzz.generateList();
    renderFizzBuzzSheet(context, result);
    await context.sync();
  });
}
```
---

#### ...これでよくね？

---

### おわり

```JavaScript
$("#run_clean").click(() => tryCatch(ヒャッハー));

async function ヒャッハー() {
  const 汚物は消毒だ = (context: Excel.RequestContext, sheet: string) => {
    context.workbook.worksheets.getItemOrNullObject(sheet).delete();
  };

  await Excel.run(async (context) => {
    const 汚物 = [
      "全選択",
      "全点数選択",
      "性別選択",
      "年齢選択",
      "点数選択",
      "FriendTable",
      "会議室予約一覧",
      "FizzBuzz"
    ];
    汚物.forEach((i) => 汚物は消毒だ(context, i));
    await context.sync();
  });
}
```

---

### 参照

* [Excel JavaScript API overview - Office Add-ins | Microsoft Learn](https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview)
* [Excel add-ins overview - Office Add-ins | Microsoft Learn](https://learn.microsoft.com/en-us/office/dev/add-ins/excel/excel-add-ins-overview)
* [script-lab/README.md at master · OfficeDev/script-lab (](https://github.com/OfficeDev/script-lab/blob/master/README.md)[github.com](github.com))

---