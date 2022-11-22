% Lab 4 Tasks
% 1) read paper: http://ai.stanford.edu/~ang/papers/nips01-spectral.pdf
% 2) implement K-eigenvector algorithm (in this script) to detect
% communities in the graphs E1 and E2
% 3) run implementation on 2 graph sets and document results in report
% 4) submit source code and report


% Importing comma-separated edge list in Matlab
E1 = csvread("C:\dev\Data Mining\Lab4\example1.dat")
E2 = csvread("C:\dev\Data Mining\Lab4\example2.dat")

% ************** MATLAB TUTORIAL PROVIDED ******************************
% Converting Edge list to the adjacency matrix
col1 = E1(:,1);
col2 = E1(:,2);
max_ids = max(max(col1,col2));
As= sparse(col1, col2, 1, max_ids, max_ids); 
A = full(As)

% Getting the eigenvalues
[v,D] = eig(A)

% Sort eigenvalues
sort(diag(D))

% For very large graphs, use the eigs function to find a few eigenvalues
% and vectors of a matrix
[V, D] = eigs(L, 2, 'SA');

% ************** MATLAB TUTORIAL END ***********************************

% ************** K-EIGENVECTOR-ALGORITHM *******************************

% 0. Choose parameter sigma^2. Either by hand as estimation or try
% different values for the following steps 1. - 5. and choose the one that
% produced the tightest (i.e. smallest distortion) clusters.
% Tip: Start choosing by hand and later see if there's time to optimize

% 1. Form the affinity matrix A (R^(nxn)). Aij = exp(-||si-sj||^2/sigma^2)
% if i != j. Aii = 0
A = 

% 2. 
% a) Define D as diagonal matrix whos i,i-element is the sum of A's i-th
% row
D = 
% b) Construct matrix L
L = D^(-1/2) * A * D^(-1/2)

% 3. Find x1, ... , xk the k-largest eigenvectors of L (chosen to be orthogonal to each
% other in case of repeated eigenvalues). X (R^(nxk))
X = [x1, ..., xk]

% 4 Form matrix Y from X (renormalize each of X's rows to have unit length)
Y = every Yij = Xij/( (Sumj(Xij^2))^1/2 )

% 5 Treating each row of Y as a point in R^k, cluster them into k clusters
% via K-means
k-Clusters = K-means(points) where point is a row in Y

% 6 Assign original point si cluster j if and only if row i of Y was
% assigned to cluster j
for every original point si:
    if row i (i.e. point) in k-Clusters[j]:
        assign si to j-th cluster

% Plot result
For every cluster in cluster:
    for every point in cluster:
        plot point in color unique for this cluster