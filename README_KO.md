# screenwriting-skills

[English](README.md) · [中文版](README_ZH.md) · [日本語](README_JA.md) · [Français](README_FR.md)

시나리오·드라마 극본·극작법을 위한 24개의 에이전트 스킬([Claude Code](https://docs.anthropic.com/en/docs/claude-code/skills) 및 [OpenAI Codex](https://developers.openai.com/codex/build-skills) 지원). 45권의 작법서와 23권의 출간 대본·악보·희곡(중국·미국·영국·일본·한국)에서 추출했습니다.

`SKILL.md` 파일은 공개 규격인 [agentskills.io](https://agentskills.io) 표준을 따르며 두 에이전트가 공유합니다 — 한 번 설치하면 어디서든 작동합니다.

**한국어로 그냥 질문하세요.** 스킬 본문은 중국어로 작성되어 있습니다. 출처 대부분이 중국어 원저 또는 중국어 번역본이기 때문입니다. 이는 구현상의 사정일 뿐 제약이 아닙니다 — 한국어로 물으면 한국어로 답합니다. 왜 언어별로 트리를 나누지 않는지는 [다국어 지원](#다국어-지원)을 참고하세요.

## 설치

### Claude Code

#### 플러그인 마켓플레이스(권장)

```
/plugin marketplace add jtydhr88/screenwriting-skills
/plugin install screenwriting@screenwriting-skills
```

설치 후에는 `/screenwriting:<skill>` 로 호출합니다(예: `/screenwriting:sw-dialogue`).

#### 개인용(모든 프로젝트)

```bash
git clone https://github.com/jtydhr88/screenwriting-skills.git
cp -r screenwriting-skills/plugins/screenwriting/skills/* ~/.claude/skills/
```

#### 프로젝트 단위

```bash
mkdir -p .claude/skills
cp -r screenwriting-skills/plugins/screenwriting/skills/* .claude/skills/
```

### Codex(CLI / ChatGPT 데스크톱 앱 / IDE 확장)

```bash
codex plugin marketplace add jtydhr88/screenwriting-skills

# 그다음 ChatGPT 데스크톱 앱이나 Codex CLI에서:
# Plugins → "Screenwriting Skills" 선택 → Install
```

개인용은 `~/.agents/skills/`, 프로젝트 단위는 `.agents/skills/` 에 복사합니다. `/skills` 로 목록을 보고 `$sw-story-structure` 로 직접 호출할 수 있습니다.

## 사용 예

```
# "12부작을 막으로 나누고 막 끝 지점을 잡아줘"
# → sw-series-structure

# "이 대사가 너무 직설적인데 고쳐줘"
# → sw-dialogue + sw-scene-craft

# "이 장편소설을 40부작 드라마 구성안으로 만들어줘"
# → sw-chinese-series-practice + sw-series-engine-bible

# "프로젝트를 시작하고 진행 상황을 기억해줘"
# → sw-workflow
```

## 다국어 지원

**소스 트리는 하나, 언어는 런타임에 해결한다.** 스킬은 중국어로 한 번만 작성되고, 에이전트가 질문받은 언어로 전달합니다.

이것은 고민 끝에 내린 결정이며, 처음의 결정은 아니었습니다. 영어판 — 20개 스킬을 모두 번역한 병렬 플러그인 `screenwriting-en` — 은 [#3](https://github.com/jtydhr88/screenwriting-skills/issues/3)에서 제안되고, 구현되고, 병합되었습니다. 그리고 삭제되었습니다. 그것을 물리친 논거는 다른 모든 언어에도 똑같이 적용됩니다. 중국어를 읽지 못하는 독자에게 번역된 트리가 필요하다면 영어를 읽지 못하는 독자에게도 필요하고, 다음은 일본어, 그다음은 한국어, 프랑스어, 러시아어입니다. 5개 언어면 230개 파일이 제각기 어긋나기 시작하고, 어느 것이 낡았는지 알려주는 장치는 아무것도 없습니다. 진짜 비용은 번역 작업이 아니라, **한 번 포크하고 나면 두 번째를 거절할 원칙적 근거가 사라진다**는 점입니다.

그래서 선은 소스 쪽에 긋고, 나머지는 런타임이 처리합니다:

- **출력 언어는 질문 언어를 따른다.** 한국어로 물으면 한국어로 답합니다. 옵션도, 별도 설치도 필요 없습니다.
- **용어는 매번 다시 번역하는 대신 원어에 고정한다.** 이 분야의 전문 용어는 원래 영어입니다 — *logline*, *act out*, *beat sheet*, *showrunner*, *staff writer*. 출처의 중국어(計程繩, 出幕, 節拍表, 劇目管理人, 試用編劇)가 오히려 번역어이고, 역자마다 선택이 다릅니다. [`sw-workflow/terms.md`](plugins/screenwriting/skills/sw-workflow/terms.md)가 각 개념을 원어에 대응시키므로 에이전트는 단어를 **복원**합니다. 그리고 이 한 장의 표가 모든 언어에 동시에 작동합니다 — 한국어로 쓰는 작가도 현장에서는 act out, logline이라고 하기 때문입니다.
- **대응어가 없는 말은 원어 그대로 두고 설명을 붙인다.** 戏眼, 扣子 같은 말은 억지로 영어에 밀어 넣지 않고 `戏眼 (xìyǎn — 각 회차에서 한마디로 지목할 수 있는 핵심 볼거리)` 형태로 나옵니다.
- **대본 본문은 작품 자신의 언어를 유지한다.** 중국어 대본을 한국어로 논의하는 것은 흔한 일입니다. 대화의 언어는 바뀌어도 원고의 언어는 바뀌지 않습니다.

이와 맞바꾸어 잃는 것은 **감사 가능성**입니다. 중국어를 읽지 못하면 지시 파일 자체는 읽을 수 없고, 그에 대한 에이전트의 보고만 읽을 수 있습니다. 이것은 실재하는 비용이며, 삭제된 영어판이 유일하게 정말로 사들였던 것이었습니다. 그러나 영구적인 5중 유지보수 부담에 값하지는 않았습니다.

**README는 별개**이며 번역되어 있습니다. 짧고, 잘 바뀌지 않으며, 처음 온 사람이 가장 먼저 마주치는 것이기 때문입니다. 일본어·한국어·프랑스어 README는 설치·구성·이 방침까지로 의도적으로 멈춰 있습니다. 스킬 상세 대조표와 출처 서지는 [English](README.md)와 [中文版](README_ZH.md)에 있으며 네 번 복제하지 않습니다 — 이유는 위와 같습니다.

## 무대 장르에 대하여

영화와 드라마는 다뤘습니다. 무대는 일부만 다뤘고 나머지는 계획 중입니다. 기준은 하나입니다: **그 장르가 모델로 하여금 구조·형식·언어 규칙이 다른 것을 쓰게 하는가.** 그렇다면 독립 스킬, 소재나 작풍만 다르다면 기존 스킬 안의 사례로 둡니다.

중국 희곡은 하나의 장르가 아니라 **두 가지 작법**입니다. 나누는 축은 극종이 아니라 성강 체계입니다. **곡패체**(원잡극·명청전기·곤곡)는 전사(填詞)——자수·구식·평측이 정해진 곡패에 가사를 채워 넣습니다. 잡극은 4절 1설자에 한 사람이 주창하고, 전기는 출(出) 단위로 갑니다. **판강체**(경극·예극·월극·진강·평극·호극)는 상하구——7자 또는 10자 대구를 판식 변화로 떠받치고, 행당이 나누어 부르며, 단위는 장(場)입니다. 구조 단위와 창사 작법이 모두 다르므로 두 개의 스킬입니다. 같은 체계 안의 극종 차이는 어느 운표(경극 십삼철인가 예극 중주운인가)·어느 판식표를 찾느냐뿐이라, 같은 방법에 다른 표이므로 reference 부록으로 두고 극종별 스킬은 만들지 않습니다. 월극(粵劇, 두 체계를 섞고 광둥어로 씀)과 천극(고강은 곡패체)은 경계 사례로 다룹니다. 지금은 네 개의 스킬(판강체·곡패체 각각의 방법 스킬과 전본 자료집, 25건의 자료에서 추출)이 있고, 각 방법 스킬 첫머리에 출처가 달린 매체 경계표를 두었습니다. 다음 순서는 예극의 운철표와 월극(粵劇) 처리, 그다음 차오위·라오서의 화극, 마지막으로 뮤지컬입니다. 세로형 숏드라마와 AI 만화 드라마는 대상이 아닙니다. 새 매체는 "새 스킬 하나＋그 안의 경계표＋`sw-workflow` 진입표에 한 줄"로만 추가하고 일반 계층은 손대지 않습니다. 전문은 [English](README.md#stage-genres) / [中文版](README_ZH.md#舞台门类).

## 4계층 구조

장편영화는 1·3·4계층을, 시리즈는 네 계층 전부를 씁니다. 시리즈 계층은 일반 계층 옆에 더해지는 것이 아니라 "한 편의 영화를 위해 설계된 구조"를 "엔진＋시즌"으로 **대체**하기 때문입니다.

```
1. 일반 극작법   전제 · 구조 · 인물 · 대사 · 장면 · 포맷 · 프로젝트 진행
2. 매체 계층     시리즈 · 회차와 시즌 구조 · 엔진과 바이블 · 작가실 · 30분 코미디
                무대 · 중국 희곡: 판강체·곡패체 두 방법, 각각 전본 자료집
3. 전통과 업계   미국 · 일본 · 한국과 프랑스 · 중국 본토 · 비즈니스
4. 원전 코퍼스   체호프 · 오즈 · Succession · 드라마 사례집
```

| 계층 | 스킬 |
|---|---|
| 1 | `sw-workflow`(진행 관리와 `story-bible.md`) · `sw-story-structure` · `sw-premise-theme` · `sw-character-conflict` · `sw-dialogue` · `sw-scene-craft` · `sw-format-adaptation` |
| 2 | 시리즈: `sw-series-structure` · `sw-series-engine-bible` · `sw-writers-room` · `sw-sitcom-comedy`<br>무대: `sw-chinese-opera-banqiang` · `sw-chinese-opera-qupai`(두 성강 체계의 방법) · `sw-chinese-opera-banqiang-cases` · `sw-chinese-opera-qupai-cases`(전본 자료집: 쇄린낭·사가빈·백사전·조양구／두아원·구풍진·모란정·도화선·장생전) |
| 3 | `sw-american-case-studies` · `sw-japanese-screenwriting` · `sw-korean-french-screenwriting` · `sw-chinese-series-practice` · `sw-industry-business` |
| 4 | `chekhov-dramaturgy` · `ozu-screenplay-style` · `succession-series-writing` · `sw-series-case-studies` |

각 스킬은 `SKILL.md`(원칙·체크리스트·작업 순서)를 갖고, 대부분 `reference.md`(표·분석·인용)를 함께 둡니다. 어떤 스킬이 무엇을 담고 어느 책에서 왔는지에 대한 완전한 대조표는 [English README](README.md#how-the-skills-are-organised)에 있습니다.

한국 관련 부분: `sw-korean-french-screenwriting`은 한국과 프랑스의 방법(감정을 먼저 쓰기, 취재 우선, 약속으로서의 장르, 두 번의 반전, 대사는 마지막에, 공동 집필)을 다루고, `sw-series-case-studies`에는 노희경 『세상에서 가장 아름다운 이별』의 7장 구조·4부 매핑·가족 갈등망·이별 배치 분석이 들어 있습니다.

## 출처

**시나리오 작법 17권** — 시드 필드, 블레이크 스나이더, 로버트 맥키(*Story*와 *Dialogue*), 줄리언 혹스터, 닐 D. 힉스, 러요시 에그리, 리사 크론, 윌리엄 인딕, 리처드 월터, 웬디 제인 헨슨, 다이아몬드＆와이스먼, 에릭 보크, 메이펑, 류다펑 편, 루쥔, 하쿠 기요, 그 외.

**텔레비전 작법 15권** — 윌리엄 랩킨, 대니얼 칼비시, 파멜라 더글러스, 캠 밀러, 에마뉘엘 오베르, 골드버그＆랩킨, 닐 랜도, 에번 S. 스미스, 리처드 A. 블룸, 야오커우건, 장웨이, 장밍즈·쑹페이이, 자오빈빈.

**출간 대본·희곡 12권** — 체호프 희곡 전집, 오즈 야스지로 각본집, Jesse Armstrong *Succession: The Complete Scripts* I–IV, Aaron Sorkin *The West Wing Script Book*, David Chase 외 *The Sopranos*, Julian Fellowes *Downton Abbey* Season Two, Phoebe Waller-Bridge *Fleabag: The Scriptures*, 사카모토 유지 『꽃다발 같은 사랑을 했다』, 노희경 『세상에서 가장 아름다운 이별』.

완전한 서지는 [English README](README.md#source-books)를 참고하세요.

## 라이선스

개인 학습용. 인용은 원저자와 역자에게 귀속됩니다.

같은 발상을 일본 작곡·편곡에 적용한 자매 프로젝트: [japanese-composition-skills](https://github.com/jtydhr88/japanese-composition-skills).
