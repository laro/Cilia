template <typename T>
void quicksort(span<T> array) {
    if (array.size() <= 1) {
        return;
    }

    T pivot = array[array.size() / 2];
    int left = 0;
    int right = array.size() - 1;

    while (left < right) {
        while (array[left] < pivot) {
            ++left;
        }
        while (array[right] > pivot) {
            --right;
        }

        if (left < right) {
            swap(array[left], array[right]);
            ++left;
            if (right > 0) { // Protection against underflow
                --right;
            }
        }
    }

    // Recursion on the two sub-arrayss
    if (right > 0) {
        quicksort(array.first(right + 1));
    }
    if (left < int(array.size()) - 1) {
        quicksort(array.subspan(left));
    }
}
