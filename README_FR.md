# screenwriting-skills

[English](README.md) · [中文版](README_ZH.md) · [日本語](README_JA.md) · [한국어](README_KO.md)

24 compétences d'agent (« skills ») pour le scénario, l'écriture télévisuelle et la dramaturgie, destinées à [Claude Code](https://docs.anthropic.com/en/docs/claude-code/skills) et [OpenAI Codex](https://developers.openai.com/codex/build-skills). Distillées de 45 ouvrages de méthode et de 23 volumes de scénarios, partitions et pièces publiés (chinois, américains, britanniques, japonais et coréens).

Les fichiers `SKILL.md` suivent la norme ouverte [agentskills.io](https://agentskills.io) et sont partagés par les deux agents : une seule installation, et les deux fonctionnent.

**Posez vos questions en français.** Le corps des skills est rédigé en chinois, parce que la plupart des sources sont des originaux chinois ou des traductions chinoises. C'est un détail d'implémentation, pas une restriction : demandez en français, vous obtenez du français. Voir [Prise en charge multilingue](#prise-en-charge-multilingue) pour comprendre pourquoi il n'existe qu'un seul arbre source et non cinq.

## Installation

### Claude Code

#### Place de marché de plugins (recommandé)

```
/plugin marketplace add jtydhr88/screenwriting-skills
/plugin install screenwriting@screenwriting-skills
```

Les skills s'invoquent ensuite par `/screenwriting:<skill>`, par exemple `/screenwriting:sw-dialogue`.

#### Personnel (tous les projets)

```bash
git clone https://github.com/jtydhr88/screenwriting-skills.git
cp -r screenwriting-skills/plugins/screenwriting/skills/* ~/.claude/skills/
```

#### Par projet

```bash
mkdir -p .claude/skills
cp -r screenwriting-skills/plugins/screenwriting/skills/* .claude/skills/
```

### Codex (CLI / application de bureau ChatGPT / extension IDE)

```bash
codex plugin marketplace add jtydhr88/screenwriting-skills

# Puis, dans l'application de bureau ChatGPT ou dans Codex CLI :
# Plugins → sélectionner « Screenwriting Skills » → Install
```

Pour une installation personnelle, copiez vers `~/.agents/skills/` ; par projet, vers `.agents/skills/`. `/skills` liste les skills disponibles, `$sw-story-structure` en invoque un explicitement.

## Exemples d'usage

```
# « Découpe ma série en 12 épisodes en actes et place les fins d'acte »
# → sw-series-structure

# « Ces dialogues sont trop explicites, reprends cette scène »
# → sw-dialogue + sw-scene-craft

# « Transforme ce roman en séquencier d'une série de 40 épisodes »
# → sw-chinese-series-practice + sw-series-engine-bible

# « Ouvre un projet et garde la trace de où j'en suis »
# → sw-workflow
```

## Prise en charge multilingue

**Un seul arbre source, toutes les langues à l'exécution.** Les skills sont écrits une fois, en chinois, et l'agent livre dans la langue de votre question.

C'est une décision réfléchie, et ce n'était pas la première. Il y a eu une édition anglaise, un plugin parallèle `screenwriting-en` traduisant les 20 skills, proposée dans [#3](https://github.com/jtydhr88/screenwriting-skills/issues/3), réalisée et fusionnée. Elle a depuis été supprimée. L'argument qui l'a emporté vaut identiquement pour toutes les autres langues : si un lecteur qui ne lit pas le chinois mérite un arbre traduit, un lecteur qui ne lit pas l'anglais le mérite aussi, et la demande suivante sera le japonais, puis le coréen, puis le français, puis le russe. Cinq langues, ce sont 230 fichiers qui divergent chacun de leur côté, sans rien pour signaler lequel est périmé. La traduction elle-même coûte peu. Le coût réel, c'est qu'**une fois le premier fork accepté, il ne reste plus aucune raison de principe pour refuser le second**.

La ligne est donc tracée à la source, et l'exécution fait le reste :

- **La langue de sortie suit celle de la question.** Demandez en français, vous obtenez du français. Aucun réglage, aucune installation séparée.
- **La terminologie est ancrée au terme d'origine.** Le vocabulaire de ce métier est à l'origine anglais : *logline*, *act out*, *beat sheet*, *showrunner*, *staff writer*. Le chinois des ouvrages sources (計程繩, 出幕, 節拍表, 劇目管理人, 試用編劇) est la traduction, et les traducteurs n'ont pas fait les mêmes choix. [`sw-workflow/terms.md`](plugins/screenwriting/skills/sw-workflow/terms.md) rattache chaque notion à son terme d'origine : l'agent **restitue** le mot au lieu d'en inventer un. Et cette table unique sert toutes les langues à la fois, car un scénariste francophone dit lui aussi *act out* et *logline*.
- **Les termes sans équivalent gardent leur forme d'origine, avec une glose.** 戏眼 et 扣子 sortent sous la forme `戏眼 (xìyǎn — l'attrait central d'un épisode, énonçable en une phrase)`.
- **Votre scénario reste dans la langue de votre scénario.** Discuter en français d'un scénario chinois est courant : la conversation change de langue, pas le texte.

Ce que l'on abandonne en échange, c'est l'**auditabilité** : sans lire le chinois, vous ne pouvez pas lire le fichier d'instructions lui-même, seulement le compte rendu qu'en fait l'agent. C'est un coût réel, et c'est la seule chose que l'édition anglaise supprimée achetait véritablement. Elle ne valait pas une charge de maintenance quintuple et permanente.

**Les README relèvent d'un autre régime** et sont traduits : ils sont courts, stables, et c'est ce qu'un nouveau venu rencontre en premier. Les README japonais, coréen et français s'arrêtent délibérément à l'installation, à la structure et à cette politique ; les tableaux détaillés des skills et la bibliographie restent dans les versions [anglaise](README.md) et [chinoise](README_ZH.md) , exactement pour la raison ci-dessus.

## Les genres de scène

Le cinéma et la télévision sont couverts. La scène l'est en partie, le reste est prévu, et une seule règle décide de ce qui reçoit un skill : **le genre fait-il écrire au modèle quelque chose dont la structure, le format ou les règles de langue diffèrent ?** Si oui, un skill à part ; si seuls le sujet ou le style changent, un cas d'étude dans un skill existant.

L'opéra chinois, ce sont **deux écritures**. L'axe qui compte est le système vocal ; le genre régional (剧种) vient ensuite. Dans le **système qupai** (曲牌体 : 元杂剧, 明清传奇, 昆曲) le texte est rempli dans un air à patron fixe (nombre de vers, longueurs, tons imposés) ; un 杂剧 tient en quatre 折 et un 楔子, un seul rôle chantant tout un 折 ; un 传奇 se découpe en 出. Dans le **système banqiang** (板腔体 : 京剧, 豫剧, 越剧, 秦腔, 评剧, 沪剧) le texte se construit en distiques de sept ou dix caractères variés par le mètre (板式), tout rôle peut chanter, et l'unité est la 场. Structure et méthode du chant diffèrent : deux skills. Les genres régionaux d'un même système ne diffèrent que par la table de rimes (京剧十三辙 ou 豫剧中州韵) et la table des mètres consultées, même méthode, autre table, donc des annexes de référence. 粤剧 (les deux systèmes mêlés, et en cantonais) et 川剧 (dont le 高腔 est qupai) sont traités comme cas limites. Quatre skills existent aujourd'hui (une méthode et une bibliothèque de textes intégraux par système vocal, distillées de 25 sources), chaque skill de méthode s'ouvrant sur une table de frontière de médium sourcée. Sont prévus, dans l'ordre : la table de rimes du 豫剧 et le cas du 粤剧, puis le théâtre parlé de 曹禺 et 老舍, et en dernier la comédie musicale. Le micro-drama vertical et le drama en bande dessinée généré par IA ne sont pas au programme. Un médium s'ajoute par « un skill nouveau, sa table de frontière, une ligne dans la table d'entrée de `sw-workflow` », sans toucher à la couche générale. Texte complet : [English](README.md#stage-genres) / [中文版](README_ZH.md#舞台门类).

## Les quatre couches

Un long métrage utilise les couches 1, 3 et 4 ; une série les utilise toutes les quatre, car la couche série ne s'ajoute pas à côté de la couche générale : elle **remplace** la « structure conçue pour un film » par une logique de moteur et de saison.

```
1. Dramaturgie générale  prémisse · structure · personnage · dialogue · scène · format · conduite de projet
2. Couche médium         série · structure de l'épisode et de la saison · moteur et bible · writers' room · comédie de 30 min
                         scène · opéra chinois : les méthodes banqiang et qupai, chacune avec une bibliothèque de textes intégraux
3. Traditions et métier  Amérique · Japon · Corée et France · Chine continentale · le business
4. Corpus de référence   Tchekhov · Ozu · Succession · études de cas télévisuelles
```

| Couche | Skills |
|---|---|
| 1 | `sw-workflow` (conduite de projet et `story-bible.md`) · `sw-story-structure` · `sw-premise-theme` · `sw-character-conflict` · `sw-dialogue` · `sw-scene-craft` · `sw-format-adaptation` |
| 2 | Série : `sw-series-structure` · `sw-series-engine-bible` · `sw-writers-room` · `sw-sitcom-comedy`<br>Scène : `sw-chinese-opera-banqiang` · `sw-chinese-opera-qupai` (les méthodes des deux systèmes vocaux) · `sw-chinese-opera-banqiang-cases` · `sw-chinese-opera-qupai-cases` (textes intégraux : 锁麟囊, 沙家浜, 白蛇传, 朝阳沟 / 窦娥冤, 救风尘, 牡丹亭, 桃花扇, 长生殿) |
| 3 | `sw-american-case-studies` · `sw-japanese-screenwriting` · `sw-korean-french-screenwriting` · `sw-chinese-series-practice` · `sw-industry-business` |
| 4 | `chekhov-dramaturgy` · `ozu-screenplay-style` · `succession-series-writing` · `sw-series-case-studies` |

Chaque skill possède un `SKILL.md` (principes, listes de contrôle, marche à suivre), et presque tous un `reference.md` (tableaux, analyses détaillées, citations). Le tableau complet de ce que contient chaque skill et des ouvrages dont il provient se trouve dans le [README anglais](README.md#how-the-skills-are-organised).

Côté français : `sw-korean-french-screenwriting` rassemble les méthodes coréennes et françaises : écrire l'émotion d'abord, la documentation avant tout, le genre comme promesse faite au spectateur, les deux renversements, le dialogue écrit en dernier, l'écriture collective.

## Sources

**Méthode du scénario, 17 ouvrages** : Syd Field, Blake Snyder, Robert McKee (*Story* et *Dialogue*), Julian Hoxter, Neill D. Hicks, Lajos Egri, Lisa Cron, William Indick, Richard Walter, Wendy Jane Henson, Diamond & Weissman, Eric Bork, Mei Feng, Liu Dapeng (dir.), Lu Jun, Haku Kiyo (dir.).

**Méthode télévisuelle, 15 ouvrages** : William Rabkin, Daniel Calvisi, Pamela Douglas, Kam Miller, Emmanuel Oberg, Goldberg & Rabkin, Neil Landau, Evan S. Smith, Richard A. Blum, Yao Kougen, Zhang Wei, Zhang Mingzhi & Song Peiyi, Zhao Binbin.

**Scénarios et pièces publiés, 12 volumes** : Œuvres théâtrales complètes de Tchekhov, Scénarios d'Ozu Yasujirō, Jesse Armstrong *Succession: The Complete Scripts* I–IV, Aaron Sorkin *The West Wing Script Book*, David Chase et al. *The Sopranos*, Julian Fellowes *Downton Abbey* saison 2, Phoebe Waller-Bridge *Fleabag: The Scriptures*, Sakamoto Yūji *Au bout du compte, je t'aimais*, Noh Hee-kyung *Le plus bel adieu du monde*.

Bibliographie complète dans le [README anglais](README.md#source-books).

## Licence

Usage d'étude personnelle. Les citations demeurent la propriété de leurs auteurs et traducteurs.

Projet frère, même idée appliquée à la composition et à l'arrangement japonais : [japanese-composition-skills](https://github.com/jtydhr88/japanese-composition-skills).
