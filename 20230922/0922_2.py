a = (1, 1)
b = (2, 4)
c = (-1, 5)
d = (6, 1)
e = (-5, 1)

t = ((a[0] + b[0] + c[0] + d[0] + e[0])/5,
     (a[1] + b[1] + c[1] + d[1] + e[1])/5)

a_dist = (t[0] - a[0])**2 + (t[1] - a[1])**2
b_dist = (t[0] - b[0])**2 + (t[1] - b[1])**2
c_dist = (t[0] - c[0])**2 + (t[1] - c[1])**2
d_dist = (t[0] - d[0])**2 + (t[1] - d[1])**2
e_dist = (t[0] - e[0])**2 + (t[1] - e[1])**2

print(a_dist, b_dist, c_dist, d_dist, e_dist, sep="\n")
