#### Summary
##### Matrix Multiplication & Exponentiation
- $\large\mathbf{A}\large\mathbf{B} \neq \large\mathbf{B}\large\mathbf{A}$
- $\large\mathbf{A}\large\mathbf{B}\large\mathbf{C}\large\mathbf{D} = (\large\mathbf{A}\large\mathbf{B})\large\mathbf{C}\large\mathbf{D} = \large\mathbf{A}(\large\mathbf{B}\large\mathbf{C})\large\mathbf{D} = \large\mathbf{A}\large\mathbf{B}(\large\mathbf{C}\large\mathbf{D}) = (\large\mathbf{A}\large\mathbf{B})(\large\mathbf{C}\large\mathbf{D})$
- $\large\mathbf{A}^m\large\mathbf{A}^n = \large\mathbf{A}^n\large\mathbf{A}^m = \large\mathbf{A}^{m+n}$
##### Inverse Matrices
- A Matrix **with an inverse** is a **singular matrix**.
- A Matrix **without an inverse** is a **non-singular matrix**.
- $\large (\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$
- For a $2 \times 2$ matrix, $\large \det(\mathbf{A}) = ad - bc$
- For a $2 \times 2$ matrix, its inverse is given by:
	$$\large
	\mathbf{A}^{-1} = \frac{1}{ad-bc}
	\begin{pmatrix}
	d & -b \\
	-c & a
	\end{pmatrix}
	$$
- For a $3 \times 3$ matrix, its determinant is given by:
	$$\large
	\det(\mathbf{A}) = a_{11}
	\begin{vmatrix}
	a_{22} & a_{23} \\
	a_{32} & a_{33}
	\end{vmatrix}
	- a_{12}
	\begin{vmatrix}
	a_{21} & a_{23} \\
	a_{31} & a_{33}
	\end{vmatrix}
	+ a_{13}
	\begin{vmatrix}
	a_{21} & a_{22} \\
	a_{31} & a_{32}
	\end{vmatrix}
	$$
###### Determinants
- $\large\det(\mathbf{A}) \neq 0$ → **Inverse Exists**
- $\large\det(\mathbf{A}) = 0$ → **Inverse Doesn’t Exist**
For row operations,
- $r_i → kr_i + lr_j$, $\large\det(\mathbf{A})_\text{new} = k\det(\mathbf{A})$.
For square matrices,
- $\large \det(\mathbf{AB}) = \det(\mathbf{BA}) = \det(\mathbf{A})\det(\mathbf{B})$
It is also **equal to the multiplicative factor the matrix transformationtion increases the area by**.
##### Matrix Transformations
![[#^10851a]]
##### Identity Matrices
An identity matrix, $\large\mathbf{I}$, is a square matrix such that $\large\mathbf{IA} = \large\mathbf{AI} = \large\mathbf{A}$.
$$
\large
\begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots& 1
\end{pmatrix}
$$

#### Matrix Operations
##### Addition
$$\Large
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} +
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix} =
\begin{pmatrix}
a + e & b + f \\
c + g & d + h
\end{pmatrix}
$$
##### Multiplication & Exponentiation
Two matrixes, $\large\mathbf{A}$ & $\large\mathbf{B}$ can only be multiplied as $\large\mathbf{A}\large\mathbf{B}$ if for the matrices, the number of $\large \text{Rows}(\mathbf{A})$ = $\large \text{Columns}(\mathbf{B})$.
$$\Large
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix} =
\begin{pmatrix}
ae + bg & af + bh \\
ce + dg & cf + dh
\end{pmatrix}
$$

![[Matrix Multiplication.gif]]

