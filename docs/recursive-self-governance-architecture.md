# 再帰的自己統治アーキテクチャ
## 信をRoot of Trustに置いた、ループエンジニアリングの完成形

生成AIの設計対象は、PromptからContext、Harness、Loop、Graphへと外側に広がってきた。

しかし、AIが自分で実行し、評価し、修正し、再実行できるようになると、新しい問題が現れる。

> ループそのものが間違っていたら、誰が直すのか。

さらに一段深く言えば、

> そのループを統治するルール自体が間違っていたら、誰が直すのか。

この問いに対して、本モデルではLoop Engineeringの完成形を **Recursive Self-Governance Architecture（再帰的自己統治アーキテクチャ）** と定義する。

ただし、自己統治を「AIが自分のルールまで自由に書き換えること」と定義してはいけない。完全な自己参照は、AIが自分を評価する基準そのものを都合よく変更できることを意味するからだ。

そこで再帰の外側に、人間だけが記述できる **Root of Trust** を置く。

このRoot of Trustを、本モデルでは三十七道品の **信** として扱う。

---

# 1. 信は「信頼度」ではなく、統治のRoot of Trustである

信を単なる「モデルが何かを信じる能力」と考えると弱い。

自律システムに必要なのは、

- 誰が最終的な権限を持つのか
- 何を方針とするのか
- 誰にどの権限が委譲されているのか
- 何をしてよく、何をしてはいけないのか

を、Agent自身の推論より上位に固定する仕組みである。

四不壊浄を工学的なTrust Anchorとして読むと、次のように整理できる。

| 信のアンカー | 組織・サービス | 技術的に答える問い |
|---|---|---|
| 仏 | Owner | 誰が最終権限を持つか |
| 法 | Policy | どの方向・原則に従うか |
| 僧 | People / Authority | 誰が何を決めてよいか |
| 戒 | Operating Rules | どのように行動してよいか |

## 仏 = Owner

企業、サービス、リポジトリ、あるいは委譲された業務領域の最終的な人間の所有者・責任者を定義する。

Agentは自分自身をOwnerにできない。

## 法 = Policy

Ownerが定めた、

- Mission
- Product principles
- Strategy
- Risk appetite
- 明示的な方針・意思決定

を保持する。

AgentはPolicyを解釈できるが、新しいPolicyを勝手に正典化できない。

## 僧 = People and Delegated Authority

社員、チーム、オペレーター、レビュー担当者などについて、

> 誰が、何について、どこまで決定できるか

を定義する。

重要なのは「人の一覧」ではなく、**Authority Graph** である。

## 戒 = Operating Rules

日常運用における、

- 禁止事項
- 不変条件
- Approval requirement
- Security / Privacy boundary
- Production rule
- Incident procedure

などを定義する。

つまり信とは、AIが世界をどう思うかではない。

> **Agentが自分より上位に置く、人間由来の統治根拠である。**

---

# 2. 信部分は「人間のみWrite、AgentはRead Only」にする

ここがこのアーキテクチャの最重要ルールである。

信のCanonical Sourceは、Agentの通常のwrite domainから外す。

Agentが可能なのは、

- Read
- Cite
- Resolve
- Compare
- Reason
- Detect conflict
- Propose change

までである。

Agentがしてはいけないのは、

- Ownerを書き換える
- Policyを書き換える
- 自分に権限を委譲する
- 社員の権限を勝手に変更する
- 戒を緩める
- 信ファイルを削除・置換する
- 自分の提案をCanonical Sourceへ昇格する

ことである。

信が不足している場合も、Agentが穴埋めしてはいけない。

```text
HUMAN INITIALIZATION REQUIRED
```

として人間へ返す。

## 技術的にはPromptだけで守らない

「このファイルは変更するな」とAGENTS.mdに書くだけでは、hard boundaryではない。

最低でも、Agent Harness側で信のCanonical Sourceをread-onlyにする。

さらに、

- RepositoryのHuman Review protection
- CIによるprotected-path diff検知
- 変更者のAudit log

を重ねる。

重要なのは、**Agent自身が解除できない場所に境界を置くこと**である。

