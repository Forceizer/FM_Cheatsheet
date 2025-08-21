Non-Parametric Tests are used when a set of data cannot be modelled into a distribution.

| Type of test      | Test                                    | Assumptions                                                                                                                                                                            |
| ----------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single sample** | Sign test                               | • The data are **independent**                                                                                                                                                         |
|                   | Wilcoxon signed-rank test               | • The underlying data are **symmetric** <br> • The data are **independent**                                                                                                            |
| **Two sample**    | Paired sign test                        | • The data are in **matched pairs**<br> • The data are **independent** <br> • Groups of data must be of **equal size**                                                                 |
|                   | Wilcoxon matched-pairs signed-rank test | • The data are in **matched pairs** <br> • The differences between matched pairs are **symmetric** <br> • The data are **independent** <br> • Groups of data must be of **equal size** |
|                   | Wilcoxon rank-sum test                  | • The two samples are **independent** <br> • The underlying data are **symmetric**                                                                                                     |
#### Sign Test
For any set of data of size $\large n$ where it is believed that the population **median** is $\large m$, one can perform a sign test as such:
1. Consider a set of data, where the **median** is believed to be $\large 330$. Let’s carry out a two-tailed sign test on it at the $\large 5\%$ significance level.
	
	| | | | |
	|---|---|---|---|
	| $\large 347$ | $\large 325$ | $\large 340$ | $\large 311$ |
	| $\large 335$ | $\large 349$ | $\large 318$ | $\large 344$ |
	| $\large 331$ | $\large 322$ | $\large 337$ | $\large 313$ |
	| $\large 342$ | $\large 315$ | $\large 339$ | $\large 346$ |
	| $\large 333$ | $\large 327$ | $\large 341$ | $\large 316$ |
2. Write the hypotheses:
	$$\Large\begin{aligned}
	&H_0: m = 330 \\
	&H_1: m \ne 330
	\end{aligned}
	$$
3. Lay them out in a flat table and find the **sign** of their difference from the median. Count how many $\large +$ signs you get to find the test statistic.

	| $\large x_i$ | $\large \textbf{Sign}$ |
	| :----------: | :------------------: |
	| $\large 347$ |      $\large \mathbf +$      |
	| $\large 325$ |      $\large \mathbf -$      |
	| $\large 340$ |      $\large \mathbf +$      |
	| $\large 344$ |      $\large \mathbf +$      |
	| $\large 335$ |      $\large \mathbf +$      |
	| $\large 349$ |      $\large \mathbf +$      |
	| $\large 341$ |      $\large \mathbf +$      |
	| $\large 313$ |      $\large \mathbf -$      |
	| $\large 336$ |      $\large \mathbf +$      |
	| $\large 338$ |      $\large \mathbf +$      |
	| **$\large \mathbf{n_+}$** |      **$\large \mathbf 8$**      |
4. Compare this test statistic to the following distribution:
	$$\Huge
	X \thicksim B(n, 0.5)
	$$
	For our example, that’d be $\large X \sim B(10, 0.5)$. As $\large n_+$ is high, we consider the “greater” tail.
	To calculate the value to compare to, we find:
	$$\Huge \begin{aligned}
	P(X \ge n_+) = P(X \ge 8) &= 0.5^{10}\Biggm(\binom{10}{8} + \binom{10}{9} + \binom{10}{10} \Biggm) \\
	&= 0.0547
	\end{aligned}
	$$
	We can factor out $\large 0.5^{20}$ as when $\large p = 0.5$, $\large q = 1-p = 0.5 = p$, so the expression becomes $\large \binom{n}{r}p^{r}q^{n-r} = \binom{n}{r}p^{r}p^{n-r} = \binom{n}{r}p^{n}$ for all values of $\large r$.
5. Now, compare the values and write the conclusion.
	$$\Large\begin{aligned}
	&0.0547 > 0.025 \\
	\therefore\ &\text{Accept } H_0\ \text{as insufficient evidence to suggest that} \\
	&\text{330 is not the median of the population.}
	\end{aligned}
	$$

