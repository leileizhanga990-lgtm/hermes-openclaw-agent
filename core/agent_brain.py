class AgentBrain:
    def __init__(self):
        self.memory = []
        self.model = "llm-placeholder"

    def plan(self, user_input):
        print(f"[Planning] Processing input: {user_input}")
        return {"task": "example task"}

    def execute(self, task):
        print(f"[Executing] Task: {task}")
        return {"result": "done"}

    def run(self):
        user_input = "demo input"
        plan = self.plan(user_input)
        result = self.execute(plan)
        print(f"[Result] {result}")


if __name__ == "__main__":
    agent = AgentBrain()
    agent.run()
