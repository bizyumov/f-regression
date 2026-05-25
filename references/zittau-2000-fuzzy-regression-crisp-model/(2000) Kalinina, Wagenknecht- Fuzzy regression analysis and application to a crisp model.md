# Kalinina, Wagenknecht- Fuzzy regression analysis and application to a crisp model

> Extracted Markdown text from the adjacent PDF primary source. Page layout, formulas, and tables are preserved only approximately.

```text
Fuzzy Regression Analysis and Application to a Crisp Model

                                        Eleonora Kalinina
                               Gubkin Russian State Univ. of Oil and Gas
                                 Laboratory of Applied Mathematics
                                        Leninskiy Prospect 65
                                           Moscow, Russia
                                          kelinor@hotmail.ru

                                       Michael Wagenknecht
                             Univ. of Applied Sciences Zittau/Goerlitz, IPM
                                       Theodor-Koerner-Allee 16
                                        02763 Zittau, Germany
                                     m.wagenknecht@htw-zittau.de


1. Introduction

When modelling real processes, one is often faced with vague non-stochastic data due to incomplete information (e.g., interval values, x > a, x < b, a < x < b), inaccuracy (e.g. non-measurable variables), linguistic vagueness (evaluation of expressions like "is present", "barely
present", "unimportant", "important"; score scales). Here, modelling in a fuzzy environment
will be considered in a traditional way, i.e. from observations (data) we build up a model being optimal in a certain sense and describing the relationship between independent and dependent variables. Fuzzy Sets Theory turns out to be the appropriate apparatus for processing
vague and fuzzy information [1-3]. In the remaining part of this section we give some elementary fuzzy sets fact.

Definition 1. Let U be a crisp set. Moreover, let A be any fuzzy set over U with membership
function .


Definition 2. If U = 1 (real axis), then A is a fuzzy number iff

       1.  at least one x* with A (x*) = 1.

       2. A is upper semicontinuous and quasi-concave.

       3. All level sets A are bounded for (0,1].

Definition 3. Fuzzy number A is of symmetric L-type if there are real numbers b, s(>0) and a
function L with

       1. L : [0,)  [0,1]; L(0)= 1, L() = 0.

       2. L is continuous, strict monotonous decreasing and


                                     .                                                        (1)

Here, b is the mean value and s is the spread. (For s = 0 we get the formal representation of

                                                                                          1


crisp numbers).

In the following we will assume that the input-output model is parametric and crisp whereas
the observations are fuzzy numbers (resp. vectors of the latter). Thus we are led to a modification of fuzzy regression analysis [2].


2. Тechnical background

In the Moscow Pipe Company "FILIT" in welding aggregates, cooling lubricants (CL) are
used in an amount of 40-50 m3. These CL are mixtures of water and mineral technical oil based emulsion. The higher the emulsion's concentration in water the better its corrosion and
biological properties and the longer the pipes are protected against corrosion. However, unreasonable increase of concentration will lead to unnecessary consumption of emulsion and
hence, to economic loss.
In the plant, quality control is carried out by measuring the emulsion's concentration (%) in
CL, corrosivity, and biological impairments. Measurements turn out to be fuzzy.
Concentration is measured by an indirect weighting method (which is adulterated by destructive products and leaks). Corrosivity and biological impairments are evaluated by score
scales.

The evaluation of corrosivity is performed by the degree of corrosion of cast iron chips, i.e.

                                  no corosion — 0 points
                                  traces of c. — 1 p.
                                  weak c.      — 2 p.
                                  moderate c. — 3 p.
                                  strong c.    — 4 p.

Biological impairments are evaluated through the amount of microorganisms per unit volume
(characterized by smell and intensity of colouring when bringing in a special substance). This
leads to the following table.

                                    colour       smell          evaluation (points)

                                    white         none              0
                                    light pink    none              1
                                    pink          none              2
                                    loud pink     weak              3
                                    red           weak              4
                                    raspberry     pungent           5

CL is usable for biological impairment less than 5, otherwise it will be removed from the welding aggregate. If corrosivity of CL exceeds 1, then it is unusable for further welding.
Now, the technical problem consists in finding the minimum concentration of emulsion ensuring corrosivity  1 and biological impairment  4.
Inputs (independent) variables are given by concentration (x1) and impairment (x2). The output
variable y is the corrosivity. Deeper analysis shows a linear connection between inputs and
output, i.e.

                                     y(x,a) = a0 + a1x1 +a2x2                                    (2)

                                                                                            2


with x =          and suited parameter vector a =               .

Now we have to solve the following tasks:
        1. Determine a from given fuzzy information

        2. Using the model obtained, solve (for positive x1)

                                       x1  min                                                      (3)

                                        0  x2  4

                                        y1


3. Fuzzy regression - the problem

We will perform modelling under the following assumptions.

    1. The relationship between inputs and output is described by a crisp linear parametric
       model with parameter vector ak.

    2. Experimental inputs Хi =(Х1i,...,Хni) and outputs Yi are given as fuzzy numbers with
       memberships      and . Here, i = 1,...,N (number of experiments), j = 1,...,n (dimen-
       sion of input).


The Problem.

By the experimental fuzzy data the optimal (in a certain sense) parameter vector a* is to be
determined.

Definition 4. Let xin and yi real; i = 1,...,N. Then fuzzy set Qi = (Xi,Yi) is called fuzzy point if

                                                                      

Definition 5 [2]. Let xin , a  k , and be y = f(x,a) a crisp function. For given fuzzy point Qi
we introduce the similarity measure of Qi with function f (for vector a) by

                                                                    .                                (5)

We can interprete Mi as measure of compatibility of point Qi with the graph of f.

Now suppose to be given N fuzzy points {Qi}. We introduce the aggregation operators MА(a)
and MG(a) as

                                                      (arithmetic mean),                             (6)


                                                                                                 3


                                                     (geometric mean).                    (7)

Recall the following properties of each. Whereas MA evaluates the "mean crossing" of f
through all Qi (compensatory), MG is an evaluation for the "simultaneous crossing" of f
through all Qi (little compensatory effect leading to weakest link policy).

The optimal parameter vector a* is determined from

                                                                                          (8)

with # = A,G.

Correspondingly, the optimal model sounds as

                                     y = f(x,a*) .                                        (9)

However, one should be cautious when choosing the aggregation operator. Non-compensatory
evaluation is problematic, since outliers can lead to false models !


4. Fuzzy regression - the Solution

Suppose inputs and outputs to be modelled by L-type fuzzy numbers, i.e.


                                                                                       (10)


In Fig. 1 we depicted the case b = 0, s = 1 for different m.


Fig. 1. Family of membership functions for fuzzy (L,L)-numbers in the sense of Dubois and
        Prade

The result of measurement is given by b, the spread (fuzziness) can be modelled by s. By va-

                                                                                      4


rying m one can reach further adaption.

m  1 : Mean value b is more or less known, but there is little fuzziness or it cannot be evalu-
       ated.

m  2 : Mean value and fuzziness can be evaluated.

m  10: Fuzzy number of interval type.

Thus, we have


                                                                                            (11)


For the linear model we obtain

                                       Mi(a)= exp(- di(a))                                  (12)

with


                             di(a) =                                                        (13)


Hence

                                                   ,                           .            (14)


When solving (14) we are faced with numerical difficulties which are due to the high nonlinearity implying poly-extremality. Here, a combination of Random Search Methods and Davidon-Fletcher-Powell Procedure (DFP) turned out to be best [4,5].

The algorithm of linear regression analysis has been realized in C++ in a WINDOWS 95 environment. Besides the optimal solutions (14) and corresponding MA(a*) и MG(a*) we can obtain the least squares solution aLS , and for each experimental point Qi we determine its individual evaluation Mi(a*) thus detecting outliers.
The program also makes possible the visualization for one-dimensional regression. In Fig. 2
shows the situation for the model y = 2 + 2x and m = 1.2. The behavior of the aggregation
operator is depicted in Fig. 3, whereas in Fig. 4 the confidence set

                                 D(a)={a: a = arg{MA(a)  MA(a*)-}

for fixed positive  is given.


                                                                                           5


Fig.2. Linear model fitting fuzzy points.


                  a0


                                                                          a1


Fig. 3. Aggregation operator "arithmetic mean" in the parameter space.


                  a0                                                        a1


Fig. 4. Area with given value of aggregation operator in the parameter space.


                                                                                 6


5. Solution analysis

The vagueness of input information leads to vagueness when determining m, i, ji. Among
others we are faced with the problem of stability of the optimal solution a* with respect to variations of m, i, ji and to outliers, as well. Moreover, it is salutary to compare a* with the
least squares solution aLS.
We analyzed different models and cite one of them for illustration.

Example. Consider y = 5 + 6x1 - 3x2 - x3 +  where  is a random noise with density


for given positive  (= 1). We used N = 16 data points; m =1.2,2,4,10; i = {0.1,1,5,10};
ji = {0.025,0.25,1}. In Table 1 we gathered the corresponding results.


Table 1. Optimal parameters

            Operator                               МА                                          МG
                m                1.2          2           4         10       1.2         2           4       10
             a* (true)                                       a* (averaged over i,ji)
             a0 = 5             5.35          5.          5.        5.      4.98         5.           5.      5.
             a1 = 6             5.85        5.93        5.95       5.90     5.57       5.83         5.94    5.81
             a2 = -3            -2.61       -2.86       -2.97     -2.91    -2.58       -2.84        -2.96   -2.83
             a3 = -1            -1.13       -1.08       -1.06     -1.05    -1.07       -1.05        -1.04   -1.04
                                                         Variance h(a) = max a – min a
              h(a0)             0.88        0.01        0.04       0.02     0.05       0.00         0.00    0.00
              h(a1)             1.43        0.18        0.13       0.18     0.02       0.09         0.06    0.05
              h(a2)             0.46        0.11        0.12       0.11     0.12       0.16         0.11    0.16
              h(a3)              1.3        0.05        0.04       0.05     0.03       0.05         0.03    0.02

(aLS evaluations: a0 = 5., a1 = 5.81, a2 = –2.83, a3 = –1.05).


Table 2 demonstrates the desired stability of the optimal a* with respect to outliers (points no.
4,6,8-10) when using operator MA (aLS turned out to be heavily biased).

Table 2. Detection of outliers

                              a0          a1             a2           a3
            a*                 5           6              -3          -1            MA(i) = MAi(a*)
            aLS              7.55        3.50           -2.84       -1.03
                                                            a*
         m = 1.2             5.79        7.44           -2.95       0.35      MA(4,10)<0.01,
                                                                              МA(6,8)<0.001, МA(9)<0.1
          m=2                5.14        5.92           -2.71       -1.12     МA(4,6,8,9,10)<10-6
          m=4                5.02        5.96           -2.97       -1.07     МA(4,6,8,9,10)<10-36
          m = 10             4.99        5.99           -3.00       -1.04     МA(4,6,8,9,10)=0


Summarizing we obtained the following results.

                                                                                                              7


1.    and     differ only little if distubance of data is small.

2. They are stable with respect to  and .

3. Same for m. Preferably m = 4, 10.

4. Estimations for       were stable w.r.t. outliers if their number was less than 30%.

5. Stability for various disturbances of data.

6. For weakly correlated inputs (r < 0.5) estimations are nearly unbiased. For r > 0.9 the results
   became useless.


6. Technical Application

Now let us return to the problem formulated in Section 2. In Table 3 we give the technical
characteristics for CL. Analysis shows that the fuzziness of data can be modelled by (10) with
m = 10, s = 1.


Table 3. Technical data

       N             concentration of emulsion [%]          biological impairment     corrosivity
                                   x1                                  x2                  y
       1                          5.2                                  0                  0
       2                          3.0                                  0                  1
       3                          1.5                                  0                  1
       4                          1.9                                  0                  1
       5                          3.4                                  1                  1
       6                          3.9                                  2                  2
       7                          4.1                                  2                  3
       8                          3.3                                  3                  3
       9                          3.2                                  4                  4
      10                          8.0                                  3                  0
      11                          6.9                                  3                  0
      12                          7.8                                  4                  1
      13                          2.1                                  1                  4

We took i =  = 1; 1i = 1 = 1%; 2i = 2 = 1. As the result of computation using MA(a) we
got

                                      y = 3.53 - 0.89 x1 + 1.11 x2

with МА(а*) = 0.999. Now for the task

                                         x1  min

                                         0  x2  4

                                          y1
we obtained x1 7.83 %.

                                                                                              8


                                         References

1. D. Dubois, H. Prade, Fuzzy Sets and Systems - Theory and Applications. Academic
   Press,N.Y.,1980.

2. H. Bandemer, S. Gottwald, Einführung in FUZZY-Methoden (in German). Akademie-Ver-
   lag, Berlin,1989.

3. D. A. Pospelov, Fuzzy Sets in Models of Control and Artificial Intelligence (in Russian).
   Nauka, Moscow, 1986.

4. D. Himmelblau, Applied Nonlinear Programming. McGraw-Hill, N.Y., 1972.

5. К. Cicinadze, Solution of Nonconvex and Nonlinear Optimization Problems (in Russian).
   Nauka, Moscow, 1983.


                                                                                        9

```
