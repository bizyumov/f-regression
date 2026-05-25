# Izyumov- Application of f-regression method to fuzzy classification problem

> Extracted Markdown text from the adjacent PDF primary source. Page layout, formulas, and tables are preserved only approximately.

```text
The problem of f-regression analysis is formulated
 APPLICATION OF F-REGRESSION                             as follows. Suppose to be given crisp parametric
METHOD TO FUZZY CLASSIFICATION                           dependency
           PROBLEM
                                                                              f(x,a) = 0,                  (1)
                                                         where
                  Boris Izyumov
                                                                    x = (t , y ) , t = (t1 ,..., tn −1 )
                                                                                 T                     T
                                                                                                           (2)
       Dpt. of Computer-Aided Management
            and nformation Processing                    (t stands for vector of independent variables, y is
      Gubkin State University of Oil and Gas             dependent variable) and N fuzzy input/output data
                                                         points. We aim at finding such parameter vector a
     Leninski pr. 65, 117917 Moscow, Russia              for which f would fit experimental points best, in a
            e-mail: bobbisson@fuzzy.ru                   certain sense.
                                                         Fuzzy input/output data are obtained from
                                                         measurements. Each value is extended from crisp
    Abstract. In regression analysis, outliers           number to fuzzy number using subject area
    always represent difficulties because they           knowledge. The fuzzy numbers being used are
    cause modeling errors. But under certain             symmetric L-type fuzzy numbers with membership
    circumstances, they can actually contain             function µA
    useful information, as shown on the
    example of problem described in this                                                  t −a .
                                                                        µ A (t ) = L                   (3)
    article. That is why the task of outlier                                              α 
    identification and analysis presents a
    twofold interest from the technical point            Here, fuzzy set A is described by two values: a is
    of view. It is shown that f-regression               the mean value and α > 0 is the spread. (For α = 0
    method has good outlier detection                    we get the formal representation of crisp numbers).
    capability and can be successfully applied           L-function used in practical implementation has the
    to fuzzy classification problem.                     following representation
    Keywords: f-regression method, fuzzy                                             (       )
                                                                     L(u ) = exp − u m , m ≥ 1             (4)
    regression, outliers, outlier detection, data
    clustering.                                          Parameter m is called form parameter and its value
                                                         defines the overall form of all fuzzy numbers: for
1   Introduction                                         m ≈ 1, the number looks more like triangular fuzzy
Original idea of fuzzy regression analysis was           number;     m ≈ 10      gives    fuzzy   numbers
proposed by Tanaka et al. in 1982 [6]. In his paper,     corresponding to uniformly distributed random
Tanaka discussed fuzzy linear model for which            values. For m ≈ 2, we obtain fuzzy numbers
fuzzy parameters were to be obtained using crisp         resembling normally distributed random numbers.
inputs and either crisp or fuzzy outputs. This
                                                         Values for m and α are chosen based on subject
problem is effectively reduced to linear
                                                         area    knowledge       and/or    common        sense
programming problem, which makes it easy to use
                                                         considerations. Generally, the more uncertainty is
and implement. A number of papers could be
named in which application of conventional fuzzy         present, the greater the α parameter has to be.
regression analysis (also referred to as possibilistic   f-regression is capable of handling of two types of
regression analysis), as well as it improvements, is     fuzzy points (by fuzzy point we mean a vector of
discussed. For instance, issue of outlier detection is   fuzzy numbers):
discussed fairly often and one of the latest
approaches which employs penalty coefficients can            –   symmetric L-type fuzzy points, which
be found in [7].                                                 were initially described in [1]. But here,
                                                                 production T-norm is applied to fuzzy
In contrary, f-regression method [3] is a fuzzy                  coordinates Xi instead of min T-norm to
regression method which is based on fuzzy input                  obtain membership function for fuzzy
and output data and crisp parametric dependency                  points:
between them. The key aspect of f-regression is its
utilization of similarity measure between a model                       µ Q ( x ) = ∏ µ X ( xi )
                                                                                              i            (5)
                                                                                         i
and a fuzzy point. Although much more
complicated, this method has inherent capability to          –   in certain circumstances, there is a
detect and analyze abnormal data, as shown below.                necessity to take interactions between


         different variables into account. For this                      For non-linear and implicit curves (i.e. for most
         case, elliptic fuzzy points were proposed                       general cases of (1)) no analytical solution exists,
         based on work of Celmi š [3]:                                   though an approach using numeric methods has
                                                                         been proposed to accomplish that. Unfortunately,
                    
                        [(                               )] 
                                                              
                                                          1


                    
                                    )
       µ Q ( x ) = L x − x A −1 x − x 2  ,
                                        T
                                               (                   (6)
                                                                         this topic falls out of the scope of current paper.
                                                                       The second key concept of f-regression is
                                                                         aggregation operator. We introduce family of
         where x denotes the vector of individual
                                                                         weighted mean-based aggregation operators that
         coordinates’ mean values, also called
                                                                         collect information about model curve passing
         point’s apex, and A is n×n positive definite                    through all fuzzy experimental data. Three
         matrix referred to as panderance matrix.                        members of this family are of interest to us due to
         As its name implies, α-cut of elliptic fuzzy                    their practical applicability: geometric mean,
         point is ellipsoid. Matrix A is calculated                      arithmetic mean and quadratic mean.
         based on spread values and interrelation
                                                                                                            N
                                                                              MG (a ) = ∏ M iwi (a ) s.t. ∑ wi = 1
         coefficients associated with desirable
                                                                                                                          (11)
         interrelation effect between variables.                                               i             i

The key f-regression concept is similarity measure.                          –     Geometric mean is a strong generalization
It is used to determine the degree to which fuzzy                                  operator. It means that when applied to
point belongs to a crisp curve. A similarity                                       similarity measures, this operator tends to
measure of fuzzy point with respect to parametric                                  give a degree of conformance of all fuzzy
curve is equal to maximum of fuzzy point’s                                         points with the model at the same time. In
membership function on the set of points                                           other words, if this operator is maximized
belonging to the curve.                                                            over parameter space, we get a model
             M (a ) =           sup           µQ ( x )                             which fits all fuzzy points at the same
                             f ( x , a )= 0
                                                                   (7)             time – like the least squares method;
                                                                                                            N
The tractability of a similarity measure is
                                                                                 MA(a ) = ∑ wi M i (a ) s.t. ∑ wi = 1     (12)
straightforward: if it is (near) 1, we say that point
                                                                                           i                i
(almost) lies on a curve; in the case of 0, the point
does not belong to that curve. With respect to                               –     Arithmetic mean is a compensatory
regression analysis, in the case of zero similarity                                operator. That is, applying this operator to
we say that a fuzzy point does not fit explicit                                    similarity measures, one gets an idea about
parametric dependency for that given parameter                                     what is the average degree of similarity
values.                                                                            measure of all fuzzy points with the model.
                                                                                   When maximized over parameter space,
For linear regression curve, analytical solution to
                                                                                   this operator yields a model that passes
(7) has been obtained for both types of fuzzy
                                                                                   through the majority of points;
points and has the following form
                                                                                                       1
                   M (a ) = L(d (a ))                              (8)                N             2     N
                                                                            MQ(a ) =  ∑ wi M i2 (a ) s.t. ∑ wi = 1      (13)
with                                                                                  i                   i

                                    (
                             y − a 0+ a T t        )                         –     Quadratic mean is an ‘elitist’ operator.
       d (a ) =                                          m −1
                                                                                   This is expressed in a fact that individual
                   mm−1 n −1        m
                                          m                       (9)             good-fitting points add more to the value
                   α y + ∑ α t a j m −1                                          of this operator than does ‘gray mass’ of
                              j         
                          j                                                      average-fitting points (opposite to
for symmetric L-type fuzzy points and                                              geometric mean logic). When maximized,
                                                                                   this operator tends to find model that
                                    (
                             y − a0+a T t          )                               passes through ‘elite’ group of points.
              d (a ) =                                            (10)
                                (a Aa )
                                   T          12                         As one can see from (11)-(13), the aggregation
                                                                         operator is bound to [0; 1] and thus can be
for elliptic points.                                                     interpreted as degree of membership of solution to
                                                                         the fuzzy set of best solutions for the problem.
For those curves which are not linear but linear in
the parameters, a transformation can be made                             So the solution of fuzzy regression analysis
which allows using formulas (9) and (10). This                           problem is effectively reduced to unconstrained
will be discussed in detail in section 4.


optimization problem, optimal solution for which         3   Technical problem
will be parameter vector
                                                         Consider the following problem (it is taken from
             a * = arg maxn MP (a )              (14)    “Robust regression and outlier detection” by
                       a∈R
                                                         Rousseeuw and Leroy, 1987, J. Wiley). We
                                                         analyze the dependency between body mass and
2   Outlier detection                                    brain mass of mammals. In our study we use
A note should be made that the similarity measure        dataset, which consists of 65 different mammals,
M effectively serves as a criteria for outlier           ranging from small (mole, rat) to big (cow,
detection. An outlier is defined as follows:             elephant). In the dataset we also put some pre-
                                                         historical animals – dinosaurs, – and primates.
Definition 1. [2] An outlier is the one that appears
to deviate markedly from other members of the            We seek to fit the dependency with function:
collected dataset.
                                                                           b = a0 ⋅ B a1 ,                 (15)
That is why, if the majority of the points shows
high level of similarity measure Mi and some point       where b and B are brain and body masses,
has value of Mi very close to 0, it is right to say      respectively.
that this point conforms to given Definition 1. It       Let’s put in some common sense considerations.
deviates markedly from other members in the sense        We know that a human has larger brain then, say, a
that it does not belong to the function which fits all   dog of the same weight. More generally, ‘body –
other points.                                            brain’ curve for primates will lie higher then
We introduce threshold value h, which is used in         average mammal curve. We don’t change the form
taking decisions about whether point should be           of analytical dependency; we just choose different
regarded as outlier or not. This value should lie        parameters for primates. The reverse consideration
within boundaries (0; 0.5). Value 0.5 is referenced      is true for dinosaurs. It is important to note that one
because a situation when similarity measure of           can solve this problem qualitatively: mind
point to a curve is 0.5 is regarded as undetermined      intuitively captures data samples that significantly
– the point belongs to the curve at the same degree      deviate from the general mass. The computer
as it does not belong to it. In practical cases,         cannot because it has no internal knowledge on
threshold value h = 0.05 can be safely taken.            how to group and classify data samples. So we
                                                         must teach it.
It is necessary to say that different aggregation
operators have different attitudes toward outliers:      We use our knowledge about subject area: since
                                                         the data are average values for each species, we
    –   geometric mean has behavior similar to           must fuzzify them. A good approach would be to
        that of LSM, it perceives fuzzy data as a        set a range on body weight and brain weight values
        whole. As a side effect, it assigns lower        to form a rectangle of all possible cases. But we
        similarity measures for points that deviate      should also reflect the fact that smaller individuals
        most significantly from others. Moreover,        have smaller brain and vice versa by setting
        it can be shown that if we assume crisp          interrelation coefficient between these variables.
        inputs, fuzzy outputs with standard              Therefore we should represent each experimental
        deviation value for spread α and form            data as an elliptic fuzzy point, with α spread value
        parameter m = 2, analysis will produce the       equal to 0.5 of the absolute value for both b and B
        same result as for conventional LSM;             and high interrelation coefficient.
    –   arithmetic mean is the one most often used       Considering the nature of experimental data, which
        in practical implementations since its           is average brain and body mass, we should set
        robustness to outliers. Theoretically it can     form parameter m = 2 to reflect its probabilistic
        provide solutions in cases when up to 50%        origin.
        of data are outliers;
                                                         The described considerations were used to input
    –   quadratic mean has a very special                data to FuReA software tools. The workflow was
        behavior and mainly can be used to               designed with a goal to minimize human effort.
        effectively spot small group of points. It is    The analytical form of equation (15) was not
        well described by the fact that for 10           changed in the course of analysis.
        experimental points, it is more favorable
        for MQ to pass only through 3 points with        First, we used geometric mean on data. The real
        degree 1.0 (others with 0.0) than to pass        world question asked was: can we obtain the most
        through all 10 with degree 0.5.                  general dependency between mammal’s body and


brain masses? The results so obtained were               which is clearly a special dependency within their
unsatisfactory; the value of aggregation operator        category. It is also interesting to note, however,
MG was nearly zero. This could potentially mean          that certain mammals, like galago which is
two things: a) the spreads chosen were too small;        biologically close to primates, reveals high
b) data contains samples wildly different from the       membership to this category.
majority. We dropped a) because we made
                                                         Gray triangles denote the other miscellaneous data
competent decision on spread configurations based
                                                         which did not fall into two main categories. They
on subject area knowledge.
                                                         are dinosaurs, opossum and tenrec. They were
Second, we used arithmetic mean. The real world          categorized together by MQ aggregation operator.
question asked this time was: what is the body –
                                                                                              10000
brain dependency for majority of mammals and
what mammals don’t fit in? This operator has
                                                                                              1000
provided us with a clearer picture: about 20% of
points (in quantity) were discarded as outliers


                                                             Brain mass (g)
                                                                                               100
(threshold was 0.05). Thus we got a confirmation
on previous b) hypothesis. Due to compensatory
property of arithmetic mean we obtained a model                                                 10


fitting as much points as it can: Rodents, Felidae,
Canis, Artiodactyla – all fell into this category. The       0,001              0,01    0,1
                                                                                                 1
                                                                                                      1         10         100   1000   10000   100000
rest of points could be either a) inconsistent,
inaccurate data or b) data too hard to fit in general                                           0,1
                                                                                                          Body mass (kg)
category or even c) data forming special
categories. Since we know the data is accurate we                              Figure 1: Result of regression analysis
proceed without a).
                                                         4                    Discussion
Last, we switched to quadratic mean. The question
now was formulated in the following way: among           Software tools
animals not falling into general category, is there a    f-regression method is implemented in software
group described by specific dependency? To               tools for fuzzy regression analysis called FuReA
proceed with this question, we excluded all              [4]. All the experiments described in this paper
‘general category’ data from our dataset                 were carried out using these tools.
(effectively setting its weight to 0). The analysis
yielded a specific dependency for a small category       Nonlinear regression approach
of primates (chimpanzee, baboon, human etc.), and        We address nonlinear curve (15) described in the
a number of points being outliers with respect to        paper by transforming it to model linear in the
this category. The c) hypothesis and a common            parameters
sense fact described in the beginning of this
paragraph were proven: primates’ body – brain                                          ln m = ln a0 + a1 ln M .                                 (16)
curve lies higher then that of general category          One should note that since m and M are fuzzy
mammals. If we exclude primates from dataset we          variables, ln m and ln M are also fuzzy and should
can once again try to find a different category. The     be calculated using fuzzy transformation approach
category thus obtained is dinosaurs (tiny brain          (this transformation is done internally by the
size).                                                   software and does not require and special action
The result is shown on Figure 1. For convenience,        from the user).
the chart placed here is in logarithmic coordinates.     There are a lot of different model classes that are
For reference, the results obtained from Least           or can be made linear in their parameters with a
Squares Method (LSM) are represented by thin             certain transformation. For example, all
black line. One can observe that it does not seem to     polynomial models fall into this category.
fit data very well. The results of MA run of f-          However, solving a system where not real
regression are depicted in dark line, running            variables but their transformations are taken, we
through rhomb points. One can see that the               intentionally distort the original problem and
majority of mammals actually fit this dependency,        produce “problem falsification” [3].
forming the largest category, except for some 20%        To obtain linear model that we know how to
data samples.                                            handle we introduce vector of variables
Primates are denoted by gray squares and their
specific dependency is represented by gray line


v = (v1 ,..., vc )       and          transformation        functions   3. Additional search is taken to determine a
h( x ) = (h1 ( x ),..., hc ( x )) :                                        number of a with high values of aggregation
                                                                           operator.
                           v = h( x )                           (17)    4. Each of vectors obtained on the previous step
In new variable space we again obtain function                             is used as a starting point for local
linear w.r.t. v and a by applying Taylor series                            optimization.
expansion to h(x) and dropping terms of second                          For step 3, combinatorial search method
and higher order, namely                                                developed especially for that purpose is use.
                  () (
         v =h x +J x− x +o x− x         ) (         )           (18)    The main idea behind combinatorial search method
                                                                        is that we can obtain a fixed (though sometimes
Here J is c×n Jacobian matrix of functions h(x):                        very large) number of solutions (essentially
                   ∂hl ( x )
                                                                        parameter vectors) for the problem, at least one of
     J : jlk =               , l = 1,..., c, k = 1,..., n       (19)    which is guaranteed to be so close to the global
                    ∂xk                                                 optimum that global optimum will be obtained
                                                                        from it after local optimization.
Now, let’s discuss the case when we have model
linear w.r.t. v. To get experimental data for this                      Suppose to be given N crisp points on x ∈ Rn. Then
transformed problem we must apply (18) to every                         for      each          index       set    c = (c1..., cn ) ,
experimental point. From fuzzy set theory we                            1 ≤ ci ≤ N , ci ≠ c j ∀i ≠ j , i,j=1,…,n, we can find
know that the result of operations on fuzzy
numbers have to be calculated through application                       unique parameter vector a (c ) : M Q (a (c )) =1∀ci
                                                                                                            c       i
of Zadeh’s extension principle. The only two                            from system of linear equations (if it is nonunambiguous operations are multiplication by a                          singular, i.e. if xc ≠ xc ∀i ≠ j ), the value of MA
                                                                                               i    j
constant and addition of two fuzzy numbers:
                                                                                                                        n
                 γ⋅X(a,α) = X(γa,|γ|α),                                 aggregation operator being MA(a (c )) ≥           .
                                                                (20)                                                    N
          X(a,α) + Y(b,β) = Z(a+b,α+β).                                                          n
                                                                        Evidently MA(a (c )) >        means that other a(c) lie
Substituting expressions (20) into (18), we                                                      N
calculate transformed experimental data.                                near that point. We introduce a procedure to find
A note on the precision of formula (18) should be                       c~ : MA(a (c~ )) = max MA(a (c )) . Moreover, we are
                                                                                           c
made. The quality of approximation can be poor if                       seeking for a solution which provides a better
the magnitude of the second order derivatives is                        solution then least squares method does, namely
relatively large compared to first order derivatives                     MA(a (c~ )) ≥ MA(a LSM ) . That way we can be sure
and spreads of variables. In some cases this
                                                                        that we apply effective filter to get a starting point
approximation error can be undesirably large due
                                                                        for local optimization method which is guaranteed
to high curvature of transformation functions near
                                                                        to lead to the same or better solution then aLSM
the expansion point.
                                                                        leads to.
Search method used in FuReA
                                                                        One immediate drawback, however, is that one
Procedure of searching for optimal solution is                          gets a total of CnN combinations between which
different for different types of aggregation
                                                                        choice is to be made. That is why some heuristics
operator. The following steps are common for all
                                                                        must be introduced to decrease this number, for
MPs:
                                                                        example, by dropping obviously ineligible
1. Conventional least squares method is used to                         combinations. This can be achieved using the fact
   solve the problem to obtain value aLSM.                              that MA values for different index sets c are not
2. aLSM is used as a starting point for a local                         completely independent.
   optimization method, for example, Simplex or                         5    Conclusion
   Nelder-Mead technique.
                                                                        In conclusion we want to summarize the main
These two steps are sufficient to obtain a* which is                    results of this investigation:
optimal solution for MG aggregation operator
                                                                            –    f-regression can approach data analysis
because it has only one global extremum.
                                                                                 problem from qualitative point of view as
Arithmetic mean and quadratic mean operators
                                                                                 well as from traditional quantitative
require additional steps due to their highly non-
                                                                                 approach;
linear attitude and multiple extrema.


    –   f-regression method produces desirable
        results when adequately calibrated and the
        right aggregation operator is chosen;
    –   f-regression outlier detection capability has
        advanced to a level of fuzzy classification;
    –   f-regression provides means to take
        additional information about subject area
        into account;
    –   the results obtained by f-regression method
        correspond to common sense as it was
        illustrated on a simple one input – one
        output problem. This induces the like
        capabilities for much more complex
        problems which cannot be illustrated on a
        graph.
6   References
[1] H. Bandemer, S. Gottwald. Einführung in
    FUZZY-Methoden (in German). Akademie-
    Verlag, Berlin, 1989.
[2] V. Barnett, T. Lewis. Outliers in statistical
    data, NY, John Wiley & Sons Ltd., 1994.
[3] A. CelmiBš. Least squares model fitting to
    fuzzy data. In Fuzzy Sets and Systems, Vol.
    22, pp. 245-269, 1987.
[4] http://www.fuzzy.ru/ – site dedicated to FuReA
    software tools.
[5] B. Izyumov, E. Kalinina, M. Wagenknecht.
    Software tools for regression analysis of fuzzy
    data. In Proceedings of 9th Zittau Fuzzy
    Colloquium, pp. 221-229, Zittau, Germany,
    2001.
[6] H. Tanaka, S. Uejima, K. Asai. Linear
    regression analysis with fuzzy model. In IEEE
    Transaction on System, Man and Cybernetics,
    Vol. 12, pp. 903-907, 1982.
[7] R.-C. Tsaur, H.-F. Wang. Outliers in Fuzzy
    Regression Analysis. In International Journal
    of Fuzzy Systems, Vol. 1, No. 2, 1999.

```
