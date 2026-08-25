#include <stdio.h>

// Function to check if a year is a leap year
int is_leap_year(int year) {
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        return 1;  // True
    } else {
        return 0;  // False
    }
}

int main() {
    int year;
    
    printf("Enter a year: ");
    scanf("%d", &year);
    
    if (is_leap_year(year)) {
        printf("%d is a leap year\n", year);
    } else {
        printf("%d is not a leap year\n", year);
    }
    
    // Test cases
    printf("\n--- Test Cases ---\n");
    int test_years[] = {2000, 2004, 2100, 2020, 2021, 1900, 2024};
    int size = sizeof(test_years) / sizeof(test_years[0]);
    
    for (int i = 0; i < size; i++) {
        int y = test_years[i];
        printf("%d: %s\n", y, is_leap_year(y) ? "Leap Year" : "Not a Leap Year");
    }
    
    return 0;
}
