#### Probability Density Function
Probability density is similar to frequency density, but with the frequency replaced with probability. In that sense, a probability density function could be thought of as a function that **approximates a histogram**. It is represented by $f(x)$
$$\Large
P(a \le X \le b) = \int^b_a{f(x)}\ dx
$$
$$\Large
f(x) = \frac{\text dF(x)}{\text{dx}}
$$
#### Cumulative Distribution Function
A cumulative distribution function is a function that is similar to the cumulative distribution curve with frequency, but with probability instead.
We know, $\large\text{Probability Density} = \frac{\text{Probability}}{\text{Class Width}}$. In a histogram, the $x-axis$ is the class width, $\therefore$ the area under the graph is the probability.
This means, to find the cumulative distribution function $F(x)$, we use:
$$\Large
F(x) = P(X \le x) = \int^x_{-\infty}{f(x)}\ dx
$$
Depending on the limit, we can replace $-\infty$ with the lower limit.

For **piecewise** functions `where a function is defined for different domains by different expressions`, we need to add the previous function’s probability to the next. For example, for:
$$\LARGE \begin{aligned}
&f(x) = \begin{cases}
f_1(x) & a \le x < b  \\
f_2(x) & b \le x \le c
\end{cases} \\ &\text{Then,} \\
&F(x) = \begin{cases}
\int_a^xf_1(t)\ dt & a \le x < b \\
\int_a^bf_1(t)\ dt + \int_b^xf_2(t)\ dt  & b \le x \le c \\
\end{cases}
\end{aligned}
$$
#### Mode
The **mode** of a continuous random variable is the highest point of the probability density function. To find it,
1. Find the solution $\large \alpha$ of
	$$\large f'(x) = 0$$
2. Find whether the point is a maximum or minimum by finding $\large f’’(x)$ and inputting the solution $\large \alpha$ from (1) as $\large x$ in $\large f’’(x)$ or by **looking at the sign of $\large x^2$** if possible.
	- $\large f’’(\alpha) < 0$ → **Maximum** → Mode = $\large \alpha$
	- $\large f’’(\alpha) > 0$ → **Minimum** → Mode is at **one of the ends** (test both to see which)
##### For $y=mx+c$
For a PDF $\large f(x) = mx+c \text{ for } a \le x \le b$,
- $\large m > 0$ → Mode = $\large a$
- $\large m < 0$ → Mode = $\large b$

For **multiple lines/curves**, find the mode of the individual functions using the above methods, and pick whichever mode is **highest**.
#### Mean & Variance
$$\Large
\text{let } f(x) \text{ have the domain } a \le x \le b
$$
$$\Large \begin{aligned}
E(X) &= \int_a^b{xf(x)}\ dx \\
E(g(X)) &= \int_a^b{g(x)f(x)}\ dx
\end{aligned}
$$
$$\Large \begin{aligned}
\text{Var}(X) &= E(X^2) - [E(X)]^2 \\
&= \int_a^b{x^2f(x)}\ dx - [E(X)]^2 \\
\text{Var}(X^n) &= E(X^{2n}) - [E(X^n)]^2 \\
\end{aligned}
$$
#### Transformations of Functions
For a continuous random variable $\large X$ and its transformation $\large Y=h(X)$,
1. Rewrite the transformation function $\large h(x)$ in terms of $\large y$, with $\large x$ as the subject, so it can be substituted into $\large F(x)$ in order to get an expression in terms of $\large y$:
	$$\Large \begin{aligned}
	y &= h(x) \\ \Rightarrow
	h^{-1}(y) &= x
	\end{aligned}
	$$
2. Then, to find $\large G(y)$,
	- For an **increasing** transformation function $\large h(x)$,
		$$\LARGE
		G(y) = P(Y \le y) = P(X \le h^{-1}(y)) = \boxed{F(h^{-1}(y))}
		$$
		![[cdf increasing.png]]
		 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
	- For  a  **decreasing** transformation function $\large h(x)$,
		$$\LARGE
		G(y) = P(Y \le y) = P(X \ge h^{-1}(y)) = \boxed{1-F(h^{-1}(y))}
		$$
		![[cdf decreasing.png]]
		 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
		The CDF is subtracted from $\large 1$ as in decreasing functions, the probability is always highest at the start. This can be seen in the graph.
##### Finding PDF from PDF
Given the PDF $\large f(x)$ of the continuous random variable $\large X$ and its transformation, $\large Y=h(x)$, there are two methods of finding the PDF $\large g(y)$ of $\large Y$:
- **Long Method**
	1. Take the **PDF** $\large f(x)$.
	2. Find the **CDF** $\large F(x)$ by integrating.
	3. Find the **CDF** $\large G(y)$ from the above method.
	4. Find the **PDF** $\large g(y)$ by differentiating.
- **Direct Method**
	$$\LARGE
	g(y) = f(h^{-1}(y))\ \times \Biggm\vert \frac{d}{dy}(h^{-1}(y)) \Biggm\vert
	$$
