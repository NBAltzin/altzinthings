Altzinthings
--------------
初一中学生Altzin一年的研究结果\
2024.08.23 v3.2\
欢迎私信和我讨论\
代数式如下 胆小勿看

$$
\begin{align}
&|x| = \sqrt{x^2} \\
&\lfloor x \rfloor = \frac{W\left(i \pi \left(\frac{1}{2} - \frac{2 \arccos\left(\left|\cos\left(\frac{\pi x}{2}\right)\right|\right)}{\pi}\right) (-1)^{-x + \frac{1}{2}}\right) }{i \pi} + x - \frac{1}{2} \\
&\lceil x \rceil = -\lfloor -x \rfloor \\
&f1(x, a, n) = \begin{cases} 
0, & x = a \\ 
n, & x \ne a 
\end{cases} = \left \lceil \left| \frac{a-x}{|a-x| + 1} \right| \right \rceil n \\
&f2(x, a, n) = \begin{cases} 
n, & x = a \\ 
0, & x \ne a 
\end{cases} = \left \lfloor 1 - \left| \frac{a-x}{|a-x| + 1} \right| \right \rfloor n \\
&f3(x, a, c, b) = \begin{cases} 
c, & x = a \\ 
b, & x \ne a 
\end{cases} = \left \lceil \left| \frac{a-x}{|a-x| + 1} \right| \right \rceil (b - c) + c \\
&f4(a) = \text{sgn}(a) = \frac{|a|}{a + 1 - f1(a, 0, 1)} \\
&f5(a, x, y, z) = \begin{cases} 
x, & a < 0 \\ 
y, & a = 0 \\ 
z, & a > 0 
\end{cases} = \left(\frac{1}{2}z + \frac{1}{2}x - y\right) f4(a)^2 + \frac{z-x}{2} f4(a) + y
\end{align}
$$
