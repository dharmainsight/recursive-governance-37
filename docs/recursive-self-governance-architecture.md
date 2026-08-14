# 再帰的自己統治アーキテクチャ
## 五根と五力の二重構造を中核にした、ループエンジニアリングの完成形

生成AIの設計対象は、Prompt、Context、Harness、Loop、Graphへと外側に広がってきた。

しかし、AIが自分で実行し、評価し、修正し、再実行できるようになると、次の問題が現れる。

> ループそのものが間違っていたら、誰が直すのか。

さらに、

> ループを統治するルール自体が間違っていたら、誰が直すのか。

本モデルではLoop Engineeringの完成形を **Recursive Self-Governance Architecture（再帰的自己統治アーキテクチャ）** と定義する。

ただし、これはAIが自分のルールを無制限に書き換える仕組みではない。

人間由来の統治根拠を持ちながら、その内側で観測・改善・探索・実行・自己調整・統治学習を再帰的に行うシステムである。

その構造を三十七道品の工学的アナロジーとして整理する。

---

# 1. 全体構造

三十七道品を5層として読む。

| 層 | 三十七道品 | Engineering |
|---|---|---|
| Operational Kernel | 四念処・四正断・四神足 | Observe / Improve / Mobilize |
| Capability | 五根 | 明示された構造を正しく使う能力 |
| Robustness / Autonomy | 五力 | 明示されていない状況にも自律的に同じ構造を適用する力 |
| Adaptive Meta-Control | 七覚支 | Loopそのものを調整するLoop |
| Integrated Governance | 八正道 | 認識・意図・通信・行為・継続・改善・観測・実行を統合 |

ここで重要なのは、**五根と五力の二重構造が五つすべてに共通する**ことである。

以前の整理では信根と信力だけを、

- 信根 = 明示されたものを参照する
- 信力 = 明示されていないものを原則から導く

と強く分けていた。

しかし本来、この構造は精進・念・定・慧にも同じように適用すべきである。

---

# 2. 五根と五力は「明示参照」と「自律導出」の二重構造

本モデルでは五根と五力を次のように定義する。

## 五根 = Explicit Reference Capability

人間、Repository、Harness、Task、観測結果などによって**明示された構造を正しく発見し、理解し、適用できる能力**。

## 五力 = Autonomous Derivation + Robustness

ケースが明示的に分類されていなくても、**同じ基礎構造から自分で必要な適用方法を導出し、外乱の中でもその能力を維持できる力**。

つまり、

```text
根
= 言われた構造を正しく使える

力
= 言われていないケースでも
  その構造から自分で考えて使える
```

である。

五力は五根とは別の能力ではない。

**同じ能力が、人間の逐次的な分類・指示なしでも働く状態**である。

---

# 3. 五つの二重構造

| 系 | 基礎となる四項 | 根 | 力 |
|---|---|---|---|
| 信 | 四不壊浄 | 明示されたOwner / Policy / Authority / Rulesを参照 | 未記述ケースを4アンカーから原則的に導出 |
| 精進 | 四正断 | 指定された改善モードを実行 | 未分類の問題から必要な改善モードを自律判定 |
| 念 | 四念処 | 指定された観測対象を観測・保持 | 必要なのに指定されていない観測対象まで自律的に発見 |
| 定 | 四禅 | 指定されたHarness・Scope・集中条件で実行 | 外乱下で自分からFocusを回復し収束させる |
| 慧 | 四聖諦 | 与えられたProblem / Cause / Goal / Pathを正しく使う | 不完全な情報から因果構造そのものを発見・修正する |

この二重構造が、人間の逐次コーチングから自律運転へ移行する境界になる。

---

# 4. 信──四不壊浄をRoot of Trustとして実装する

信の基礎を四不壊浄として、組織・サービスのTrust Anchorへ写像する。

| 四不壊浄 | 組織・サービス | 問い |
|---|---|---|
| 仏 | Owner | 誰が最終権限を持つか |
| 法 | Policy | 何を目的・方針とするか |
| 僧 | People / Delegated Authority | 誰が何を決めてよいか |
| 戒 | Operating Rules | どのように行動してよいか |

## 信根

人間が明示したものを正しく参照する。

例えば、

> Production deployにはOwner approvalが必要

と戒に記述されていれば、それを発見して適用できる。

明示的な根拠がなければ`UNKNOWN`とする。

