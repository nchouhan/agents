from flask import Flask, request, render_template
import asyncio
import dotenv
from pydantic import BaseModel
from agents import Agent, Runner, FileSearchTool, WebSearchTool
from agents import GuardrailFunctionOutput
# from main import triage_agent  # Assuming main.py is in the same directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # result = await Runner.run(triage_agent, user_input)
        # Run the async main function and get the result
        result = asyncio.run(main(user_input))
        # return render_template('index.html', result=result.final_output)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

dotenv.load_dotenv();

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

# agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
# print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.

#handoff_descriptions provides additional context for determining handoff routing

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)
#Agent to identify correct agents based on user's question
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent]
)

async def main(user_input):
    result = await Runner.run(triage_agent, user_input)
    print(result.final_output)
    return result.final_output
    # result = await Runner.run(triage_agent, "What is the capital of France?")
    # print(result.final_output)


async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )



if __name__ == "__main__":
    app.run(debug=True)