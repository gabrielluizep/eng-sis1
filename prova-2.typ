#import "./typst-ifsc/templates/article.typ": article

#show: doc => article(
  title: "Atividade avaliativa de Sistemas LIT",
  subtitle: "2º Avaliação de Sinais e Sistemas I",
  authors: ("Gabriel Luiz Espindola Pedro",),
  date: "28/10/2023",
  doc,
)

= Questão 1
Considere um SLIT (Sistema Linear Invariante no Tempo) discreto com resposta ao
impulso dada por $h[n] = a^n u[n]$:

#enum(
  numbering: "a)",
  [O sistema é causal?],
  [O sistema é estável segundo as condições BIBO (Bounded Input - Bounded Output)?],
)

== Resposta

Sim, o sistema é causal, pois $h[n] = 0$ para $n < 0$, issos se dá pela
influência da função degrau multiplicando todo o restante da função, pois
sabemos que:

$
u[n] := cases(0 quad n < 0, 1 quad "c. c.")
$

Por definção um sistema é estável se toda entrada limitada produz uma saída
limitada. Podemos utilizar a seguinte formula para determinar se um sistema é
estável:

$
sum_(k=-oo)^oo |h[k]| < oo
$

Devido a causalidade do sistema $h[n]$, demonstrada anteriormente, podemos
reescrever a equação acima como:

$
sum_(k=0)^oo |h[k]| < oo
$

Substituindo $h[n]$ na equação acima e desconsiderando o degrau unitário, pois
ele implica apenas na causalidade do sistema, obtemos:

$
sum_(k=0)^oo |a^k| < oo
$

Dada a propriedade da multiplicatividade do módulo, podemos fazer a análise do
módulo aplicado a função exponencial:

$
|a^k| = overbrace(|a dot.op a dot.op ... dot.op a|, "k") = overbrace(|a| dot.op |a| dot.op ... dot.op |a|, "k") = |a|^k
$

Portanto, obtemos:

$
sum_(k=0)^oo |a^k| = sum_(k=0)^oo |a|^k
$

Por se tratar de uma série geométrica, para que a série acima seja convergente, $|a| < 1$,
pois caso contrário a série divergiria. Portanto, o sistema é estável segundo as
condições BIBO.

$
sum_(k=0)^oo |a|^k = 1/(1 - |a|) < oo\
$

= Questão 2
A entrada $x(t)$ e a resposta ao impulso $h(t)$ de um sistema contínuo, linear e
invariante no tempo são:

$
x(t) &= u(t)\
h(t) &= e^(-t) u(t)
$

#enum(
  numbering: "a)",
  [Determine a resposta de estado nulo do sistema. Nessa questão não é permitido o
    uso da tabela.],
  [O sistema é estável segundo as condições BIBO (Bounded Input - Bounded Output)?],
)

== Resposta

Para Obtermos a resposta de estado nulo do sistema, devemos realizar a
convolução entre a entrada e a resposta ao impulso do sistema:

$
y(t) = integral_(-oo)^oo x(tau) h(t - tau) dif tau
$

Substituindo $x(t)$ e $h(t)$ na equação acima, obtemos:

$
y(t) = integral_(-oo)^oo u(tau) e^(-t + tau) u(t - tau) dif tau
$

Podemos reescrever a equação acima como:

$
y(t) = integral_(0)^t e^(-t + tau) dif tau
$

Resolvendo a integral acima, obtemos:

$
y(t) &= integral_(0)^t e^(-t + tau) dif tau\
&= integral_(0)^t e^(-t) e^(tau) dif tau\
&= e^(-t) integral_(0)^t e^(tau) dif tau\
&= e^(-t) (e^(tau))|_(0)^t\
&= e^(-t) (e^(t) - e^(0))\
&= e^(-t) (e^(t) - 1)\
&= e^(-t + t) - e^(-t)\
&= 1 - e^(-t)

$

// TODO:
BIBO

$
integral_(-oo)^oo h(t) dif t < oo\
$

Então:

$
integral_(0)^oo e^(-t) dif t
= -e^(-t)|_(0)^oo
= -e^(-oo) + e^(0)
= -0 + 1
= 1
$

Portanto, o sistema é estável segundo as condições BIBO.

$
integral_(-oo)^oo e^(-t) dif t < oo\
$

= Questão 3
Um sistema discreto e invariante no tempo tem a resposta ao impulso $h[n]$ desenhada
na figura a seguir. Determine a resposta de estado nulo do sistema.

#image("./assets/p2q3.png", width: 80%)

Determine a saída $y[n]$ do sistema partindo do princípio que o sistema é linear
e invariante, e as entradas são?

#enum(
  numbering: "a)",
  [$x[n] = 3 delta[n] - 2 delta[n-1]$],
  [$x[n]$ está expresso na figura a seguir],
)

#image("./assets/p2q3-2.png", width: 80%)

= Questão 4
Para uma entrada degrau unitário, determine a resposta total dos seguintes
sistemas LIT (Lineares Invariantes no Tempo):

== Primeiro sistema

$
(dif^2 y(t))/(dif t^2) + 5(dif y(t))/(dif t) + 6y(t) = (dif x(t))/(dif t)\ y_0(0)
= 0 ;quad (dif y_0(0))/(dif t) = -2
$

=== Resposta

Para facil leitura e manipulação podemos reescrever o sistema utilizando a
notação do operador $D$:

$
D^2 y(t) + 5D y(t) + 6y(t) = D x(t)\
$

== Segundo sistema

$
(dif^2 y(t))/(dif t^2) + 4(dif y(t))/(dif t) + 4y(t) = (dif x(t))/(dif t)\ y_0(0)
= 1 ;quad (dif y_0(0))/(dif t) = 2
$

=== Resposta

Para facil leitura e manipulação podemos reescrever o sistema utilizando a
notação do operador $D$:

$
D^2 y(t) + 4D y(t) + 4y(t) = D x(t)\
$

== Terceiro sistema

$
(dif^2 y(t))/(dif t^2) + 4(dif y(t))/(dif t) + 40y(t) = (dif x(t))/(dif t)\ y_0(0)
= 2 ;quad (dif y_0(0))/(dif t) = 10
$

=== Resposta

Para facil leitura e manipulação podemos reescrever o sistema utilizando a
notação do operador $D$:

$
D^2 y(t) + 4D y(t) + 40y(t) = D x(t)\
$

== Quarto sistema

$
y[n+2] + y[n+1] + 0.16y[n] = 5x[n]\ y[-1] = 0; quad y[-2] = 1/4
$

=== Resposta

Para facil leitura e manipulação podemos reescrever o sistema utilizando a
notação do operador de avanço $E$:

$
E^2 y[n] + E y[n] + 0.16y[n] = 5x[n]
$

== Quinto sistema

$
y[n+2] + 1.6y[n+1] + 0.64y[n] = 5x[n]\ y[-1] = 1; quad y[-2] = 2
$

=== Resposta

Para facil leitura e manipulação podemos reescrever o sistema utilizando a
notação do operador de avanço $E$:

$
E^2 y[n] + 1.6E y[n] + 0.64y[n] = 5x[n]
$

== Sexto sistema

$
y[n+2] - 1.56y[n+1] + 0.81y[n] = 5x[n]\ y[-1] = 1; quad y[-2] = 3
$

=== Resposta

Para facil leitura e manipulação podemos reescrever o sistema utilizando a
notação do operador de avanço $E$:

$
E^2 y[n] - 1.56E y[n] + 0.81y[n] = 5x[n]
$