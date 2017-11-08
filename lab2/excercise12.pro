
cgCleanUp

; Load files
ff = list()
for i=0,15 do begin
    filename = 'ff' + strtrim(i+1,2) + '.bmp'
    
    image = double(read_bmp(filename))
    ff.add, image[226:526, 90:390]
endfor

; Calculate sigma
sigma = list()
sigma.add, stddev(ff[0] - ff[1])
sigma.add, stddev((ff[0]+ff[2]) - (ff[1]+ff[3]))
sigma.add, stddev((ff[0]+ff[2]+ff[4]) - (ff[1]+ff[3]+ff[5]))
sigma.add, stddev((ff[0]+ff[2]+ff[4]+ff[6]) - (ff[1]+ff[3]+ff[5]+ff[7]))
sigma.add, stddev((ff[0]+ff[2]+ff[4]+ff[6]+ff[8]) - (ff[1]+ff[3]+ff[5]+ff[7]+ff[9]))
sigma.add, stddev((ff[0]+ff[2]+ff[4]+ff[6]+ff[8]+ff[10]) - (ff[1]+ff[3]+ff[5]+ff[7]+ff[9]+ff[11]))
sigma.add, stddev((ff[0]+ff[2]+ff[4]+ff[6]+ff[8]+ff[10]+ff[12]) - (ff[1]+ff[3]+ff[5]+ff[7]+ff[9]+ff[11]+ff[13]))
sigma.add, stddev((ff[0]+ff[2]+ff[4]+ff[6]+ff[8]+ff[10]+ff[12]+ff[14]) - (ff[1]+ff[3]+ff[5]+ff[7]+ff[9]+ff[11]+ff[13]+ff[15]))

; or, if you want:

;t1 = ff[0]
;t2 = ff[1]
;sigma_1 = list()
;k = 0
;for i= 1,7 do begin
;    sigma_1.add, stddev(t1 - t2)
;    t1 = t1 + ff[2*i]
;    t2 = t2 + ff[(2*i)+1]
;endfor
;sigma_1.add, stddev(t1 - t2)

;help, ff
;plot_image, ff[0]

;for i= 0,7 do begin
;    print, sigma[i]
;    print, sigma_1[i]
;    print, '----'
;endfor

; Calculate the normalized values:
print, 'Normalized values'
sigma_norm = list()
for i= 0,7 do begin
    sigma_norm.add, sigma[i]/((i+1))
    print, sigma[i]
    print, sigma_norm[i]
    print, '----'
endfor

x = [2,4,6,8,10,12,14,16]
plot, x, sigma_norm.toarray()

save_plots, 'decreasing_normalized_noise','eps', x, sigma_norm.toarray(), xtitle='Number of paired images', ytitle='Noise'

end
