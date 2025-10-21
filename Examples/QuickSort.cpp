template <Sortable T>
void quickSort(span<T> array) {
    if (array.size() <= 1) {
        return;
    }

    auto pivot = array[array.size() / 2];
    auto left  = 0;
    auto right = subarray.size() - 1;

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
