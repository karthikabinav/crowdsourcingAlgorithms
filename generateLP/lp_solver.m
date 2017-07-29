root = '~/crowdsourcing/small_dataset/LP/'
fname = strcat(strcat(strcat(bfile, pfile), afile), noInt);

val = csvread(strcat(strcat(strcat(root, 'vals_'), fname), '.csv'));
I = csvread(strcat(strcat(strcat(root, 'I_'), fname), '.csv'))+1;
J = csvread(strcat(strcat(strcat(root, 'J_'), fname), '.csv'))+1;

b = csvread(strcat(strcat(strcat(root, 'b_'), fname), '.csv'));
c = csvread(strcat(strcat(strcat(root, 'c_'), fname), '.csv'));


A = sparse(I,J, val);
size(A)
size(c)
options = optimoptions(@linprog,'Display', 'iter')
[x, fval] = linprog(-c,A,b,[], [], zeros(size(c)), ones(size(c)), [], options);

csvwrite(strcat(strcat(strcat(root, 'LPval_'), fname), '.csv'), fval);
csvwrite(strcat(strcat(strcat(root, 'X_'), fname), '.csv'), x);
