#### Products
##### Dot Product
The dot product returns a **scalar**. It shows a measure of how much a vector **extends out** in the **directon of another**. Essentially,
	$$\large \mathbf{a}⋅\mathbf{b}=|\mathbf{b}|×\text{(Length of the projection of a onto b)} $$
###### Formulae
$$\Large
\begin{aligned}
\mathbf{a} \cdot \mathbf{b} &= |\mathbf{a}||\mathbf{b}|\cos\theta \\
\mathbf{a} \cdot \mathbf{b} &= a_ib_i + a_jb_j + a_kb_k \\
\end{aligned}
$$
![[Dot Product.png]]
Make sure that the two vectors are **pointing outward from a point** while using dot product. Otherwise, the angle may be changed (The acute angle $\theta$ in the image may be changed to obtuse).
##### Cross Product
The cross product returns a **vector**. Its **magnitude** is equal to the **area** of the **parallelogram** the two vectors make. Its direction is the **common perpendicular** of both vectors.
###### Formulae
$$\Large
\begin{aligned}
\mathbf{a} \times \mathbf{b} &= \underbrace{|\mathbf{a}||\mathbf{b}|\sin\theta}_\text{Magnitude} \underset{\ \hookrightarrow}{\hat n}\underset{\text{Direction Unit Vector}}{} \\
\mathbf{a} \times \mathbf{b} &=
\begin{vmatrix}
i & j & k \\
a_i & a_j & a_k \\
b_i & b_j & b_k
\end{vmatrix} \\
\text{Area of Parallelogram} &= |\mathbf{a} \times \mathbf{b}| \\
\text{Area of Triangle} &= \frac{1}{2}|\mathbf{a} \times \mathbf{b}|
\end{aligned}
$$
![[Cross Product.png]]
#### Planes
Planes are defined by their **normal**, $\large \mathbf n$ and one other vector **in the plane** and perpendicular to the normal, $\large \mathbf a$. Their equations can be found using either **3 vector points in the plane** `(one to define its displacement from origin, the rest to calculate direction vectors/normal)`, or one point and the normal.
![[Vector Planes.png]]
Planes have **two types of equations**:
- **Cartesian Equation**: The Cartesian Equation is of the form $ax + by + cz = d$. It can be found using the scalar product,
	$$\large
	\mathbf{r} \cdot \mathbf{n} = \mathbf{a} \cdot \mathbf{n}
	$$
	The vector, $\large \mathbf r$ is a **placeholder** vector for any point on the plane, and $\large \mathbf a$ is a **position vector** for a point on the plane. This simplifies to:
	$$\large
	\mathbf{r} \cdot (a\mathbf i + b \mathbf j + c \mathbf k) = d
	$$
	The $a$, $b$, $c$, and $d$ values can be directly replaced into the Cartesian form to give:
	$$\large
	ax + by + cz = d
	$$
- **Vector Form**: The Vector Equation is of the form $\large \mathbf a + \mathbf bs + \mathbf ct$, where $\large \mathbf a$ is the **position vector**, and $\large \mathbf b$ and $\large \mathbf c$ are **direction vectors**.
	$$
	\large \mathbf a + \mathbf bs + \mathbf ct
	$$
The **cross product** of the two **direction vectors** on the plane gives the **normal**.
$$\large
\mathbf b \times \mathbf c = \mathbf n
$$
#### Formulae
##### Lines & Points
###### Shortest Distance Between Point & Line
For any line, $\large \mathbf r = \mathbf a + \mathbf bt$, where $\large \mathbf a$ is the position vector of the point $\large A$ and $\large \mathbf b$ is the direction vector, to find the shortest distance between the line and any point $\large P$,
1. Find the **unit vector** $\large \mathbf{\hat b}$ of $\large \mathbf b$.
2. Find the **vector** $\large \overrightarrow{AP}$.
3. This forms a triangle with $\large \mathbf r$, where the shortest distance is given by $\large |\overrightarrow{AP}|\sin\theta$. To make calculations easier, we can multiply with $\large |\mathbf{\hat b}|$ which doesn’t change the magnitude, but as $\large |\overrightarrow{AP} \times \mathbf{\hat b} | = |\overrightarrow{AP}||\mathbf{\hat b} |\sin\theta$, the shortest distance is now given by the **magnitude** of the **cross product**:
	$$\large |\overrightarrow{AP} \times \mathbf{\hat b} |$$
![[Shortest Distance between Point & Line.png]]
###### Shortest Distance Between 2 Lines
For any two lines $\large \mathbf r_1 = \mathbf a_1 + \mathbf b_1s$ and $\large \mathbf r_2 = \mathbf a_2 + \mathbf b_2t$, their shortest distance is given by:
$$\Large
\Biggm\vert \frac{(\mathbf a_2 - \mathbf a_1) \cdot (\mathbf b_2 \times \mathbf b_1)}{|\mathbf b_2 \times \mathbf b_1|}\Biggm\vert
$$
For the position vectors of the **points that connect the shortest path**,
1. Let $\large P$ be a point on $\large \mathbf r_1$ and let $\large Q$ be a point on $\large \mathbf r_2$ such that $\large \overrightarrow{PQ}$ is the shortest distance between the two lines.
2. Find an expression of $\large \overrightarrow{PQ}$ in terms of $\large s$ and $\large t$ by subtracting one line from the other.
3. As the shortest line is always the perpendicular, we know that,
	$$\large
	\begin{aligned}
	\overrightarrow{PQ} \cdot \mathbf r_1 = 0 \\ 
	\overrightarrow{PQ} \cdot \mathbf r_2 = 0 \\ 
	\end{aligned}
	$$
