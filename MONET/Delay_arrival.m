% This figure will illustrate how arrival rate and service rate impact the
% delay

n = 5;
b = 3;
epsilon = 0.00001;
a = 1;
vp = ((n+1)*a)/epsilon;

lambda = 15:1:25;

c = 46;
d = ((n+1) ./ (b*(c-lambda))) * log(vp);
plot(lambda, d, '-+');
hold on;

c = 47;
d = ((n+1) ./ (b*(c-lambda))) * log(vp);
plot(lambda, d, '-');
hold on;

c = 48;
d = ((n+1) ./ (b*(c-lambda))) * log(vp);
plot(lambda, d, '-<');

xlabel('Arrival Rate (Gbit/s)');
ylabel('Delay (ms)');
legend('Service Rate: 46Gbit/s', 'Service Rate: 47Gbit/s', 'Service Rate: 48Gbit/s', 'Location', 'northwest');
