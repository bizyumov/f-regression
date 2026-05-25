# Izyumov- Software tools for regression analysis of fuzzy data

> Extracted Markdown text from the adjacent PDF primary source. Page layout, formulas, and tables are preserved only approximately.

```text
SOFTWARE TOOLS FOR REGRESSION ANALYSIS OF FUZZY DATA


                               Boris Izyumov, Eleonora Kalinina
           Department of Computer-Aided Information Processing and Management
                          Russian State University of Oil and Gas
                          Leninsky pr. 65, 117917 Moscow, Russia
                                email: bobbisson@fuzzy.ru

                                      Michael Wagenknecht
         Institute of Process Technique, Process Automation and Measuring Technique
                           University of Applied Sciences Zittau/Görlitz
                        Theodor-Körner-Allee 16, 02763 Zittau, Germany
                                   m.wagenknecht@hs-zigr.de


Abstract
The software tools are described that are designed for multivariate linear regression analysis of fuzzy
data. The underlying method of f-regression is thoroughly described in [4]. The tools can be used for
modeling both linear relationships and relationships that are nonlinear by nature, but linear in the parameters. Source data can be both crisp and fuzzy. The solution of a technical problem is described,
namely the modeling of a nonlinear univariate function with large uncertainties in source data. It is
shown that software tools enable detecting "outlying" data and achieving stable solution.


1       Introduction
Researchers are considering problem of modeling uncertain, imprecise data for many years.
Tanaka et al. proposed classical fuzzy regression analysis in [5]. In that work, the deviations
between the observed values and the estimated values were supposed to be due to the fuzziness of the parameters of the model. This approach is still one of the most frequently used
analyses [6] due to its use of linear programming and its simplicity. However, that approach
has a weakness, namely sensitiveness to outliers, though there are recent works in this field
[2].
Method of f-regression is based upon the following principles:
    – input (independent) and output (dependent) variables are described by fuzzy sets,
      namely fuzzy points;
    –    model is crisp by nature and parametrical. Parameters are to be determined using
         fuzzy observations;
    – conventional fuzzy regression analyses uses distance between fuzzy point and model
      characterizing their degree of dissimilarity. Here, similarity measure of point with
      model is used.
Method is a modification of fuzzy regression analysis [1].
Fuzzy numbers of symmetrical L-type are used that give certain flexibility when modeling
different classes of fuzzy data, from nearly crisp to interval. Special operators aggregate in-


formation about function fitting individual points. Thus the problem of optimal parameter
finding is reduced to non-linear function optimization problem. In the following section we
give basic definitions and concepts of f-regression method.


2     Method of f-regression

Definition 1. Fuzzy number A is of symmetric L-type if there are real numbers b, s (>0) and a
function L with
    1. L : [0,∞) → [0,1]; L(0)= 1, L(∞) = 0.
    2. L is continuous, strict monotonous decreasing and

                                         t -b 
                            µ A (t ) = L      .
                                               
                                                                                           (1)
                                         s 

Here, b is the mean value and s is the spread. (For s = 0 we get the formal representation of
crisp numbers). L-function being used has the following representation:

                               t - b  m 
                µ (t ) = exp −         ; s ≥ 0 , m > 1.
                                                                                          (2)
                                 s    

In Fig. 1 we depicted the case b = 0, s = 1 for different m.


    Fig. 1. Family of membership functions for fuzzy (L,L)-numbers in the sense of
           Dubois and Prade


The result of measurement is given by b, the spread (fuzziness) can be modelled by s. By varying m one can reach further adaption.
m ≈ 1: Mean value b is more or less known, but there is little fuzziness or it cannot be evalu-
       ated.
m ≈ 2: Mean value and fuzziness can be evaluated.
m ≈ 10: Fuzzy number of interval type.


Definition 2. Let xi∈Ρn and yi real; i = 1,...,N. Then fuzzy set Qi = (Xi,Yi) is called fuzzy point
if

               µ Q ( x i , y ) = µ X ( x1 ) ⋅ ... ⋅ µ X ( x n ) ⋅ µ Y ( y ) .
                   i                  1i                ni             i
                                                                                                  (3)

Thus, for a fuzzy point Qi we obtain:

                        x − x  m                 x − x  m           y − y  m 
µ Qi ( x i , y ) = exp−  1      1i
                                        ⋅ ... ⋅ exp− 
                                                        
                                                           n      ni
                                                                       ⋅ exp− 
                                                                                 
                                                                                        i
                                                                                           .
                                                                                                 (4)
                           β 1i                     β ni             α i    

Definition 3 [1]. Let xi ∈ Ρn , a ∈ Ρk , and be y = f(x,a) a crisp function. For given fuzzy point
Qi we introduce the similarity measure of Qi with function f (for vector a) by

                         M i (a) = sup µ Qi ( x , f ( x , a)) .                                   (5)
                                   x∈n


We can interpret Mi as a measure of compatibility of fuzzy point Qi with the graph of f. Fig. 2
shows similarity measures for two different parameter vectors.


Fig. 2. Similarity measures of fuzzy point Q with linear models with two different parameter
         vectors

For the linear model we get by Lagrange multipliers method:

                                Mi(a) = exp(– di(a))                                              (6)

with
                                                                  m
                                       n              
                                  a 0 +∑ a j ⋅ x ji )  − yi
                                                      
                                                      
                d i (a ) =
                                        j
                                                                      m −1
                                                                             .                    (7)
                              m m −1       n
                                                     m m −1 
                             α i
                                     + ∑ a j ⋅ β ji        
                                                            
                                       j                   


Now suppose to be given N fuzzy points {Qi}. We introduce the weighted aggregation operators M#(a) as

                 MA(a ) = ∑ wi M i (a ) (arithmetic mean),                                  (8)
                             i


                 MG (a ) = ∏ M iwi (a ) (geometric mean),                                   (9)
                             i


or, in general form,
                                                         1
                                   N             P
                         MP(a ) =  ∑ wi M iP (a )                                        (10)
                                   i             

subject to

                                   ∑ w = 1.
                                    i
                                          i                                                (11)


The properties of this operator are different for different P. With P equal to (arithmetic mean)
or greater than 1 individual points’ measures have greater influence on the operator value;
therefore MA conforms to "mean crossing" of model through all fuzzy points. On the other
hand, with P equal to (geometric mean) or smaller than 0 MG can be regarded as an evaluation of "simultaneous crossing" of f through all Qi. Parameter vector that maximizes aggregation operator is considered to be optimal.
Using (6) and (8), we obtain for MA:

                                    n +1 ∑
                       a *A = arg max      wi e − d i ( a ) .                              (12)
                                    a∈R
                                              i


Similarly, from (6) and (9), we obtain for MG:

                                    n +1 ∑
                       a G* = arg min      wi d i ( a ) .                                  (13)
                                    a∈R
                                              i


In the rest of the paper, we will omit MG because we will mainly focus on the compensatory
effect of MA.


3       Software tools "FuReA"
We have developed software tools that implement the described algorithm of linear regression
analysis problem solving. It is written in C++ under C++ Builder Integrated Developer’s Environment. Tools run under Windows 95 or later versions.
Being compact and powerful enough to analyze fuzzy data, FuReA enables:
    -    entering of experimental points, points’ weights and hypothetical fuzziness parame-
         ters;
    -    conducting necessary transformations of variables;
    -    constructing models using existing variables;
    -    performing optimal solution search with necessary level of reliability;


      -    graphic representation of the results of modeling in Euclidian and parameter space.

We would like to stress the last two points.


3.1       Searching for optimal solution
When solving (12) we are faced with numerical difficulties due to the high nonlinearity implying poly-extremality. Fig. 3 highlights the situation. To find the global maximum, special
procedure is used, namely a combination of random or regular search method for rough estimating of maximum and precise Davidon-Fletcher-Powell gradient method for improving results.


              Fig. 3. Aggregation operator arithmetic mean MA in the parameter space

First, conventional weighted least squares method (LSM) is used. Doing so we obtain a good
starting point for our gradient method. But with respect to our criterion, LSM results may lead
to a local maximum, especially when dealing with outliers. That is why on the next step full
search in the parameter space either by simple net search or by modified Cicinadze [3]
method is performed to find other maxima in order to improve them by gradient method. Thus
we get a set of parameter combinations. The result with the largest value of aggregation criterion is considered to be the global maxima.
Table 1 contains the calculation times for different numbers of independent variables and experimental points. One can easily see that regular search is faster for smaller numbers of independent variables, but grows slower and slower as the number of dimensions grows.

                    Table 1. Computational times for different search methods.

  Number of           Number of      Calculation time for random     Calculation time for regular
 experiments         independent     search with normal severity,    search with thorough sever-
                       variables                 sec.                          ity, sec.
16                  3               35.37                           87.11
36                  2               3.46                            5.00
54                  1               1.21                            0.72


3.2   3D graphics
One of the most important capabilities of FuReA software consists in its graphic possibilities,
i.e. we can view fuzzy points and aggregation operators using 3D graphs. Fig. 4 shows source
fuzzy points and the model fitting them. It is helpful for general problem understanding and
visual outlier detection.


                        Fig. 4. Crisp linear model fitting fuzzy points.

FuReA also enables user to see the confidence set analog for fuzzy model. The confidence set
is defined as

                D(a)={a: a = arg{MA(a) ≥ MA(a*)-δ},                                       (14)

and physically it means that model with parameters within this set fits the points "good
enough". Fig. 5 gives a confidence set for δ = 0.2⋅ MA(a*). Often, the confidence set cannot
be described analytically and thus can be obtained only this way.


                  Fig. 5. Confidence set for parameters fitting fuzzy model


4     Technical problem: forecasting of surface protection from being overgrown by sea
       organisms

To protect sea ships and constructions from being overgrown we must add special biocidecontaining substance into their coating. Biocide keeps growing organisms at bay or kills them
if its mass is sufficient. Mass is determined from the so called intensity of biocide separation
by the surface unit. Intensity of separation is the main characteristic of coating effectiveness.

4.1   The problem
The problem of coating effectiveness forecasting is reduced to modeling the dependence between intensity of separation V and time t under some conditions. Using that model, the critical time tcr is determined when critical intensity Vcr is achieved that is too small to prevent
overgrowing. Value of tcr is the effectiveness criterion.
We took source data from stand tests conducted for a long time in natural environment. First
of all we need to learn experimental curves’ behavior and select appropriate model for intensity V(t). Then, we can determine tcr using that model. Critical time tcr is corresponding to the
critical intensity Vcr. In literature it is recommended to assume Vcr to be 20 mcg/cm2⋅day.
Experimental data obtained through stand test at Black Sea are presented in table 2. We have
to make surface protection forecasting for Black Sea based upon these data.

                     Table 2. Intensity of biocide separation from coating

Time of expo- Separation inten- Time of expo- Separation inten-  Time of ex- Separation inten-
 sition, days sity, mcg/cm2⋅day  sition, days sity, mcg/cm2⋅day position, days     sity,
                                                                               mcg/cm2⋅day
       11           41.2                  132         81.2              255            54.6
       20           41.3                  141         85.8              264            40.1
       28           44.5                  151         80.1              273            40.1
       41           45.8                  161          76               284            45.8
       52           45.9                  171         72.5              293             40
       61            46                   181         67.6              305             36
       71           52.5                  192          70               314            37.6
       80           73.3                  201         67.8              322            35.9
       91            76                   210         52.6              335            21.7
      102           75.9                  221          75               344             21
      111           67.8                  231         45.6              356            20.8
      120            80                   242         47.9              364            20.7

As one can see from table 2, intensity V(t) is increasing during several first months, then
reaches its maximum and starts decreasing. Gamma function describes the process under consideration in best manner:

                             V (t ) = at b e − kt                                             (15)

Here a, b and k are parameters influencing the shape of the process curve. Parameter a reflects
scaling of curve along V axis, i.e. overall intensity of the process. Parameter b is more signifi-


cant in the beginning: the greater b, the later maximum V(t) is reached. Parameter k is more
significant at the end of the process: the greater k, the faster the process ends.
The problem of modeling (15) is reduced to determination of parameters a, b и k using experimental data.
Equation (15) can be made linear w.r.t. parameters by applying logarithm transformation to
response function V(t). Therefore, parameter estimates lna, b, k can be obtained through regression analysis:

                             ln V (t ) = ln a + b ln t − kt                                    (16)

Here we assume t to either be non-random value or have an error of 1 day. At the same time,
intensity V must be considered fuzzy. The way of obtaining V values gives us only approximate value due to slime growing on samples. Moreover, temperature of sea water and laboratory water may differ significantly, which alters the separation intensity. Therefore, uncertainty of V value depends on the value itself and can be assumed to be about 10-20%. Consequently, the spread of lnV is 0.1 – 0.2.
Parameter of the form m of all fuzzy numbers is 4, because the general shape of values’ uncertainties is closer to interval.

4.2   The solution
Parameters obtained through f-regression with different spread values in comparison with
LSM solution are presented in Table 3. We get the values of critical times tcr graphically using built in FuReA graph drawer.

         Table 3. Results obtained using f-regression in comparison with LSM results.

                                                                                           Critical
      Variable spreads                              Parameter values            Value of    time
                                                                                  MA
  T        ln(t)     ln(V)            ln(a)          a          b        k                   tкр
                                                      LSM
  –         –            –           1.428         4.17      0.805     0.0082      –        396
                                                  f-regression
  1        0.01          0.2         -1.675       0.187      1.563     0.0123    0.760      373
  0          0           0.2         0.929        2.532      0.957     0.0094    0.700      386

Fig. 6 shows three curves (model with parameters obtained through LSM is marked by thin
line). One can easily observe that first of two f-regression curves reflects intensity V(t) behavior best of all. Maximum for this curve almost coincides with points’ intuitive maximum.
Furthermore, it better approximates the most important piece of curve at large t. At any rate
usage of f-regression yields more confident results which are free from outliers’ disturbance.
Number of outliers is respectively 5 и 8 (a point was considered to be an outlier if its similarity measure with a curve was less then 0.3≈1/e, i.e. curve lies more than one spread value from
the center), i.e. about 20%.


                              V (t ) = 2.532 ⋅ 0.957 t ⋅ e −0.0094⋅t


                    V (t ) = 0.187 ⋅1.563t ⋅ e −0.0123⋅t


              Fig. 6. Results of f-regression solution in comparison with LSM.


References
[1]   H. Bandemer, S. Gottwald, Einführung in FUZZY-Methoden (in german), Akademie-
      Verlag, Berlin (1989).
[2]   Y.S. Chen, Outliers detection and confidence interval modification in fuzzy regression,
      Fuzzy Sets and Systems 119 (2001) 259-272.
[3]   К. Cicinadze, Solution of nonconvex and nonlinear optimization problems (in russian),
      Nauka, Moscow (1983).
[4]   E. Kalinina, M. Wagenknecht, Fuzzy regression analysis and application to a crisp
      model, Proceeding of 8th Zittau Fuzzy Colloquium, Zittau (2000) 9-18.
[5]   H. Tanaka, S. Uejima, K. Asai, Linear regression analysis with fuzzy model, IEEE
      Trans. SMC-12 (1982) 903-907.
[6]   R. Xu, C. Li, Multidimensional least-squares fitting with a fuzzy model, Fuzzy Sets and
      Systems 119 (2001) 215-223.

```
