For a probability distribution table,

| $\large x_1$ | $\large x_2$ | $\large x_3$ | $\large ...$ | $\large x_n$ |
|-------------|-------------|-------------|-------------|-------------|
| $\large P(X=x_1)$ | $\large P(X=x_2)$ | $\large P(X=x_3)$ | $\large ...$ | $\large P(X=x_n)$ |
The probability generating function, $\large G_X(t)$, is:
$$\large G_X(t) =  P(X=x_1)t^{x_1} +  P(X=x_2)t^{x_2} +  P(X=x_3)t^{x_3} +  ... +  P(X=x_n)t^{x_n}$$

Written more formally,
$$\Huge G_X(t) = \sum_{r=1}^{n} t^{x_r} P(X=x_r)$$
$\large t$ acts as a dummy variable that allows us to modify the function to get different results such as $\large E(X)$ or $\large P(X=x)$. ^78a431

$$\Huge
G_X(1) = 1
$$

To find probability, $\large P(X=r)$, one can look at the coefficient of $\large t^r$ in the expansion of $\large G_X(t)$ or use:
$$\Huge
P(X = r) = \frac{G^{(r)}_X(0)}{r!}
$$
#### $\large E(X)$ & $\large \text{Var}(X)$
$$\Huge\begin{aligned}
E(X) &= G_X'(1) \\ \\
\text{Var}(X) &= G_X''(1) + E(X) - [E(X)]^2 \\
&= G_X''(1) + G_X'(1) - [G_X'(1)]^2
\end{aligned}
$$
From above, we know: ![[#^78a431]]This form is similar to that of $\large E(X)$. As such, we can say:
$$\Huge
E(t^X) = G_X(t)
$$
#### Combination of Independent Random Variables
$$\Huge\begin{aligned}
G_{X+Y}(t) &= G_X(t) \times G_Y(t) \\
G_{aX+b}(t) &= t^bG_X(t^a) \\
G_{aX+bY}(t) &= G_X(t^a) \times G_Y(t^b)
\end{aligned}$$
#### PGFs of Common Distributions

| $\large \text{Probability distribution}$ | $\large P(X = r)$                                                                     | $\large G_X(t)$                    |
| ---------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------- |
| $\large \text{Uniform Distribution}$     | $$\large \begin{cases} \frac{1}{n} & r=1,2,3,…,n \\ 0 & \text{otherwise}\end{cases}$$ | $$\large \frac{t(1-t^n)}{n(1-t)}$$ |
| $\large \text{Bin}(n, p)$                | $\large \binom{n}{r}  p^r q^{n-r}$                                                    | $\large (q + pt)^n$                |
| $\large \text{Po}(\lambda)$              | $\large \frac{e^{-\lambda} \lambda^r}{r!}$                                            | $\large e^{\lambda(t-1)}$          |
| $\large \text{Geo}(p)$                   | $\large q^{r-1} p$                                                                    | $\large \frac{pt}{1 - qt}$         |
