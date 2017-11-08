
A = imread('interference_1.png');

[h, w] = size(A)

x = linspace(0, w-1, w);
y = sum(A)./h;

center = 355

minima_1 = 1000000000;
minima_xpos_1 = 0;

minima_2 = 1000000000;
minima_xpos_2 = 0;

for i=(center-100):(center)
    if y(i) < minima_1
        minima_1 = y(i);
        minima_xpos_1 = i
    end
end

for i=(center):(center+100)
    if y(i) < minima_2
        minima_2 = y(i);
        minima_xpos_2 = i
    end
end

distance_to_minima = (minima_xpos_2-minima_xpos_1)/2

%imshow(A)
%hold on
%plot([center center], [0 h], '-r')

plot(x, y)
hold on
plot(minima_xpos_1, minima_1, '-ro')
plot(minima_xpos_2, minima_2, '-ro')
plot([center center], [0 255], '-r')
xlabel('y coordinate')
ylabel('pixel value')


pause()



