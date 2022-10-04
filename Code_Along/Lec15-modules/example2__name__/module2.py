import numpy as np

def trigonometric_identity(angle: float) -> float:
    """Calculates trig identity

    param:
    angel: angle in radians

    return: trigonometric one
    """

    print("Running trigonometric_identity()")
    return np.cos(angle) ** 2 + np.sin(angle) ** 2

print(trigonometric_identity(42))

if __name__ == "__main__":
    print("Running direcetly from module2.py")
    print(trigonometric_identity(42))

else:
    print("You have imported me!")
