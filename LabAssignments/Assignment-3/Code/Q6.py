import simpy

class QueueSystem:
    def __init__(self, env, lambda1, lambda2, mu1, mu2):
        self.env = env
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.mu1 = mu1
        self.mu2 = mu2
        self.x1 = 0
        self.x2 = 0

    def update_queue1(self):
        while True:
            dx1 = self.lambda1 - (self.x1 / (1 + self.x1)) * self.mu1
            yield self.env.timeout(1)
            self.x1 = max(0, self.x1 + dx1)

    def update_queue2(self):
        while True:
            dx2 = self.lambda2 - (self.x2 / (1 + self.x2)) * self.mu2
            yield self.env.timeout(1)
            self.x2 = max(0, self.x2 + dx2)

def main():
    # parameters
    lambda1 = 0.8
    lambda2 = 1.0
    mu1 = 1.0
    mu2 = 1.5
    sim_duration = 1000

    # simulation environment
    env = simpy.Environment()
    queue_system = QueueSystem(env, lambda1, lambda2, mu1, mu2)
    env.process(queue_system.update_queue1())
    env.process(queue_system.update_queue2())
    env.run(until=sim_duration)
    equilibrium_x1 = (lambda1 / mu1) / (1 - (lambda1 / mu1))
    equilibrium_x2 = (lambda2 / mu2) / (1 - (lambda2 / mu2))

    print(f"Equilibrium Queue Size for Queue 1: {equilibrium_x1:.2f}")
    print(f"Equilibrium Queue Size for Queue 2: {equilibrium_x2:.2f}")

if __name__ == '__main__':
    main()