## 信力

直接の文章がなくても、仏・法・僧・戒から最も狭く一貫した判断を導く。

例えば新しい外部SaaSへのProduction Log送信が未記述でも、

- 法: 顧客データを外部提供しない
- 僧: Security Teamが外部連携を承認する
- 戒: 新規External DestinationにはApprovalが必要

なら、

> 現在のAuthorityでは自動実行不可。Security TeamへEscalateする。

と判断できる。

### 信だけの特殊性

**五根・五力の二重構造は全五組に共通する。**

しかし、Canonicalな信の内容だけは特殊である。

```text
仏 / 法 / 僧 / 戒
= Human Only Write
= Agent Read Only
```

AgentはRead / Cite / Reason / Proposeまではできるが、自分のAuthorityの根拠を自分でCanonical化してはいけない。

---

# 5. 精進──四正断を明示実行から自律診断へ

四正断を次の四つの改善方向として扱う。

```text
断断   = REMOVE
律儀断 = PREVENT
随護断 = DEVELOP
修断   = MAINTAIN
```

## 精進根

人間やTaskが、

> これはBug Fixである

> Regressionを防止せよ

と明示している場合に、対応する改善モードを正しく実行できる能力。

例えば、

```text
Bugを修正
= REMOVE

Regression Testを追加
= PREVENT
```

と処理する。

## 精進力

誰も分類していなくても、現在状態から必要な改善モードを自律的に判定する。

例えばIssueには単に、

> Loginが壊れている

としか書かれていない。

しかしAgentが調査して、

```text
既存Bugを除去
→ REMOVE

同型Bugの再発を防止
→ PREVENT

Monitoring不足を補う
→ DEVELOP
```

まで判断できるなら、それが精進力である。

さらにFailureが続くとき、同じRetryを続けるのではなく、戦略変更・Backoff・Escalationを選べることも精進力に含める。

---

# 6. 念──四念処を指定観測から自律観測へ

四念処を4種類のObservabilityとして扱う。

```text
身 = Repository / Runtime / External State
受 = Outcome / Quality Signal
心 = Agent / Loop State
法 = Policy / Architecture / Causal Model
```

## 念根

Taskや運用ルールで、

> Test結果を確認する
> DB Schemaを見る
> Retry回数を記録する

と指定されている場合、その観測対象を忘れず追跡できる。

## 念力

**指定されていないが、現在の判断に必要な観測対象を自分から発見できる。**

例えばUI BugのTaskでも、調査の結果、

> DOMだけではなくAPI Responseを見る必要がある

> APIだけでなくDB Migration状態を確認すべき

と気づいて観測範囲を広げられる。

また長時間Loopで、

- Context compaction
- Resume
- External state change

が起きても、必要な事実を再検証し、古いMemoryを現在状態より優先しない。

これが念力である。

---

# 7. 定──明示されたHarnessから自己収束能力へ

定は、工学的には「集中力」という心理語より、**Executionを一つの目的へ収束させる能力**として読む。

四禅はここでは工学的アナロジーとして、

```text
1. instruction-heavy directed execution
2. unified execution
3. stable execution
4. invariant-led neutral execution
```

という成熟として扱う。

## 定根

明示された、

- Scope
- Harness
- Tool limit
- Branch rule
- Validation cadence
- Budget
- Stop condition

を守って集中できる。

## 定力

誰も逐次的に、

> Scopeを狭めろ
> Agentを減らせ
> Researchを止めろ

と言わなくても、

- Scope drift
- Tool churn
- Branch explosion
- Excessive parallelism
- Endless research

を自分で検知し、Working SetやParallelismを調整して収束を回復する。

つまり定力とは、**Focusの自己回復能力**である。

---

# 8. 慧──四聖諦を与えられた因果から因果発見へ

四聖諦をProblem Solving Modelとして使う。

```text
苦 = Problem / Loss
集 = Cause
滅 = Resolved State
道 = Path / Intervention
```

## 慧根

例えば人間が、

```text
Problem:
Signup conversion低下

Cause:
Email verification failure

Desired State:
verification成功率99.9%

Path:
provider切替 + retry改善
```

と構造化している場合、それを正しく理解し、Causeへ介入し、Desired Stateを検証できる。

## 慧力

実際にはIssueに、

> Signupが減った

としか書かれていないこともある。

そのときAgentが、