For **large n ($\large n > 10$)**, we can approximate the binomial distribution as a normal distribution:
$$\Huge\begin{aligned}
T \thicksim N(\frac{n}{2}, \frac{n}{4}) \ \ \ \Bigm(\mu = \frac{n}{2}, \sigma^2 = \frac{n}{4}\Bigm)
\end{aligned}
$$
##### Paired-Sample Sign Test
1. Consider a set of data, such as the following, where data is **paired** together (Math & English grades are paired for each student).
	
	Perform a hypothesis test that the **median** marks for Maths is **greater** than the **median** marks for English at the $\large 5\%$ significance level.

	| Student | Math        | English     |
	| ------- |: ----------- :|: ----------- :|
	| A       | $\large 97$ | $\large 61$ |
	| B       | $\large 89$ | $\large 67$ |
	| C       | $\large 83$ | $\large 71$ |
	| D       | $\large 79$ | $\large 73$ |
	| E       | $\large 75$ | $\large 65$ |
	| F       | $\large 78$ | $\large 60$ |
	| G       | $\large 62$ | $\large 76$ |
	| H       | $\large 74$ | $\large 64$ |
	| I       | $\large 68$ | $\large 70$ |
	| J       | $\large 66$ | $\large 72$ |
2. Write the hypotheses.
	$$\Huge\begin{aligned}
	&\begin{cases}
	H_0: m_M - m_E = 0 \\
	H_1: m_M - m_E > 0
	\end{cases} \\
	& \text{or} \\
	&\begin{cases}
	H_0: m_d = 0 \\
	H_1: m_d > 0
	\end{cases} \\
	\end{aligned}
	$$
3. Lay out the data onto a flat table and find the **sign** of $\large L_i - R_i$ for each row. In our case, that would be $(\large \text{Math Marks} - \text{English Marks})$ for each student and count the number of $\large +$ signs like before.

	|    Math     |     English      | Sign           |
	| :---------: | :--------------: | :------------- |
	| $\large 97$ |   $\large 61$    | $+$            |
	| $\large 89$ |   $\large 67$    | $+$            |
	| $\large 83$ |   $\large 71$    | $+$            |
	| $\large 79$ |   $\large 73$    | $+$            |
	| $\large 75$ |   $\large 65$    | $+$            |
	| $\large 78$ |   $\large 60$    | $+$            |
	| $\large 62$ |   $\large 76$    | $-$            |
	| $\large 74$ |   $\large 64$    | $+$            |
	| $\large 68$ |   $\large 70$    | $-$            |
	| $\large 66$ |   $\large 72$    | $-$            |
	|             | **$\large n_+$** | **$\large 7$** |
4. Continue with the sign test like normal, as shown above.

#### Wilcoxon Signed-Rank Test
1. Consider a set of data, where the median $\large m$ is believed to be $\large 7.5$. Carry out a two-tailed hypothesis test to test this claim at the $\large 5\%$ significance level:
	
	|               |               |               |               |               |               |               |               |               |               |
	| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
	| $\large 6.75$ | $\large 6.89$ | $\large 7.23$ | $\large 7.54$ | $\large 7.68$ | $\large 7.91$ | $\large 8.02$ | $\large 8.17$ | $\large 8.33$ | $\large 8.45$ |

2. Write the hypotheses:
	$$\Large\begin{aligned}
	&H_0: m = 7.5 \\
	&H_1: m \ne 7.5
	\end{aligned}
	$$
3. Lay out the data in a flat table and calculate for each row, $\large x_i - m$:
	
	| $\large x_i$  | $\large x_i - m$ |
	|: ------------- :|: ---------------- :|
	| $\large 6.75$ | $\large -0.75$   |
	| $\large 6.89$ | $\large -0.61$   |
	| $\large 7.23$ | $\large -0.27$   |
	| $\large 7.54$ | $\large +0.04$    |
	| $\large 7.68$ | $\large +0.18$    |
	| $\large 7.91$ | $\large +0.41$    |
	| $\large 8.02$ | $\large +0.52$    |
	| $\large 8.17$ | $\large +0.67$    |
	| $\large 8.33$ | $\large +0.83$    |
	| $\large 8.45$ | $\large +0.95$    |
4. Now, rank the **magnitude** $\large |x_i - m|$ of our calculated values. Sort them according to whether they are positive or negative. Finally, add up the ranks for the positive and negative columns.
	
	| $\large x_i$  | $\large x_i - m$ | **$\large \textbf{P}$**  | **$\large \textbf{N}$**  |
	|: ------------- :|: ---------------- :|: ------------------------ :|: ------------------------ :|
	| $\large 6.75$ | $\large -0.75$   |                          | **$\large \mathbf{8}$**  |
	| $\large 6.89$ | $\large -0.61$   |                          | **$\large \mathbf{6}$**  |
	| $\large 7.23$ | $\large -0.27$   |                          | **$\large \mathbf{3}$**  |
	| $\large 7.54$ | $\large +0.04$   | **$\large \mathbf{1}$**  |                          |
	| $\large 7.68$ | $\large +0.18$   | **$\large \mathbf{2}$**  |                          |
	| $\large 7.91$ | $\large +0.41$   | **$\large \mathbf{4}$**  |                          |
	| $\large 8.02$ | $\large +0.52$   | **$\large \mathbf{5}$**  |                          |
	| $\large 8.17$ | $\large +0.67$   | **$\large \mathbf{7}$**  |                          |
	| $\large 8.33$ | $\large +0.83$   | **$\large \mathbf{9}$**  |                          |
	| $\large 8.45$ | $\large +0.95$   | **$\large \mathbf{10}$** |                          |
	|               | **$\large \textbf{Total}$**        | **$\large \mathbf{38}$** | **$\large \mathbf{17}$** |

