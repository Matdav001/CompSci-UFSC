# 2.1 Propositions

> [!NOTE]
>
> Exercícios marcados com (K; Capítulo; Número) são do livro do Kolman.
>
> KOLMAN, B., BUSBY, R. C., ROSS, S.. Discrete mathematical structures. 5th ed. Prentice Hall, 2003
>

## Resoluções

1) (K; 2.1; 1)
    - São Proposições a letra D, e E

2) (K; 2.1; 2, 3)
    - a) 2 + 7 > 11
    - b) 2 é um inteiro ímpar e 8 é um inteiro par
    - c) Não vai chover amanhã e vai fazer sol amanhã.
    - d) Se você dirigir, eu irei a pé.

3) (K; 2.1; 4, 5)
    - a1) $p\land q =$ $3 + 1 < 5$ **e** $7 = 3 × 6$
    - a2) $p\lor q =$ $3 + 1 < 5$ **ou** $7 = 3 × 6$
    - b1) $p\land q =$ eu sou rico **e** eu sou feliz
    - b2) $p\lor q =$ eu sou rico **ou** eu sou feliz
    - b1) $p\land q =$ eu vou de carro **e** eu vou chegar atrasado
    - b2) $p\lor q =$ eu vou de carro **ou** eu vou chegar atrasado

4) (K; 2.1; 6)
    - a) Verdade
    - b) Falso
    - c) Falso
    - d) Falso

5) (K; 2.1; 7)
    - a) Verdade
    - b) Verdade
    - c) Verdade
    - d) Falso

6) (K; 2.1; 10)
    - D) 2 é ímpar ou -3 não é negativo 

7) (K; 2.1; 11)
    - D) 2 é ímpar e -3 não é negativo 

8) (K; 2.2; 3)
    - a) Se eu não sou o presidente do Brasil, então $2+2=4$.
    - b) Se eu vou a pé para o trabalho, então eu não sou o presidente do Brasil.
    - c) Se eu perdi o ônibus para o trabalho, então eu estou atrasado.
    - d) Se eu vou para o shopping, então eu tenho tempo e não estou muito cansado.
    - e) Se eu comprar um carro e uma casa, então eu tenho dinheiro suficiente. 

9) (K; 2.2; 4)
    - a) Se eu sou o presidente do Brasil, então $2+2\neq4$.
    - b) Se eu não vou a pé para o trabalho, então eu sou o presidente do Brasil.
    - c) Se eu não perdi o ônibus para o trabalho, então eu não estou atrasado. 
    - d) Se eu não vou para o shopping, então eu não tenho tempo ou estou muito cansado.
    - e) Se eu não comprar um carro ou não comprar uma casa, então eu não tive dinheiro suficiente. 

10. (K; 2.2; 5)
    - a) Verdade
    - b) Falso
    - c) Verdade
    - d) Verdade


11. (K; 2.2; 6)
    - a) $\lnot r\to q$
    - b) $\lnot q\land p$
    - c) $q \to \lnot p$
    - d) $\lnot p\to \lnot r$

12. (K; 2.2; 5)
    - a) Se eu não vou estudar estruturas discretas e vou ao cinema, então eu estou de bom humor.
    - b) Se estou de bom humor, então eu vou estudar estruturas discretas ou vou ao cinema. 
    - c) Se não estou de bom humor, então não vou ao cinema ou vou estudar estruturas discretas.
    - d) vou ao cinema e não vou estudar estruturas discretas se, e somente se, estou de bom humor.

13. (K; 2.2; 10, 11, 12)

<details>
<summary>a) Contradição</summary>

| $p$ | $p \land \lnot p$ |
| :---:| :---: |
| F | F |
| V | F |

</details>

<details>
<summary>b) Tautologia</summary>

| $p$ | $q$ | $p \to (q \to p)$ |
| :---:| :---: | :---: |
| F | F | V |
| F | V | V |
| V | F | V |
| V | V | V |

</details>

<details>
<summary>c) Contingência</summary>

| $p$ | $q$ | $q \to (q \to p)$ |
| :---:| :---: | :---: |
| F | F | V |
| F | V | F |
| V | F | V |
| V | V | V |

</details>

<details>
<summary>d) Contingência</summary>

| $p$ | $q$ | $q \lor (\lnot q \land p)$ |
| :---:| :---: | :---: |
| F | F | F |
| F | V | V |
| V | F | V |
| V | V | V |

</details>

<details>
<summary>e) Contingência</summary>

| $p$ | $q$ | $(q \land p) \lor (q \land \lnot p)$ |
| :---:| :---: | :---: |
| F | F | F |
| F | V | V |
| V | F | F |
| V | V | V |

</details>

<details>
<summary>f) Tautologia</summary>

| $p$ | $q$ | $(p \land q) \to p$ |
| :---:| :---: | :---: |
| F | F | V |
| F | V | V |
| V | F | V |
| V | V | V |

</details>

<details>
<summary>g) Contingência</summary>

| $p$ | $q$ | $p \to (q \land p)$ |
| :---:| :---: | :---: |
| F | F | V |
| F | V | V |
| V | F | F |
| V | V | V |

</details>

14. (K; 2; Review)
    - Nas notas

15. (Extras)
(a) P = p, Q = p ∨ q
(b) P = p ∧ q, Q = ¬p ∨ ¬q
(c) P = p ∧ q, Q = p ∨ ¬q
(d) P = p ∧ (¬q ∨ r), Q = p ∨ (q ∧ ¬r)
(e) P = p ∧ (q ∨ r), Q = (p ∨ q) ∧ (p ∧ r)
(f) P = p → q, Q = ¬q → ¬p
(g) P = p → q, Q = q ↔ p
(h) P = (p → q) ∧ (q → r), Q = p → r
(i) P = (p → q) → r, Q = p → (q → r)
(j) P = (s → (p ∧ ¬r)) ∧ ((p → (r ∨ q)) ∧ s), Q = p ∨ t

## Notas

### Proposição
### Variável proposicional
### Proposição composta
### Conectivos lógicos
### Conjunção
### Disjunção
### Condicional
### Bicondicional
### Inversa
### Conversa
### Contrapositiva
### Equivalência
### Tautologia
### Contradição
### Contingência
### Equivalência lógica
