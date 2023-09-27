
class Physics:
    
    @staticmethod
    def getPosition(x_0, v_x_0, a, t) -> int:
        return int(x_0 + v_x_0 * t + 1/2 * (a * t ** 2))
