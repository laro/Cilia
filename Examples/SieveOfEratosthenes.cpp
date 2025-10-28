vector<int> sieve_of_eratosthenes(int n) {
    if (n < 2) {
        return {};
    }
    
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = false;
    is_prime[1] = false;

    int limit = static_cast<int>(sqrt(n));
    for (int i = 2; i <= limit; ++i) {
        if (!is_prime[i]) {
            continue;
        }
        for (int j = i * i; j <= n; j += i) {
            is_prime[j] = false;
        }
    }

    vector<int> primes;
    primes.reserve(n / 10);
    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }
    
    return primes;
}
