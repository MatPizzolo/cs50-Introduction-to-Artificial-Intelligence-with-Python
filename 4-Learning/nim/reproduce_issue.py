from nim import Nim, NimAI

def test_best_future_reward():
    ai = NimAI()
    
    # Setup a state and some q-values
    state = [1, 3, 5, 7]
    state_tuple = tuple(state)
    
    # Add some Q-values to AI
    # Action (0, 1) -> Q=0.4
    # Action (1, 1) -> Q=0.2
    ai.q[(state_tuple, (0, 1))] = 0.4
    ai.q[(state_tuple, (1, 1))] = 0.2
    
    # Check best_future_reward
    # It should return 0.4
    result = ai.best_future_reward(state)
    print(f"State: {state}")
    print(f"Q-values in AI: {ai.q}")
    print(f"Result: {result}")
    
    if abs(result - 0.4) < 0.0001:
        print("Test PASSED")
    else:
        print("Test FAILED")

if __name__ == "__main__":
    test_best_future_reward()
