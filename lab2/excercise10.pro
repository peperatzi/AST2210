
bf1 = double(read_bmp('bf1.bmp'))
bf2 = double(read_bmp('bf2.bmp'))

bias_add = bf1 + bf2
bias_sub = bf1 - bf2

ff1 = double(read_bmp('ff1.bmp'))
ff2 = double(read_bmp('ff2.bmp'))

ff_add = ff1 + ff2
ff_sub = ff1 - ff2

b = (mean(ff_add[226:526,90:390]) - mean(bias_add[226:526,90:390]))/(stddev(ff_sub[226:526,90:390])^2 - stddev(bias_sub[226:526,90:390])^2)

print, 'b = ', b


end
