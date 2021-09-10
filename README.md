# ComputePI

<p align="center">
  <img width="400" height="400" src="https://github.com/dylannalex/ComputePI/blob/master/images/simulation.png">
</p>


PI approximation with Monte Carlo method.

## How does it work?
1. Draw a square.
2. Draw a circle inside that square.
3. Start drawing dots at a random place on the in the square.
4. Count the dots that fall inside the circle: ```dots_in_circle```.


```
# Approximate the area of the circle:
circle_area = screen_area * (dots_in_circle / total_dots)

# Use the circle_area approximation to calculate PI:
PI = circle_area / (self._circle.radius ** 2)
```

## Usage
You can run the project with:
```
$ python compute_pi.py
```
