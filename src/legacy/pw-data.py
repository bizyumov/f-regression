# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:04:43 2017

@author: Velizar
"""

#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyFuReA as fr
from matplotlib import rc
from matplotlib import cm

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 18}
rc('font', **font)
grayscale = [(g,g,g) for g in .2+np.linspace(.78, 0., num=10)]


def base10bounds(arr):
    los,his = .5*np.min(arr,axis=0),2.*np.max(arr,axis=0)
    return [(np.floor(np.log10(lo)),np.ceil(np.log10(hi))) for (lo,hi) in zip(los,his)]

def space_merge(src, pivots, deltas, limits):
    return np.sort([t for t in np.append(src, [pivots-deltas, pivots, pivots+deltas]) if(t>limits[0] and t<limits[1])])

def plotmesh(x, y, z, title, levels='default', colors=None):
    fig,(ax) = plt.subplots()
    #im = ax.pcolormesh(x, y, z)
    if levels=='default':
        levels = np.linspace(0.,1.,num=11)
    im = ax.contourf(x, y, z, levels=levels, colors=colors)
    ax.set_title(title)
    ax.set_xlim(np.min(x),np.max(x))
    ax.set_xlabel(r'$t_D$')
    ax.set_xscale('log')
    ax.set_ylim(np.min(y),np.max(y))
    ax.set_ylabel(r'$\Delta p_D/dt_D$')
    ax.set_yscale('log')
    fig.colorbar(im, ax=ax)
    #plt.show()
    return ax

def eval_pw(pw_a, x1, x2):
    num = len(pw_a)/2 - 1
    pw_curve = np.zeros((num+2, 2))
    _a0,_a1 = pw_a[0:2]
    pw_curve[0,:] = x1, _a0+_a1*x1
    for i in range(1,num+1):
        pw_curve[i,0] = pw_a[1+i]
        pw_curve[i,1] = _a0+_a1*pw_curve[i,0]
        _a1 += pw_a[1+num+i]
        _a0 -= pw_curve[i,0]*pw_a[1+num+i]
    pw_curve[i+1,:] = x2, _a0+_a1*x2
    return pw_curve

#constants
const_B = 1.3 # RB/STB
const_pzero = 7248 # psig
const_deltap_conv = .00872 # 1/psi
const_time_conv = 370 # 1/hours
const_pstar = 7843 # psig


# read source data
csv = np.genfromtxt('SPE 12777 Bourdet.csv', delimiter = ',', skip_header=1)
time = csv[:,0]
deltap = csv[:,1]
# NB: dp should be calculated proper using Bourdet algorithm
#  (see Excel spreadsheet for details)
dp_D = csv[:,2]
# NB: spreads should be calculated proper using common sense and domain area considerations
#  (as discussed in Izyumov, 2013)
s_time = csv[:,3]
s_deltap = csv[:,4]
s_dp = csv[:,5]

# transform data
t_D = time*const_time_conv
log_t = np.log10(t_D)
p_D = deltap*const_deltap_conv
log_p = np.log10(p_D)
log_dp = np.log10(dp_D)


aMA_pw5 = np.array([ -0.18565,  0.79309,  0.40012,  1.15321,  1.68389,  2.46390,  3.79351, -1.11463, -0.84007,  0.75549,  0.97895,  0.00000 ])
aFINAL = np.array([ -0.18691,  0.79748,  0.39951,  1.15322,  1.66433,  2.50998,  3.55631, -1.11867, -0.84079,  0.70301,  1.13691, -0.45399 ])

if False:
    plt.figure()
    plt.loglog(t_D, p_D)
    plt.loglog(t_D, dp_D)
    #plt.figure()
    #plt.plot(log_t, log_p)

    a = aFINAL
    pw = eval_pw(a, log_t[0], log_t[-1])
    plt.loglog(10.**pw[:,0], 10.**pw[:,1])


if True:
# BUILD HEAT MAP OF SOURCE DATA
    nx = 100
    ny = 1000
    N = 151
    Tnorm = 'sum'
    m = 4. # form parameter
    w = .05 # window
    data = np.array(zip(t_D,dp_D)[:N]) # HACK
    spreads = np.array(zip(100.*s_time,s_dp)[:N])
    points = []
    bounds_t,bounds_dp = base10bounds(data)
    space_t,space_dp = np.logspace(*bounds_t, num=nx),np.logspace(*bounds_dp, num=ny)
    
    space_t = space_merge(space_t, data[:,0], spreads[:,0], np.power(10.,bounds_t))
    #space_dp = space_merge(space_dp, data[:,1], spreads[:,1], np.power(10.,bounds_dp))
    nx,ny = len(space_t),len(space_dp)
    real_Z = np.zeros((ny,nx))
    xx,yy = np.meshgrid(space_t, space_dp)
    for idx,apex in enumerate(data):
        pt = fr.Ppoint(apex,spreads[idx],m)
        #if(Tnorm == 'max'):
        #    real_Z = np.maximum(real_Z, pt.mesh2d(space_t,space_dp))
        #else:
        #    real_Z += pt.mesh2d(space_t,space_dp) * (1.-real_Z)
        points.append(pt)
    #ax1 = plotmesh(space_t, space_dp, real_Z, r'!', 'default', grayscale) #r'Параметр формы $m=%s$' % m)
 
#   MATLAB:
#    weight=zeros(length(log_t(:,2)),1);for i=1:length(weight) weight(i) = 1/sum(exp(-((log_t(:,2)-log_t(i,2))/0.05).^4)); end
    weight = np.zeros(len(log_t))
    for i in range(len(weight)):
        weight[i] = 1./np.sum(np.exp(-((log_t[:]-log_t[i])/w)**m))


def dataline2d(space, fpt, axis=1, scale=1.):
    idx = int(not axis)
    line = np.repeat(fpt.apex[idx],len(space))
    for i,x in enumerate(space):
        line[i] += scale * fpt.membership([
            idx*x + axis*fpt.apex[0],
            axis*x + idx*fpt.apex[1]
        ])
    return line

cmap = cm.get_cmap('coolwarm')
#fig,(ax) = plt.subplots()
fakeim = plt.contourf([[0,0], [0,0]], levels=np.arange(0.,1.+1e-6,.05), cmap=cmap)
plt.clf()
#ax = fig.add_subplot()
#ax.set_title(title)
#ax.set_xlim(np.min(x),np.max(x))
plt.xlabel(r'$t_D/C_D$')
plt.xscale('log')
#ax.set_ylim(np.min(y),np.max(y))
plt.ylabel(r'$\left[ t_D/C_D \right] p_D \prime $')
plt.yscale('log')
plt.grid(which='major', linestyle='solid')
plt.grid(which='minor', linestyle='dotted')

#for wt,pt in zip(weight,points):
#    _w = wt
#    _x0 = pt.apex[0]
#    plt.plot([_x0,_x0], [space_dp[0], space_dp[-1]], color=cmap(_w), linewidth=1., alpha=.5)

for wt,pt in zip(reversed(weight),reversed(points)):
    _w = wt
    _x0 = pt.apex[0]
    line = dataline2d(space_dp, pt, 1, .5*_x0)
    _x,_y = line,space_dp
    #_cond = line > _x0
    #_x,_y = line[_cond],space_dp[_cond]
    #plt.loglog(line, space_dp, color='gray')
    plt.plot([_x0,_x0], [space_dp[0], space_dp[-1]], color=cmap(_w), linewidth=1., alpha=.5)
    plt.plot(line, space_dp, color=cmap(_w), linewidth=1., alpha=.5)
    plt.fill_betweenx(_y, _x0, _x, edgecolor='none', facecolor=cmap(_w), linewidth=.5, alpha=.6)
plt.colorbar(fakeim)
plt.show()
