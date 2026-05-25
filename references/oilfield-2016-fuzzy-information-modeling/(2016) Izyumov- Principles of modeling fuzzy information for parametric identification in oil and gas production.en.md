# Principles of Modeling Fuzzy Information for Solving Parametric Identification Problems in Oil and Gas Production

**B. D. Izyumov**  
Gubkin Russian State University of Oil and Gas (National Research University)

> English translation of: Б.Д. Изюмов, “Принципы моделирования нечеткой информации для решения задач параметрической идентификации в нефтегазодобыче”, *Автоматизация, телемеханизация и связь в нефтяной промышленности*, 2016, No. 6, pp. 21–32.

## Introduction

The modern approach to reservoir development design and management is based on three-dimensional computer models of fields. Such models contain a large number of different parameters obtained by solving parametric identification problems, i.e. inverse coefficient problems [1]. The quality of the resulting three-dimensional model directly depends on the quality of the parameter estimates.

In practice, statistical methods are often used to solve such problems, including least squares (LS), with or without regularization. However, it is often overlooked that LS estimates are theoretically justified within mathematical statistics only when assumptions about the input data are satisfied (see the conditions of the Gauss–Markov theorem). Strictly speaking, methods of mathematical statistics should be applied with caution to field data obtained from unique, non-repeatable experiments: core studies, well logging measurements, pressure-transient curves, and similar data.

Heuristic methods that have proved useful in parametric identification problems, including neural networks, can achieve high-quality solutions for specific problems. However, because of their heuristic nature they do not provide sufficiently justified parameter values and must also be used with caution.

In oil and gas production, parametric identification is further complicated by questionable input-data quality and by the presence of outliers, i.e. observations that stand apart from the ensemble of experimental data. The traditional way out is expert interpretation of data: for example, by comparing experimental pressure-build-up data with typical curves manually or semi-automatically. In doing so, the reservoir engineer brings his or her own knowledge into the problem and, where necessary, uses additional data to obtain correct—subjectively correct—interpretations from imperfect information.

Thus, it becomes relevant to search for new parametric-identification methods capable of:

- “perceiving” inaccurate and unreliable experimental data at a qualitative level;
- taking additional domain knowledge into account;
- obtaining justified qualitative parameter estimates;
- being robust to outliers.

These properties are possessed by a parametric-identification method that uses a fuzzy model of imperfect field information. The method, called **f-regression**, was first described in [2]. The method’s operability and the robustness of f-estimates to outlying observations were later demonstrated for well-test data analysis (using the clustered extension [3] and the piecewise-linear extension of f-regression [4]), geophysical data [5], and several other problems.

The purpose of this paper is to examine the systemic foundations of the method and to provide a theoretical justification for properties of f-regression estimates.

## 1. Characteristic Features of Field Information

A hydrocarbon field, as a natural-technical system, has a number of features that manifest themselves primarily through the imperfection typical of field information. The causes of this imperfection differ: inaccurate or indirect measurements, incomplete or simplified representations of processes and their models, unreliable assumptions about those processes, and so on.

By perfect information we mean information that is accurate, consistent, and fully determined. In real conditions this situation is the exception rather than the rule, which makes it necessary to carry out a systemic study of the characteristics of initial field information. It should also be emphasized that a purely statistical view of the nature of information is not always adequate to reality and may therefore lead to decisions that are far from optimal.

As an example of a successful attempt to systematize the many manifestations of imperfect information, one may cite the classification described by P. Smets [6]. As shown in the scheme in Fig. 1, “imprecision,” “inconsistency,” and “uncertainty” are the three main types of information imperfection. Imprecision and inconsistency characterize the substantive aspect of information: “I am certain that reservoir permeability is at least 10 mD.” Uncertainty, as a rule (though not necessarily), arises from imprecision and characterizes the epistemic aspect of information, i.e. the inability to conclude with complete certainty whether a given proposition is true or false: “the reservoir permeability may be 15 mD.” As Smets notes, “these aspects coexist, but they are clearly distinguishable” [6].[^1]

For clarity, let us give several examples of information imperfection encountered when solving oil and gas production problems:

