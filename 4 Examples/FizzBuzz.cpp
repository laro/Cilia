void fizzBuzz(int count) {
    for (int i = 1; i <= count; ++i) {
        if (i % 15 == 0)
            cout << "FizzBuzz\n";
        else if (i % 3 == 0)
            cout << "Fizz\n";
        else if (i % 5 == 0)
            cout << "Buzz\n";
        else
            cout << i << '\n';
    }
}