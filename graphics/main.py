from TwoD_graphics.rectangle import area, perimeter
from TwoD_graphics.circle import area as c_area, perimeter as c_peri
from ThreeD_graphics.cuboid import surface_area, perimeter as cub_peri
from ThreeD_graphics.sphere import surface_area as s_area, perimeter as s_peri

print("Rectangle Area:", area(5, 4))
print("Rectangle Perimeter:", perimeter(5, 4))

print("Circle Area:", c_area(7))
print("Circle Perimeter:", c_peri(7))

print("Cuboid Surface Area:", surface_area(2, 3, 4))
print("Cuboid Perimeter:", cub_peri(2, 3, 4))

print("Sphere Surface Area:", s_area(5))
