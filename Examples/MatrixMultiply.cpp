Matrix multiply(const Matrix& A, const Matrix& B) {
    int m = A.rows();
    int n = A.columns();
    int p = B.columns();

    Matrix C(m, n);

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            for (int k = 0; k < n; ++k) {
                C[i, j] += A[i, k] * B[k, j];
            }
        }
    }

    return C;
}
