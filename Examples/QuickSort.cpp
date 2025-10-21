template <typename T>
void quicksort(span<T> array) {
    if (array.size() <= 1) {
        return;
    }

    int pivot = array[array.size() / 2];
    int left  = 0;
    int right = subarray.size() - 1;

    while (left < right) {
        while (array[left] < pivot) {
            ++left;
        }
        while (array[right] > pivot) {
            --right;
        }

        if left < right {
            swap(array[left], array[right]);
            ++left;
            if (right > 0) { // Schutz vor Unterlauf
                --right;
            }
        }
    }

    // Rekursion auf die zwei Teilbereiche
    if (right > 0) {
        quickSort(array.first(right + 1));
    }
    if (left < int(array.size()) - 1) {
        quickSort(array.subspan(left));
    }
}
