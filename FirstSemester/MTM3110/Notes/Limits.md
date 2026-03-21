# Limites

## Continuidade
Dizemos que uma função $f$ é contínua em um ponto $x_0$ de seu domínio quando o seu comportamento,
nas proximidades de $x_0$, não apresenta descontinuidades, como saltos ou interrupções.

De maneira mais precisa, $f$ é contínua em $x_0$ quando, ao fazermos $x$ se aproximar de $x_0$,
os valores de $f(x)$ se aproximam de $f(x_0)$.

| ![Continuous graph 01](/FirstSemester/MTM3110/Notes/LimitsImages/Continuous-01.png) | ![Non continuos graph](/FirstSemester/MTM3110/Notes/LimitsImages/NonContinuous-01.png) | ![Continuous graph 02](/FirstSemester/MTM3110/Notes/LimitsImages/Continuous-02.png) |
| :-: | :-: | :-: |
| $f$ é contínua em $x_0$ | $f$ não é contínua em $x_0$ | $f$ é contínua em $x_0$ |

## Definição

Dizemos que o limite de $f(x)$ quando $x\to x_0$ é $L$ quando,
ao aproximar $x$ de $x_0$, os valores de $f(x)$ se aproximam de $L$,
independentemente do valor da função exatamente no ponto $x_0$.

$$
\lim_{x \to x_0} f(x) = L
$$

<details>
<summary><b>Exemplos</b></summary>

> A) Calcule $\lim_{x \to 1} (x+1)$
>
> $$\lim_{x \to 1} (x+1) = 2 = f(1)$$
>
> <img src="/FirstSemester/MTM3110/Notes/LimitsImages/Example-01-A.png" alt="Normal Function" width="40%">

> B) Considere $f:\mathbb{R}\setminus\{1\}\to\mathbb{R}$; dada por $f(x)=\frac{x^2−1}{x−1}$; Encontre: $\lim_{x \to 1} f(x)$
>
> $$\frac{x^2 - 1^2}{x-1} = \frac{(x+1) . \cancel{(x-1)}}{\cancel{x-1}} = x+1$$
>
> <img src="/FirstSemester/MTM3110/Notes/LimitsImages/Example-01-B.png" alt="Example 01 B) Function" width="40%">
>
> Valor do limite não depende do valor da função no ponto, assim $\lim_{x \to 1} f(x) = 2$

</details>

### Limites à esquerda e direita

Seja $f$ uma função definida em $(x_0−l,x_0)$, com $l>0$. Escrevemos

$$\lim_{x \to x_0^-} f(x) = L$$

Se $f(x)$ se aproxima de $L$ à medida que $x$ se aproxima de $x_0$ por valores menores que $x_0$.
Nesse caso, $L$ é o **LIMITE À ESQUERDA** de $f$ em $x_0$.


Analogamente, seja $g$ uma função definida em $(x_0,x_0+l)$, com $l>0$. Escrevemos

$$
\lim_{x \to x_0^+} g(x) = L
$$

Se $g(x)$ se aproxima de $L$ à medida que $x$ se aproxima de $x_0$ por valores maiores que $x_0$.
Nesse caso, $L$ é o **LIMITE À DIREITA** de $g$ em $x_0$.

<details>
<summary><b>Exemplos</b></summary>

> A) Considere a função $f$:
>
> <img src="/FirstSemester/MTM3110/Notes/LimitsImages/Example-02-A.png" alt="Normal Function" width="40%">
>
> $$\lim_{x \to 2^-} f(x) = 3 \qquad \lim_{x \to 2^+} f(x) = 2 \qquad \lim_{x \to 2} f(x) = \nexists $$ 
>
> $$\lim_{x \to 5^-} f(x) = 3 \qquad \lim_{x \to 5^+} f(x) = 3 \qquad \lim_{x \to 5} f(x) = 3 $$

</details>

Seja $f$ uma função definida por um intervalo aberto que contém 
$x_0$, com exceção possivelmente de $x_0$, logo:

$$
\begin{aligned}
\lim_{x \to x_0} f(x) = L 
\iff {} & \lim_{x \to x_0^-} f(x) = L \\
        & \lim_{x \to x_0^+} f(x) = L
\end{aligned}
$$

## Limites infinitos

> [!NOTE]
> Quando $f(x) = \pm \infty$

para $f:\mathbb{R}\setminus\{0\}\to\mathbb{R}$, dada por $f(x)=\frac{1}{x}$

<img src="/FirstSemester/MTM3110/Notes/LimitsImages/Infinity-01.png" alt="Quadratic Function" width="40%">

Se nos aproximarmos de 0 pela direita, os valores de $f(x)$ tendem a $+\infty$.
E se nos aproximarmos pela esquerda, tende a $−\infty$:

$$\lim_{x \to 0^+}\frac{1}{x}=+\infty \qquad \lim_{x \to 0^-}\frac{1}{x}=-\infty$$


$$\therefore \ \lim_{x \to 0^-} f(x) \neq \lim_{x \to 0^+}f(x) \Rightarrow \lim_{x \to 0} f(x) = \nexists$$

Para $g(x)=\frac{1}{x^2}$, o gráfico é dado por:

<img src="/FirstSemester/MTM3110/Notes/LimitsImages/Infinity-02.png" alt="Quadratic Function" width="40%">

$$\lim_{x \to 0^-} g(x) = \lim_{x \to 0^+}g(x) \Rightarrow \lim_{x \to 0} g(x) = +\infty$$

## Limites no infinito

> [!NOTE]
> Quando $x = \pm \infty$

Seja $f$ definida em $(a,+\infty)$, Dizemos que

$$\lim_{x \to +\infty} f(x) = L $$

Quando $f \to L$ à medida que $x \to +\infty$:

$$\lim_{x \to +\infty} \frac{1}{x}=0$$

De forma análoga, para $g$ definida em $(−\infty,b)$,

$$\lim_{x \to -\infty} g(x) = L$$

Quando $g \to L$ à medida que $x \to -\infty$:

$$\lim_{x \to -\infty} \frac{1}{x}=0$$

<details>
<summary><b>Exemplos</b></summary>

> A) $f(x) = x$:
>
> <img src="/FirstSemester/MTM3110/Notes/LimitsImages/Example-03-A.png" alt="Normal Function" width="40%">
>
> $$\lim_{x \to +\infty} f(x) = +\infty \qquad \lim_{x \to -\infty} f(x) = -\infty$$

> B) $g(x) = \frac{1}{x}$:
>
> <img src="/FirstSemester/MTM3110/Notes/LimitsImages/Infinity-01.png" alt="Quadratic Function" width="40%">
>
> $$\lim_{x \to +\infty} g(x) = 0 \qquad \lim_{x \to -\infty} g(x) = 0$$

> C) $h(x) = e^x$:
>
> <img src="/FirstSemester/MTM3110/Notes/LimitsImages/Example-03-C.png" alt="Normal Function" width="40%">
>
> $$\lim_{x \to +\infty} h(x) = +\infty \qquad \lim_{x \to -\infty} h(x) = 0$$

> D) $k(x) = x^2$:
>
> <img src="/FirstSemester/MTM3110/Notes/LimitsImages/Example-03-D.png" alt="Normal Function" width="40%">
>
> $$\lim_{x \to +\infty} k(x) = +\infty \qquad \lim_{x \to -\infty} k(x) = +\infty$$

</details>
