Polar coordinates are coordinates defined in terms of their **radius** with respect to the **angle** (**anticlockwise** about the centre origin). They are expressed as $\large (r, \theta)$, where $r$ is the radius and $\theta$ is the angle.
#### Conversion
To convert a cartesian function to a polar one and vice versa, one must remember the following identities:
- $\large x^2+y^2=r^2$
- $\large x=r\cos\theta$
- $\large y=r\sin\theta$
#### Formulae
- **Integration**: The area enclosed by the curve $r=f(\theta)$, the limits $m$ and $n$, and the origin, is given by
	$$\large
	\frac{1}{2}\int_n^mr^2\ d\theta
	$$
	![[Polar Function Integration.png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
	For example, the above integral is equal to:
	$$\large \frac{1}{2}\int_{\pi \over 16}^{\pi \over 4}(5\theta + 10)^2\ d\theta  $$
- **Differentiation**: By using the identities $x=r\cos\theta$ and $y=r\sin\theta$, or otherwise, you can find the **furthest point** from the axes or the origin by equalling their respective derivatives to $0$.
	- $\Large \frac{\text{dr}}{\text{d}\theta} = 0$: Solution gives Furthest Point from **Origin** 
	- $\Large \frac{\text{dy}}{\text{d}\theta} = 0$: Solution gives Furthest Point from **$\large\theta = 0$** ($x-axis$) 
	- $\Large \frac{\text{dx}}{\text{d}\theta} = 0$: Solution gives Furthest Point from **$\large\theta = \frac{\pi}{2}$** ($y-axis$) 
	![[Polar Coordinates Differentiation.png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
#### Sketching
Take an example function, $r=\sin2\theta$.
1. Choose an **appropriate scale** for your graph. For polar graphs, this means choosing a **multiplier** $k$ so that the **values match up to a predetermined max radius based on the space you have**. As an example, let’s use $k = 6$.
2. Create a **table of values** for your polar function using the “table” mode on your calculator for your domain, such as $0 \leq \theta \leq \frac{\pi}{2}$ with intervals of $\frac{\pi}{16}$. Your values of $\theta$ will show up on the table as decimals, but we already know that each value of $\theta$ is incremented by $\frac{\pi}{16}$.
	
	| $\theta$ | $6\sin2\theta$ |
	| -------- | -------------- |
	| 0        | 0              |
	| 0.1963   | 2.2961         |
	| 0.3926   | 4.2426         |
	| 0.589    | 5.5432         |
	| 0.7853   | 6              |
	| 0.9817   | 5.5432         |
	| 1.178    | 4.2426         |
	| 1.3744   | 2.2961         |
	| 1.5707   | 0              |
	
	As seen above, there’s clear **symmetry** about $\theta = \frac{\pi}{4}$. This means that we could have plotted points only until $\theta = \frac{\pi}{4}$, drawn until that, and reflect that along $\theta = \frac{\pi}{4}$. This can **save a lot of time** when spotted.
3. WIth a **protractor**, plot points for **each increment of $\frac{\pi}{16}$** with any arbitrary radius.
	![[geogebra-export(Sketch-2).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
4. **Angle** your **ruler** such that any line drawn with it passes through both the **origin** and the **points drawn with protractor**. Then, measure out the radius from origin according to your **table of values** for each value of the angle $\theta$ (each increment of $\theta = \frac{\pi}{16}$), and draw points according to them.
	![[geogebra-export(Sketch-3).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
5. Join the points you drew in Step **(4)** to complete the curve.
	![[geogebra-export(Sketch-4).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
- For **1 mark** questions, draw a rough outline of the shape without values.
- For **2 mark** questions, try to find symmetrical lines and such to speed up the process.
- For **3 mark** questions, carefully plot each and every point so as to get the shape correct.
#### Common Curves
The **dotted curves** indicate portions where **$r<0$** and so aren’t usually drawn in the FP1 syllabus.
##### Spirals
- $r=k\theta$
	![[GeoGebra-export(r=kθ).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
- $r=ae^{k\theta}$
	![[geogebra-export(r=aexp(kθ)).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
- $r=\frac{k}{\theta}$
	![[geogebra-export(r=1 over θ).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
##### Sin & Cos Curves
For $\sin k\theta$ and $\cos k\theta$ curves,
- The **angle of rotation** of the $\sin k\theta$ curve with respect to the $\cos k\theta$ curve is $\Large \frac{\pi}{2k}$.
- The **number of petals** of the curves are equal to $k$.
###### $\large\sin k\theta$ & $\large\cos k\theta$ Curves
- $r=\sin\theta$ & $r=\cos \theta$
	![[GeoGebra-export(r=sincosθ).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
- $r=\sin 2\theta$ & $r=\cos 2\theta$
	![[GeoGebra-export(r=sincos2θ).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
###### Limacons
Limacons are curves of the form $r=a+b\cos(\theta)$. Their shape changes as followed:
- $a=b$
	![[GeoGebra-export(limacon - a=b).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
- $a > b$
	![[GeoGebra-export(limacon a more b).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>
- $a < b$
	![[GeoGebra-export(limacon - a less b).png]]
	 <font size="1px"> Modified from an Exported Image Made with [GeoGebra®](https://www.geogebra.org) </font>