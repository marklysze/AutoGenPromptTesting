## Prompt Testing for AutoGen when using local LLMs

This repository is my playground for testing prompts that generate suitable responses from local LLMs.

I'm investigating points in the AutoGen workflow (from the code base to the agent descriptions) that need to be tailored to accommodate local LLMs that aren't as capable as large private models like AI's ChatGPT.

Currently testing with a "Group Chat" debating scenario (see [debate.py](debate.py)) using Mixtral and various other local LLMs to get the LLM to return the name of the next agent/role consistently.

I'll put any findings in here.
