


bf2 = double(read_bmp('bf2.bmp'))

print, 'BIAS frame 2, average', avg(bf2)
print, 'BIAS frame 2, min', min(bf2)
print, 'BIAS frame 2, max', max(bf2, location)

max_index = array_indices(bf2, location)
print, max_index

hist_bf2 = histogram(bf2, locations = values)
window, 0
plot, values, hist_bf2

window, 1
plot_image, bf2

df1_2 = double(read_bmp('df1_2.bmp'))

print, 'Dark frame (1_2), average', avg(df1_2)
print, 'Dark frame (1_2), min', min(df1_2)
print, 'Dark frame (1_2), max', max(df1_2, location)

max_index = array_indices(df1_2, location)
print, max_index

hist_df1_2 = histogram(df1_2, locations = values)
window, 2
plot, values, hist_df1_2

window, 3
plot_image, df1_2

;save_plots, 'new_test_file', 'eps', df1_2, xtitle='Test'


end
