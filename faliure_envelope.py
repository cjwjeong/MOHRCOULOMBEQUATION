import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


class FailureEnvelope:
    def __init__(self, circles):
        """
        Failure Envelope 생성자
        :param circles: MohrCircle 객체들의 리스트
        """
        self.circles = circles
        self.centers = [circle.center for circle in circles]
        self.radii = [circle.radius for circle in circles]
        self.scaleX = np.linspace(1, 90, 9000, endpoint=True)  # 0.01 단위로 각도 설정

    def getlineParam(self, angle):
        """
        주어진 각도에서 접선을 찾고, 회귀선을 계산
        :param angle: 회전 각도 (degree)
        :return: 기울기, 절편, 접점 X 좌표, 접점 Y 좌표
        """
        meetPointX = [self.centers[i] - (self.radii[i] * np.cos(np.deg2rad(angle)))
                      for i in range(len(self.centers))]

        meetPointY = [self.radii[i] * np.sin(np.deg2rad(angle))
                      for i in range(len(self.centers))]

        slope, intercept, _, _, _ = stats.linregress(meetPointX, meetPointY)
        return slope, intercept, meetPointX, meetPointY

    def getBestAngle(self):
        """
        모든 각도에 대해 평균 오차가 가장 작은 최적의 접선 각도 찾기
        :return: 최적의 각도
        """
        Avgs = []

        for angle in self.scaleX:
            slope, intercept, _, _ = self.getlineParam(angle)
            avg_distance = np.mean([
                self.radii[i] - abs(slope * self.centers[i] + intercept) / np.sqrt(slope ** 2 + 1)
                for i in range(len(self.centers))
            ])
            Avgs.append(avg_distance)

        # 최적의 각도 (가장 오차가 작은 경우)
        best_angle = self.scaleX[np.argmin(Avgs)]
        return best_angle

    def plot_envelope(self):
        """
        Mohr Circle들과 파괴 포락선을 그린다.
        """
        fig, ax = plt.subplots(figsize=(8, 6))

        # Mohr Circles 그리기
        for circle in self.circles:
            x, y = circle.calculate_points()
            ax.plot(x, y, label=f"σ1={circle.sigma1}, σ3={circle.sigma3}")
            ax.scatter([circle.sigma1, circle.sigma3], [0, 0], color='red')

        # 최적의 접선 구하기
        best_angle = self.getBestAngle()
        slope, intercept, _, _ = self.getlineParam(best_angle)

        # 포락선 그리기
        x_envelope = np.linspace(min(self.centers) - max(self.radii), max(self.centers) + max(self.radii), 500)
        y_envelope = slope * x_envelope + intercept

        ax.plot(x_envelope, y_envelope, 'r--', label="Failure Envelope")

        # Plot 설정
        ax.set_xlabel("Normal Stress (σ)")
        ax.set_ylabel("Shear Stress (τ)")
        ax.legend()
        ax.grid(True)
        ax.set_aspect('equal', 'box')
        plt.show()

