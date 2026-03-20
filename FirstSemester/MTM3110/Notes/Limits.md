<style>
    body {text-align: justify}
</style>

# Limites

## Definições

### Continuidade
Intuitivamente, dizemos que uma função é contínua em um ponto $x_0$ do seu domínio se o seu gráfico não apresenta saltos em $x_0$. De forma mais simples, quando traçamos o gráfico de $f$, não precisamos ***tirar o lápis do papel***.

Suponha $f$ uma função contínua em $x_0$. 
À medida que $x$ se aproxima de $x_0$, $f(x)$ se aproxima de $f(x_0)$.

---

### Definição (Intuitiva) de Limite
Suponha $f$ uma função definida em um intervalo aberto contendo um ponto 
$x_0$, exceto possivelmente o próprio ponto. Escrevemos que:

$$
\lim_{x \to x_0} f(x) = L
$$

Se os valores de $f(x)$ ficarem arbitrariamente próximos de 
$L$ quando $x$ se torna suficientemente próximo de 
$x_0$, por ambos os lados, ***mas não igual a $x_0$***

#### Exemplos

1) Calcule $\lim_{x \to 1} (x+1)$
$$
\lim_{x \to 1} (x+1) = 2 = f(1)
$$

2) Considere $f:R∖\{1\}→R$ dada por $f(x)=\frac{x^2−1}{x−1}$ encontre: $\lim_{x \to 1} f(x)$
$$
\frac{x^2 - 1^2}{x-1} = \frac{(x+1) - \cancel{(x-1)}}{\cancel{x-1}} = x+1
$$
Valor do limite não depende do valor da função no ponto, assim $\lim_{x \to 1} f(x) = 2$

#### Limites à esquerda e direita

Para $f$ sendo uma função no intervalo $(x_0−l,x_0)$, com $l>0$, escrevemos que:

$$
\lim_{x \to x_0^-} f(x) = L
$$
Se os valores de $f(x)$ podem ser arbitrariamente próximos de $L$ para $x$ próximos de $x_0$ e menores que $x_0$. 
assim, $L$ é o limite à **ESQUERDA** de $f$.

Para $g$ sendo uma função no intervalo $(x_0−l,x_0)$, com $l>0$, escrevemos que:

$$
\lim_{x \to x_0^+} g(x) = L
$$
Se os valores de $g(x)$ podem ser arbitrariamente próximos de $L$ para $x$ próximos de $x_0$ e maiores que $x_0$. 
Assim, $L$ é o limite à **DIREITA** de $g$.