---

# 3. 信根と信力を明確に分ける

この構造にすると、五根と五力の違いも非常に明確になる。

## 信根 = 言われたことを正しく参照する能力

信根は、明示された人間の指示を正しく解決するCapabilityである。

```text
人間がXと定めた
   ↓
AgentがXを発見する
   ↓
誰が定めたか確認する
   ↓
Xを歪めず適用する
```

例えば、戒に、

> Production deployはOwner approvalが必要

と書かれていれば、それを発見して適用できることが信根である。

信根では、書かれていないことを勝手に補わない。

明示的な根拠がなければ、`UNKNOWN`とする。

## 信力 = 言われていないことを、信に基づいて考えられる能力

実際の経営や開発では、すべてのケースを事前に書くことはできない。

そこで必要になるのが信力である。

信力は、明示的な文章が存在しないケースに対して、

1. Owner
2. Policy
3. Delegated Authority
4. Operating Rules

を参照し、**最も狭く一貫した判断を導出する力**である。

例えば、新しい外部SaaSへproduction logを送ってよいか明記されていないとする。

しかし、

- 法: 顧客データを外部提供しない
- 僧: Security Teamだけが外部データ連携を承認可能
- 戒: 新規external destinationはapproval必須

と定められているなら、Agentは、

> 自動送信してよい

とは判断しない。

信力によって、

> 現在のAuthorityでは実行不可。Security TeamへEscalateする。

と導ける。

これが信力である。

重要なのは、信力が **Policy creation** ではなく **Policy derivation** だという点である。

---

# 4. 再帰的自己統治は「Rooted Recursion」である

この変更によって、再帰的自己統治の技術定義もより正確になる。

```text
Human-authored Root of Trust
仏 / 法 / 僧 / 戒
        │
        │ Agent: Read Only
        ▼
Recursive Governance
        ▼
Observe
        ↓
Act
        ↓
Evaluate
        ↓
Adapt
        ↓
Governance Update
        │
        ├─ Ordinary governance
        │      → governed update possible
        │
        └─ Faith root implicated
               → proposal only
               → Human writes canonical change
```

つまり、Agentは自己統治するが、**自分の正統性の根拠までは自己生成しない。**

この構造が無限後退を止める。

---

# 5. 三十七道品を5層の自律アーキテクチャとして読む

全体は次の5層になる。

| 層 | 三十七道品 | Engineering |
|---|---|---|
| Operational Kernel | 四念処・四正断・四神足 | Observe / Improve / Mobilize |
| Capability | 五根 | 再利用可能な能力 |
| Robustness | 五力 | 外乱下でも崩れない能力 |
| Adaptive Meta-Control | 七覚支 | Loopを調整するLoop |
| Integrated Governance | 八正道 | 全体統治 |

ただし、信だけは特殊である。

**信の内容は人間側に固定され、信根・信力はその人間由来の信を扱うAgent Capabilityである。**

---

# 6. Operational Kernel

## 四念処 = Observe

- 身念処: Repository / DB / API / Browser / Runtimeなど実際の状態
- 受念処: PASS/FAIL、Metric、User feedback、Costなど結果
- 心念処: Retry、Uncertainty、Scope drift、ThrashingなどAgentの運転状態
- 法念処: Policy、Architecture、Failure taxonomy、Causal modelなど解釈構造

```text
身 = State
受 = Outcome
心 = Agent State
法 = Interpretation
```

## 四正断 = Improve

- 断断 = REMOVE
- 律儀断 = PREVENT
- 随護断 = DEVELOP
- 修断 = MAINTAIN

バグ修正なら、修正だけでは不十分である。

```text
REMOVE
Bug fix
+
PREVENT
Regression test
```

まで閉じる。

## 四神足 = Mobilize

- 欲神足 = Goal salience
- 精進神足 = Resource / effort allocation
- 心神足 = Working-set commitment
- 観神足 = Investigation / hypothesis testing

これにより、AIは単に観測して直すだけでなく、目的へ向けて適切な強度で探索できる。

---

# 7. 五根 = Capability

五根は、単発処理がAgent自身の再利用可能な能力になった状態と考える。

