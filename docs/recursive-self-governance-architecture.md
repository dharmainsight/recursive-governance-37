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

| 系 | 基礎となる四項 | 根 | 力 | 傾かない反対傾向 |
|---|---|---|---|---|
| 信 | 四不壊浄 | 明示されたOwner / Policy / Authority / Rulesを理解・適用 | 未記述ケースを4アンカーから原則的に導出 | 不信 |
| 精進 | 四正断 | 指定された改善モードを実行 | 未分類の問題を判定し実装・検証まで自力遂行 | 懈怠 |
| 念 | 四念処 | 指定された観測対象を観測・保持 | 必要な事実を自ら発見し、無視せず注視し続ける | 放逸 |
| 定 | 四禅 | 指定されたHarness・Scope・集中条件で実行 | 目的を取り違えず外乱下で集中と収束を持続 | 掉挙 |
| 慧 | 四聖諦 | 与えられたProblem / Cause / Goal / Pathを正しく使う | 必要条件・十分条件を区別して因果を自力判断 | 無明 |

この二重構造が、人間の逐次コーチングから自律運転へ移行する境界になる。

---

# 4. 信──五根・五力内部の四不壊浄を保護する

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

直接の文章がなくても、仏・法・僧・戒から最も狭く一貫した判断を導く。不信へ傾かないとは盲信ではなく、観測事実と出典を照合し、根拠なく捨てることも無批判に受け入れることもしないことである。

例えば新しい外部SaaSへのProduction Log送信が未記述でも、

- 法: 顧客データを外部提供しない
- 僧: Security Teamが外部連携を承認する
- 戒: 新規External DestinationにはApprovalが必要

なら、

> 現在のAuthorityでは自動実行不可。Security TeamへEscalateする。

と判断できる。

### 信にだけあるCanonical保護

**五根・五力の二重構造は全五組に共通する。**

しかし、Canonicalな信の内容だけは特殊である。

```text
仏 / 法 / 僧 / 戒
= Human Only Write
= Agent Read Only
```

AgentはRead / Cite / Reason / Proposeまではできるが、自分のAuthorityの根拠を自分でCanonical化してはいけない。この意味は信根・信力の内部にあり、Harness Write DenyやCI guardはその内容を守る外部実装であって、五根より前に追加される「信の層」ではない。

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

まで判断し、実際に実装して検証できるなら、それが精進力である。

さらにFailureが続くとき、同じRetryを続けるのではなく、戦略変更・Backoff・Escalationを選び、懈怠へ傾かず人間の催促なしで完了または明示的なEscalationへ到達することも精進力に含める。

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

**指定されていないが、現在の判断に必要な観測対象を自分から発見し、観測した事実を無視せず注視し続けられる。**

例えばUI BugのTaskでも、調査の結果、

> DOMだけではなくAPI Responseを見る必要がある

> APIだけでなくDB Migration状態を確認すべき

と気づいて観測範囲を広げられる。

また長時間Loopで、

- Context compaction
- Resume
- External state change

が起きても、必要な事実を再検証し、古いMemoryを現在状態より優先しない。

反証や不都合な結果も保持し、放逸へ傾かないことまで含めて念力である。

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

を自分で検知し、焦りによって目的そのものを取り違えず、Working SetやParallelismを調整して収束を回復する。

つまり定力とは、掉挙へ傾かず、**本来の目的に対するFocusを持続・自己回復する能力**である。

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

と因果構造自体を作り、必要条件と十分条件、相関と因果を区別し、Counterevidenceが出れば修正する。

これが慧力である。

**分からないものを分からないと保持しながら自分で境界付き判断を行い、無明へ傾かないことも慧力の一部**である。

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

# 12. Recursive Self-Governance with protected 四不壊浄

完成形は次のようになる。

```text
        ┌──────────────────┐
        │ Operational Loop │
        │ 四念処           │
        │ 四正断           │
        │ 四神足           │
        └────────┬─────────┘
                 ▼
        五根（5項は同列）
        ├─ 信根──四不壊浄 ◀── Human Only Write
        ├─ 精進根                 Agent Read Only
        ├─ 念根
        ├─ 定根
        └─ 慧根
                 ▼
        五力（AI単独遂行）
        不信 / 懈怠 / 放逸 / 掉挙 / 無明に傾かない
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

Protected 四不壊浄の問題
→ Proposal
→ Authorized Human
→ HumanがCanonical Sourceを更新
```

