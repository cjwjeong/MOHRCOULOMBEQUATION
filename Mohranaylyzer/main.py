from mohr_circle import MohrCircle
from faliure_envelope import FailureEnvelope

keep_input = True
circles = []


while keep_input:
    sigma1, sigma3 = map(float, input("공백을 두어 최대 주응력과 최소 주응력을 입력하시오").split())
    circles.append(MohrCircle(sigma1, sigma3))

    if input("계속 입력을 원하시면 1을 입력하세요: ") != "1":
        keep_input == False
        


if __name__ == "__main__":
    line = FailureEnvelope(circles)
    line.plot_envelope()

    MohrCircle.plot_multiple(circles])