- failures of pumping equipment may be treated as an example of precise and determined information. The failure stream can conveniently be considered random, since this allows methods of reliability theory to be used, for example, to estimate the number of failures over a certain period. It should be noted that such estimates may contain uncertainty (“the probability of 3 failures during a year is 95%”), imprecision (“the mean number of failures per year is 3.1”), or both types of imperfection simultaneously (“with probability 99%, the number of failures during a year will be 3.1 ± 0.2”);
- estimates of reservoir properties obtained by any means, including expert judgments and statistical methods, may be treated as additional “a priori” precise data whose reliability is questionable. In Mirzadjanzadeh et al. [1], parametric-identification problems in the presence of such estimates are proposed to be reduced to fuzzy multicriteria optimization problems or optimization problems solved by regularization methods;
- the position of the oil-water contact (OWC) may be considered imprecise but determined: due to wetting and capillary-pressure effects, a transition oil-water zone forms above the OWC. The difficulty of describing the transition zone is that saturation can be determined precisely at the scale of an individual pore (the micro level), whereas at the scale of the entire reservoir an exact, single value of the parameters is physically absent and—this should be emphasized separately—is not a random variable. The practical recommendations given in [7] amount to using fuzzy numbers to describe such properties;
- the criteria on which an expert bases field-data interpretation should be regarded as imprecise and uncertain. As noted in [4], interpretation is based on peculiarities of the expert’s perception of the data: for example, the ability to identify groups of points lying along a line, to perceive clusters of points as information “granules,” to relate patterns to previously observed ones, and so on.

Given this variety of information imperfection, it becomes important to develop new methods for analyzing field information based on the most general, i.e. systemic, approach to formalizing both the substantive and the epistemic aspects of imperfect field information.

Let us examine the possibilities of mathematical formalization for modeling both imprecision and uncertainty offered by fuzzy set theory and possibility theory.

## 2. Fuzziness and Possibility

Over the past decades, the established purely quantitative view of information—whose theoretical justification was given by Fisher, Shannon, and Wiener—has repeatedly been subjected to constructive criticism. Various mathematical theories have been proposed for working with the qualitative, semantic component of information. Among these, fuzzy set theory and fuzzy logic stand out; their development was inspired by the human capacity for qualitative evaluation of information [8].

Modeling imperfect information by fuzzy sets, proposed by L. A. Zadeh [9], is primarily suitable for formalizing imprecise, blurred values (“porosity around 10%”) or statements containing linguistic uncertainty (“the formation is low-permeability,” “the sandstone is light brown, fine-grained, medium-strength, with rare interbeds of gray-green argillite”). To formalize logical inference and reasoning based on fuzzy sets—sets whose element membership is determined by a degree in the interval [0, 1]—the mathematical apparatus of fuzzy logic was proposed, defining logical operations of negation, intersection, and union for fuzzy sets.

The principle of extending the classical bivalent degree of truth to the entire unit interval proved fruitful in many applied fields. Later, Zadeh proposed the idea [10], and Dubois and Prade developed the conceptual apparatus of **possibility theory**, a multivalued extension of modal logic that includes the concepts of possibility and necessity. In their view, measures of possibility and necessity can serve as a full-fledged basis for constructing a reasoning system under partial belief, complementing probability theory [11].

The key distinction between fuzzy logic and possibility logic is that the semantic core of the former consists of the concept of a **degree of truth** and a set of fuzzy logical operators, whereas the core of the latter consists of the concepts of an agent’s **degree of belief** in some knowledge about the state of the world, **possibility**, and **necessity**. The similarity is that both logics may be based on fuzzy sets. In the first case, a fuzzy set `X` is interpreted as a **membership function** `μX`, with limiting values `μX(x) = 1` meaning “x belongs to X” and `μX(x) = 0` meaning “x does not belong to X.” In the second case, it is interpreted as a **possibility distribution** `πX`, with limiting values `πX(x) = 1` meaning “x is perfectly possible, or plausible”[^2] and `πX(x) = 0` meaning “x is impossible.”

It should also be noted that, from a mathematical point of view, fuzzy sets are a generalization of classical sets; therefore their domain of application is not limited to any single type of information imperfection. They can be used wherever ordinary sets are used [6].

## 3. Modeling Fuzzy Information

Different methods for solving parametric-identification problems proceed from different assumptions about the nature of the initial data. In particular, least squares assumes that measurements of independent variables are exact and that measurements of dependent variables contain random errors.

This section describes the principles of modeling fuzzy information that underlie the method of fuzzy regression analysis called **f-regression**. Since the mathematical formulation of experimental-data representation in f-regression has already been described earlier (see, for example, [4]), here we give a description of the general principles more suitable for the purposes of this paper. These principles can be used to build a broad family of parametric-identification methods.

### 3.1. Principle of Fuzzy Restriction of Possible Values

The main principle of modeling fuzzy information is that for each measurement `a`, a fuzzy restriction of its possible true values is specified by means of a symmetric L-type fuzzy number

```text
A = <a, α>L
```

with membership function

```text
μA(t) = L((t - a) / α),                                      (1)
```

where `a` is the measured value (the mode of the number), and `α` is the fuzziness (spread), most often selected manually or chosen with account taken of domain knowledge.

The function `L` may be any continuous, strictly decreasing function

```text
L : [0, +∞) → [0, 1],   L(0) = 1,   L(+∞) = 0.
```

For example, previous work used the L-function

```text
L(u) = exp(-u^m),                                             (2)
```

where the shape parameter `m > 1` is chosen according to the nature of the imperfection of the experimental data.

