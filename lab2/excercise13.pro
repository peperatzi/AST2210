
; Load original image 
diff= double(read_bmp('interference_1.bmp'))
window, 0
plot_image, diff

; Load flats
ff = list()
for i=0,15 do begin
    filename = 'ff' + strtrim(i+1,2) + '.bmp'
    
    image = double(read_bmp(filename))
    ;ff.add, image[226:526, 90:390]
    ff.add, image
endfor
F_avg = (ff[0]+ff[1]+ff[2]+ff[3]+ff[4]+ff[5]+ff[6]+ff[7]+ff[8]+ff[9]+ff[10]+ff[11]+ff[12]+ff[13]+ff[14]+ff[15])/16.0
window, 1
plot_image, F_avg

; Load darks
ff_df = list()
for i=0,4 do begin
    filename = 'ff_df_' + strtrim(i+1,2) + '.bmp'
    
    image = double(read_bmp(filename))
    ;ff_df.add, image[226:526, 90:390]
    ff_df.add, image
endfor
D_avg = (ff_df[0]+ff_df[1]+ff_df[2] + ff_df[3] + ff_df[4])/5.0
window, 2
plot_image, D_avg


; Load darks
df_raw = list()
for i=0,4 do begin
    filename = 'df' + strtrim(i+1,2) + '_1.bmp'
    
    image = double(read_bmp(filename))
    ;df_raw.add, image[226:526, 90:390]
    df_raw.add, image
endfor
D_irawavg = (df_raw[0]+df_raw[1]+df_raw[2] + df_raw[3] + df_raw[4])/5.0
window, 3
plot_image, D_irawavg

F_master = F_avg - D_avg

window, 4
plot_image, F_master

F_normmaster = F_master/mean(F_master)

window, 5
plot_image, F_normmaster


;I_raw = diff[226:526, 90:390]
I_raw = diff

I_corr = (I_raw - D_irawavg) / F_normmaster

window, 6
plot_image, I_corr

save_img, I_corr, 'corrected_image', type='eps', color_table = 2, title='Corrected diffraction image'

end
