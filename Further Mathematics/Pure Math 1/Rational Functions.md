 All Rational Functions can be plotted by considering their asymptotes, their turning points, and whether they go to $+\infty$ or $-\infty$ as they approach the asymptote. 
#### Asymptotes
##### Vertical Asymptotes ($x-axis$)
For any function,
$$\large
F(x) = {g(x) \over f(x)}
$$
The vertical asymptote is where $f(x) → 0$.
For example, for
$$\large
F(x) = \frac{5x + 3}{(x+5)(x-4)}
$$
Solve $(x+5)(x-4) = 0$. This evaluates to $x=-5$, $x=4$.
So, the vertical asymptotes for this function are:
- $\large x=-5$
- $\large x=4$
##### Horizontal Asymptotes ($y-axis$)
The horizontal asymptote is where $x → \infty$. This can usually be found by considering the coefficients of the **highest powers** in the numerator and denominator as the rest become negligible.
$$\large
F(x) = {6x^2 + 3x + 2 \over 3x^2 + 2x + 9}
$$
For this function, as $x→ \infty$, $F(x) → \frac{6}{3} = 2$.
$\therefore$ the horizontal asymptote is $y=2$.
$$\large
G(x) = {3x + 2 \over 3x^2 + 2x + 9}
$$
For this function, as $x→ \infty$, $G(x) → \frac{0}{3} = 0$.
$\therefore$ the horizontal asymptote is $y=0$.
$$\large
H(x) = {6x^2 + 3x + 2 \over 3x + 2}
$$
For this function, as $x→ \infty$, $H(x) → \frac{1}{0} \rightarrow \infty$.
$\therefore$ this function **doesn’t** have a horizontal asymptote.

For horizontal/oblique asymptotes, it is generally true that:
- $\deg (\text{Numerator}) = \deg (\text{Denominator}) = \text{Horizontal asymptote, } y=\frac{a}{b}$
- $\\ \deg (\text{Numerator}) > \deg (\text{Denominator}) = \text{Oblique/Curved asymptote}$
- $\\ \deg (\text{Numerator}) < \deg (\text{Denominator}) = \text{Horizontal asymptote, }y=0$
##### Oblique Asymptote
An oblique asymptote is, unlike the other two, **a linear equation**. For any function,
$$\large
F(x) = {g(x) \over f(x)}
$$
The oblique asymptote can be found by dividing $g(x)$ by $f(x)$ and taking the **quotient**.
For example,
$$\large
F(x) = {x^2 - 1 \over 2x-3} = \boxed{{1 \over 2}x + {3 \over 4}} + {5 \over 4(2x-3)}
$$
This means the oblique asymptote for $F(x)$ is $y = \frac{1}{2}x + \frac{3}{4}$.
#### Sketching Curves
1. Find the **asymptotes** of the function.
2. **Differentiate** the function to find its **turning points**. You may use the partial fractions from before, if you have split them into those, to make differentiating easier.
3. Find the value of the function on **either side of the asymptote**, and check their **signs**.
	- For **vertical** asymptote $x=k$, find $f(k-0.0001)$ and $f(k+0.0001)$.
		- This also helps to find the **natures** of the turning points.
		- If you are confused, you can also **double differentiate** to verify both the natures of the turning points and also the signs on either side of the asymptote.
	- For **horizontal** asymptotes, **infer** the direction of the curve as it converges using other information such as the intercepts and the turning point.
	- For **oblique** asymptotes, find the value of $f(1000)$ or with some similarly **large $x-value$**, and determine whether that value is **above or below** the line.
4. It is often helpful to make a **table of values** of $f(x)$ using “table” mode on the calculator.
5. Pick an appropriate **scale** for your graph.
6. **Draw** the **asymptotes** as **dotted** lines.
	- For modulus graphs, **adjust asymptotes accordingly**.
7. **Draw** the curve using the previous information and the **table of values**.
##### Special Curves
- $y = |f(x)|$ can be sketched by **reflecting** the curve **below** $x-axis$ to the top.
- $y=f(|x|)$ can be sketched by **reflecting** the curve on the **right** of the $y-axis$ to the left.
- $y^2=f(x)$ can be sketched by considering domain $f(x)≥0$ (above $x-axis$), sketching $y=\sqrt{f(x)}$ for that domain, and **reflecting** that part **above** $x-axis$ to the bottom.
	- A **table of values** of $f(x)$ is recommended to use alongside that to ensure accuracy.