1. To find the test statistic, we need to take the **minimum** of the positive and negative ranks:
	$$\Huge
	T = \min(P, N)
	$$
	In our case, that’d be **$\large T = \min(P, N) = \min(38, 17) = 17$**.
2. Use the table to find the **critical value** for the question’s $\large n$ and significance level $\large \alpha$. In our case, there are 10 numbers in the table, so our $\large n = 10$. From the table, we can see that the critical value for $\large n = 10$ at $\large \alpha = 0.05$ for a two-tailed test is $\large 8$. Thus, we compare our test statistic $\large T$ with $\large 8$:
	$$\Huge \begin{aligned}
	&T = 17 > 8 \\
	\therefore\ &\text{Accept } H_0\ \text{as insufficient evidence to suggest} \\
	&\text{that the median is not 7.5}
	\end{aligned}
	$$
	As we take the minimum, we **always reject for $\large <$ and accept for $\large >$** regardless of alternative hypothesis.

For **large n ($\large n > 20$)** that are not on the table, we can approximate the last step using:
$$\Huge\begin{aligned}
X \thicksim N\Bigm(\frac{1}{4}n(n+1), \frac{1}{24}n(n+1)(2n+1)\Bigm)
\end{aligned}
$$
This is done by finding the probability $\large P(X \le T)$ and comparing with the significance level. This is a **discrete** distribution so there must be an appropriate **continuity correction**.

##### Wilcoxon Matched-Pairs Signed-Rank Test
1. Consider a set of data, such as the following, where data is **paired** together (Theory & Practical grades are paired for each student).
	
	Perform a hypothesis test that the **median** marks for theory is **greater** than the **median** marks for practicals at the $\large 5\%$ significance level.

	| Student | Theory      | Practicals   |
	| ------- |: ----------- :|: ----------- :|
	| A       | $\large 97$ | $\large 60$ |
	| B       | $\large 89$ | $\large 62$ |
	| C       | $\large 83$ | $\large 64$ |
	| D       | $\large 79$ | $\large 65$ |
	| E       | $\large 73$ | $\large 67$ |
	| F       | $\large 61$ | $\large 74$ |
	| G       | $\large 67$ | $\large 72$ |
	| H       | $\large 71$ | $\large 70$ |
2. Write the hypotheses.
	$$\Huge\begin{aligned}
	&\begin{cases}
	H_0: m_T - m_P = 0 \\
	H_1: m_T - m_P > 0
	\end{cases} \\
	& \text{or} \\
	&\begin{cases}
	H_0: m_d = 0 \\
	H_1: m_d > 0
	\end{cases} \\
	\end{aligned}
	$$
3. Lay out the data onto a flat table and find the **difference**, $\large L_i - R_i$ for each row. In our case, that would be $(\large \text{Theory Marks} - \text{Practical Marks})$ for each student.

	|   Theory    | Practicals  |  Difference  |
	| :---------: | :---------: | :----------: |
	| $\large 97$ | $\large 60$ | $\large +37$ |
	| $\large 89$ | $\large 62$ | $\large +27$ |
	| $\large 83$ | $\large 64$ | $\large +19$ |
	| $\large 79$ | $\large 65$ | $\large +14$ |
	| $\large 73$ | $\large 67$ | $\large +6$  |
	| $\large 61$ | $\large 74$ | $\large -13$ |
	| $\large 67$ | $\large 72$ | $\large -5$  |
	| $\large 71$ | $\large 70$ | $\large +1$  |