In general,
- $\large\mathbf{A}\large\mathbf{B} \neq \large\mathbf{B}\large\mathbf{A}$
- $\large\mathbf{A}\large\mathbf{B}\large\mathbf{C}\large\mathbf{D} = (\large\mathbf{A}\large\mathbf{B})\large\mathbf{C}\large\mathbf{D} = \large\mathbf{A}(\large\mathbf{B}\large\mathbf{C})\large\mathbf{D} = \large\mathbf{A}\large\mathbf{B}(\large\mathbf{C}\large\mathbf{D}) = (\large\mathbf{A}\large\mathbf{B})(\large\mathbf{C}\large\mathbf{D})$
- $\large\mathbf{A}^m\large\mathbf{A}^n = \large\mathbf{A}^n\large\mathbf{A}^m = \large\mathbf{A}^{m+n}$
#### Identity Matrix
An identity matrix, $\large\mathbf{I}$, is a square matrix such that $\large\mathbf{IA} = \large\mathbf{AI} = \large\mathbf{A}$.
$$
\Large
\begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots& 1
\end{pmatrix}
$$
#### Inverse Matrix
Matrices may have inverses such that $\large\mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$.
- A Matrix **with an inverse** is a **singular matrix**.
- A Matrix **without an inverse** is a **non-singular matrix**.
- $\large (\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$
##### Determinants
The determinant of a matrix is a number that identifies whether a matrix has an inverse or not. 
- $\large\det(\mathbf{A}) \neq 0$ → **Inverse Exists**
- $\large\det(\mathbf{A}) = 0$ → **Inverse Doesn’t Exist**
For row operations,
- $r_i → kr_i + lr_j$, $\large\det(\mathbf{A})_\text{new} = k\det(\mathbf{A})$.
For square matrices,
- $\large \det(\mathbf{AB}) = \det(\mathbf{BA}) = \det(\mathbf{A})\det(\mathbf{B})$
It is also **equal to the multiplicative factor the matrix transformationtion increases the area by**.
###### 2 × 2
For a square matrix of size $2 \times 2$, its determinant is:
$$\large
\det(\mathbf{A}) =
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}
= ad - bc
$$
###### 3 × 3
For a square matrix of size $3 \times 3$, its determinant can be calculated by splitting it into smaller $2 \times 2$ determinants. For a matrix,
$$\large
\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\ 
a_{31} & a_{32} & a_{33} 
\end{pmatrix}
$$
We can take any row of elements, usually the top, $a_{11}, a_{12}, a_{13}$, and then write them as coefficients for the smaller determinants. Their signs are determined by the cofactor matrix, where each element is determined by their rows $m$ and their columns $n$ by using $(-1)^{m+n}$.
$$\large
\text{Cofactor Matrix = }
\begin{pmatrix}
+ & - & + \\
- & + & - \\
+ & - & + \\
\end{pmatrix}
$$
By comparison, we can see that $a_{11}$ and $a_{13}$ are positive, and $a_{12}$ is negative, so:
$$\large
\det(\mathbf{A}) = a_{11}\det(\mathbf{A}_{11}) - a_{12}\det(\mathbf{A}_{12}) + a_{13}\det(\mathbf{A}_{13})
$$
To find the corresponding determinants, we **delete** the **row** and **column** corresponding to the coefficients in the matrix and take the remainder $2 \times 2$ matrix:
$$\Large
\det(\mathbf{A}) = a_{11}
\begin{vmatrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{vmatrix}
- a_{12}
\begin{vmatrix}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{vmatrix}
+ a_{13}
\begin{vmatrix}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{vmatrix}
$$
##### Direct Methods
###### 2 × 2
For a square matrix of size $2 \times 2$, its inverse is given by:
$$\large
\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})}
\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix} = \frac{1}{ad-bc}
\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$
###### 3 × 3
For a square matrix of size $3 \times 3$,
$$\large
\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\ 
a_{31} & a_{32} & a_{33} 
\end{pmatrix}
$$
Its inverse can be directly found as followed:
1. Calculate the determinant of the matrix,
	$$\large
	\det(\mathbf{A}) = a_{11}
	\begin{vmatrix}
	a_{22} & a_{23} \\
	a_{32} & a_{33}
	\end{vmatrix}
	- a_{12}
	\begin{vmatrix}
	a_{21} & a_{23} \\
	a_{31} & a_{33}
	\end{vmatrix}
	+ a_{13}
	\begin{vmatrix}
	a_{21} & a_{22} \\
	a_{31} & a_{32}
	\end{vmatrix}
	$$
