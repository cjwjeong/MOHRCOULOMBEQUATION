from mohr_circle import MohrCircle
from faliure_envelope import FailureEnvelope


if __name__ == "__main__":
    mc1 = MohrCircle(163, 3.5)
    mc2 = MohrCircle(211, 11)
    mc3 = MohrCircle(180, 6)
    mc4 = MohrCircle(211, 7)
    line = FailureEnvelope([mc1, mc2, mc3, mc4])
    line.plot_envelope()

    MohrCircle.plot_multiple([mc1, mc2, mc3, mc4])


