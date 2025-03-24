from agents import Runner
#from main import main

async def main():
    result = await Runner.run(main.triage_agent, "What is the capital of France?")
    print(result.final_output)