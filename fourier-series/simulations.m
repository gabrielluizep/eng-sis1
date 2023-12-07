clear all; close all; clc;

t = -5 : 0.01 : 5;

y_a = 0;
y_d = 0;
y_e = 0;
y_f = 0;

for k = 1 : 1000
  y_a = y_a + (j*(-1)^k) / (k*pi)                                   * e.^(j * k * pi * t);
  y_d = y_d + (1/2 - (-1)^k)                                        * e.^(j * k * pi * t);
  y_e = y_e + 1/(j*k*pi) * (cos(2*k*pi/3) - cos(k*pi/3))            * e.^(j * k * pi * t);
  y_f = y_f + 1/(j*k*pi) * (2 - e^(-2*j*k*pi/3) - e^(-4*j*k*pi/3))  * e.^(j * k * pi * t);
endfor

y_d = 2 * y_d - 1/2; % Amplitude está multiplicada por 1000, isso se dá por ser um impulso (?)
%y_e = 1/3* y_e;
y_e = 2 * y_e;
%y_f = 2/3 * y_f + 1/2; % Se não multiplicar por dois fica como esperado (?)
y_f = 1/2 * y_f + 1 / 2;

figure;
subplot(2,2,1); grid on;

plot(t, real(y_a));

subplot(2,2,2); grid on;
plot(t, real(y_d));

subplot(2,2,3); grid on;
plot(t, real(y_e));

subplot(2,2,4); grid on;
plot(t, real(y_f));