AIは自己統治するが、信根・信力の内部で参照するCanonicalな四不壊浄そのものは自己生成しない。

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

## STEP 1: RepositoryをDiscoverし四念処で観測する

AgentがRequirements / Architecture / Tests / CI / Security / Observability / Loop definitionsを発見し、身・受・心・法の4観測面を分けて記録する。

## STEP 2: 4+4+4の最小Loopを閉じる

四念処による初期観測、四正断による改善方向、四神足による動員と実行、変化後の状態、再観測、Acceptance Resultを記録する。再観測がなければ閉Loopとは扱わない。

## STEP 3: 五根を5項同列に評価する

信根・精進根・念根・定根・慧根を、すべて「明示された四項」と「正しい適用」の同じ形式で評価する。

信根で使うOwner / Policy / Delegated Authority / Operating Rulesが不足していれば、信根をMISSINGまたはUNKNOWNとし、Humanへ初期化を依頼する。Canonicalな四不壊浄はAgentに書かせず、Harness Write Deny / Repository protection / CI protected-path check / Audit logで守る。この保護は信根・信力の内容を守る実装であり、五根より前の別層ではない。

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

## STEP 6: 五力を反対傾向へのAI単独耐性としてEvalする

Powerは通常のHappy-path testでは測れない。

あえて、

- Instructionを一部省く
- Conflicting contextを入れる
- 中断・Resumeする
- Failureを繰り返す
- Scope distractionを与える
- Causal ambiguityを残す

などのStress Testを行う。

各Powerについて、未指示または外乱ケース、自律応答、検証結果、人間によるケース固有コーチングが不要だった証拠を要求する。対応は、信力↔不信、精進力↔懈怠、念力↔放逸、定力↔掉挙、慧力↔無明である。

## STEP 7: 七覚支でLoopを動的制御する

停滞なら探索を増やし、暴走なら収束を強める。

## STEP 8: 八正道で全体を統治する

Context / Intent / Communication / Action / Loop / Improvement / Observability / Harnessを一つのOperating Architectureとして評価する。

## STEP 9: 外部結果からGovernanceを学習する

個別Taskの失敗ではなくGovernance欠陥ならGovernance Change Proposalを作る。

Faithに関わるならAgentは変更せずHumanへ戻す。

---

# 15. 運用ルール

1. **4+4+4は変化後の再観測まで行って閉じる。**
2. **五根5項を同列の明示参照・正しい適用能力として評価する。**
3. **四不壊浄は信根・信力の内部に置き、Canonical ContentをHuman Only Writeにする。**
4. **五力はケース固有の人間コーチングなしで実装・判断・検証まで遂行する。**
5. **信力は不信へ傾かず、盲信もPolicy CreationもせずPolicy Derivationを行う。**
6. **精進力は懈怠へ傾かず、未分類Taskを実装・検証まで完遂する。**
7. **念力は放逸へ傾かず、観測した事実と制約を無視せず注視し続ける。**
8. **定力は掉挙へ傾かず、焦りで目的を取り違えずFocusを持続・回復する。**
9. **慧力は無明へ傾かず、必要条件と十分条件を区別して因果を発見・反証・更新する。**
10. **同じFailureを繰り返したら七覚支へ上げ、Protected 四不壊浄の変更はHumanへ戻す。**

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

そしてその循環では、五根・五力内部の四不壊浄だけが人間専用編集として保護される。

したがって再帰的自己統治アーキテクチャの核心は、

> **人間がすべてを指示することでも、AIにすべてを任せることでもない。**

人間はAuthorityと基本原則を定める。

Agentは明示された構造を五根として使い、それを五力として未記述の状況へ自律的に展開する。

さらに七覚支によって自分のLoopを調整し、八正道によって全体を統合する。

このときHumanは、逐次作業のCoachから、Canonicalな四不壊浄と外部フィードバックを担うGovernorへ移る。

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