2. Calculate the minor matrix. This is done by calculating the **determinant corresponding to each element** by **deleting** the element’s **row** and **column** and finding the determinant of the resultant $2 \times 2$ matrix.
	For example, for $a_{22}$, its minor matrix element can be calculated as shown:
	$$\large\begin{aligned}
	&\text{Let } M_{22} \text{ be the element on the minor matrix corresponding to } a_{22}. \\
	&\therefore \ M_{22} =
	\begin{vmatrix}
	a_{11} & a_{13} \\
	a_{31} & a_{33}
	\end{vmatrix} = a_{22} \times a_{33} - a_{23} \times a_{32}
	\end{aligned}
	$$
	Repeat this for all the elements to calculate the minor matrix:
	$$\large
	\text{Minor}(\mathbf{A}) = 
	\begin{pmatrix}
	M_{11} & M_{12} & M_{13} \\
	M_{21} & M_{22} & M_{23} \\ 
	M_{31} & M_{32} & M_{33} 
	\end{pmatrix}
	$$
3. Apply the **cofactor matrix** to the **minor matrix** to get the **cofactor matrix $\large\mathbf{C}$ of $\large\mathbf{A}$**.
	$$\large
	\text{Cofactor Matrix = }
	\begin{pmatrix}
	+ & - & + \\
	- & + & - \\
	+ & - & + \\
	\end{pmatrix}
	$$
	$$\large
	\mathbf{C} = 
	\begin{pmatrix}
	+M_{11} & -M_{12} & +M_{13} \\
	-M_{21} & +M_{22} & -M_{23} \\ 
	+M_{31} & -M_{32} & +M_{33} 
	\end{pmatrix}
	$$
4. **Transpose** the Cofactor Matrix $\large\mathbf{C}$ to get the **Adjugate Matrix**. This is done by **switching the rows and columns**.
	$$\large
	\mathbf{C} = 
	\begin{pmatrix}
	+M_{11} & -M_{12} & +M_{13} \\
	-M_{21} & +M_{22} & -M_{23} \\ 
	+M_{31} & -M_{32} & +M_{33} 
	\end{pmatrix}
	\longrightarrow
	\text{adj}(\mathbf{A}) = 
	\begin{pmatrix}
	+M_{11} & -M_{21} & +M_{31} \\
	-M_{12} & +M_{22} & -M_{32} \\ 
	+M_{13} & -M_{23} & +M_{33} 
	\end{pmatrix}
	$$
5. Finally, **divide $\large\text{adj}(\mathbf{A})$ by the determinant** to find the **inverse matrix**.
	$$\Large
	\mathbf{A}^{-1} =
	\frac{1}{\det(\mathbf{A})}\text{adj}(\mathbf{A}) = 
	\frac{1}{\det(\mathbf{A})}
	\begin{pmatrix}
	+M_{11} & -M_{21} & +M_{31} \\
	-M_{12} & +M_{22} & -M_{32} \\ 
	+M_{13} & -M_{23} & +M_{33} 
	\end{pmatrix}
	$$
This method is usually much **less error-prone** and can be **faster** since it follows set steps rather than thinking randomly. It is especially useful when the question asks you for just a few elements of the inverse matrix such as finding the first row of elements.
##### Row Operations
There are three row operations,
- $r_i \leftrightarrow r_j$ — **Row Switching**
- $r_i \rightarrow kr_i$ — **Row Multiplication**
- $r_i \rightarrow r_i + kr_j$ — **Row Addition** 

