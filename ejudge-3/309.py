class Circle:
   def __init__(self, radius):
      self.radius = radius

   def area(self):
      return (self.radius**2) * 3.14159

n = int(input())
s = Circle(n)
print(f"{s.area():.2f}")