4. Now, rank the **magnitude** of our calculated values of the **differences**. Sort them according to whether they are positive or negative, and add the ranks for the positive and negative columns.

	|   Theory    | Practicals  |         Difference          | **$\large \textbf{P}$**  | **$\large \textbf{N}$** |
	| :---------: | :---------: | :-------------------------: | :----------------------: | :---------------------: |
	| $\large 97$ | $\large 60$ |        $\large +37$         | **$\large \mathbf{8}$**  |                         |
	| $\large 89$ | $\large 62$ |        $\large +27$         | **$\large \mathbf{7}$**  |                         |
	| $\large 83$ | $\large 64$ |        $\large +19$         | **$\large \mathbf{6}$**  |                         |
	| $\large 79$ | $\large 65$ |        $\large +14$         | **$\large \mathbf{5}$**  |                         |
	| $\large 73$ | $\large 67$ |         $\large +6$         |                          | **$\large \mathbf{3}$** |
	| $\large 61$ | $\large 74$ |        $\large -13$         | **$\large \mathbf{4}$**  |                         |
	| $\large 67$ | $\large 72$ |         $\large -5$         |                          | **$\large \mathbf{2}$** |
	| $\large 71$ | $\large 70$ |         $\large +1$         | **$\large \mathbf{1}$**  |                         |
	|             |             | **$\large \textbf{Total}$** | **$\large \mathbf{31}$** | **$\large \mathbf{5}$** |
5. Continue the Wilcoxon Signed-Rank Test as normal.

#### Wilcoxon Rank-Sum Test
1. Consider a set of data, such as the following:

	| **$\large \textbf{Teacher A}$** | $\large 61$ | $\large 67$ | $\large 71$ | $\large 73$ | $\large 79$ | $\large 60$ | $\large 62$ | $\large 64$ | $\large 66$ |
	| ------------------------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
	| **$\large \textbf{Teacher B}$** | $\large 83$ | $\large 89$ | $\large 97$ | $\large 68$ | $\large 70$ | $\large 72$ | $\large 74$ |             |             |
	
	You are asked to carry out a hypothesis test at the $\large 5\%$ significance level that Teacher B awards **higher** marks than Teacher A.
2. Write the hypotheses.
	$$\Huge\begin{aligned}
	&\begin{cases}
	H_0: m_A - m_B = 0 \\
	H_1: m_A - m_B < 0
	\end{cases} \\
	& \text{or} \\
	&\begin{cases}
	H_0: m_d = 0 \\
	H_1: m_d < 0
	\end{cases} \\
	\end{aligned}
	$$
3. Rank the numbers from above according to the teacher. You need to find out the **sum of the ranks for the smaller set of data**, denoted as $\large R_m$, which would be Teacher B in our case.
	$$\Large
	R_m = 7 + 8 + 10 + 12 + 14 + 15 + 16 = 82
	$$
4. Given two sets of data of size $\large m$ and $\large n$, where $\large m \le n$, and the sum of the ranks of the numbers in the smaller data set is $\large R_m$, the **test statistic** $\large W$, is given by:
	$$\huge
	W = \min(R_m, \boxed{m(n+m+1) - R_m})
	$$
	where, $\large (m(n+m+1) - R_m)$ represents the ranking in the opposite order (biggest to smallest instead of smallest to biggest).

	To check which value of the two we should take, we need to calculate the opposite order:
	$$\Large
	m(n+m+1) - R_m = 7(9+7+1) - 82 = 37 < 82
	$$
	Therefore, our test statistic, **$\large W = \min(82, 37) = 37$**.
5. Use the table to find the **critical value** for the question-specific $\large m$ and $\large n$ as well as the significance level $\large \alpha$.
	
	For our example, $\large m = 7$, $\large n = 9$, and $\large \alpha = 0.05$. We are also conducting a one-tailed test. Therefore, according to the table, our critical value is $\large 43$. Now, we compare our test statistic to the critical value:
	$$\Huge \begin{aligned}
	&W = 37 < 43 \\
	\therefore\ &\text{Reject } H_0\ \text{as sufficient evidence to suggest that} \\
	&\text{Teacher B awards higher marks than Teacher A.}
	\end{aligned}
	$$
	As we take the minimum, we **always reject for $\large <$ and accept for $\large >$** regardless of alternative hypothesis.

For **large m and n ($\large m \ge 10$, $\large n \ge 10$)**, we can approximate the last step using a normal distribution instead of the table:
$$\Huge\begin{aligned}
E(X) = \frac{m(n+m+1)}{2} \ \ \ \text{Var}(X) = &\frac{mn(n+m+1)}{12} \\ \\
X \thicksim N(E(X), \text{Var}(X))
\end{aligned}
$$
This is done by finding the probability $\large P(X \le W)$ and comparing with the significance level. This is a **discrete** distribution so there must be an appropriate **continuity correction**.