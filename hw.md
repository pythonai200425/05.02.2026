# OOP Exercise: Point Class

## Goal

Build a simple **Point** class that represents a point in a 2D coordinate system.
The class should store `x` and `y` coordinates and allow moving the point in four directions.

Later, this class will be used by external code (example provided below), so **the public interface must match exactly**.

## What You Need to Build

Create a class named `Point` with the following requirements:

### 1. Constructor (`__init__`)

The constructor should:

* Receive two parameters: `x` and `y`
* Store them as instance attributes

Example intention:

* `x` represents the horizontal coordinate
* `y` represents the vertical coordinate

### 2. Movement Methods

Implement **four methods** that modify the point’s position:

* `move_left(value)`
  Decreases `x` by `value`

* `move_right(value)`
  Increases `x` by `value`

* `move_up(value)`
  Increases `y` by `value`

* `move_down(value)`
  Decreases `y` by `value`

Each method should:

* Receive a numeric value
* Update the internal coordinates of the point
* Not return anything

### 3. String Representation (`__str__`)

Implement a `__str__` method so that printing a `Point` object displays:

* The class name
* The current `(x, y)` coordinates

Format example (exact format is important):

```
Point(x=5.4, y=8.1)
```

## Example Usage (DO NOT CHANGE)

The following code will be used later to test your class:

```python
p1 = Point(x=5.4, y=8.1)
print(p1)

p1.move_right(2.5)
p1.move_up(3)

print(p1)
```

## Expected Output

```
Point(x=5.4, y=8.1)
Point(x=7.9, y=11.1)
```

## Notes

* Do not add extra print statements inside the class
* Do not change method names
* Focus on clean, readable OOP design
* Assume all inputs are valid numbers

Good luck 🚀

Submit email: **[pythonai200425+oop1@gmail.com](mailto:pythonai200425+oop1@gmail.com)**