These can be used to find the inverse matrix.
1. Create an **augmented matrix** with $\large\mathbf{A}$ alongisde $\large\mathbf{I}$.
	If the left side of the augmented matrix is converted into the identity matrix, the right side becomes $\large\mathbf{A}^{-1}$.
	$$\large
	\begin{pmatrix}
	0 & 0 & 1 & \vdots & 1 & 0 & 0 \\
	1 & 2 & 0 & \vdots & 0 & 1 & 0 \\
	1 & 3 & 1 & \vdots & 0 & 0 & 1
	\end{pmatrix}
	$$

2. Start with the row operation $r_1 \leftrightarrow r_3$. As shown, when row operations are applied on a row $r_i$, the row $r_i$ **gets modified on both matrices**.
	$$\large
	\begin{pmatrix}
	1 & 3 & 1 & \vdots & 0 & 0 & 1 \\
	1 & 2 & 0 & \vdots & 0 & 1 & 0 \\
	0 & 0 & 1 & \vdots & 1 & 0 & 0 
	\end{pmatrix}
	$$
3. Continue with the matrix operations $r_2 → r_2 - r_1$, $r_1 → r_1 + 3r_2 + 2r_3$, $r_2 → r_2 + r_3$, and finally, $r_2 → -r_2$.
	$$\large
	\begin{pmatrix}
	1 & 0 & 0 & \vdots & 2 & 3 & -2 \\
	0 & 1 & 0 & \vdots & 1 & 1 & -1 \\
	0 & 0 & 1 & \vdots & 1 & 0 & 0
	\end{pmatrix}
	$$
	This means that,
	$$\large
	\mathbf{A}^{-1} = 
	\begin{pmatrix}
	2 & 3 & -2 \\
	1 & 1 & -1 \\
	1 & 0 & 0
	\end{pmatrix}
	$$

If any sequence of row operations gives a matrix such that two of its **rows are identical**, that matrix **doesn’t have an inverse** and is singular, such as:
	$$\large
	\begin{pmatrix}
	2 & 8 & 5 \\
	1 & 0 & 2 \\
	1 & 0 & 2
	\end{pmatrix}
	$$
#### Matrix Transformations
Any list of points can be expressed in matrix form with $x$ coordinates occupying the first row and $y$ coordinates occupying the second. For example, for a triangle and a square,
$$\Large
\begin{array}{c c}
\triangle = 
\begin{pmatrix}
x_{1} & x_2 & x_3\\
y_1 & y_2 & y_3
\end{pmatrix} &
\square =
\begin{pmatrix}
x_{1} & x_2 & x_3 & x_4 \\
y_1 & y_2 & y_3 & y_4
\end{pmatrix}
\end{array}
$$
These points can be  **transformed** by **multiplication** with a **transformation matrix**:

| Description                                                                             | Matrix                                                                                           |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Stretch** by a scale factor of $k$ in the **$x-direction$**                           | $$\large \begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}$$                                          |
| **Stretch** by a scale factor of $k$ in the **$y-direction$**                           | $$\large \begin{pmatrix} 1 & 0 \\ 0 & k \end{pmatrix}$$                                          |
| **Enlargement** by scale factor $k$ with **centre origin**                              | $$\large \begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$$                                          |
| **Rotation** about the **centre origin** by $\theta$ in the **anticlockwise** direction | $$\large \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$ |
| **Shear** by factor $k$ in the **$x-direction$**                                        | $$\large \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$$                                          |
| **Shear** by factor $k$ in the **$y-direction$**                                        | $$\large \begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}$$                                          |
| **Reflection** in the line **$y=x$** `(this works by swapping x and y coordinates)`     | $$\large \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$                                          |

^10851a

The **factor by which the transformed shape’s area increases is equal to the determinant of the matrix**. For example, if a shape’s area increases by $\large 2 \times$, $\large\det(\mathbf{A}) = 2$. 
