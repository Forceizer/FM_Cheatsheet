
> [!NOTE] Notation
> Let $P_k$ be the statement that, for some positive integer $n$, such that $[\text{condition}]$ `(if there is a specific domain)`,
> $$\large \text{Statement} $$
> For the **base case** $n=1$, `(or whatever is the minimum)`
> $$\large [\text{Proof that the statement is true for }n=1] $$
> Assume that, for some positive integer $n=k$, such that $[\text{condition}]$ `(if there is a specific domain)`, 
> $$\large \text{Statement with } k \text{ instead of } n $$
> Then, for $n=k+1$,
> $$\large [\text{Proof for n=k+1}] $$
> $\large \therefore P_k \Rightarrow P_{k+1}$
> As $P_1$ `(or with the minimum)` is true, and $P_k \Rightarrow P_{k+1}$, it is true that for all positive integers $n$, such that $[\text{condition}]$ `(if there is a specific domain)`,
> $$\large \text{Statement} $$
#### Special Case
##### Using Two Base Cases
![[FP1 Induction WS 2_1_00000_updated.png]]
This works as since $P_1$ is true and $P_2$ is true, then, by using $n=k+2$, we can get to any integer, and as $P_k \Rightarrow P_{k+2}$, we know that it will be true for that integer.
- With **$k=1$**, $n=1+2=3$
- With **$k=2$**, $n=2+2=4$
- With **$k=3$**, $n=3+2=5$  `(we have established that P₃ is true as P₁ ⇒ P₃)`
- $…$
#### Types
##### Formula
![[FP1 Induction WS_1_00000_updated.png]]
![[FP1 Induction WS_1_00001_updated.png]]
##### Summation
![[FP1 Induction WS_2_00000_updated.png]]
![[FP1 Induction WS_2_00001_updated.png]]
##### Matrices
![[FP1 Induction WS_3_00000_updated.png]]
![[FP1 Induction WS_3_00001_updated.png]]
##### Inequality
###### Informal
![[FP1 Induction WS_4_00000_updated.png]]
###### Formal
![[Formal Inequality Induction.jpg]]
##### Sequences
![[FP1 Induction WS_5_00000_updated.png]]
##### Divisibility
![[FP1 Induction WS_6_00000_updated.png]]
##### Differentiation
![[FP1 Induction WS_7_00000_updated.png]]
![[FP1 Induction WS_7_00001_updated.png]]
---
![[FP1 Induction WS_8_00000_updated.png]]
![[FP1 Induction WS_8_00001_updated.png]]
![[FP1 Induction WS_8_00002_updated.png]]