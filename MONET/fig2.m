%start to build a delay and violation probability relastionship figure.

%C = [40,45,50]; %kbit/ms
lambda = 20; %Gbit/ms
n = 5;
b = 3;
epsilon = 0.000005:0.000001:0.000015;
a = 1;
reliability = ((n+1)*a)./epsilon;
%print the 1st time.
c = 45;
d = ((n+1) / (b*(c-lambda))) * log(reliability);
plot(epsilon, d, ':k');
hold on;
%print the 2nd time.
c = 46;
d = ((n+1) / (b*(c-lambda))) * log(reliability);
plot(epsilon, d, '--k');
hold on;
%print the 3rd time.
c = 47;
d = ((n+1) / (b*(c-lambda))) * log(reliability);
plot(epsilon, d, '-k');
%print the 3rd time.
c = 48;
d = ((n+1) / (b*(c-lambda))) * log(reliability);
plot(epsilon, d, '-.k');

xlabel('Violation Probability');
ylabel('Delay (ms)');
legend('45Gbit/s', '46Gbit/s', '47Gbit/s', '48Gbit/s','Location', 'northeast');






