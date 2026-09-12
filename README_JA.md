# screenwriting-skills

[English](README.md) · [中文版](README_ZH.md) · [한국어](README_KO.md) · [Français](README_FR.md)

脚本執筆・テレビドラマ・劇作法のための 21 個のエージェントスキル（[Claude Code](https://docs.anthropic.com/en/docs/claude-code/skills) と [OpenAI Codex](https://developers.openai.com/codex/build-skills) 対応）。32 冊の理論書と 12 巻の出版シナリオ・戯曲（中国・アメリカ・イギリス・日本・韓国）から抽出したもの。

`SKILL.md` はオープン規格 [agentskills.io](https://agentskills.io) に準拠し、両方のエージェントで共有されます——一度入れれば、どちらでも動きます。

**日本語でそのまま質問してください。** スキル本文は中国語で書かれています。出典の多くが中国語の原著または中国語訳だからです。これは実装上の都合であって制約ではありません——日本語で訊けば日本語で返ってきます。なぜ言語ごとにツリーを分けないのかは[多言語対応](#多言語対応)を参照してください。

## インストール

### Claude Code

#### プラグインマーケットプレイス（推奨）

```
/plugin marketplace add jtydhr88/screenwriting-skills
/plugin install screenwriting@screenwriting-skills
```

インストール後は `/screenwriting:<skill>` で呼び出せます（例：`/screenwriting:sw-dialogue`）。

#### 個人用（全プロジェクト）

```bash
git clone https://github.com/jtydhr88/screenwriting-skills.git
cp -r screenwriting-skills/plugins/screenwriting/skills/* ~/.claude/skills/
```

#### プロジェクト単位

```bash
mkdir -p .claude/skills
cp -r screenwriting-skills/plugins/screenwriting/skills/* .claude/skills/
```

### Codex（CLI / ChatGPT デスクトップアプリ / IDE 拡張）

```bash
codex plugin marketplace add jtydhr88/screenwriting-skills

# その後、ChatGPT デスクトップアプリまたは Codex CLI で：
# Plugins → "Screenwriting Skills" を選択 → Install
```

個人用は `~/.agents/skills/`、プロジェクト単位は `.agents/skills/` にコピーします。`/skills` で一覧、`$sw-story-structure` で明示的に呼び出せます。

## 使用例

```
# 「12 話構成の幕を切って、幕切れの位置を決めて」
# → sw-series-structure

# 「この台詞が説明的すぎるので直して」
# → sw-dialogue + sw-scene-craft

# 「この長編小説を 40 話の連続ドラマの構成案にして」
# → sw-chinese-series-practice + sw-series-engine-bible

# 「企画を立ち上げて、進捗を憶えておいて」
# → sw-workflow
```

## 多言語対応

**ソースツリーは一つ、言語は実行時に解決する。** スキルは中国語で一度だけ書かれ、エージェントが質問された言語で返します。

これは考えた末の決定であり、最初の決定ではありませんでした。英語版——20 個のスキルをすべて翻訳した並行プラグイン `screenwriting-en`——は [#3](https://github.com/jtydhr88/screenwriting-skills/issues/3) で提案され、実装され、マージされました。そして削除されました。それを退けた論拠は、他のどの言語にも等しく当てはまります。中国語が読めない読者に翻訳されたツリーが必要なら、英語が読めない読者にも必要であり、次は日本語、その次は韓国語、フランス語、ロシア語です。5 言語なら 230 ファイルが各々勝手にずれていき、どれが古いのかを教えてくれるものは何もありません。本当のコストは翻訳作業ではなく、**一度フォークしてしまえば、二度目を断る原則的な根拠が失われる**ことです。

そこで線はソースの側に引き、残りは実行時に処理します：

- **出力言語は質問の言語に従う。** 日本語で訊けば日本語で返る。フラグも別インストールも不要。
- **用語は毎回訳し直すのではなく、原語に錨を下ろす。** この分野の専門語はもともと英語です——*logline*、*act out*、*beat sheet*、*showrunner*、*staff writer*。出典の中国語（計程繩、出幕、節拍表、劇目管理人、試用編劇）のほうが訳語であり、訳者によって選択が違います。[`sw-workflow/terms.md`](plugins/screenwriting/skills/sw-workflow/terms.md) が各概念を原語に対応づけるので、エージェントは語を**復元**します。そしてこの一枚の表がすべての言語に同時に効きます——日本語で書く脚本家も現場では act out や logline と言うからです。
- **対応語のない語は原語のまま、注釈を添える。** 戏眼、扣子 は英語に押し込まず、`戏眼 (xìyǎn — 各話の一言で指させる中心的な見どころ)` の形で出ます。日本語の術語（柱・ト書き・セリフ・決定稿）は `sw-format-adaptation` が正面から扱っており、日本語で訊けばそのまま日本語の術語で返ります。
- **脚本本文は作品自身の言語のまま。** 中国語の脚本を日本語で議論するのは普通のことです。会話の言語は変わっても、原稿の言語は変わりません。

これと引き換えに失われるのは**監査可能性**です。中国語が読めなければ、指示ファイルそのものは読めず、エージェントによるその報告しか読めません。これは実在するコストであり、削除された英語版が唯一本当に買っていたものでした。しかし恒久的な 5 方向の保守負担に見合うものではありませんでした。

**README は別扱い**で、翻訳されています。短く、変動が少なく、新しく来た人が最初に出会うものだからです。日本語・韓国語・フランス語の README は、インストール・構成・この方針までで意図的に止めています。スキルの詳細対照表と出典書誌は [English](README.md) と [中文版](README_ZH.md) にあり、4 回複製することはしません——理由は上と同じです。

## 舞台の諸ジャンルについて

映画とテレビドラマは網羅済み。舞台は一部のみで、残りは計画中です。基準は一つ：**そのジャンルは、モデルに構成・書式・言語規則の異なるものを書かせるか。** 書かせるなら独立したスキル、題材や作風が違うだけなら既存スキル内の事例にとどめます。中国戯曲はこの基準を満たします（唱詞は韻轍と板式に拘束され、場は頁ではなく折／出で切られ、行当が心理より先に人物の書き方を決める）。現在は `sw-chinese-opera` に陸軍の唱詞の方法と媒体境界表があり、未収録の部分はスキル内に明記しています。次に予定しているのは翁偶虹・范鈞宏・李漁による劇種横断の方法、劇種別の付録（表）、曹禺・老舎の話劇、そして最後にミュージカル。縦型ショートドラマと AI 漫画ドラマは対象外です。新しい媒体は「新スキル一つ＋その中の境界表＋`sw-workflow` の入口表に一行」だけで追加し、汎用層には手を入れません。全文は [English](README.md#stage-genres) / [中文版](README_ZH.md#舞台门类)。

## 四層構成

長編映画は第 1・3・4 層を使い、連続ドラマは四層すべてを使います。シリーズ層は通用層の隣に足されるのではなく、「一本の映画のために設計された構成」を「エンジン＋シーズン」で**置き換える**からです。

```
1. 一般劇作法   前提 · 構成 · 人物 · 台詞 · 場面 · 書式 · プロジェクト進行
2. 媒体層       連続ドラマ · 各話とシーズンの構成 · エンジンとバイブル · ライターズルーム · 30 分コメディ
                舞台 · 中国戯曲（唱詞と境界表、他は計画中）
3. 伝統と業界   アメリカ · 日本 · 韓国とフランス · 中国大陸 · ビジネス
4. 原典コーパス チェーホフ · 小津 · Succession · テレビドラマ事例集
```

| 層 | スキル |
|---|---|
| 1 | `sw-workflow`（進行管理と `story-bible.md`）· `sw-story-structure` · `sw-premise-theme` · `sw-character-conflict` · `sw-dialogue` · `sw-scene-craft` · `sw-format-adaptation` |
| 2 | 連続ドラマ：`sw-series-structure` · `sw-series-engine-bible` · `sw-writers-room` · `sw-sitcom-comedy`<br>舞台：`sw-chinese-opera`（中国戯曲の唱詞の方法と媒体境界表。板式・行当・様式は未収録と明記） |
| 3 | `sw-american-case-studies` · `sw-japanese-screenwriting` · `sw-korean-french-screenwriting` · `sw-chinese-series-practice` · `sw-industry-business` |
| 4 | `chekhov-dramaturgy` · `ozu-screenplay-style` · `succession-series-writing` · `sw-series-case-studies` |

各スキルは `SKILL.md`（原則・チェックリスト・手順）を持ち、ほとんどが `reference.md`（表・分析・引用）を伴います。各スキルが何を含み、どの本から来ているかの完全な対照表は [English README](README.md#how-the-skills-are-organised) にあります。

日本語に関わる部分：`sw-japanese-screenwriting` は日本の監督・脚本家 10 人の方法（構成先行と断片先行、小ネタ帳、「もし＋しかも」、人物＝俳優＋欠点、主題は後から立ち上がる）、`ozu-screenplay-style` は小津安二郎の脚本 6 本を作法として読み解いたもの、`sw-format-adaptation` は柱・ト書き・セリフの日本式書式、`sw-series-case-studies` には坂元裕二『花束みたいな恋をした』の場面統計が入っています。

## 出典

**脚本理論 17 冊** — シド・フィールド、ブレイク・スナイダー、ロバート・マッキー（*Story* と *Dialogue*）、ジュリアン・ホクスター、ニール・D・ヒックス、ラヨシュ・エグリ、リサ・クロン、ウィリアム・インディック、リチャード・ウォルター、ウェンディ・ジェーン・ヘンソン、ダイアモンド＆ワイズマン、エリック・ボーク、梅峰、劉大鵬編、陸軍、泊貴洋編。

**テレビ理論 15 冊** — ウィリアム・ラプキン、ダニエル・カルヴィージ、パメラ・ダグラス、カム・ミラー、エマニュエル・オバーグ、ゴールドバーグ＆ラプキン、ニール・ランダウ、エヴァン・S・スミス、リチャード・A・ブラム、姚扣根、張巍、張明智・宋培義、趙彬彬。

**出版シナリオ・戯曲 12 巻** — チェーホフ戯曲全集、小津安二郎脚本集、Jesse Armstrong *Succession: The Complete Scripts* I–IV、Aaron Sorkin *The West Wing Script Book*、David Chase 他 *The Sopranos*、Julian Fellowes *Downton Abbey* Season Two、Phoebe Waller-Bridge *Fleabag: The Scriptures*、坂元裕二『花束みたいな恋をした』、盧熙京『世界で最も美しい別れ』。

完全な書誌は [English README](README.md#source-books) を参照。

## ライセンス

個人学習用。引用は原著者および訳者に帰属します。

同じ発想を日本の作曲・編曲に応用した姉妹プロジェクト：[japanese-composition-skills](https://github.com/jtydhr88/japanese-composition-skills)。
