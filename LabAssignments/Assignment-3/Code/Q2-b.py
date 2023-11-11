import numpy as np

def calculate_steady_state(A, b):
    n = A.shape[0]
    I = np.identity(n)
    x = np.linalg.inv(I - A) @ b
    return x

def main():
    A = np.array([[0.2, 0.3, 0.7],
                [0.3, 0.1, 0.7],
                [0.7, 0, 0]])
    b = np.array([0.2, 0.8, 0])
    steady_state_x = calculate_steady_state(A, b)
    print("Steady state x:", steady_state_x)

if __name__ == '__main__':
    main()