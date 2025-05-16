import numpy as np
import matplotlib.pyplot as plt

class MohrCircle:
    def __init__(self, sigma1, sigma3):
        """
        Mohr Circle 생성자
        :param sigma1: 최대 주응력(σ1)
        :param sigma2: 최소 주응력(σ3)
        """
        self.sigma1 = sigma1
        self.sigma3 = sigma3
        self.center = (sigma1 + sigma3) / 2
        self.radius = (sigma1 - sigma3) / 2

    def calculate_points(self, num_points = 100):
        """
        Mohr Circle 점들의 좌표 계산
        :param num_points: Circle을 표현할 점들의 개수
        :return: x, y 좌표 리스트
        """
        theta = np.linspace(0, np.pi, num_points)
        x = self.center + self.radius * np.cos(theta)
        y =   self.radius * np.sin(theta)

        return x, y

    @staticmethod
    def plot_multiple(circles):
        """
        여러 개의 Mohr Circle을 한 화면에 그린다.
        :param circles: MohrCircle 객체들의 리스트
        """
        fig, ax = plt.subplots(figsize=(8, 6))

        # 모든 Circle 그리기
        for circle in circles:
            x, y = circle.calculate_points()
            ax.plot(x, y, label=f"σ1={circle.sigma1}, σ3={circle.sigma3}")
            ax.scatter([circle.sigma1, circle.sigma3], [0, 0], color='red')

        ax.set_xlabel("Normal Stress (σ)")
        ax.set_ylabel("Shear Stress (τ)")
        ax.legend()
        ax.grid(True)
        ax.set_aspect('equal', 'box')
        plt.show()