4. Solve the simultaneous equations to find $\large s$ in terms of $\large t$ and then, the values of $\large s$ and $\large t$.
##### Planes
###### Acute Angle Between Planes
The **acute** angle between two planes can be found using the formula:
$$\Large
\cos \alpha = \frac{\mathbf n_1 \cdot \mathbf n_2}{|\mathbf n_1||\mathbf n_2|}
$$
where $\alpha$ is one of the angles between the planes.
- $\large \alpha \leq 90 \degree$ → $\large \text{Ans} = \alpha$
- $\large \alpha > 90 \degree$ → $\large \theta = 180 \degree - \alpha \ (\text{Ans})$
![[Angle Between Planes.png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
###### Line of Intersection of 2 Planes
For two planes $\large \Pi_1$ and $\large \Pi_2$ with normals $\large \mathbf n_1$ and $\large \mathbf n_2$, their line of intersection $\large \mathbf r = \mathbf a + \mathbf bt$ can be found like so:
1. As $\large \mathbf b$’s **direction** is **parallel** to both planes, it is **perpendicular** to their **normals**. Hence,
	$$\large
	\mathbf b = \mathbf n_1 \times \mathbf n_2
	$$
2. To find the position vector $\large \mathbf a$, there are two methods:
	- Assuming **neither plane is perpendicular to the axis chosen**,
		1. Choose an axis. For example, for the $z-axis$, assuming $z = 0$ exists on both,
			$$\large \text{let } z = 0 $$
		2. This eliminates a variable from the **Cartesian Equation** of the planes, leaving us with two 2-variable equations to solve simultaneously.
			$$\large
			\begin{rcases}
			a_1x+b_1y = d_1 \\
			a_2x + b_2y = d_2
			\end{rcases}
			$$
	- Taking a **free variable**: For two example planes, $3x+y-z=2$ and $x-y+5z=2$,
		1. **Add** the two equations to **eliminate** a variable. For our case, this returns
			$$\large x = 1-z$$
		2. **Substitute** this equation to any of the two planes. For example, with the second, this returns,
			$$\large y=-1+4z$$
		3. Now that we have two of the axes, $\large x$ and $\large y$ expressed in terms of one, $\large z$, we can **take $\large z$ as a free variable**, where it will serve as a **parameter**. To achieve this,
			$$\large \text{let } z = t$$
			Then, as we can express it as $\large z = 0 + 1t$, we can write the line equation as:
			$$\Large
			\begin{pmatrix} x \\ y \\ z \end{pmatrix} =
			\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} +
			\begin{pmatrix} -1 \\ 4 \\ 1 \end{pmatrix}t
			$$
			This works without needing to make any assumptions.

![[geogebra-export(plane intersection line).png]]
 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
###### Angle Between Line & Plane
$$\Large
\cos \alpha = \frac{\mathbf b \cdot \mathbf n}{|\mathbf b||\mathbf n|}
$$
- $\large \alpha \leq 90 \degree$ → $\large \theta = 90 \degree - \alpha$
	![[geogebra-export(vector - plane, line up).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
- $\large \alpha > 90 \degree$ → $\large \theta = \alpha - 90 \degree$
	![[geogebra-export(vector - plane, line down).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
###### Shortest Distance Between Point & Plane
To find the shortest distance between any plane $\large \Pi: \mathbf r \cdot \mathbf n = \mathbf a \cdot \mathbf n$ with the Cartesian Equation $\large ax + by + cz = d$, and any point $\large P(x_p, y_p, z_p)$ such that its position vector is $\large \mathbf p$, there are three methods:
- **Intersection Method**
	1. Create a line passing through $\large P$ that is **perpendicular** to the plane and hence, **parallel** to its **normal**:
		$$\large
		\mathbf l = \mathbf p + \lambda\mathbf n
		$$
	2. Rewrite the line in **parametric** form:
		$$\large
		\mathbf l = (p_i + \lambda n_i)\mathbf i + (p_j + \lambda n_j)\mathbf j + (p_k + \lambda n_k)\mathbf k
		$$
		where $p_i$, $p_j$ and $p_k$ are equal to $x_p$, $y_p$ and $z_p$ respectively, and $n_i$, $n_j$, and $n_k$ are equal to $a$, $b$, and $c$ respectively.
	3. Find the **intersection** of the line and plane using the latter’s Cartesian Equation, solving for $\large \lambda$:
		$$\large
		a(p_i + \lambda n_i) + b(p_j + \lambda n_j) + c(p_k + \lambda n_k) = d
		$$
	4. Calculate the **point** of intersection by putting the value of $\large \lambda$ calculated in the last step back into the line equation of $\large \mathbf l$.
	5. Calculate the **magnitude** of the **point** to find the shortest distance.
- **Dot Product Method**
	1. Take **any point** $\large Q$ that is on the plane, such as $\large \mathbf a$, and calculate the vector $\large \overrightarrow{PQ}$:
		$$\large
		\overrightarrow{PQ} = -\overrightarrow{OP} + \overrightarrow{OQ} = -\mathbf p + \mathbf a
		$$
	2. Then, use the following expression to find the **perpendicular distance** of $\large \Pi$ from $\large P$:
		$$\Large
		\Biggm\vert \frac{\overrightarrow{PQ} \cdot \mathbf n}{|\mathbf n|} \Biggm\vert
		$$
- **Direct Method**
	It is also possible to directly find the shortest distance with a single formula, given that’s all they asked for, by simplifying the above dot product method:
	$$\Large
	\frac{|ax_p+by_p+cz_p+d|}{\sqrt{a^2+b^2+c^2}}
	$$