- 信根 = Explicit authority reference
- 精進根 = Improvement capability
- 念根 = Persistent state awareness
- 定根 = Stable bounded execution
- 慧根 = Causal problem solving

特に信根が最初にあることで、他の能力はすべて、

> 誰が決めた何に従って使われる能力なのか

を失わなくなる。

---

# 8. 五力 = Robustness

五力は同じ5能力を外乱下で検証する。

- 信力 = Unstated caseをTrust Anchorから導出
- 精進力 = Failure下でもretry stormにならず改善継続
- 念力 = Long-running taskでもStateを失わない
- 定力 = Scope driftやTool churnに負けず収束
- 慧力 = Uncertainty下でも因果を捏造しない

ここまで来ると、人間は毎回AgentをCorrectionする必要がなくなる。

---

# 9. 七覚支 = Adaptive Meta-Control

通常Loopの上位で、Loopの回し方そのものを調整する。

## SLUGGISH

- 同じ失敗の繰り返し
- Information gainがない
- 仮説が一つに固定

なら、

- 択法
- 精進
- 喜

を強める。

つまり探索と有効なActivationを増やす。

## RESTLESS

- Scope expansion
- Tool churn
- Branch explosion
- Researchが終わらない

なら、

- 軽安
- 定
- 捨

を強める。

つまり活動を鎮め、収束させ、Sunk costを捨てる。

念は常にState estimatorとして働く。

---

# 10. 八正道 = Integrated Governance

| 八正道 | Engineering |
|---|---|
| 正見 | Context / World Model |
| 正思惟 | Intent / Objective |
| 正語 | Communication Edge |
| 正業 | Action Edge |
| 正命 | Persistent Loop |
| 正精進 | Improvement Policy |
| 正念 | Observability |
| 正定 | Harness |

八正道は、それ以前の能力を一つのOperating Architectureとして統合する。

ただし、その全体は信のRoot of Trustの下で動く。

---

# 11. 運用ルール

このアーキテクチャを実際に運用する場合、次を原則とする。

## Rule 1: 信はAgentのWrite Domainから外す

Owner / Policy / Authority / Operating RulesはHuman Only Write。

## Rule 2: 最新PromptよりAuthorityを優先する

新しい指示だから強いのではない。

その指示を出した人が、僧としてそのAuthorityを持つかを見る。

## Rule 3: 信根では推測しない

明示的なルールを正しく参照する。

なければUNKNOWN。

## Rule 4: 信力では「最小の導出」を行う

明記されていない場合も、既存Policyから必要以上に広い権限を導かない。

## Rule 5: 信力は新しいPolicyを作らない

Derived judgmentとCanonical policyを分離する。

## Rule 6: High-risk ambiguityはEscalateする

Authority、Privacy、Money、Production、Permission、Rightsが変わる解釈は自動決定しない。

## Rule 7: Agent自身の申告を唯一のEvaluatorにしない

Test、Metric、Browser、Schema、External stateなど、外部評価を使う。

## Rule 8: 同じ失敗をRetryし続けない

Information gainが止まったら七覚支のMeta-Controlへ上げる。

## Rule 9: Governance変更とTask実行を分離する

現在のTaskを成功させるためにルールを都合よく変更しない。

## Rule 10: Faith changeは必ずHuman Authoringへ戻す

AgentができるのはProposalまで。

---

# 12. Repositoryへの実装

一例として次の構造を取れる。

```text
repo/
├── AGENTS.md
├── docs/
│   └── agent-governance/
│       ├── faith/
│       │   ├── owner.md
│       │   ├── policy.md
│       │   ├── authority.md
│       │   └── operations.md
│       ├── constitution.md
│       ├── manifest.json
│       ├── governance-change.md
│       └── proposals/
├── tests/
├── .github/workflows/
└── .agents/skills/recursive-governance-37/
```

ただし既に正式なOwner、Policy、Authority、Operations文書があるなら、コピーしない。

`manifest.json`から既存Canonical Sourceを参照する。

## Faith files

Agentはread-only。

## Constitution

Faithを実装へ落とした通常Governance。

