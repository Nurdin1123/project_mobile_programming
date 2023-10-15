img = imread('profile.jpg');
lpf1=[1/16 1/8 1/16;1/8 1/4 1/8;1/16 1/8 1/16];
lpf2=[1/10 1/10 1/10;1/10 1/5 1/10;1/10 1/10 1/10];
lpf3=[1 1 1;1 1 1;1 1 1]/9;
J1=uint8(conv2(double(img),lpf1,'same'));
J2=uint8(conv2(double(img),lpf2,'same'));
J3=uint8(conv2(double(img),lpf3,'same'));

figure(1);
subplot(2,2,1);imshow(img);title('Citra Asli');
subplot(2,2,2);imshow(J1);title('Low Pass Filtering 1');
subplot(2,2,3);imshow(J2);title('Low Pass Filtering 2');
subplot(2,2,4);imshow(J3);title('Low Pass Filtering 3');