Modeling measurements by a fuzzy quantity—in this case, a symmetric L-number—may have at least two interpretations:

- **Imprecision model.** The fuzzy set `A` semantically expresses the similarity between some `t` and the prototype element `a`. The membership function (1) is numerically equal to the L-function of the distance between the argument `t` and the measurement `a`; the rate at which the distance increases as one moves away from `a` is controlled by the spread `α`.
- **Uncertainty model.** The fuzzy set `A` with membership function (1) semantically expresses the degree of possibility that an element belonging to `A` takes value `t`. The degree of possibility may be interpreted in two ways: as the subjective degree of belief that `t` belongs to `A`, or as the objective degree of physical realizability or attainability of value `t` by an element from `A`.

Dubois and Prade [12] provide a detailed discussion of different semantics of fuzzy sets and possible interpretations of the membership function.

As an example, consider the fuzzy restriction “temperature around 20 °C,” modeled by the fuzzy L-number `T = <20, τ>L`. Under the first interpretation, the degree of similarity of temperature `t = 20 °C` to the fuzzy quantity “around 20” is essentially maximal and equal to 1, whereas for temperature `−10 °C` it will be close to 0—unless the quantitative uncertainty parameter, the spread `τ`, is unjustifiably large. In other words, the membership function is assumed to be a measure of closeness of the true value to the measured value. This assumption will be false in the case of outliers.

Under the second interpretation, the fuzzy quantity “around 20 °C” specifies the possibility for the true value of the temperature to be equal to some `t`. This possibility is maximal at `t = 20 °C`, and it is practically impossible for the true value of the temperature to be `−10 °C`. In other words, the membership function specifies a distribution of possible values for a known measured prototype value [6]. In general, the true value need not be exact or unique.

### 3.2. Principle of Intersection of Fuzzy Coordinates

In the space of measured variables `x ∈ R^n`, a fuzzy point

```text
Q = {Xj},   Xj = <xj, βj>L
```

is defined by the membership function of a multidimensional fuzzy quantity

```text
μQ(x) = μX1,...,Xn(x1, ..., xn),                              (3)
```

where `μX1,...,Xn : R^n → [0, 1]` is the n-dimensional membership function of a vector of fuzzy quantities for the vector of measured values `x = {x1, ..., xn}` and spreads `β = {β1, ..., βn}`. In the special case where the fuzzy quantities `Xj` are non-interactive [10], the membership function of the fuzzy point takes the form

```text
μQ(x) = μX1(x1) *~ ... *~ μXn(xn),                            (4)
```

where `*~` is a T-norm: an operator of intersection of fuzzy sets or measures, i.e. fuzzy logical “AND” (see Appendix 1).

### 3.3. Principle of Similarity Between a Fuzzy Point and a Model

Now consider a parametric model given in implicit form:

```text
f(x, a) = 0,   x ∈ R^n,   a ∈ R^q.                            (5)
```

In possibility theory, one key concept is the possibility measure `Π`, which for a multidimensional fuzzy set with membership function `μX1,...,Xn(x1, ..., xn)` on some crisp subset `D` is defined as [10]

```text
Π(X1, ..., Xn ∈ D) = sup_D μX1,...,Xn(x1, ..., xn).             (6)
```

While membership function (3) reflects measurement imprecision or uncertainty of the true value of a variable, possibility measure (6) expresses the degree of belief that the crisp set `D` contains the true value of the multidimensional fuzzy quantity.

Introduce the key possibility measure: the **similarity measure** (also called “correspondence measure” in [3, 4]) `M(a′)` between a fuzzy point `Q = {Xj}`, given by membership function (3), and model (5) at some parameter values `a′`:

```text
M(a′) = Π(Q ∈ {x : f(x, a′) = 0}; a′)
      = sup_{f(x, a′)=0} μQ(x).                                (7)
```

Here the similarity measure (7) determines the degree of possibility that the fuzzy point `Q`, with membership function (3), measured values `{xj}`, selected spread parameters `{βj}`, and any other selected parameters (for example, the shape parameter `m` in L-function (2) or the type of the L-function itself), belongs to model (5), or lies on curve (5), at parameter values `a′`.

As an example, take a fuzzy point

```text
Q = [<-0.5, 1>L, <0, 0.75>L]
```

(Fig. 2). In the plane `{x1, x2}` a straight line `x2 = a0 + a1 x1` is given with parameters `a′0 = −0.5` and `a′1 = 0.5`. The point `x* = [−0.04; −0.52]` on this line where the membership function reaches its maximum, `μQ(x*) = M(a′) = 0.5`, is marked by a circle. The dashed line marks the boundary of the α-level 0.5.

In the context of the possibility measure, consider the necessity measure `N` that the point `Q` belongs to the model. By definition, for a logical proposition `A`, “the necessity of A is the impossibility of not-A” [6]. From this definition, which is easily formalized within possibility theory (see Appendix 1), it follows that in the general case no fuzzy point necessarily lies on the model.

