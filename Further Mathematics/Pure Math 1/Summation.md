#### Formulae
$$\large
\begin{align*}
\sum_{r=1}^nn &= \frac{1}{2}n(n+1) \\
\sum_{r=1}^nn^2 &= \frac{1}{6}n(n+1)(2n+1) \\
\sum_{r=1}^nn^3 &= \frac{1}{4}n^2(n+1)^2 \\
\end{align*}
$$
#### Method of Differences
When most terms in a summation cancel out, the method of differences is used. Often, this may involve rewriting a fraction as a sum of partial fractions. For example, for $\large \underset{r=2}{\overset{n}{\sum}}\Large\frac{1}{r^2-1}$,
$$\large
\frac{1}{r^2 - 1} = \frac{1}{(r+1)(r-1)} = \frac{1}{2(r-1)} - \frac{1}{2(r+1)}
$$
Now,
1. We input values into the partial fractions starting from the minimum, $r=2$ in this case, until we spot a **pattern of terms cancelling**.
2. Skip the rest of the terms by putting a “$+ … +$”.
3. Write an appropriate number of terms in $n$ at the end such that **at least one of them is cancelled by another term in $n$ that you wrote**.

$$\large\begin{align*}
\therefore \sum_{r=2}^n\frac{1}{r^2-1} &= \frac{1}{2} - \bcancel{\boxed{\frac{1}{6}}}
\\ &+ \frac{1}{4} - \bcancel{\frac{1}{8}}
\\ &+ \bcancel{\boxed{\frac{1}{6}}} - \bcancel{\frac{1}{10}}
\\ &+ \bcancel{\frac{1}{8}} - \bcancel{\frac{1}{12}} + …
\\ &+ \bcancel{\frac{1}{2(n-3)}} - \bcancel{\boxed{\frac{1}{2(n-1)}}}
\\ &+ \bcancel{\frac{1}{2(n-2)}} - \frac{1}{2n}
\\ &+ \bcancel{\boxed{\frac{1}{2(n-1)}}} - \frac{1}{2(n+1)}
\\ &= \frac{1}{2} + \frac{1}{4} - \frac{1}{2n} - \frac{1}{2(n+1)}
\\ &= \frac{3}{4} - \frac{1}{2n} - \frac{1}{2n+2}
\end{align*} 
$$
- The boxed numbers, $1 \over 6$ are the first instance of cancelling. We see that it is happening between the second term of $r=2$ and the first of $r=4$. We can spot the **pattern** if we look further as well, with $1 \over 8$ cancelling in a similar fashion. This tells us that every second term since $r=2$ cancels with every first term since $r=4$.
- We stop cancelling when we see the last term that cancels *in terms of $\large n$* at the end.

It is **very important** that we pick the **appropriate number of iterations** in order to **spot a pattern** to **decide which terms cancel**.


