import time
from openai import AsyncOpenAI
import chainlit as cl
from langchain_ollama import OllamaLLM


# Initialize OpenAI client with Ollama configuration
# Using localhost:11434 as Ollama's default endpoint
client = AsyncOpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1/"
    )


@cl.on_message
async def on_message(msg: cl.Message):
    """
    Main message handler for Chainlit chat interface.
    Processes incoming messages and streams responses from DeepSeek model.
    
    Args:
        msg (cl.Message): Incoming message object from Chainlit
    """
    # Track response generation time
    start = time.time()
    
    # Create streaming chat completion request
    stream = await client.chat.completions.create(
        model="deepseek-r1:latest",
        messages=[
            {"role": "system", "content": "You are an helpful assistant"},
            *cl.chat_context.to_openai()  # Convert chat history to OpenAI format
        ],
        stream=True
    )

    # Flag to track thinking state
    thinking = False
    
    # Handle streaming response with thinking visualization
    async with cl.Step(name="Thinking") as thinking_step:
        # Initialize empty message for final response
        final_answer = cl.Message(content="")

        # Process each chunk from the stream
        async for chunk in stream:
            delta = chunk.choices[0].delta

            # Handle thinking state markers
            if delta.content == "<think>":
                thinking = True
                continue
                
            if delta.content == "</think>":
                thinking = False
                # Update step name with thinking duration
                thought_for = round(time.time() - start)
                thinking_step.name = f"Thought for {thought_for}s"
                await thinking_step.update()
                continue
            
            # Stream tokens to either thinking step or final answer
            if thinking:
                await thinking_step.stream_token(delta.content)
            else:
                await final_answer.stream_token(delta.content)
                
    # Send the complete response
    await final_answer.send()