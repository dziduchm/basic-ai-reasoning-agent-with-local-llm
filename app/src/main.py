from graph.workflow import Workflow

def main():
    workflow = Workflow()
    # Define the initial state with a query and empty lists for chunks and reasoning steps
    initial_state = {
        "query": "Based on the meeting notes, which team should receive the most resources, and why?",
        "chunks": [],
        "reasoning_steps": [],
        "final_answer": ""
    }
    # Run the workflow with the initial state
    final_answer = workflow.run(initial_state)
    print("Final Answer:", final_answer)

if __name__ == "__main__":
    main()