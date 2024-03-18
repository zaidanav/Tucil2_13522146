import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

class BezierCurve:
    def __init__(self, num_points):
        self.num_points = num_points
        self.user_contpt = self.get_control_points()
        self.time = 0
        

    def get_control_points(self):
        points = []
        for i in range(self.num_points):
            x, y = map(float, input(f"Point {i+1} (x,y): ").split(','))
            points.append([x, y])
        return np.array(points)

    def calculate_bezier_point(self, t, koordinat):
        start = time.time()
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
        self.time += time.time() - start
        return point
    
    def gettime(self):
        return self.time

    def animate(self, i, it): 
        plt.cla()

        curve_points_user = []

        for j in range(i + 2):
            t = j / (i + 1) 
            curve_points_user.append(self.calculate_bezier_point(t, self.user_contpt))
    
        curve_points_user = np.array(curve_points_user)
        plt.plot(curve_points_user[:, 0], curve_points_user[:, 1], 'b-', label="Bezier Curve (Brute Force)")
        plt.scatter(curve_points_user[:, 0], curve_points_user[:, 1], color='blue')
        plt.plot(self.user_contpt[:, 0], self.user_contpt[:, 1],'ro-', label="Control Points")
        
        # Check if all iterations have been completed
        if i < it:
            plt.title("Bezier Curve with Brute Force Method (Process)") 
        else:
            plt.title("Bezier Curve with Brute Force Method (Completed)")
        
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)

def main():
    num_points = int(input("Masukkan n jumlah titik: "))
    bezier = BezierCurve(num_points)
    it = ((int(input("Masukkan jumlah iterasi: "))) * (num_points-1)) 
    anim = FuncAnimation(plt.gcf(), lambda i: bezier.animate(i, it), frames=it+2, repeat=False)  
    plt.show()
    print(f"Time: {bezier.gettime()}s")

if __name__ == "__main__":
    main()