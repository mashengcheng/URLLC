% this figure will illustrate the reliability and violate probability.

%BLER = 0.00001;
vp = 0.00001:0.00001:0.001;
%vp = [0.000001,0.00001,0.0001,0.001,0.01,0.1]
theta = 1000000;
%theta*(gamma-x) = log(vp);
sigma = -0.000008;
gamma = 0.00001;
error_rate  =gamma + sigma - (1/theta) * log(vp) ;
plot( vp, error_rate, ':k');
hold on;

gamma = 0.00002;
error_rate  =gamma + sigma - (1/theta) * log(vp) ;
plot( vp, error_rate, '-k');
hold on;

gamma = 0.00003;

error_rate  =gamma + sigma - (1/theta) * log(vp) ;
plot( vp, error_rate, '-.k');

xlabel('Violation Probability');
ylabel('Block Error Rate');

legend('\gamma=0.00001','\gamma=0.00002','\gamma=0.00003', 'Location', 'northeast');

