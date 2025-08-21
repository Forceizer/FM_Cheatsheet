Chi-Squared tests are used to check if observed values are similar to the expected values. The test statistic has the formula:
$$\Large
\sum\Bigm(\frac{(O_i-E_i)^2}{E_i} \Bigm) \thicksim \chi^2(\nu)
$$
where,
- $\large O_i$ = Observed Value
- $\large E_i$ = Expected Value
- $\large \chi$ is the Greek letter “Chi”

For the test,
- **Condition**: $\large E_i \ge 5$
- **Degrees of Freedom**: $\large \nu = n(\text{rows of expected values}) - 1 - (\text{number of predicted parameters})$

To carry out the test at $\large \alpha \%$ significance level (for example $\large 5\%$),
1. Write the hypotheses according to the question.
	$$\large\begin{aligned}
	&\begin{cases}
	H_0: \text{There's no difference between Observed \& Expected Values} \\
	H_0: \text{There's a difference between Observed \& Expected Values}
	\end{cases}	\\
	&\text{or} \\
	&\begin{cases}
	H_0: \text{[Distribution] is a good fit for the observed values} \\
	H_0: \text{[Distribution] is not a good fit for the observed values}
	\end{cases}	\\
	\end{aligned}
	$$
2. Draw out a table with the observed as well as the expected values from calculation (if foe example, a distribution is given and you are expected to calculate $\large E_i$ values for each observed $\large x$) or otherwise.

	| $\large x_i$ | $\large O_i$ | $\large E_i$  | **$\mathbf{\large \frac{(O_i - E_i)^2}{E_i}}$** |
	|: ------------ :|: ------------ :|: ------------- :|: ----------------------------------------------- :|
	| $\large 1$   | $\large 8$   | $\large 10.2$ |                                                 |
	| $\large 2$   | $\large 10$  | $\large 9.5$  |                                                 |
	| $\large 3$   | $\large 3$   | $\large 6.6$  |                                                 |
	| $\large 4$   | $\large 9$   | $\large 10.1$ |                                                 |
	| $\large 5$   | $\large 4$   | $\large 2.3$  |                                                 |
	| $\large 6$   | $\large 1$   | $\large 1.1$  |                                                 |

3. Add up any rows where $\large E_i < 5$ with other rows until no row has expected value $\large E_i < 5$.
	
	For example, as rows `4`, `5`, and `6` have $\large E_i = 10.1, 2.3, 1.1$, they need to be added up to give the single row `4-6`. Note that we don’t stop at just the merged row `5-6` as that row still wouldn’t yield an expected value $\large E_i \ge 5$.

	| $\large x_i$               | $\large O_i$ | $\large E_i$  | **$\mathbf{\large \frac{(O_i - E_i)^2}{E_i}}$** |
	|: ------------ :|: ------------ :|: ------------- :|: ----------------------------------------------- :|
	| $\large 1$                 | $\large 8$   | $\large 10.2$ |                                                 |
	| $\large 2$                 | $\large 10$  | $\large 9.5$  |                                                 |
	| $\large 3$                 | $\large 3$   | $\large 6.6$  |                                                 |
	| $\large 4\text{-}\large 6$ | $\large 14$  | $\large 13.5$ |                                                 |
4. Calculate the $\Large \frac{(O_i - E_i)^2}{E_i}$ values for each row. It’s best to use the `CALC` function on the calculator for this so that you can always get all values in **3 d.p.** and do so quickly.

	|$\large x_i$|$\large O_i$|$\large E_i$|**$\mathbf{\large \frac{(O_i - E_i)^2}{E_i}}$**|
	|:---:|:---:|:---:|:---:|
	|$\large 1$|$\large 8$|$\large 10.2$|**$\mathbf{\large 0.475}$**|
	|$\large 2$|$\large 10$|$\large 9.5$|**$\mathbf{\large 0.026}$**|
	|$\large 3$|$\large 3$|$\large 6.6$|**$\mathbf{\large 1.964}$**|
	|$\large 4\text{-}\large 6$|$\large 14$|$\large 13.5$|**$\mathbf{\large 0.019}$**|
	The column for $\large x_i$ is actually not needed, but has been present through steps 2-4 for clarity.
5. Calculate $\large \nu$.
	$$\Large
	\nu = 4-1-0 = 3
	$$
6. Calculate the test statistic and compare with the $\large \chi^2$ table’s value. If it is
	- $\large < \chi^2(\nu)$ → **Accept $\large H_0$**
	- $\large > \chi^2(\nu)$ → **Reject $\large H_0$**
		$$\Large
		\sum\Bigm(\frac{(O_i-E_i)^2}{E_i} \Bigm) = 2.484 > 0.3518 \therefore \text{Reject } H_0
		$$
7. Write the statement (e.g. Reject $\large H_0$ as sufficient evidence to suggest that …)

#### Goodness of fit
As mentioned in step **(2)**, one might need to **calculate** the expected values. For
##### Binomial/Poisson Distribution
For a suggested binomial distribution $\large X \sim B(N, p)$ or a Poisson distribution $\large X \sim Po(\lambda)$, $\large n$ is always given, but the parameters $\large p$ or $\large \lambda$ may or may not be given.
- If they **are** given,
	- $\large \nu = n(\text{rows of expected values}) - 1 - 0$
- If they **aren’t** given,
	- $\large \nu = n(\text{rows of expected values}) - 1 - 1$
	- The estimated parameter is calculated:
		$$\Huge
		\hat p / \hat \lambda = \frac{\sum(x_i \times f_i)}{N}
		$$
		where,
		- $\large f_i$ = Frequency for the specific $\large x_i$
		- $\large N$ is **not** the number of rows of expected values, but a parameter `(150 students, 80 days, etc.)`
##### Normal Distribution
For a suggested normal distribution $\large X \sim N(\mu, \sigma)$,
- If **$\large \mu$** and **$\large \sigma$** are **both** given,
	- $\large \nu = n(\text{rows of expected values}) - 1 - 0$
- If **either** of **$\large \mu$** or **$\large \sigma$** is given,
	- $\large \nu = n(\text{rows of expected values}) - 1 - 1$
- If **neither** **$\large \mu$** nor **$\large \sigma$** is given,
	- $\large \nu = n(\text{rows of expected values}) - 1 - 2$

In case the parameter(s) aren’t given,
- $\large \mu$ can be estimated using $\large \bar x$ to get $\large \hat \mu$
- $\large \sigma$ can be estimated using $\large s$ to get $\large \hat \sigma$

For any set of data, whether the parameters are given or not,

| Weight / $\large \text{kg}$ | $\large 1.9$ – $\large 2.4$ | $\large 2.5$ – $\large 3.2$ | $\large 3.3$ – $\large 3.7$ | $\large 3.8$ – $\large 4.5$ |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| **Frequency**               | $\large 10$                 | $\large 15$                 | $\large 86$                 | $\large 38$                 |
Since the given intervals are discrete, calculate the expected values of
- **Lowest** Interval by finding $\large P(X < 2.45)$
- **Middle** Interval by taking $\large P(2.45 \leq X < 3.25)$, …
- **Highest** Interval by taking $\large P(X \ge 4.55)$
#### Contingency Tables
For any contingency table of data, 
1. Check the table given in the question. For example, in this set of data, the columns represent hair colour and the rows represent eye colour:
	
	| Observed                            | $\large \text{Black}$ | $\large \text{Blonde}$ | $\large \text{Red}$ | **$\large \textbf{Row Totals}$** |
	| ----------------------------------- | --------------------- | ---------------------- | ------------------- | -------------------------------- |
	| $\large \text{Brown}$               | $\large 5$            | $\large 14$            | $\large 21$         |                                  |
	| $\large \text{Blue}$                | $\large 7$            | $\large 27$            | $\large 26$         |                                  |
	| $\large \text{Red}$                 | $\large 18$           | $\large 29$            | $\large 53$         |                                  |
	| **$\large \textbf{Column Totals}$** |                       |                        |                     |                                  |

2. Calculate the **totals**.
	
	| Observed                            | $\large \text{Black}$    | $\large \text{Blonde}$   | $\large \text{Red}$       | **$\large \textbf{Row Totals}$**  |
	| ----------------------------------- | ------------------------ | ------------------------ | ------------------------- | --------------------------------- |
	| $\large \text{Brown}$               | $\large 5$               | $\large 14$              | $\large 21$               | **$\mathbf{\large 40}$**          |
	| $\large \text{Blue}$                | $\large 7$               | $\large 27$              | $\large 26$               | **$\mathbf{\large 60}$**          |
	| $\large \text{Red}$                 | $\large 18$              | $\large 29$              | $\large 53$               | **$\mathbf{\large 100}$**         |
	| **$\large \textbf{Column Totals}$** | **$\mathbf{\large 30}$** | **$\mathbf{\large 70}$** | **$\mathbf{\large 100}$** | **$\boxed{\mathbf{\large 200}}$** |

3. Take note of the row totals, $\large R_i$
	- $\large R_1 = 40$
	- $\large R_2 = 60$
	- $\large R_3 = 100$
	
	Take note of the column totals, $\large C_j$
	- $\large C_1 = 30$
	- $\large C_2 = 70$
	- $\large C_3 = 100$
	
	Moreover, take note of the whole total, $\large T = 200$.
	
	The table above was the observed contingency table. To calculate values for the **expected contingency table**, we use the equation:
	$$\Huge
	E_{ij} = \frac{R_i \times C_j}{T}
	$$
	Using the three types of totals, we calculate the values for the expected table:
	
	| Expected                            | $\large \text{Black}$                           | $\large \text{Blonde}$                          | $\large \text{Red}$                              | **$\textbf{Row Totals}$**  |
	| ----------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ------------------------------------------------ | --------------------------------- |
	| $\large \text{Red}$                 | $\large \frac{100 \times 30}{200} = \boxed{15}$ | $\large \frac{100 \times 70}{200} = \boxed{35}$ | $\large \frac{100 \times 100}{200} = \boxed{50}$ | **$\mathbf{\large 100}$**         |
	| $\large \text{Blue}$                | $\large \frac{60 \times 30}{200} = \boxed{9}$   | $\large \frac{60 \times 70}{200} = \boxed{21}$  | $\large \frac{60 \times 100}{200} = \boxed{30}$  | **$\mathbf{\large 60}$**          |
	| $\large \text{Brown}$               | $\large \frac{40 \times 30}{200} = \boxed{6}$   | $\large \frac{40 \times 70}{200} = \boxed{14}$  | $\large \frac{40 \times 100}{200} = \boxed{20}$  | **$\mathbf{\large 40}$**          |
	| **$\textbf{Column Totals}$** | **$\mathbf{\large 30}$**                        | **$\mathbf{\large 70}$**                        | **$\mathbf{\large 100}$**                        | **$\mathbf{\large 200}$** |

	You don’t actually have to show the working ($\large \frac{100 \times 30}{200}$, $\large \frac{60 \times 30}{200}$, …). Just the answer will suffice.
4. Find the degrees of freedom $\large \nu$ using:
	$$\Huge
	\nu = (r-1)(c-1)
	$$
	where,
	- $\large r =$ Number of Rows
	- $\large c =$ Number of Columns
	
	For this example,
	$$\Huge
	\nu = (3-1)(3-1) = 4
	$$
4. Lay out the table using values from both the **Observed** and **Expected** contingency tables and continue the $\large \chi^2$ test:

	| Cell             | $\large O_i$ | $\large E_i$ | **$\mathbf{\large \frac{(O_i - E_i)^2}{E_i}}$** |
	| ---------------- |: ------------ :|: ------------ :|: ----------------------------------------------- :|
	| **Brown-Black**  | $\large 5$   | $\large 6$   | **$\mathbf{\large 0.167}$**                     |
	| **Brown-Blonde** | $\large 14$  | $\large 14$  | **$\mathbf{\large 0.000}$**                     |
	| **Brown-Red**    | $\large 21$  | $\large 20$  | **$\mathbf{\large 0.050}$**                     |
	| **Blue-Black**   | $\large 7$   | $\large 9$   | **$\mathbf{\large 0.444}$**                     |
	| **Blue-Blonde**  | $\large 27$  | $\large 21$  | **$\mathbf{\large 1.714}$**                     |
	| **Blue-Red**     | $\large 26$  | $\large 30$  | **$\mathbf{\large 0.533}$**                     |
	| **Red-Black**    | $\large 18$  | $\large 15$  | **$\mathbf{\large 0.600}$**                     |
	| **Red-Blonde**   | $\large 29$  | $\large 35$  | **$\mathbf{\large 1.029}$**                     |
	| **Red-Red**      | $\large 53$  | $\large 50$  | **$\mathbf{\large 0.180}$**                     |
	You don’t have to make the `Cell` column. It’s simply present for clarity.