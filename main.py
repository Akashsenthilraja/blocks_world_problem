from BlockWorldAgent import BlockWorldAgent


def test():

    test_agent = BlockWorldAgent()

    initial_arrangement_1 = [["A", "B", "C"], ["D", "E"]]
    goal_arrangement_1 = [["A", "C"], ["D", "E", "B"]]
    goal_arrangement_2 = [["A", "B", "C", "D", "E"]]
    goal_arrangement_3 = [["D", "E", "A", "B", "C"]]
    goal_arrangement_4 = [["C", "D"], ["E", "A", "B"]]

    print("\nIteration 1")
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_1))
    print("\nIteration 2")
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_2))
    print("\nIteration 3")
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_3))
    print("\nIteration 4")
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_4))

    initial_arrangement_2 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    goal_arrangement_5 = [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]
    goal_arrangement_6 = [["I", "H", "G", "F", "E", "D", "C", "B", "A"]]
    goal_arrangement_7 = [["H", "E", "F", "A", "C"], ["B", "D"], ["G", "I"]]
    goal_arrangement_8 = [["F", "D", "C", "I", "G", "A"], ["B", "E", "H"]]

    print("\nIteration 5")
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_5))
    print("\nIteration 6")
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_6))
    print("\nIteration 7")
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_7))
    print("\nIteration 8")
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_8))


if __name__ == "__main__":
    test()