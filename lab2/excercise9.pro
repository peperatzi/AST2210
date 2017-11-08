

ff1 = double(read_bmp('ff1.bmp'))
ff2 = double(read_bmp('ff2.bmp'))

ff_add = ff1 + ff2

print, 'Average avg(ff_add)', avg(ff_add[226:526,90:390])
print, 'Average avg(ff1) + avg(ff2)', avg(ff1[226:526,90:390]) + avg(ff2[226:526,90:390])

ff_sub = ff1 - ff2
print, 'Standard deviation of (ff1 - ff2)', stddev(ff_sub[226:526,90:390])

print, 'sqrt(2)*stddev(ff1)', sqrt(2)*stddev(ff1[226:526, 90:390])


end