### 3.4. Principle of Fuzzy Plausibility

Given expression (7) for the similarity measure `M(a′)` between fuzzy point `Q` and model (5) at specific parameter values `a′`, it is straightforward to find the set of values of the possibility measure

```text
Π(Q ∈ Da; a),   where Da = {x : f(x, a) = 0},
```

for all possible parameter values `a ∈ R^q`. The resulting set of values, expressed as a function of the model parameters `a` for measured values `{xj}` and the membership function of fuzzy point `Q` (3), will be called the **fuzzy plausibility distribution** `Λ` of the proposition “the model with parameters `a` passes through fuzzy point `Q`.” Numerically, `Λ(a; Q)` is equal to the similarity measure (7) at the given `a`:

```text
Λ(a; Q) = Π(Q ∈ Da; a).                                       (8)
```

For the fuzzy point `Q` shown in Fig. 2, the fuzzy plausibility distribution in parameter space is shown in Fig. 3 (`a1` is the horizontal axis, `a0` the vertical axis). The point `a′ = [a′1 = 0.5; a′0 = −0.5]`, for which `M(a′) = 0.5`, is marked by a circle. The dashed line shows the level line `M(a) = 0.5`, bounding the set of parameters `{a : M(a) > 0.5}`, i.e. such parameters of the line for which it “more likely passes through point Q than not.”

## 4. Fuzzy Principle of Maximum Plausibility

As noted in Section 3, the principles described above can be used to construct methods for solving very different parametric-identification problems. As an example, consider the formulation of a regression-analysis problem:

- given a limited number of observations `xi ∈ R^n`, `i = 1, ..., N`, find such parameter values of an analytical model `a ∈ R^q` (`N > q`) that the model predicts, in the best possible way (in a certain sense), the values of some variable (called dependent or output) from the values of the remaining variables (independent or input).

As described in the previous section, each of the `N` measurements in the ensemble of experimental data is represented by a fuzzy point (a multidimensional fuzzy quantity) `Qi`. In a hypothetical ideal scenario, all fuzzy points lie on the model with parameters `a′` with certainty, so that `Mi(a′) = 1` for all `i = 1, ..., N`. From the requirement that the L-function strictly decrease, such a situation is possible if and only if all `xi` lie on model (5). Otherwise there exists some `k` such that `Mk(a′) < 1`, and changing parameters `a′` in the direction of increasing the similarity measure of the k-th fuzzy point to the model will in general decrease the similarity measures of other points.

Thus the problem of fuzzy regression analysis can be reduced to a multicriteria optimization problem in which the `N` criteria are the fuzzy plausibility distributions of fuzzy points

```text
Λi(a; Qi) : R^q → [0, 1],   i = 1, ..., N.                     (8)
```

The criteria are aggregated using an N-place averaging aggregation operator

```text
F : [0, 1]^N → [0, 1].
```

The result of this aggregation is an aggregated fuzzy plausibility distribution `Λ(a; {Qi})`, modeling the degree of plausibility of the proposition “the model with parameters `a` passes through (all, most, etc., depending on the selected operator) the points of the ensemble” [4]. This formulation is called **f-regression**.

### 4.1. Selecting an Averaging Aggregation Operator

There is a sufficient body of work on operators that aggregate measures—values in the interval [0, 1] interpreted as degrees of fulfillment of certain criteria. In particular, Yager [13] notes that the choice of an averaging aggregation operator should depend on the desired behavior. One extreme is simultaneous satisfaction of all criteria, achieved by the T-norm (fuzzy logical “AND”) “minimum”:

```text
F(v1, ..., vN) = min{vi}.                                     (9)
```

The opposite extreme is satisfaction of at least any one criterion, for which the S-norm (fuzzy logical “OR”) “maximum” may be used:

```text
F(v1, ..., vN) = max{vi}.                                    (10)
```

The operators `min` and `max` belong, respectively, to families of parametric T-norms and S-norms (see Appendix 1).

An averaging aggregation operator should have the following properties:

- **monotonicity**: `F(u1, ..., uN) ≥ F(v1, ..., vN)` when `ui ≥ vi` for all `i = 1, ..., N`;
- **commutativity**: `F(v1, ..., vN) = F(v′1, ..., v′N)` if `(v′1, ..., v′N)` is any permutation of `(v1, ..., vN)`;
- **idempotence**: `F(v1, ..., vN) = v` if `vi = v` for all `i = 1, ..., N`.

Yager proposed the ordered weighted averaging (OWA) aggregation operator for this purpose [13]. In [4] and in the preceding works, a family of parametric aggregation operators called the **weighted power mean** `Mp` is considered:

```text
F(v1, ..., vN) = Mp(v1, ..., vN; w1, ..., wN)
              = [Σ wi vi^p]^(1/p),                          (11)
```

