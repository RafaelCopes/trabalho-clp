#include <calculations.h>

float f1_x(float x, float y) {
    return 0.00;
}

float f1_y(float x, float y) {
    return 0.16 * y;
}

float f2_x(float x, float y) {
    return (0.85 * x) + (0.04 * y);
}

float f2_y(float x, float y) {
    return (-0.04 * x) + (0.85 * y) + 1.6;
}

float f3_x(float x, float y) {
    return (0.2 * x) - (0.26 * y);
}

float f3_y(float x, float y) {
    return (0.23 * x) + (0.22 * y) + 1.6;
}

float f4_x(float x, float y) {
    return (-0.15 * x) + (0.28 * y);
}

float f4_y(float x, float y) {
    return (0.26 * x) + (0.24 * y) + 0.44;
}

int main() {
    return 0; 
}