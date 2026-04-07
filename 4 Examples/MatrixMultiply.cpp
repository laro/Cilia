#include <cassert>

auto multiply(const Matrix& A, const Matrix& B) -> Matrix {
    int m = A.rows();
    int n = A.columns();
    int o = B.rows();
    int p = B.columns();

    assert(n == o && "A.columns() must equal B.rows() for matrix multiplication");

    Matrix C(m, p);

    for (int i = 0; i < m; ++i) {
        for (int k = 0; k < n; ++k) {
            for (int j = 0; j < p; ++j) {
                C[i, j] += A[i, k] * B[k, j];
            }
        }
    }

    return C;
}