with the limiting case

```text
lim_{p→0} [Σ wi vi^p]^(1/p) = Π vi^wi,
```

where `−∞ < p < +∞` is the power parameter of averaging, and `wi ≥ 0`, `Σ wi = 1` are weights. The weights must be associated with specific points; otherwise the commutativity property will be violated.

Since the aggregation operator `Mp` at limiting parameter values demonstrates the behavior of fuzzy logical “AND” (9),

```text
Mp→−∞({vi}; {wi}) = min{vi},                                (12)
```

and fuzzy logical “OR” (10),

```text
Mp→+∞({vi}; {wi}) = max{vi},                                (13)
```

choosing the value of `p` makes it possible to obtain any required behavior in this range. In practice, the properties of operators with values in the interval `−1 ≤ p ≤ 2` were studied, in particular `M−1.0` (“harmonic mean”), `Mp→0` (“geometric mean”), `M1.0` (“arithmetic mean”), and `M2.0` (“quadratic mean”). The operator `M0.5`, for example, also has practically useful properties.

In terms of demonstrated behavior, the geometric mean `Mp→0` is semantically closer to searching for a compromise model that captures “all” points (the “AND” operator), while the arithmetic mean `M1.0` is closer to searching for a model passing through “most” points: low values of individual similarity measures are compensated by high values of the others, which makes it possible to recognize outliers as “incompatible with the majority.”

### 4.2. Formulation of the Fuzzy Principle of Maximum Plausibility

Taking (11) into account, the objective function of the regression-analysis problem for an ensemble of experimental data `{xi}` is an aggregated fuzzy plausibility distribution:

```text
Λ(a; {Qi}) = Mp({Λi(a; Qi)}; {wi})
           = [Σ wi Mi^p(a)]^(1/p) → max,                    (14)
```

where

- `Qi = {Xij}`, `Xij = <xij, βij>L`, `i = 1, ..., N`, `j = 1, ..., n`, are the fuzzy points of the ensemble;
- `Λi(a; Qi)` is the fuzzy plausibility distribution of the i-th point;
- `wi ≥ 0` are weights associated with points, `Σ wi = 1`;
- `p ∈ (−∞, +∞)` is the power parameter of the weighted averaging operator.

The **fuzzy principle of maximum plausibility** for f-regression is formulated as follows.

Let an ensemble of experimental data `{xi}` and observation weights `{wi}` be given. Let an L-function with its parameters (such as the shape parameter in (2)) and the spreads `{βij}` also be defined. Let the form of the parametric model (5) be specified. Let the similarity measure between a fuzzy point and the model be described by (7). Let the aggregated fuzzy plausibility distribution as a function of parameters `a` be described by (14) for some value of the power parameter `p`.

Then f-estimates of the model parameters are determined by

```text
a*p = arg max_{a ∈ R^q} Λ(a; {Qi}),                         (15)
```

and if:

1. the model is correctly specified, i.e. correctly defined and adequate to the data;
2. the imprecision or uncertainty of the measured quantities modeled by attributes of the L-numbers—spreads `βij` and so on—is adequate to the true uncertainty, independent for different observations, and not systematic in nature;
3. outliers, i.e. gross measurement errors `xij`, do not dominate the experimental data quantitatively or qualitatively,

then under these conditions the resulting f-estimates will be the most plausible in the sense of the selected aggregation operator `Mp`.

## 5. Discussion of Properties of f-Estimates

As an example, consider a synthetic dataset resembling microseismic monitoring data for hydraulic-fracture propagation. The task is to determine the number of fractures, the strike directions, and the sizes of each fracture zone. Real data are four-dimensional (fracture development over time), but for clarity we restrict ourselves to the two-dimensional case and simple linear models. In this special case, the problem of linear fuzzy regression consists in obtaining the most plausible linear estimates of the model parameters

```text
a^T x = 0,   a = {a1, ..., an}.                              (16)
```

If a model with an intercept is considered, parameter `a0` and variable `x0 ≡ 1` are added, i.e. the parameter vector becomes `a = {a0, a1, ..., an}`.

The ensemble of experimental data (Fig. 4) was obtained as follows:

- for random values of `x1`, two sets of 50 values of `x2` were calculated, belonging to two models:

```text
x2 = 0.25 x1,
x2 = −3 x1;                                                  (17)
```

- random noise was imposed on `x1` and `x2`: `εx1 = εx2 = N(0; 0.05)`;
- 100 random points uniformly distributed over the whole interval were added as outliers.

We show that if the formal requirements of the fuzzy principle of maximum plausibility are met, i.e. if:

- the data are described by an adequate number of linear models;
- data imprecision is modeled by L-function (2) with shape parameter `m = 2` and spread values `β = 0.1`, adequate to the imposed random noise;
- outliers do not dominate useful data,

