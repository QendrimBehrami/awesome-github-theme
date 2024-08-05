#include <iostream>
#include <memory>
#include <string>
#include <vector>

using namespace std;

// Base class
class Shape {
   public:
    virtual void draw() const = 0;  // Pure virtual function
    virtual ~Shape() = default;     // Virtual destructor
};

// Derived class
class Circle : public Shape {
   private:
    double radius;

   public:
    Circle(double r)
        : radius(r) {
    }

    void draw() const override {
        cout << "Drawing a circle with radius " << radius << endl;
    }

    double getRadius() const {
        return radius;
    }
};

// Function to display shapes
void displayShapes(const vector<shared_ptr<Shape>>& shapes) {
    for (const auto& shape : shapes) {
        shape->draw();
    }
}

int main() {
    vector<shared_ptr<Shape>> shapes;

    shapes.push_back(make_shared<Circle>(5.0));

    cout << "Shapes to display:" << endl;
    displayShapes(shapes);

    return 0;
}
