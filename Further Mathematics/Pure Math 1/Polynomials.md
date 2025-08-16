For any polynomial of $n^{th}$ degree,
$$\large\begin{array}{c c c c c}
ax^2+bx+c & & ax^3+bx^2+cx+d & & ax^4+bx^3+cx^2+dx+e
\end{array}$$
The amount of roots they have depends on their maximum power, $x^n$.
- $x^2$ -> 2 roots — $\alpha, \beta$
- $x^3$ → 3 roots — $\alpha, \beta, \gamma$
- $x^4$ → 4 roots — $\alpha, \beta, \gamma, \sigma$
#### Formulae
##### Coefficients & Summation Relations
For these roots, their sums correspond to the polynomial’s coefficients as follows:
$$\Large
\begin{rcases}
\begin{rcases}
\begin{rcases}
   \sum\alpha \ \ \ \ \ \ = -\frac{b}{a}& \\
   \sum\alpha\beta \ \ \ \ = \frac{c}{a}&
\end{rcases} \ x^2
   \\\sum\alpha\beta\gamma \ \ = -\frac{d}{a}
\end{rcases} \ x^3
   \\\sum\alpha\beta\gamma\sigma = \frac{e}{a}
\end{rcases} \ x^4
$$
where,
- $\sum\alpha = \alpha + \beta + …$
	- $x^2$ → $\sum\alpha = \alpha + \beta$
	- $x^3$ → $\sum\alpha = \alpha + \beta + \gamma$
	- $x^4$ → $\sum\alpha = \alpha + \beta + \gamma + \sigma$
- $\sum\alpha\beta = \alpha\beta + \alpha\gamma + \beta\gamma + …$
	- $x^2$ → $\sum\alpha\beta = \alpha\beta$
	- $x^3$ → $\sum\alpha\beta = \alpha\beta + \alpha\gamma + \beta\gamma$
	- $x^4$ → $\sum\alpha\beta = \alpha\beta + \alpha\gamma + \alpha\sigma + \beta\gamma + \beta\sigma + \gamma\sigma$
- $\sum\alpha\beta\gamma = \alpha\beta\gamma + \alpha\beta\sigma + \beta\gamma\sigma + …$
	- $x^3$ → $\sum\alpha\beta\gamma = \alpha\beta\gamma$
	- $x^4$ → $\sum\alpha\beta\gamma = \alpha\beta\gamma + \alpha\beta\sigma + \alpha\gamma\sigma + \beta\gamma\sigma$
- $\sum\alpha\beta\gamma\sigma = \alpha\beta\gamma\sigma + …$
	- $x^4$ → $\sum\alpha\beta\gamma\sigma = \alpha\beta\gamma\sigma$

The signs alternate as such: $-\frac{b}{a}, +\frac{c}{a}, -\frac{d}{a}, +\frac{e}{a}$
##### Summation of Roots’ Powers
$S_r$ is defined as the summation of the roots to the $r^{th}$ power
$$\Large
S_r = \sum\alpha^r
$$
- $S_1 = \sum\alpha$
- $S_2 = \sum\alpha^2 = (\sum\alpha)^2 - 2\sum\alpha\beta$
- $S_{-1} = \sum\frac{1}{\alpha}$
	$S_{-1}$ is always equal to the negative of the coefficient of $x$ divided by the cofficient of the constant term (The denominator, $a$ cancels out as their respective sums get divided).
	$$\large\begin{array}{c c c c c}
	ax^2+\underline{b}x+\underline{c} & & ax^3+bx^2+\underline{c}x+\underline{d} & & ax^4+bx^3+cx^2+\underline{d}x+\underline{e}
	\end{array}	
	$$
    - $\large x^2$ → $\large S_{-1} = \sum\frac{1}{\alpha} = -\frac{\sum\alpha}{\sum\alpha\beta} = -\frac{b}{c}$
	- $\large x^3$ → $\large S_{-1} = \sum\frac{1}{\alpha} = -\frac{\sum\alpha\beta}{\sum\alpha\beta\gamma} = -\frac{c}{d}$
	- $\large x^4$ → $\large S_{-1} = \sum\frac{1}{\alpha} = -\frac{\sum\alpha\beta\gamma}{\sum\alpha\beta\gamma\sigma} = -\frac{d}{e}$
	
###### The Summation Form
Any polynomial can be converted into their summation form as follows:
$$\large
\begin{align*}
5x^{\boxed{\small 4}} + 2x^3 + 9x^2 + 4x + 3 &= 0
\\ \Rightarrow 5S_4 + 2S_3 + 9S_2 + 4S_1 + \boxed 4(3) &= 0
\end{align*}
$$
In general, for any polynomial of the $n^{th}$ degree,
- All terms of form $x^r \rightarrow S_r$
- The constant $k → nk$
It is also possible to multiply a polynomial with $x^m$ to get the corresponding $S_m$. For example, for $S_{-2}$:
$$\large
\begin{align*}
5x^{\boxed{\small 4}} + 2x^3 + 9x^2 + 4x + 3 &= 0
\\ \Rightarrow  5x^2 + 2x + 9 + 4x^{-1} + 3x^{-2} &= 0
\\ \Rightarrow 5S_2 + 2S_1 + \boxed 4(9) + 4S_{-1} + 3S_{-2} &= 0
\end{align*}
$$
Note that the constant term despite the powers changing, $k → nk$ still occurs with the original power $n$.
##### Substitution
When a polynomial $P(x)$ which has roots $\alpha, \beta, \gamma$, is transformed into $F(y)$ such that $y=f(x)$, the new equation, $F(y)$ has roots $f(\alpha),\  f(\beta),\  f(\gamma)$. For example,
> [!NOTE] $y=x^3 + x^2 -5 = 0$. Find the equation with roots $\large\frac{1}{\alpha - 2},\ \frac{1}{\beta - 2},\ \frac{1}{\gamma - 2}$
> $$\large
  \begin{align*}
  \text{Let }y=\frac{1}{x + 2} \Rightarrow x &= \frac{1+2y}{2y}
  \\ \\ (\frac{1+2y}{y})^3 + (\frac{1+2y}{y})^2 - 5 &= 0
  \\ 7y^3 + 16y^2 + 7y + 1 &= 0
  \end{align*}
   $$
  