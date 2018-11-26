% this figure shows different BLER's influence to the Delay.

lambda = 20; %Gbit/ms
n = 5;
a = 1;
b = 3;
epsilon = 0.00001;
vp = ((n+1)*a)./epsilon;

c = 46:0.5:48;
BLER=0.00001;
rc = c*(1-BLER);
d = ((n+1) ./ (b*(rc-lambda))) * log(vp);
plot(c, d, '-o','LineWidth',1);
hold on;

BLER=0.005;
rc = c*(1-BLER);
d = ((n+1) ./ (b*(rc-lambda))) * log(vp);
plot(c, d, '-*');
hold on;

BLER=0.001;
rc = c*(1-BLER);
d = ((n+1) ./ (b*(rc-lambda))) * log(vp);
plot(c, d, '-.');
hold on;
BLER=0.02;
rc = c*(1-BLER);
d = ((n+1) ./ (b*(rc-lambda))) * log(vp);
plot(c, d, '-^');
hold on;

xlabel('Service Rate (Gbit/s)');
ylabel('Delay (ms)');
legend('BLER=0.00001', 'BLER=0.001', 'BLER=0.01', 'BLER=0.05','Location', 'northeast');