then the f-regression method will restore models (17), and the obtained f-estimates will be the most plausible in the sense of the arithmetic-mean aggregation operator `M1.0`.

Verbally, the goal of this problem may be formulated as follows: find a small number of linear models that together describe most of the experimental data.

The goal is internally contradictory: the more linear models are used, the more points they will cover. For problems that require simultaneous achievement of several fuzzy criteria, the objective function can be formulated using the fuzzy logical connective “AND”:

```text
μFew(k) *~ Λp=1(a(1), ..., a(k); {Qi}) → max,                 (18)
```

where:

- `{Qi}` is the ensemble of fuzzy points, `Qi = {Xi1, Xi2}`, `i = 1, ..., 200`, `Xij = <xij, βij>L`, `j = 1, 2`;
- `k` is the number of linear models (“clusters” of points);
- `a(1), ..., a(k)` are the parameter vectors of the linear models;
- `μFew(·)` is the membership function of the fuzzy set “small number”;
- `Λp=1(·)` is the aggregated fuzzy plausibility distribution obtained using the arithmetic-mean averaging aggregation operator (11) and based on clustered similarity measures [3];
- `*~` is fuzzy logical “AND,” implemented by the T-norm “algebraic product” (see Appendix 1).

For solving such multicriteria problems, Mirzadjanzadeh et al. proposed formulating the objective function as the geometric mean of fuzzy measures [1]. Obviously, taking a root of degree `c > 1` of the left-hand side of expression (18) does not affect the values of the optimal parameters.

Let us consider two subgoals of this problem.

### 5.1. Identifying Model Parameters Describing Most of the Data

If to each value `xi1` and `xi2` we assign a spread attribute with identical values `β = 0.1` and choose L-function (2) with `m = 2`, we obtain an ensemble of fuzzy points `Qi = {Xi1, Xi2}`, `i = 1, ..., 200`, with the corresponding representation of membership functions in the original space (Fig. 5). In this example, the true uncertainty model—the parameters of normally distributed random noise—is known; in practice, determining the spread model is one of the most important tasks, since inadequate parameter values may lead to an inadequate solution.

The specific feature of this problem is the requirement to describe the ensemble of experimental data by `k` models, i.e. to distribute points among `k` clusters, while each point may belong to all clusters simultaneously (if it lies at the intersection of linear models) or to none of them (in the case of outliers). The goal, however, is to associate each point `Qi` with at least one of the `k` models. As shown in [3], such a parametric-identification problem for a given value of `k` can be solved using the **clustered similarity (correspondence) measure**

```text
MiC(a(1), ..., a(k)) = Mi(a(1)) +~ ... +~ Mi(a(k)),            (19)
```

where `Mi(a(l))` is the similarity measure of point `Qi` to the model with parameters `a(l)`, and `+~` is fuzzy logical “OR,” implemented by the S-norm “algebraic sum” (see Appendix 1).

The aggregated fuzzy plausibility distribution then takes the form

```text
Λp=1(a(1), ..., a(k); {Qi}) = Σ wi MiC(a(1), ..., a(k)),       (20)
```

where `MiC(·)` is the clustered correspondence measure of point `Qi` to any of the `k` linear models (19).

Since there is no a priori information about which points are “good” and which are outliers, by default point weights should be taken equal:

```text
wi = 1/N  for all i.
```

The parameter space of such a problem has dimension `q = 2k` (i.e. `k` linear models with two parameters each). The resulting distribution (20) for `k = 1` is shown in Fig. 6. Taking into account the true parameter values of models (17), theoretically the aggregated plausibility distribution should have two local maxima near the points `[a1 = −3, a0 = 0]` and `[a1 = 0.25, a0 = 0]`. This is precisely what occurs in practice.

It should be noted that the large number of outliers (100 points) had practically no effect on the position of the local maxima of the aggregated plausibility distribution, but it did affect the absolute value of the maximum of the objective function (0.225).

### 5.2. A Small Number of Linear Models

The second subgoal is a fuzzy restriction on the possible number `k` of linear models. Its degree of fulfillment can conveniently be defined through the degree of membership of integer `k` in the fuzzy set “small number”

```text
Few = <0, 4>L
```

with L-function (2) at `m = 4` (Fig. 7).

### 5.3. Overall Result

The solution procedure for optimization problem (18) consists in sequentially solving optimization problem (20) for increasing `k`, starting from `k = 1`. The procedure stops when, at the next iteration, the value of (18) becomes smaller than at the previous one.

The results of the described procedure are given in the table. As can be seen, the optimal number of models is `k = 2`; the parameter estimates obtained by optimization are close to the true values (17).

