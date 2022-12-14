clear;
clc;
close all;
% Parameters
n_runs = 1000;

% The flight Mach number will be held fixed at 0.2 for the complete
% analysis.

% The modified eddy viscosity ratio is varied between 4.6228 and 100.036

% The Stagnation Pressure is varied +/- 5 or 10% around p0 = 10525.
%p0 = 10525;
p0 = 10218.4466;

l_bound = [4.6228 0.97*p0];
u_bound = [100.036 1.03*p0];

% Fixes random seeding
rng(2020);

for i = 1:n_runs
    full_table(:, 1) = (1:n_runs)';
%     Sample from log uniform distribution
    full_table(:, 2) = exp(rand(n_runs, 1).*(log(u_bound(1)) - log(l_bound(1))) + log(l_bound(1)));

%    Sample from uniform distribution                                                            full_table(:, 3) = rand(n_runs, 1).*(u_bound(2) - l_bound(2)) + l_bound(2);


%     fID = fopen(['inputs_reference_list_MEVR_pressure.txt'], 'w');
%     fprintf(fID, '%d     %23.16f    %23.16f\n', full_table');
%     fclose(fID);
%
end