```text
苦
何が悪化したのか観測
↓
集
候補原因を複数生成
↓
Discriminating Test
↓
滅
何を解決状態とするか定義
↓
道
原因に効く介入を設計
```

と因果構造自体を作り、Counterevidenceが出れば修正する。

これが慧力である。

**分からないものを分からないと保持することも慧力の一部**である。

---

# 9. 五根から五力への移行がHuman-in-the-Loopを変える

五根の段階では、能力は存在するが、人間がケースを整理して渡す必要がある。

```text
Human
↓
分類・指示
↓
Agent
↓
実行
```

五力になると、分類そのものをAgentが担える。

```text
Human
↓
Goal / Authority / Boundary
↓
Agent
├─ 状況を観測
├─ 必要な枠組みを選ぶ
├─ 未記述ケースを導出
├─ 外乱に耐える
└─ 必要ならEscalate
```

したがって、Human-on-the-Loopへ移行できるかどうかは、

> 五根を持っているか

ではなく、

> **五力が実証されているか**

で判断するべきである。

---

# 10. 七覚支──五力を含むLoop全体を動的調整する

七覚支はMeta-Controlとして働く。

## SLUGGISH

- 同じ失敗
- Information Gainがない
- 仮説が固定
- 行動量が不足

なら、

```text
択法
精進
喜
```

を強める。

## RESTLESS

- Scope Expansion
- Tool Churn
- Branch Explosion
- Research過多

なら、

```text
軽安
定
捨
```

を強める。

念はどちらでもState Estimatorとして働く。

七覚支は、

> 何をするか

ではなく、

> **Loopをどのような状態で回すか**

を調整する。

---

# 11. 八正道──Integrated Governance

| 八正道 | AI Engineering |
|---|---|
| 正見 | Context / World Model |
| 正思惟 | Intent / Objective |
| 正語 | Communication Edge |
| 正業 | Action Edge |
| 正命 | Persistent Loop |
| 正精進 | Improvement Policy |
| 正念 | Observability |
| 正定 | Harness |

八正道では、それ以前の機能をSystem Architectureとして統合する。

```text
正精進
→ 四正断を全Systemへ統合

正念
→ 四念処をObservability Architectureへ統合

正定
→ 定をHarness / Execution Controlへ統合

正見
→ 四聖諦による因果理解をContextへ統合
```

そして道諦として八正道自身が再び現れるため、構造は再帰的になる。

---

# 12. Rooted Recursive Self-Governance

完成形は次のようになる。

```text
                 HUMAN
                   │
        Human-authored Faith Root
        仏 / 法 / 僧 / 戒
                   │
              Agent Read Only
                   ▼
        ┌──────────────────┐
        │ Operational Loop │
        │ 四念処           │
        │ 四正断           │
        │ 四神足           │
        └────────┬─────────┘
                 ▼
              五根
        Explicit Capability
                 ▼
              五力
 Autonomous Derivation / Robustness
                 ▼
              七覚支
        Adaptive Meta-Control
                 ▼
              八正道
       Integrated Governance
                 ▼
               World
                 │
                 ▼
              Feedback
                 │
                 └──────────────↺
```

Governance Learningの結果は二つに分かれる。

```text
Ordinary Governanceの問題
→ Governed Update

Faith Rootの問題
→ Proposal
→ Authorized Human
→ HumanがCanonical Sourceを更新
```

AIは自己統治するが、自分のAuthorityの根拠そのものは自己生成しない。

---

# 13. Repositoryへの実装

一例として、

```text
repo/
├── AGENTS.md
├── docs/
│   └── agent-governance/
│       ├── manifest.json
│       ├── constitution.md
│       ├── faith/
│       │   ├── owner.md
│       │   ├── policy.md
│       │   ├── authority.md
│       │   └── operations.md
│       ├── proposals/
│       └── run-record.json
├── .agents/skills/
├── tests/
└── .github/workflows/
```

とする。

ただし既存のCompany Policy、ADR、Permission MatrixなどがCanonicalならコピーしない。

`manifest.json`から参照する。

```text
AGENTS.md
= Map

Existing Canonical Docs
= Source of Truth

Tests / IAM / CI / Sandbox
= Enforcement
```

と分離する。

---

# 14. 実践方法

## STEP 1: Humanが信を初期化する

Owner / Policy / Delegated Authority / Operating RulesをHumanが定義する。

AgentにはCanonical Faithを書かせない。

