# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:08:25 2016

@author: Velizar
"""

# coding: utf-8
import numpy as np
from scipy.optimize import minimize #,basinhopping
from sklearn.linear_model import LinearRegression


class FuzzyPoint:
    n = 2 # number of variables
    m = 2.
    apex = None
    spreads = None
    __L = None

    def __init__(self, x, s, m=2.):
        self.apex = np.array(x)
        self.n = self.apex.size
        try:
            m = float(m)
        except:
            raise ValueError('Form parameter m must be float value')
        if not m > 1.:
            raise ValueError('Form parameter m must be >1')
        self.m = float(m)
        self.spreads = np.array(s)
        self.__L = FuzzyPoint.L
        if self.spreads.size != self.n:
            raise ValueError('Spreads dimension must be equal to the apex dimension %d' % self.n)
        if not np.all(self.spreads>=0.):
            raise ValueError('Spreads values must be non-negatve')
        if not np.any(self.spreads>0.):
            raise ValueError('At least one of the spreads values must be > 0')
            
    def L(self, u):
        #if u < 0:
        #    raise ValueError('L-function argument must be non-negative')
        return np.exp(-np.abs(u)**self.m)

class Ppoint(FuzzyPoint):
    def __init__(self, x, s, m=2.):
        FuzzyPoint.__init__(self, x, s, m)

    def membership(self, x):
        x = np.array(x)
        if x.size != self.n:
            raise ValueError('Array with coordinates must contain %d values' % self.n)
        return np.prod(self.L((self.apex - x) / self.spreads))

    def similarity(self, params, intercept=0., return_point=False):
        params = np.array(params)
        if params.size != self.n:
            raise ValueError('Array with parameter must contain %d values' % self.n)
        params = np.array(params)
        di = params.dot(self.apex) + intercept
        si = np.sum(np.abs(params*self.spreads) ** (self.m/(self.m-1.)))
        Mi = self.L(np.abs(di)/si**((self.m-1.)/self.m))
        if not return_point:
            return Mi
        xopt = self.apex - np.sign(params)*np.abs(params)**(1./(self.m-1.)) * self.spreads**(self.m/(self.m-1.))*di/si
        return Mi,xopt

    def mesh2d(self, xspace, yspace, dims=(0,1)):
        # primary and secondary dimensions
        p,s = dims
        xx,yy = np.meshgrid(xspace-self.apex[p], yspace-self.apex[s])
        return np.exp(-(abs(xx)/self.spreads[p])**self.m-(abs(yy)/self.spreads[s])**self.m)

class Epoint(FuzzyPoint):
    R = None
    A = None
    Ainv = None
    __slowpoke = False

    def __init__(self, x, s, m=2., R=None):
        FuzzyPoint.__init__(self, x, s, m)
        if R is None:
            self.R = np.eye(self.n)
            return
        R = np.array(R)
        if R.shape != (self.n,self.n):
            raise ValueError('Rotation matrix shape must have shape (%d,%d)' % (self.n,self.n))
        if not np.all([R[i,i]==1. for i in range(self.n)]):
            raise ValueError('Rotation matrix diagonal elements must be equal to 1')
        if not np.all(np.abs(R-np.eye(self.n)) < 1.):
            raise ValueError('Rotation matrix off-diagonal element absolute values must be less then 1')
        if not np.all([R[i,j] == R[j,i] for i in np.arange(self.n) for j in np.arange(i+1,self.n)]):
            raise ValueError('Rotation matrix must be symmetric')
        self.R = R
        
    # returns r_xy value provided 
    def __getitem__(self, key):
        if not type(key) is tuple or len(key) != 2:
            raise IndexError('Elliptic point index must be a tuple')
        i,j = key
        return self.R[key]        

    # returns r_xy value provided 
    def __setitem__(self, key, value):
        if not type(key) is tuple or len(key) != 2:
            raise IndexError('Elliptic point index must be a tuple')
        old = self.R[key]
        #except IndexError as e:
        i,j = key
        if i==j:
            raise IndexError('Elliptic point rotation matrix diagonal elements cannot be changed')
        try:
            value = float(value)
        except:
            raise ValueError('Elliptic point rotation matrix values must be float values')
        if not np.abs(value) < 1.:
            raise ValueError('Interaction coefficient (%d,%d) absolute value must be less then 1' % key)
        if old==value:
            return
        self.R[i,j] = self.R[j,i] = value
        self.A = None
    
    def __prepare(self):
        S = np.eye(self.n)*self.spreads
        self.A = S.dot(self.R).dot(S)
        self.Ainv = np.linalg.inv(self.A)
    
    # assumes (a^T,x) + a0 = 0
    def similarity(self, params, intercept=0., return_point=False):
        if len(params) != self.n:
            raise ValueError('Array with parameter must contain %d values')
        if self.A is None:
            self.__prepare()
        params = np.array(params)
        di = params.dot(self.apex) + intercept
        si = params.dot(self.A).dot(params)
        Mi = self.L(np.abs(di)/np.sqrt(si))
        if not return_point:
            return Mi
        xopt = self.apex - self.A.dot(params)*di/si
        return Mi,xopt

    def mesh2d(self, xspace, yspace, dims=(0,1)):
        if self.A is None:
            self.__prepare()
        # primary and secondary dimensions
        p,s = dims
        if self.__slowpoke:
            surf = np.zeros((len(yspace),len(xspace)))
            var = np.zeros(self.n)
            for i,x in enumerate(xspace):
                var[p] = x-self.apex[p]
                for j,y in enumerate(yspace):
                    var[s] = y-self.apex[s]
                    surf[j,i] = np.exp(-np.sqrt(var.dot(self.Ainv).dot(var))**self.m)
            return surf
        else:
            xx,yy = np.meshgrid(xspace-self.apex[p], yspace-self.apex[s])
            return np.exp(-np.sqrt(self.Ainv[p,p]*xx**2 + 2.*self.Ainv[p,s]*xx*yy + self.Ainv[s,s]*yy**2)**self.m)


class WeightedPowerMean:
    power = 1.
    N = 0
    weights = None
 
    def __init__(self, power, weights=None):
        self.power = power
        self.__use_max = False

    def mean(self, points, params, intercept=0.):
        if len(points) < 2:
            raise ValueError('List must contain at least two points')
        N = len(points)
        if self.weights is None:
            self.weights = np.repeat(1./N, N)
        # !!! CHECK SIZES
        # check if several linear models are present; 
        params = np.array(params)
        if len(params.shape) > 1:
            v = np.zeros(N)
            # for the moment, just assume params are 
            for a,a0 in zip(params,intercept):
                _v = np.array([pt.similarity(a, a0) for pt in points])
                if self.__use_max:
                    v = np.maximum(v, _v)
                else:
                    v += _v * (1. - v)
        else:
            v = np.array([pt.similarity(params, intercept) for pt in points])
        return np.sum(self.weights*v**self.power)**(1./self.power) if self.power else np.prod(v**self.weights)

class RotationMatrix():
    _R = None
    
    def __init__(self, size, R=None):
        pass
        

#class FuzzyPointSet(list):
#    def __init__(self):
#        list.__init__(self)
        
class LinearfRegression:
    #_points = []
    #_mean = None
    
    def __init__(self, fit_intercept=True, normalize=False, copy_X=True, n_jobs=1):
        self.fit_intercept = fit_intercept
        self.normalize = normalize
        self.copy_X = copy_X
        self.n_jobs = n_jobs
        
    def fit(self, X, y=None, sample_weight=None, 
            point_type='P', spreads_x=0., spreads_y='std', m=2., rotation={},
            mean=0., params0=None, intercept0=None):
                
        # inout data
        #for k in range(y.shape[1]):
        n_samples, n_features = X.shape # from _pre_fit
        _points = []
        for i in range(n_samples):
            if point_type=='P':
                pt = Ppoint(X[i], spreads_x, m)
            elif point_type=='E':
                pt = Epoint(X[i], spreads_x, m)
                for k,v in rotation.iteritems():
                    pt[k] = v
            else:
                raise ValueError('Illegal point_type %s supplied (must be P or E)' % point_type)
            _points.append(pt)

        # plausibility estimator
        _mean = WeightedPowerMean(mean, sample_weight)
        
        y_idx = n_features-1
        # function for 1 model
        target = lambda params: \
            -_mean.mean(_points, 
                       [x if i!=y_idx else -1. for (i,x) in enumerate(params)],
                        params[y_idx])
        if intercept0 is None:
            intercept0 = 0.
        if params0 is None:
            params0 = np.repeat(0., n_features)
        res = basinhopping(target, x0=[x if i!=y_idx else intercept0 for (i,x) in enumerate(params0)])
        self.coef_ = np.array([x if i!=y_idx else -1. for (i,x) in enumerate(res.x)])
        self.intercept_ = res.x[y_idx]
        
        return -res.fun

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

class ClusteredLinearfRegression(LinearfRegression):
    def __init__(self, clusters=1, fit_intercept=True, normalize=False, copy_X=True, n_jobs=1):
        LinearfRegression.__init__(self, fit_intercept, normalize, copy_X, n_jobs)
        self.clusters = clusters

    def fit(self, X, y=None, sample_weight=None, 
            point_type='P', spreads_x=0., spreads_y='std', m=2., rotation={},
            mean=0., clusters=1, params0=None, intercept0=None):
        self.clusters = clusters
        # inout data
        #for k in range(y.shape[1]):
        n_samples, n_features = X.shape # from _pre_fit
        _points = []
        for i in range(n_samples):
            if point_type=='P':
                pt = Ppoint(X[i], spreads_x, m)
            elif point_type=='E':
                pt = Epoint(X[i], spreads_x, m)
                for k,v in rotation.iteritems():
                    pt[k] = v
            else:
                raise ValueError('Illegal point_type %s supplied (must be P or E)' % point_type)
            _points.append(pt)

        # plausibility estimator
        _mean = WeightedPowerMean(mean, sample_weight)

        y_idx = n_features-1
        # function for multiple models        
        target = lambda params: \
            -_mean.mean(_points, 
                        np.reshape(
                            [x if (i % n_features)!=y_idx else -1. for (i,x) in enumerate(params)], 
                            (self.clusters,n_features)),
                        params[y_idx::n_features])
        if intercept0 is None:
            intercept0 = np.repeat(0., self.clusters)
        if params0 is None:
            params0 = np.zeros((self.clusters,n_features))
        #res = basinhopping(target, 
        res = minimize(target, method='Nelder-Mead',
                       options={ 'ftol': 1e-16 },
                       x0=[x if (i % n_features)!=y_idx else intercept0[i // n_features] 
                          for (i,x) in enumerate(params0.reshape(params0.size))])
        #print res.x
        self.coef_ = np.reshape(
                         [x if (i % n_features)!=y_idx else -1. for (i,x) in enumerate(res.x)],
                         (self.clusters,n_features))
        self.intercept_ = res.x[y_idx::n_features]

        return -res.fun

