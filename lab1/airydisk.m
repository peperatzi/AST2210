
%A = imread('images/b42.jpg');
A = imread('images/b10.jpg');

_y = 221
_x = 362

[h, w] = size(A)

x = linspace(0, h-1, h);
y = A(:,_x);

center = 220

minima_1 = 10000;
minima_1_x_pos = 0;

minima_2 = 10000;
minima_2_x_pos = 0;

for i=center:center+5
    if y(i) < minima_2
        minima_2 = y(i);
        minima_2_x_pos = i-1;
    end
    j = center-(i-center)
    if y(j) < minima_1
        minima_1 = y(j);
        minima_1_x_pos = j-1;
    end
end

minima_3 = 10000;
minima_3_x_pos = 0;

minima_4 = 10000;
minima_4_x_pos = 0;

for i=center:center+10
    if y(i) < minima_4
        minima_4 = y(i);
        minima_4_x_pos = i-1;
    end
    j = center-(i-center)
    if y(j) < minima_3
        minima_3 = y(j);
        minima_3_x_pos = j-1;
    end
end


minima_1_x_pos
minima_2_x_pos
minima_3_x_pos
minima_4_x_pos

size_of_airydisk = minima_2_x_pos-minima_1_x_pos

%imshow(A)
%hold on
%plot([0 w], [_y _y], '-r')
%plot([_x _x], [0 h], '-r')

plot(x, y)
hold on
plot([220 220], [0 h], '-r')
plot((minima_1_x_pos),(minima_1),'-ro')
plot((minima_2_x_pos),(minima_2),'-ro')
plot((minima_3_x_pos),(minima_3),'-ro')
plot((minima_4_x_pos),(minima_4),'-ro')
xlabel('y coordinate')
ylabel('pixel value')


pause()



