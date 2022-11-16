from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Cambria']
import matplotlib.pyplot as plt
import numpy as np

mod = 12
pcset_input = [0,3,5,8]
pcset = pcset_input
card = int(len(pcset))
cyclic = True # True of False
r = 1 # universal radius

#interval composition
def ic_func():
    ic = []
    for i in range(card-1):
        ci = (pcset[i+1]-pcset[i]) % mod
        ic.append(ci)
    ic.append((pcset[0]-pcset[card-1]) % mod)
    return ic

ic = list(ic_func())

#ic_hex
dic = {0:mod}
ic_hex = [dic.get(n, n) for n in ic]

#dots
def dots_func():
    dots = []
    for i in range(mod):
        d = i*(360/mod)*(np.pi/180)
        dots.append(d)
    dots.append(dots[0])
    return dots

dots = list(dots_func())
dots_radius = [r,r,r,r,r,r,r,r,r,r,r,r,r]

#theta
def theta_func():
    theta = []
    for i in range(card):
        t = pcset[i]*(360/mod)*(np.pi/180)
        theta.append(t)
    if cyclic == True:
        theta.append(theta[0])
    return theta

theta = list(theta_func())

#radius
def radius_func():
    radius = []
    for i in range(card):
        radius.append(r)
    if cyclic == True:
        radius.append(radius[0])
    return radius

radius = list(radius_func())

#size
plt.figure(figsize=(8, 8))

#plot
ax = plt.subplot(111, polar=True)

#dots plot
ax.plot(dots, dots_radius, color='k', ls='', marker='o', markersize=8, lw=1, label=(pcset, ic), clip_on=False, alpha=1, zorder=10)

#starting point
#ax.plot(theta[0], radius[0], color='k', marker='s', clip_on=False, alpha=1, zorder=-10)

#pcset plot
ax.plot(theta, radius, color='firebrick', ls='-', marker='o', markersize=8, lw=2, label=(pcset, ic), clip_on=False, alpha=1, zorder=20)

#fill plot
#ax.fill(theta, radius, color='tab:blue', alpha=0.2)

#axis
index = 6
axis1 = index/2
axis2 = (axis1-(mod/2)) % mod
axis_theta = [axis1*(360/mod)*(np.pi/180), axis2*(360/mod)*(np.pi/180)]

#axis plot
#ax.plot(axis_theta, [1.2, 1.2], color='grey', ls=':', marker='', lw=1, label=(axis1, axis2), clip_on=False, alpha=1, zorder=-50)

#ic plot
length = int(len(theta)-1)
for i in range(length): # card or card-1
    if ic[i] < mod/2:
        k = ic[i]/2
        d = 0 # d = 0.04
    else:
        k = -(mod-ic[i])/2
        d = 0 # d = -0.04
    #ax.annotate(
        #ic_hex[i], # labels
        #xy=(theta[(i+1)%mod],r),
        #xytext=((((pcset[i]+k)%mod))*(360/mod)*(np.pi/180), (np.cos(k*(360/mod)*(np.pi/180))*r)-d),
        #c='k', fontsize=12, fontweight='bold', zorder=-10, ha='center', va='center', annotation_clip=False, 
        #bbox=dict(boxstyle='circle', ec='none', fc='w'),
        #arrowprops=dict(arrowstyle='simple, head_length=1, head_width=1, tail_width=0', connectionstyle='arc3', fc='k', ec='none', shrinkB=6),
    #    )
    
    #ax.annotate(ic[i], xy=((((pcset[i]+k)%mod))*(360/mod)*(np.pi/180), np.cos(k*(360/mod)*(np.pi/180))-d), bbox=dict(boxstyle='circle', fc='tab:blue', ec='tab:blue'), c='w', fontsize=10, fontweight='bold', zorder=20, ha='center', va='center', clip_on=False)


ax.set_rmax(1*r) # outer radial limit
ax.set_rticks([1]) # to set the radial ticks
ax.set_rlabel_position(0) # set the angle of labels
#ax.set_title('Pitch Clock', fontsize=12)
ax.grid(ls='', visible=False)
#ax.xaxis.grid(True, ls='--', lw=0.5)
#ax.yaxis.grid(True, ls='-', c='black', lw=3)
#ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2))

# hide polar
ax.spines['polar'].set_visible(True)

# suppress the radial labels
plt.setp(ax.get_yticklabels(), visible=False)

# set the circumference labels
ax.set_xticks(np.linspace(0, 2*np.pi, mod, endpoint=False))
ax.set_xticklabels(range(mod), fontsize=16, fontweight='normal')

# make the labels go clockwise
ax.set_theta_direction(-1)

# place 0 at the top
ax.set_theta_offset(np.pi/2.0)    

#plt.grid('off')

#export to svg
#plt.savefig("figura2.svg", format="svg", dpi=600, bbox_inches='tight', pad_inches=0.1, frameon=None, transparent=True)

#show
plt.show()

