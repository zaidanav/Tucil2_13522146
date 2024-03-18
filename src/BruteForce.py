import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

class BezierCurve:
    def __init__(self, num_points):
        self.num_points = num_points
        self.user_contpt = self.get_control_points()

    def get_control_points(self):
        points = []
        for i in range(self.num_points):
            x, y = map(float, input(f"Point {i+1} (x,y): ").split(','))
            points.append([x, y])
        return np.array(points)

    def calculate_bezier_point(self, t, koordinat):
        n = len(koordinat) - 1
        point = np.zeros(2)
        for i in range(n+1):
            # Calculate binomial coefficient
            if i < 0 or i > n:
                binom_coef = 0
            elif i == 0 or i == n:
                binom_coef = 1
            else:
                k = min(i, n - i)
                binom_coef = 1
                for j in range(k):
                    binom_coef = binom_coef * (n - j) // (j + 1)
            point += binom_coef * (t ** i) * ((1 - t) ** (n - i)) * koordinat[i]
        return point

    def animate(self, i):
        plt.cla()
        curve_points_user = []
        for j in range(i + 2):
            t = j / (i + 1) 
            curve_points_user.append(self.calculate_bezier_point(t, self.user_contpt))
        curve_points_user = np.array(curve_points_user)
        plt.plot(curve_points_user[:, 0], curve_points_user[:, 1], 'b-', label="Bezier Curve (Brute Force)")
        plt.plot(self.user_contpt[:, 0], self.user_contpt[:, 1],'ro-', label="Control Points")
        plt.title("Bezier Curve with Brute Force Method")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)

def main():
    num_points = int(input("Masukkan n jumlah titik: "))
    bezier = BezierCurve(num_points)
    iterasi = ((int(input("Masukkan jumlah iterasi: "))) * (num_points-1)) 
    time_start = time.time()
    anim = FuncAnimation(plt.gcf(), bezier.animate, frames=iterasi+2, repeat=False)
    time_end = time.time()
    print(f'Waktu eksekusi: {time_end - time_start} detik')
    plt.show()

if __name__ == "__main__":
    main()