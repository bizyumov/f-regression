# Izyumov- Processing of the oil-producing well testing data by means of fuzzy f-regression model

> Extracted Markdown text from the adjacent PDF primary source. Page layout, formulas, and tables are preserved only approximately.

```text
Processing of the Oil-Producing Well Testing
     Data by Means of Fuzzy f-regression Method

                                        Boris Izyumov

               Gubkin Russian State University of Oil&Gas, Moscow, Russia
                                bizyumov@gubkin.ru

         Abstract. Present paper expands on the fuzzy input – fuzzy output
         regression analysis method that employs the degree of membership
         of a fuzzy point to a crisp parametric curve (hereafter "f -
         regression"). Method outline and formulae are provided.
         A generalized “Maximum Plausiblity Estimator” concept is intro-
         duced as a formal means for defining the best fit of a parametric
         curve to fuzzy data concerning à priori uncertainty information.
         Clustering f-regression extension is defined for use in conjunction
         with “generalizing”, “majority” and “grouping” estimators intro-
         duced in previous papers. An artificial example of clustering f -
         regression is provided.
         Last section contains a well testing example of the pressure build-
         up analysis. The focus of this example is to show the f - regression
         capability to correctly identify linear fragments in the data even if
         each fragment contributes only a small portion of the ensemble.

         Keywords: f-regression, fuzzy data, fuzzy plausibility, measure of
         plausibility, maximum plausibility estimate, data clustering, well tes-
         ting, bottomhole pressure, build-up curve.


1      Introduction

   An oilfield is a natural geological object containing an unknown quantity of hydrocarbons that represent a commercial opportunity. Modern oilfield development planning involves building 3D computer models based on the data from seismic surveys
and exploration wells and updating them as more data becomes available. As drilled
wells provide direct access to the field, they are perceived the most reliable data
source. Extensive research is carried out to extract every bit of useful information
from the (very limited) well data for the sake of oilfield evaluation.
   Well testing is a means of obtaining crucial parameters of the near-wellbore zone:
skin-factor, transmissibility, formation features etc. It involves producing a well at a
known rate while recording the bottomhole pressure. In particular, “pressure buildup” test is conducted after the well is “shut-in” (rate = 0). Pressure build-up and pressure derivative profiles reflect multiple simultaneously occurring processes melded
into a single curve. The effects of these processes on the resulting curve have been


                                               14


investigated to a great extent [1]. Matching pressure derivative in log-log coordinates
with an ideal “type curve” is a common technique used by reservoir engineers. Linear
fragments of the derivative profile indicate the domination of a particular effect, and
getting parameter estimates by fitting groups of points with straight lines allows obtaining sought-after filtration parameters.
   In Section 5 we provide an example of the automatic discovery of linear features in
the pressure build-up data leveraging the uncertainty information available.


2      Linear Regression Analysis – an Overview

   General regression analysis problem is formulated as follows: based on a limited
number N of observations of independent variables           and dependent variable y
one has to identify such vector          that provides the best (in a strictly defined
sense) prediction capabilities for     (    ), where            .
   Linear least squares (LLS) criterion introduced by Karl Gauss uses the assumption that for each observation       ,
                                                 ,                                  (1)
   with normally distributed measurement error         (    ). Hence the regression
problem is reduced to finding such that minimizes the dispersion of formulated as
                               ( ) ‖           ‖        ,                           (2)
   For well-defined experimental matrix X, (2) is solved analytically, providing the
equation that has the sense of conditional expectation of    ( )       (    ).
   The method has an inherent measure of both initial and residual uncertainty in a
probabilistic sense, but no mechanism to account for à priori uncertainty information.
A generalization of the LLS employs weights to reflect individual points’ reliability,
but no other inherent means are present.
   Fuzzy regression analysis techniques, on the contrary, acknowledge the fact that
“Uncertainty is an attribute of information” [2]. Most notably, possibilistic regression initially presented by Tanaka et al. [3] has the built-in capability to explicitly
specify uncertainty information.


3      Fuzzy Linear f-regression Method

   Definition 1. Fuzzy number         ( ̅ ) defined on U = R1 is of symmetric L-type
(or L-number for simplicity) if there are real numbers ̅, (  ) and a function L with
   1. L: [0,)  [0,1]; L(0)= 1, L() = 0.
   2. L is continuous, strict monotonous decreasing and
                                                  ̅
                                     ( )      (     ).                           (3)
   Here, ̅ is the mean value and is the spread of A. (For            we get the formal
representation of crisp numbers). ■


                                         15


  In [4], a fuzzy regression approach was proposed to fit fuzzy input          (       )
and output       (      ) data with crisp linear parametric models. The following Lfunction is used in the implementation:
                                  ( )                 ,                          (4)
   with m being the form parameter, allowing to emulate various types of fuzzy numbers from triangular to interval depending on the value of m chosen.


3.1     Measure of Similarity between a Fuzzy Point and a Parametric Curve

   Definition 2 [5]. Let                 , and be      (     ) a crisp function. For given fuzzy point Qi we introduce the similarity measure of Qi with function f (for vector
a) by
                             ( )                (    (    ))                         (5)
   with ( )         or ( )         interpreted as “fuzzy point Qi belongs or does not
belong to the function f with vector a”. ■

  There are two ways to formally introduce fuzzy points to f-regression.
  1. Production T-norm. Assuming spreads for all input and output variables are
        independent, experimental data representation by fuzzy points Qi = (Xi,Yi) is
        given as:
                         (    )       ( )           ( )     ( )                    (6)
  Because of the choice of (4) and (6), for a linear model explicit analytical dependencies for the point’s similarity measure ( ) can be obtained:
                                                ( )
                                    ( )    ( ( ) ),                                (7)
  with                        ( )          ∑                                          (8)

  and                 ( )    (         ∑       |    |         )                       (9)

  2.    Elliptic fuzzy points. We refer the reader to [6] for further information on the
        elliptic fuzzy points and to [7] for an f-regression case utilizing this approach.
   As one can see, the à priori uncertainty information is captured in the spreads and
form attributes of fuzzy numbers and transformed directly and explicitly into a measure of fitness between a curve and a fuzzy point.


3.2     Measure of Similarity between the Ensemble and a Parametric Curve
   To propagate the described similarity metric through the dataset of N fuzzy points,
the family of mean-based aggregation operators has been initially introduced in [4].
   Here we generalize this idea through the concept of plausibility. For example,
   ( ) provides the maximum plausibility of assumption “i-th fuzzy point in the ensemble belongs to         (    )”, which makes ( ) the maximum plausibility estimator for given i, f and a. Aggregated plausibility estimators (referred to as the “aggregation operators” in [4] and [7]) provide the following measures of plausibility:


                                           16


    1.  Geometric mean provides plausibility estimate of the assertion “curve with
        parameters a fits all points in the ensemble simultaneously”:
                              ( ) ∏           ( )     ∑                                (10)
    2. Arithmetic mean provides plausibility estimate of the assertion “curve with
        parameters a fits the majority of points in the ensemble”:
                              ( ) ∑           ( )     ∑                                (11)
    3. Quadratic mean provides plausibility estimate of the assertion “curve with a
        fits the tight group of points in the ensemble”:
                             ( ) √∑            ( )     ∑                               (12)
    The following definition formally introduces the “best fit” criteria of f-regression.

   Definition 3. The Maximum Plausibility Estimate (MPE) is the vector of crisp linear model parameters       that, for the given ensemble of fuzzy points, delivers maximum to the selected plausibility measure      ( ):
                                                    ( ).                           (13)
   NB: As the form parameter m impacts the MPE for the given        , the value should
be indicated for disambiguation where necessary, e.g.       .■


3.3      Data Clustering

    Initial approach to data clustering via f-regression was discussed in [7]. Here we
provide a generalized approach to the regression analysis of experimental data representing multiple classes, each described by a linear model with unique parameters
  ( )
      , ( ) etc. The plausibility measure for the assumption “i-th point belongs to any
class”,      ( ), extends the ordinary similarity measure via:
                         ( ( )      ( )
                                        )     ( ( )) ̃ ̃ ( ( ))                     (14)
    where k is the total number of classes, chosen by the experimenter, and ̃ denotes
the algebraic sum S-norm.
    Any aggregated plausibility estimator         (10)-(12) may be used in conjunction
with (14). In general, upon maximization every           provides unique parameter vectors that are “Maximum Plausibility Estimates” in their particular sense.
    Section 4 provides an example and contains some practical considerations.


4        Impact of Data Uncertainty on the Model Fitness

   Consider the following artificial example (Fig. 1). We have taken 7 points belonging to                   (Class 1) and injected points #5-#7 belonging to
        (Class 2). Both dependent and independent variable were added uniformly
distributed noise       (              ) and        (        ) with         to obtain
             and             that were given to the LLS and f-regression to obtain
parameter estimates (Table 1). This section provides an example of how initial dataset
can be reconstructed from the uncertainty attributes.


                                            17


35

30

25

20

15

10                                                   Noisy
                                                     Real
 5                                                   Least squares
                                                     Class 1 (clustering f-estimator MQ, m=10)
                                                     Class 2 (clustering f-estimator MQ, m=10)
 0
  0        2        4        6         8       10        12        14          16      18      20
               Fig. 1. LLS and Clustering f-regression fitting experimental data

   First, the least-squares regression estimates (dashed line) are obtained as a benchmark. Residual dispersion                  (             ). Since no à priori uncertainty
attributes are utilized by LLS, the same estimate can be obtained with f-regression via
             (geometric mean): if we set                         any positive number ,
we obtain exactly the same result. As one can see from (8)-(10), maximizing (11) is
numerically equivalent to minimizing (3), which enables f-regression to produce LLS
estimates      as a special case.
   Second, we explicitly model the introduced uniform noise through fuzzy numbers
with                                    selecting             (quadratic mean) for group
detection. Cross-check of LLS estimates            against these uncertainty assumptions
reveals already quite high plausibility (0.817) for      . Furthermore, f-regression estimated parameters            are almost indistinguishable from the LLS ones (see Table
1, under f-estimator) and therefore not present on the graph. Point-by-point comparison shows that f-estimates have excellent fit across Class 1 points and               ( )
        (points #5 and #6 clearly marked as “outliers”). The f-estimates get biased towards point #7 to maximize plausibility (0.844) due to near-interval uncertainty.
   (NB: It is of practical relevance that running the same dataset with form parameter
         provides          [           ] that are spot-on for Class 1, and marks all three
Class 2 points as “outliers”. Collected empirical evidence suggests             as the “best
bet” for many problems.)
   Independent results show that the difference between conventional regression and
f-regression can be insignificant even for carefully picked uncertainty data [8]. Running into this situation might be just the nature of the problem under consideration, or
might indicate excessive uncertainty in the data.
   Third, we want to see if outlying points form a specific class. Therefore clustering
f-regression is set with        classes, with all other parameters left intact.


                                             18


              Table 1. Source data and results for the artificial problem in Section 4

                                                     f-estimator       Clustering f-estimator
          Real data        “Noisy” data    LLS                                    (using    )
                                            ( )      ( )       ( )
    #     x         y                    (m = 10) (m = 10) (m = 4)      ( )     ( ( ))       ( ( ))
    1      2.0       5.5    1.94    5.38 0.9980 0.9927             1       1             1        0
    2      4.0       8.5    3.80    8.10 0.9825 0.9677 0.9997              1             1        0
    3      5.0      10.0    5.05   10.10 0.9976 0.9965             1       1             1        0
    4      7.0      13.0    7.20   13.40 0.9989 0.9992 0.9996              1             1        0
    5      9.0      18.3    9.19   18.68        0         0        0       1             0        1
    6     10.5      20.1   10.73   20.56        0         0        0       1             0        1
    7     12.0      21.9   11.76   21.41 0.8700 0.6517 0.0001              1             0        1
    8     14.0      23.5   13.95   23.41 0.8787 0.9770             1       1             1   0.9865
    9     15.0      25.0   15.18   25.36 0.9699 0.9972 0.9998              1             1        1
    10    17.0      28.0   16.82   27.64 0.4976 0.9114 0.9997              1             1   0.4361
                                                                        –        ( )          ( )


                                      =    2.8750    2.9605   2.4926            2.4963       8.9875
                                      =    1.5195    1.5056   1.5007            1.5004       1.0669
Residual dispersion (LLS)                    8.04      8.11    11.27        –        –            –
Plausibility measure (f-regression)        0.8168    0.8437   0.8365        1   0.8367       0.7186

     Further observations can be made to highlight the results (Fig. 1):
     – Plausibility measure for          ( ( ) ( ))        (see Table 1, under “Clustering
         f-estimator”), meaning no points are left outside either class.
                      ( )
     – Estimates             [          ] are spot-on (thick black line). Comparing previ-
         ously obtained MQ (            ) with Class 1, one can see that     ( )
         vs.    ( ( ))      , the decrease enabled and compensated by ( ( ) )         .
                      ( )
     – Estimates             [          ]  are noticeably different from their true values
         (thick grey line), explained by too few Class 2 points in the ensemble.
     – Estimator          is highly non-linear with plethora of local extrema. Optimiza-
         tion method used here is genetic algorithm (MATLAB implementation). Fine-
         tuning is required in order to reliably obtain correct estimates.


5        Well-Testing Data Analysis

   Pressure buildup test is one of the key methods used throughout the reservoir development, and it is conducted as follows. After an oil well has been producing at a
rate q for     hours, it is closed (“shut-in”). The bottomhole pressure difference,
       ( )     ( ), is measured vs. the time since the shut-in,             . The plots
of ( ) and its derivative are known to exhibit linear behavior in log-log or semilog coordinates, based on the currently dominating effect such as e.g. wellbore storage


                                                19


(“afterflow”) and skin in early time, heterogeneous formation behavior in mid-time
and homogenized formation radial flow in late time [1].
   Example used in this section is a dual-porosity pressure buildup test Example 2
presented in [9]. The following combined plot shows pressure build-up and pressure
change rate over “effective time”,           , converted into dimensionless units,
vs.       ⁄     , on a log-log scale (Fig. 2).


5.1       Assumptions and Results
      The following key assumptions were used in the analysis:
      – Form parameter has been set to             .
      – Number of classes (linear fragments) has been set to            .
      – Weights of data points across the ensemble were adjusted based on their per-
          ceived “density”: log-log      ( ) curve clearly has accumulations of data
          points in certain areas, whereas they provide little additional information to the
          observer; hence, their impact should be lowered. Therefore the weights          of
          experimental points were adjusted based on the density of data around the i-
          th point (with defining the width of proximity “window”) as
                                                              |   (   )       (   ) |
                                , where          ∑        (                         ).   (15)
                           ∑

      –       Time-based data is a difference between the time measured with discretiza-
              tion of ca. 1.85 seconds and shut-in time, resulting in the base spread of 0.92
              seconds. Furthermore we adjusted individual spreads based on the value of
              to accommodate rounding errors from having only 5 significant digits.
      –       Pressure data uncertainty stems from (1) measurement errors (0.01 bar) in
              both ( ) and ( ) and value-dependent rounding error in            ; (2) multiple
              phenomena producing stochastic behavior. Varying spreads were adopted in
              early, mid and late times, averaging 1% of mean value across the board.
      –       Pressure derivative data uncertainty is derived from the source variables.
              The weighted formula used in [9] for the derivative calculation at point is:
                                             (        )           (       )
                                 |                                                       (16)
         with           , denoting the time function used.
   As described in [7], relations involving L-numbers can be approximated using firstorder Taylor series expansion that uses only unambiguous operations: addition and
multiplication by a constant. Applying a sequence of transformations, we can estimate
the spread of pressure derivative for each point.
   While efficiently smoothing the        curve, applying (16) leads to the escalation of
fuzziness, yielding the average spread of pressure derivative amounting to 163% of
the mean value. Therefore it has been substituted by the uncertainty of a simplified
non-weighted formula, averaging to 15% of the absolute derivative value.


                                                     20


                                                    1
                                           10
                                         D/CD]pD'
Dimensionless pressure pD and derivative [t


                                                    0
                                           10


                                                    -1
                                           10
                                                               Dimensionless pressure pD
                                                               Dimensionless pressure derivative [t D/CD]p'D
                                                               Class 1 (Wellbore storage unit slope)
                                                               Class 2 (Wellbore storage negative slope)
                                                               Class 3 (Dual-porosity transition)
                                                    -2
                                                               Class 4 (Total system flow)
                                           10 -1                            0                   1                 2                   3               4            5
                                             10                        10                  10                 10                 10              10           10
                                                                                                    Dimensionless time, t D/CD

                                                                  Fig. 2. Log-log match of dual-porosity data with linear fragments


                                                         Table 2. Results of the clustering f-regression applied to pressure build-up data

                                                                                       ()
                                                                                MPEs
                                                                                                          Number of fitting           Number of outliers
                                                     Classes                           [    ]            points ( ( )>0.9)              ( ( )<0.1)           ( )

                                                                                                         Count      Weighted              Count Weighted
  Class 1                                                                –0.1983         0.6797                   6      17.5                144   130.1   0.3413
  Class 2                                                                 0.2010        –0.2617                  21      23.5                113   109.6   0.4440
  Class 3                                                                 0.3192        –0.5839                  22      47.5                126    98.2   0.5639
  Class 4                                                                –0.1348        –0.0403                  48      18.3                  97  128.9   0.3539
  All classes                                                                                                    94      94.1                  37   38.3   0.8150

     151 data points were fitted with 4 linear models, resulting in an 8-dimensional op-
  timization problem. Solving the problem provided plausibility and MPE of the clus-
  tering f-regression shown in Table 2. Further comments highlight the obtained results.
     Early time ( ⁄             ) consists of (1) wellbore storage unit slope described by
  Class 1 ( ( )      suggests that the shut-in time can be fine-tuned), (2) maximum arch,
  (3) wellbore storage negative slope described by Class 2 (see note at the end of this
  section) and (4) transition radial period (virtually non-existent in this example).
     Mid-time ( ⁄                 ) shows characteristic dual-porosity transition valley
  with            . Initial homogenous behavior of high-conductivity fissures is now
  complemented by the response of porous matrix. Class 3 parameters allow further
  estimation of e.g. storativity ratio and interporosity flow.


                                                                                                            21


   Late time ( ⁄               ) shows the homogenized total system radial flow with
theoretical           (zero slope). Descending Class 4 slope ( )           suggests the
well system is gradually approaching reservoir pressure.
   NB: Two observations should be made. First, ensemble-wide generalization of the
clustering f-regression can lead to biased estimates (see dotted extension of the Class
4 line interfering with Class 2). Second, there is a lack of smooth transition between
the fragments. Piecewise-linear or Sugeno extensions can be introduced to fregression to further improve the results.
   MATLAB scripts for running f-regression and the examples in this paper can be
downloaded from http://bizyumov.gubkin.ru/fest/matlab/.


6      Conclusions

   Generalized measure of plausibility (MP) concept is defined as a formal means of
evaluating model fitness provided à priori uncertainty attributes. Maximizing MP
yields the maximum plausibility estimate (MPE) of parameter values. An extension of
the previously published f-regression method is discussed that allows fitting the ensemble of fuzzy points with multiple linear fragments.
   A well testing analysis example is provided that shows the capability of fregression to reproduce the approach of domain expert and accurately identify multiple linear trends on the log-log scale. The paper demonstrates how the explicit à priori uncertainty information can be utilized to identify complex non-linear datasets
reflecting multiple simultaneous processes merged into one curve.


References
1.   Bourdet, D.P.: Well Test Analysis: the Use of Advanced Interpretation Models. 1st ed.
     Elsevier, The Netherlands (2002).
2.   Zadeh, L.A.: Generalized theory of uncertainty (GTU) – principal concepts and ideas.
     Computational Statistics & Data Analysis No. 51, pp. 15-46 (2006).
3.   Tanaka, H., Uejima, S., and Asai, K.: Linear regression analysis with fuzzy model. IEEE
     Transaction on System, Man and Cybernetics No. 12, pp. 903-907 (1982).
4.   Kalinina, E., Wagenknecht, M.: Fuzzy regression analysis and application to a crisp mod-
     el. In: Proceedings of the 8th Zittau Fuzzy Colloquium, pp. 9-18 (2000).
5.   Bandemer H., Gottwald S.: Introduction to Fuzzy Methods (in German). Akademie-
     Verlag, Berlin (1989).
6.   Celminš, A.: Least squares model fitting to fuzzy data. Fuzzy Sets and Systems, No. 22,
     pp. 245-269 (1987).
7.   Izyumov, B.: Application of f-regression method to fuzzy classification problem. In:
     Proceedings of the EUSFLAT Conference, pp. 761-766 (2003).
8.   Sicilia, M.Á., García, E.: On the Use of Bipolar Scales in Preference–Based Recom-
     mender Systems. Berlin Heidelberg, pp. 268-276 (2004).
9.   Bourdet, D.P., Ayoub, J.A., and Pirard, Y.M., SPE 12777 Use of Pressure Derivative in
     Well Test Interpretation, SPEFE, pp. 293-302 (1989).


                                            22

```
