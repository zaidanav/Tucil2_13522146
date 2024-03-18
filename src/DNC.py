import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

class BezierCurve:
    def __init__(self, ctrl_points, iterations):
        self.ctrl_points = ctrl_points
        self.iterations = iterations
        self.bezier_points = []
        self.time = 0
        self.generate_bezier()

    def midpoint(self, point1, point2):
        return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

    def interpolate_bezier_points(self, ctrl1, ctrl2, ctrl3, current_iteration):
        if current_iteration < self.iterations:
            mid1 = self.midpoint(ctrl1, ctrl2)
            mid2 = self.midpoint(ctrl2, ctrl3)
            mid3 = self.midpoint(mid1, mid2)

            current_iteration += 1
            self.interpolate_bezier_points(ctrl1, mid1, mid3, current_iteration)
            self.bezier_points.append(mid3)
            self.interpolate_bezier_points(mid3, mid2, ctrl3, current_iteration)

    def generate_bezier(self):
        start = time.time()
        ctrl1, ctrl2, ctrl3 = self.ctrl_points
        self.bezier_points = [ctrl1]
        self.interpolate_bezier_points(ctrl1, ctrl2, ctrl3, 0)
        self.bezier_points.append(ctrl3)
        self.time += time.time() - start
    
    def gettime(self):
        return self.time

def get_input():
    print("Masukkan 3 titik point:")
    ctrl_points = [tuple(map(float, input(f"Point {i+1} (x,y): ").split(','))) for i in range(3)]
    iterations = int(input("Masukkan jumlah iterasi: "))
    return ctrl_points, iterations

def animate(i):
    plt.cla()
    bezier_curve = BezierCurve(ctrl_points, i)
    points = np.array(bezier_curve.bezier_points)
    ctrl_points_array = np.array(ctrl_points)
    plt.plot(points[:, 0], points[:, 1], 'b-', label='Bezier Curve')
    plt.scatter(points[:, 0], points[:, 1], color='blue')
    plt.plot(ctrl_points_array[:, 0], ctrl_points_array[:, 1], 'ro-', label='Control Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Bezier Curve with Divide and Conquer Method ke-{0}'.format(i))
    plt.grid(True)

def main():
    global ctrl_points
    ctrl_points, iterations = get_input()

    anim = FuncAnimation(plt.gcf(), animate, frames=iterations+1, repeat=False)


    plt.show()
    print(f"Time: {BezierCurve(ctrl_points, iterations).gettime()} seconds")

if __name__ == "__main__":
    main()