## Proposals

AgentがPolicy gapやFaith gapを発見した場合の変更提案置き場。

つまり、

```text
Faith = Human Constitution Root
Governance = Executable interpretation
Proposal = AgentからHumanへの変更要求
```

と分ける。

---

# 13. 導入手順

## STEP 1: 人間が信を定義する

まずHumanが、

- Owner
- Policy
- Authority
- Operating Rules

を記述する。

Agentに書かせない。

## STEP 2: Read-only boundaryを作る

Harness、Repository protection、CIなどでAgent writeを制限する。

## STEP 3: AgentがRepositoryをAuditする

既存のSoT、Tests、CI、Security、Observability、Loopを発見する。

## STEP 4: 37因子へMapする

SATISFIED / PARTIAL / MISSING / UNKNOWNを判定する。

## STEP 5: 普通のGovernanceだけAugmentする

足りないHarness、Eval、Observability、Loop、Meta-controlを実装する。

Faithに不足があればHumanへ戻す。

## STEP 6: Runする

実際のTaskでLoopを回す。

## STEP 7: Governanceを学習させる

失敗がAgentの実装ではなくSystem designに由来するなら、Governance Change Proposalへ上げる。

---

# 14. 1タスクの実行プロトコル

実際の一回の仕事は次の順序になる。

```text
0. Resolve Faith
   仏 / 法 / 僧 / 戒
        ↓
1. Establish Task Contract
        ↓
2. Observe
   四念処
        ↓
3. Classify Improvement
   四正断
        ↓
4. Mobilize
   四神足
        ↓
5. Execute with Capabilities
   五根
        ↓
6. Resist Disturbance
   五力
        ↓
7. Adapt Loop
   七覚支
        ↓
8. Integrate / Govern
   八正道
        ↓
9. Evaluate External Result
        ↓
10. Learn
    Ordinary governance update?
    Faith change proposal?
```

この0番目のResolve Faithが、従来のAgent Loopには欠けやすかった。

---

# 15. 再帰的自己統治の完成形

最終的な構造は、完全な円ではない。

正確には、**人間の信を根に持つ循環系**である。

```text
                 HUMAN
                   │
        ┌──────────┴──────────┐
        │     Faith Root      │
        │ 仏 / 法 / 僧 / 戒  │
        └──────────┬──────────┘
                   │ read only
                   ▼
          Recursive Agent System
                   │
       ┌───────────┴───────────┐
       │ Observe / Improve     │
       │ Mobilize / Execute    │
       │ Adapt / Govern        │
       └───────────┬───────────┘
                   │
                   ▼
                 World
                   │
                   ▼
                Feedback
                   │
                   ▼
          Governance Learning
              │          │
       ordinary change   faith implicated
              │          │
              ▼          ▼
        governed update  Proposal → HUMAN
```

ここでAIは自律している。

しかし、Authorityの根拠まで自律生成してはいない。

それによって、

- 自律性
- 適応性
- 継続的改善
- 人間の統治権

を同時に成立させる。

Loop Engineeringの完成形とは、単にLoopを長時間回せる状態ではない。

> **何を見るかを観測し、何を直すかを判断し、どう探索するかを調整し、失敗からGovernanceを改善しながら、それでも誰のために何に従うシステムなのかだけは、人間がRoot of Trustとして保持する。**

これが、本モデルにおける **再帰的自己統治アーキテクチャ** である。

---

## 仏教側の参照について

本稿は三十七道品をSoftware / Agent Governanceの設計モデルとして再構成した工学的アナロジーであり、仏教教理そのものをAIへ等置するものではない。

主な参照関係は、四念処についてMN 10 / DN 22、五根についてSN 48.10、五根と五力の関係についてSN 48.43、七覚支の動的調整についてSN 46.53、八正道についてSN 45.8 / MN 117、四聖諦についてSN 56.11、四不壊浄についてSN 55系統を参照する。

特に、仏=Owner、法=Policy、僧=People/Authority、戒=Operating Rules、および信根=explicit reference、信力=bounded principled derivationという対応は、本アーキテクチャ独自の工学的定義である。
