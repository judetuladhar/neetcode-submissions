class DynamicArray {
public:
    int* arr;
    int capacity;
    int size;

    DynamicArray(int cap) {
        capacity = cap;
        size = 0;
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity){
            resize();
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        int n = arr[size - 1];
        size--;
        return n;
    }

    void resize() {
        int* newArr = new int [capacity * 2];
        capacity *= 2;
        for (int i = 0; i < size; i++){
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