| Indicator | k = 1 | k = 2 | k = 3 |
|---|---:|---:|---:|
| `{a(l)}` | `a(1) = (−0.0389; −2.97)` | `a(1) = (−0.0411; −2.97)`; `a(2) = (0.0182; 0.259)` | `a(1) = (−0.0348; −2.99)`; `a(2) = (0.0192; 0.257)`; `a(3) = (5.42; 3.35)` |
| `Λp=1({a(l)}; {Qi})` | 0.225 | 0.426 | 0.468 |
| Effect | — | 0.201 | 0.042 |
| `μFew(k)` | 0.996 | 0.939 | 0.729 |
| Result | 0.225 | 0.400 | 0.341 |

It should be noted that the procedure is easily algorithmized for execution without an interpreting expert. It could also be constructed without introducing the additional concept “small number,” simply by analyzing the behavior of the optimal value `Λp=1` as `k` increases: after all “true” lines have been identified, at `k > 2` the method will switch to searching for lines among the outliers (Fig. 8). If outliers do not dominate—one of the stated conditions—then the effect of the new model at the k-th iteration, measured as the difference in the value of `Λp=1` between `k` and `k−1`, will drop abruptly immediately after the optimal `k` is passed (see the table).

Methods that do not explicitly take uncertainty into account cannot be reliably used to estimate parameters in the presence of so many outliers. This applies in particular to Bezdek’s switching regression method [14], proposed as an extension of the fuzzy c-means clustering algorithm. The high robustness of f-regression to outliers is easy to explain by considering how the method “perceives” the data (see Fig. 5): the outliers are visually “noticeably different” from the other points. It should be particularly noted that without knowledge of the spreads, or with spreads that are too large or too small, this distinction will no longer be so obvious (see Fig. 4).

To summarize, let us note several features of f-regression:

- parameter estimates are invariant to the choice of the “independent” variable, unlike least-squares estimates;
- the most general form of dependence (5) implies the possibility of solving parametric-identification problems for nonlinear models given in implicit form;
- similarity measure (7) by default has the meaning of the degree of plausibility of the proposition “the model with parameters `a` passes through point `Q`,” but it may be extended to solve more complex or specific problems (see the description of the clustered measure [3] and the piecewise-linear extension [4]);
- the f-regression problem reduces to unconstrained optimization of a nonconvex function and in general is computationally difficult;
- the aggregated plausibility distribution may be interpreted as the degree of certainty of various fuzzy logical propositions achieved at certain parameter values `a`. In this capacity, the certainty function may be extended by union or intersection with other fuzzy logical propositions to obtain fuzzy formulations of ill-posed problems analogous to those described in [1]. Appendix 1 gives formulas for fuzzy logical operations.

The source code of the analyzed example and the Python f-regression library implementing the f-regression method can be downloaded at: <https://github.com/bizyumov/f-regression>.

## Conclusion

A wide range of production problems in oil and gas extraction require estimates of reservoir properties and other characteristics of the reservoir system by solving inverse problems. Classical methods that consider information purely in statistical, quantitative terms do not guarantee correct parameter estimates when the data are unique, non-repeatable, qualitative, effective, and so on.

As an alternative basis for methods possessing a qualitative view of information, this paper proposes a set of principles based on fuzzy set theory, fuzzy logic, and possibility theory. Using the formulation of the f-regression problem as an example, it is shown that this approach makes it possible to obtain the most plausible parameter estimates (in the sense of the described conceptual apparatus), robust to the presence of outliers in experimental data and, under a number of conditions, guaranteed to be close to the true theoretical values.

## Appendix 1. Ways of Extending Measures of Possibility and Certainty

This section gives, for reference, well-known formulas needed to assemble more complex compositions of fuzzy sets or measures: operations of negation, intersection, union, implication, and so on. It is recommended to use the following continuous functions, since they make it possible to obtain smooth certainty functions.

1. **Negation** is defined by a function `N : [0, 1] → [0, 1]`:

```text
N(a) = 1 − a.                                                 (21)
```

2. **Intersection** (fuzzy logical “AND”) is defined by a parametric function `Tr : [0, 1] × [0, 1] → [0, 1]`, a T-norm:

```text
Tr(a, b) = log_r(1 + ((r^a − 1)(r^b − 1))/(r − 1)),  0 < r < +∞.  (22)
```

The most frequently used implementations are “minimum”

```text
Tr→0(a, b) = min(a, b),                                      (23)
```

and “algebraic product”

```text
Tr→1(a, b) = ab.                                             (24)
```

These two functions, implementing elementary fuzzy logical operations, are sufficient to define all the others.

3. **Union** (fuzzy logical “OR”) is defined by a parametric function `Sr : [0, 1] × [0, 1] → [0, 1]`, a T-conorm or S-norm:

```text
Sr(a, b) = N(Tr(N(a), N(b))).                                (25)
```

The S-norm complementary to T-norm “minimum” (23) is “maximum”:

```text
Sr→0(a, b) = max(a, b).                                      (26)
```

The S-norm complementary to T-norm “algebraic product” (24) is “algebraic sum”:

```text
Sr→1(a, b) = a + b − ab.                                     (27)
```

