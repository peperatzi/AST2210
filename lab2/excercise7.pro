

bf1 = double(read_bmp('bf1.bmp'))
bf2 = double(read_bmp('bf2.bmp'))

bias_add = bf1 + bf2

print, 'Average avg()', avg(bias_add[226:526,90:390])

bias_sub = bf1 - bf2
print, 'Standard deviation of (bf1 - bf2)', stddev(bias_sub[226:526,90:390])

print, 'sqrt(2)*stddev(bf1)', sqrt(2)*stddev(bf1[226:526, 90:390])


end