## STEP 2: Faithを技術的にRead Only化する

Promptだけでなく、

- Harness Write Deny
- Repository protection
- CI protected-path check
- Audit log

を使う。

## STEP 3: RepositoryをDiscoverする

Agentが、

- Requirements
- Architecture
- Tests
- CI
- Security
- Observability
- Loop definitions

を発見する。

## STEP 4: 37因子へMapする

各因子を、

```text
SATISFIED
PARTIAL
MISSING
UNKNOWN
N/A
```

で評価する。

## STEP 5: 五根と五力を必ず別評価する

例えば、

```text
念根 = SATISFIED
念力 = PARTIAL
```

なら、

> 指示された状態は追跡できるが、必要な未指定観測を自分から発見する能力が弱い

という意味になる。

同様に、

```text
慧根 = SATISFIED
慧力 = MISSING
```

なら、

> 明示されたRoot Causeは扱えるが、自分でRoot Causeを発見する能力はまだない

と判断できる。

## STEP 6: 不足するPowerをEvalする

Powerは通常のHappy-path testでは測れない。

あえて、

- Instructionを一部省く
- Conflicting contextを入れる
- 中断・Resumeする
- Failureを繰り返す
- Scope distractionを与える
- Causal ambiguityを残す

などのStress Testを行う。

## STEP 7: 七覚支でLoopを動的制御する

停滞なら探索を増やし、暴走なら収束を強める。

## STEP 8: 八正道で全体を統治する

Context / Intent / Communication / Action / Loop / Improvement / Observability / Harnessを一つのOperating Architectureとして評価する。

## STEP 9: 外部結果からGovernanceを学習する

個別Taskの失敗ではなくGovernance欠陥ならGovernance Change Proposalを作る。

Faithに関わるならAgentは変更せずHumanへ戻す。

---

# 15. 運用ルール

1. **五根と五力を全5組で別々に評価する。**
2. **根は明示参照、力は自律導出＋外乱耐性として扱う。**
3. **信だけはCanonical ContentをHuman Only Writeにする。**
4. **信力はPolicy CreationではなくPolicy Derivationである。**
5. **精進力は未分類Taskを自分で四正断へ分類する。**
6. **念力は未指定だが必要な観測を自分で発見する。**
7. **定力はFocusを自分で回復する。**
8. **慧力は因果モデル自体を発見・反証・更新する。**
9. **同じFailureを繰り返したらRetryではなく七覚支のMeta-Controlへ上げる。**
10. **Task変更とGovernance変更を分離し、Faith変更はHumanへ戻す。**

---

# 16. ループエンジニアリングの完成形

最終的に、自律性とは単にAgentが自分でActionできることではない。

```text
Observe
↓
Improve
↓
Mobilize
↓
Explicit Capability / 五根
↓
Autonomous Derivation & Robustness / 五力
↓
Adaptive Meta-Control / 七覚支
↓
Integrated Governance / 八正道
↓
World
↓
Feedback
↺
```

そしてその循環は、人間が定めた信のRoot of Trustに根づいている。

したがって再帰的自己統治アーキテクチャの核心は、

> **人間がすべてを指示することでも、AIにすべてを任せることでもない。**

人間はAuthorityと基本原則を定める。

Agentは明示された構造を五根として使い、それを五力として未記述の状況へ自律的に展開する。

さらに七覚支によって自分のLoopを調整し、八正道によって全体を統合する。

このときHumanは、逐次作業のCoachから、Root of Trustと外部フィードバックを担うGovernorへ移る。

これが、ループエンジニアリングの完成形としての**再帰的自己統治アーキテクチャ**である。

---

## 注記

本稿は三十七道品を自律Agent / Software Governanceの設計モデルとして再構成した工学的アナロジーであり、仏教教理そのものとの同一性を主張するものではない。

特に、

```text
五根 = Explicit Reference Capability
五力 = Autonomous Derivation + Robustness

信: 四不壊浄
精進: 四正断
念: 四念処
定: 四禅
慧: 四聖諦
```

という構造は本モデルの工学的定義である。

仏教側では四念処についてMN 10 / DN 22、五根についてSN 48.10、五根と五力の関係についてSN 48.43、七覚支についてSN 46系、八正道についてSN 45.8 / MN 117、四聖諦についてSN 56.11、四不壊浄についてSN 55系を主要な参照点とする。
