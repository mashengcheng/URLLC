%d * delay;
%C * service rate;
%lambda * poisson distribution parameter;
%n * number of tandem server nodes;
%a * bound function parameter of service;
%b * bound function parameter of service;
%epsilon * violation probability;
%C = 47;
lambda = 20;
%n = 5;
b = 3;
%epsilon = 0.000005:0.000001:0.000015;
a = 1;
%reliability = ((n+1)*a)./epsilon;
%求出来的是一个比较大的数，因为epsilon非常小
%d = ((n+1) / (b*(C-lambda))) * log(reliability);
%fprintf('%f\n',d);
%m = 3;
%reliability = ((n+1)*a)*(1./epsilon);
%d_3 = ((m+1) / (b*(C-lambda))) * log(reliability);
%plot(epsilon,d_5, '-*k', epsilon, d_3, '-+k');

ns = 3:1:10;
C = 30:1:50;
epsilon = 0.00001;

[C, ns] = meshgrid(C, ns);
reliability = ((ns+1)*a)./epsilon;
para = (ns+1) ./ (b*(C-lambda));

%fprintf('%f\n',reliability);
d = para .*  log(reliability);
%d = ((ns+1) / (b*(C-lambda))) .* log(reliability);

mesh(C, ns, d);
hold on;
surface = ones(8,21);
mesh(C, ns, surface);