4. **Fuzzy implication** `A → B` is a measure of truth of the proposition “B is at least as true as A” [15] and is defined by a parametric function `Jr : [0, 1] × [0, 1] → [0, 1]`, which in the special case `r → 1` takes the form[^3]

```text
Jr→1(a, b) = Sr→1(N(a), b) = 1 − a + ab.                     (28)
```

5. In addition to the **possibility measure**, possibility theory introduces the **necessity measure**, defined as the “impossibility of the opposite” in modal logic. The necessity measure `N(A)` on a crisp subset `A ⊆ Ω` is defined as the negation of possibility measure `Π(Ā)` on the complement `Ā`, where `A ∪ Ā = Ω`:

```text
N(A) = N(Π(Ā)) = 1 − sup_{x ∉ A} πX(x).                     (29)
```

A trivial example is the necessity measure of a line passing through a fuzzy point, complementing possibility measure (7). Obviously, in general, if parameter values `a` are not restricted in some special way, the necessity measure of the proposition “point `Qi` cannot fail to lie on model (5)” will be equal to 0.

## References

1. Mirzadjanzadeh A. Kh., Khasanov M. M., Bakhtizin R. N. *Modeling of Oil and Gas Production Processes: Nonlinearity, Nonequilibrium, Uncertainty*. Moscow–Izhevsk: Institute of Computer Research, 2004. 368 p.
2. Kalinina E., Wagenknecht M. “Fuzzy regression analysis and application to a crisp model.” *Proceedings of the 8th Zittau Fuzzy Colloquium*, Sept. 2000, pp. 9–18.
3. Izyumov B. “Emulation of the expert approach to processing well-test curves based on a fuzzy criterion of maximum truth.” *Naftogazova Energetika*, 2013, No. 2 (20), pp. 30–37.
4. Izyumov B. D. “Piecewise-linear fuzzy regression analysis of well-test data.” *Automation, Telemechanization and Communication in the Oil Industry*, Moscow: VNIIOENG, 2013, No. 11, pp. 22–29.
5. Kalinina V., Ermolaev A. I., Izyumov B. D. “Method and software for fuzzy regression analysis and its application to processing geophysical data.” Abstracts of the 4th Scientific and Technical Conference “Current State and Development Problems of the Russian Oil and Gas Production Industry,” Moscow, 2001, p. 19.
6. Smets P. “Imperfect information: imprecision and uncertainty.” In: *Uncertainty Management in Information Systems*. Springer US, 1997, pp. 225–254.
7. Grigoriev L. I., Mukhina A. G., Izyumov B. D. “Formation of the ‘Reservoir Life’ model for improving reservoir-development management efficiency.” *Vestnik TsKR Rosnedra*, 2012, No. 4, pp. 6–15.
8. Zadeh L. A. “Outline of a new approach to the analysis of complex systems and decision processes.” In: *Mathematics Today* (collection of articles translated from English). Moscow: Znanie, 1974, 64 p.
9. Zadeh L. A. “Fuzzy Sets.” *Information and Control*, 1965, No. 8, pp. 338–353.
10. Zadeh L. A. “Fuzzy sets as a basis for a theory of possibility.” *Fuzzy Sets and Systems*, 1978, Vol. 1, pp. 3–28.
11. Dubois D., Prade H. “Possibility Theory and its Applications: Where Do We Stand?” In: *Springer Handbook of Computational Intelligence*. Springer Berlin Heidelberg, 2015, pp. 31–60.
12. Dubois D., Prade H. “The three semantics of fuzzy sets.” *Fuzzy Sets and Systems*, 1997, Vol. 90, No. 2, pp. 141–150.
13. Yager R. R. “On ordered weighted averaging aggregation operators in multicriteria decision-making.” *IEEE Transactions on Systems, Man, and Cybernetics*, 1988, Vol. 18, No. 1, pp. 183–190.
14. Hathaway R. J., Bezdek J. C. “Switching regression models and fuzzy clustering.” *IEEE Transactions on Fuzzy Systems*, Aug. 1993, Vol. 1, No. 3, pp. 195–204.
15. Smets P., Magrez P. “The measure of the degree of truth and of the grade of membership.” *Fuzzy Sets and Systems*, 1988, Vol. 25, pp. 67–72.

[^1]: Here and below, quotations from sources not previously published in Russian are given in the author’s translation.
[^2]: *Plausible*: trustworthy, reasonable, seeming true. In Russian, “plausibility” is often translated by a word also used for “likelihood”; to avoid confusion with the “maximum likelihood principle,” the author suggests translating “plausibility” as “fuzzy plausibility.”
[^3]: The most common classical-logic expression for implication is used here: `a → b ↔ ¬a ∨ b`. In fuzzy logic, using other expressions that are equivalent in classical logic—for example, `a → b ↔ ¬a ∨ (a ∧ b)`—will produce a different result.
