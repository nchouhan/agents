from agents import Agent, FileSearchTool, Runner, WebSearchTool
import asyncio

agent = Agent(
    name="Assistant",
    tools=[
        WebSearchTool(),
        FileSearchTool(
            max_num_results=3,
            # vector_store_ids=["vector_store.index"],
            # Note Faiss vector doesn't work use open ai or any other storage
            vector_store_ids=["vs_67e253433b3c8191a7ac85308bd288c8"]
        ),
    ],
)

async def main():
    result = await Runner.run(agent, "Which coffee shop should I go to, taking into account my preferences and the weather today in SF?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())