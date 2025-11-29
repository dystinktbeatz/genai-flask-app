# llm_test.py  (complete file)
from model import llama3_response, granite_response, mixtral_response

def call_all_models(system_prompt, user_prompt):
    try:
        llama_result = llama3_response(system_prompt, user_prompt)
    except Exception as e:
        llama_result = f"Error from llama3_response: {e}"

    try:
        granite_result = granite_response(system_prompt, user_prompt)
    except Exception as e:
        granite_result = f"Error from granite_response: {e}"

    try:
        mixtral_result = mixtral_response(system_prompt, user_prompt)
    except Exception as e:
        mixtral_result = f"Error from mixtral_response: {e}"

    print("Llama3 Response:\n", llama_result)
    print("\nGranite Response:\n", granite_result)
    print("\nMixtral Response:\n", mixtral_result)

if __name__ == "__main__":
    call_all_models(
        "You are a helpful assistant who provides concise and accurate answers",
        "What is the capital of Canada? Tell me a cool fact about it as well"
    )
