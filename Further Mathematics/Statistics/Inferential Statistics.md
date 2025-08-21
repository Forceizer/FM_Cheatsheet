###### Unbiased Estimator of Variance
$$\large
s^2 = \frac{1}{n-1}(\Sigma x^2 - \frac{(\Sigma x)^2}{n}) = \frac{1}{n-1}(\Sigma x - \bar x)^2 = \frac{1}{n-1}(\Sigma x^2 - n\bar x^2)
$$
where,
$$\large
S_{xx} = (\Sigma x^2 - \frac{(\Sigma x)^2}{n}) = (\Sigma x - \bar x)^2 = (\Sigma x^2 - n\bar x^2)
$$
therefore,
$$\large
s^2 = \frac{S_{xx}}{n-1}
$$
#### Normal & t-distributions
For a normal distribution with sample size $\large n$,
- If $\large n<30$, we use the **t-distribution**.
- The **Degrees of Freedom**, $\large \nu = n-1$
The test statistic, $\large t$ is calculated as such:
$$\huge
t = \frac{\bar x - \mu}{\frac{s}{\sqrt{n}}}
$$
The distribution is represented as $\large t_{n-1}$.
The critical value is written as $\large t_{\alpha,\ n-1}$ for one-tailed and $\large t_{{\alpha \over 2},\ n-1}$ for two-tailed.
To use the table for a significance level $\large \alpha$,
- For $\large \alpha > 50\%$, use the values as is.
- For $\large \alpha < 50\%$, use the **negative** of the value for $\large 100(1 - \alpha)\%$.

##### Difference in Sample Means
The hypotheses are usually written as:
$$\Large \begin{aligned}
&H_0: \mu_x - \mu_y = k \\
&\begin{cases}
H_1: \mu_x - \mu_y > k \\
\text{or} \\
H_1: \mu_x - \mu_y < k \\
\end{cases}
\end{aligned}
$$
When the questions asks you to test if there is any difference at all, $\large k = 0$.

When using a normal distribution,
$$\LARGE
z = \frac{(\bar x - \bar y) - (\mu_x - \mu_y)}{\sqrt{\frac{\sigma_x^2}{n_x} + \frac{\sigma_y^2}{n_y}}}
$$
When the sample sizes are small, we can assume equal population variance, and **pool** the variances together to get a more appropriate variance to use in our t-distribution:
$$\LARGE\begin{aligned}
s^2_p &= \frac{S_{xx} + S_{yy}}{n_x+n_y-2} \\
&= \frac{\Sigma x^2 -\frac{(\Sigma x)^2}{n_x} + \Sigma y^2 -\frac{(\Sigma y)^2}{n_y}}{n_x+n_y-2}
\end{aligned}
$$
Then, for the test statistic,
$$\LARGE
t = \frac{(\bar x - \bar y) - (\mu_x -\mu_y)}{\sqrt{s_p^2(\frac{1}{n_x} + \frac{1}{n_y})}}
$$
- where $\large \nu = n_x + n_y - 2$
##### Paired t-tests
For a paired t-test with $\large n$ pairs of data, where $\large x_i$ and $\large y_i$ represent one pair, and $\large d$ represents the difference $\large x_i - y_i$,
$$\Large\begin{aligned}
&H_0: \mu_d = k \\
&\begin{cases}
H_1: \mu_d > k & \\
\text{or}
\\H_1: \mu_d < k
\end{cases}
\end{aligned}
$$
To find the test statistic,
$$\huge
z / t = \frac{\bar d - k}{\frac{s_d}{\sqrt{n}}}
$$
where $\large s_d$ is the standard deviation of the differences.
- $\large \nu = n-1$
##### Confidence Intervals of Means of Small Samples
To calculate the confidence interval for a confidence interval $\alpha\%$,
1. Find the upper limit $\large \beta$
	$$\large
	\frac{100 - \alpha}{2} = \beta\
	$$
2. Take the decimal value of the resulting upper limit percentage and find the confidence interval, replacing the normal distribution with the t-distribution as required:
	$$\LARGE
	\Bigm(\bar x - t_{\beta,\ n-1}\frac{s}{\sqrt{n}},\ \bar x + t_{\beta,\ n-1}\frac{s}{\sqrt{n}}\Bigm)
	$$
##### Confidence Intervals for Difference in Means
1. Find the upper limit $\large \beta$
	$$\large
	\frac{100 - \alpha}{2} = \beta\
	$$
2. Calculate with $\large z$ or $\large t$ according to the sample size $\large n$,
	$$\LARGE \begin{aligned}
	&(\bar x - \bar y) \pm z_\beta\sqrt{\frac{s^2_x}{n_x} + \frac{s^2_y}{n_y}} \\
	&(\bar x - \bar y) \pm t_{\beta,\ n_x + n_y - 2}\sqrt{s^2_p\Bigm(\frac{1}{n_x} + \frac{1}{n_y}\Bigm)}
	\end{aligned}
	$$
#### Assumptions
##### Paired Sample t-test
- **Differences** are **normally distributed**
- Samples’ **Populations’ Variances** are **equal**
- Data are **matched pairs**
##### Difference in Means: Two-Sample t-test
- Underlying distributions are **normal**
- Populations are **independent**
- Samples’ **Populations’ Variances** are **equal**

For two-sample tests using **normal distribution**, another assumption is a **large sample size**.
