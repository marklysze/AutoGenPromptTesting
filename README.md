## Prompt Testing for AutoGen when using local LLMs

This repository is my playground for testing prompts that generate suitable responses from local LLMs. As it's a playground, it isn't structured well so feel free to ask any questions should you have them. The [AutoGen Discord](https://discord.gg/QKUXYrqD) is a great place for discussion, see the #alt-models channel within it.

I'm investigating points in the AutoGen workflow (from the code base to the agent descriptions) that need to be tailored to accommodate local LLMs that aren't as capable as large private models like AI's ChatGPT.

Currently testing with a "Group Chat" debating scenario (see [debate.py](speaker_selection/debate.py)) using Mixtral and various other local LLMs to get the LLM to return the name of the next agent/role consistently.

I'll put any findings in here.

### LLMs I'm trying
- Llama2 13B Chat
- Mistral 7B v0.2 Instruct
- Mixtral 8x7B v0.1 Instruct (Q4)
- Neural Chat 7B
- OpenHermes 7B Mistral v2.5 (Q6)
- Orca 2 13B
- Phi-2
- Qwen 14B Chat (Q6)
- SOLAR 10.7B Instruct
- Yi-34B Chat (Q3)

I'm using Ollama when testing against AutoGen libraries and with LiteLLM when testing through AutoGenStudio.

Learnings to date:

### LLMs differ
Results differ significantly between LLMs, unsurprisingly, however tweaking prompts was changing the way they behaved independently - e.g. Changing a word or two in a prompt would mean that Mistral 7B, which had been producing the right outcome, would produce something unexpected. That same change would mean that Solar 10.7B, which wasn't producing what I wanted, would all of a sudden be generating the correct outcome.

So, at this stage I believe we'll need to tailor a lot of the prompts (both the ones we can control through agent descriptions and system messages, through to the underlying prompts such as the speaker selection) to suit the LLMs we are using. That is until a minimum standard can be achieved.

### Temperature
I learnt quickly that to get consistent outcomes, at least for the speaker selection prompt, I had to set the temperature to zero (may work with low numbers rather than just zero). Although, even at zero, the responses do vary at times they are generally consistent.

The ability to be able to set the temperature for models in AutoGen is important for these small LLMs.

### Context length
As the chat messages continue to grow in number, so too does the chance that a model will stop producing good responses. Some, like Phi-2 with a 2K context length, would stop generating outcomes less than halfway through my testing with the debate group chat. Others, including Mixtral 8x7B with 32K context window, showed improvement when context lengths were reduced (well before the content was that long).

At the moment there doesn't seem to be a mechanism for compressing the conversation history, however I think this could be useful to keep the context of the full chat as more chatting occurs.

### Speaker Selection (Auto mode) in a Group Chat
I've been focusing on testing this as it's critical to having agents selected correctly. This task, which is largely done in the underlying AutoGen code, is tailored to Open AI's ChatGPT. The prompt it generates likely works with other very large models, too. However, controlling this prompt is necessary to provide the specific direction for our smaller local LLMs.

The default prompt is
```
You are in a role play game. The following roles are available:\n{self._participant_roles(agents)}.\n\nRead the following conversation.\nThen select the next role from {[agent.name for agent in agents]} to play. Only return the role.
```

For my testing on the debating workflow, I'm continuously tailoring the prompt and an example of what it looks like for Mixtral 8x7B is:
```
Read the above conversation and select the next role, the list of roles is ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge']. What is the next role to speak, answer concisely please?
```

Interestingly, even a small tweak such as changing (in the above text)
```
answer concisely please
```
to
```
return only the name of the role
```
changed the response to an incorrect one for Mixtral but to a correct one for Llama 13B.


### Plain text outputs
Most models returned plain text responses and this is important for matching agent names to the text returned from the LLM.

However, and painfully as it's the primary model I wanted to use, Mixtral appears to provide a response in Markdown (?) format most of the time. So if an agent was named
```
Negative_Constructive_Debater
``` 
it may return
```
Negative\_Constructive\_Debater
```
or
```
Negative Constructive Debater
```

And that would throw off AutoGen from matching it against an agent's name.

I tried to change prompts to get Mixtral to provide a plain text output but couldn't get it to do so consistently.

Perhaps a tactic here is not to use underscores, though I think it has been mentioned to avoid spaces in agent names and use underscores instead, so it's worth tackling this.

Changes to the matching code to accommodate `\_` and spaces for underscores would go a long way to supporting local LLMs who may mix these up.

### So, what do I think are the best local LLMs to use?
As a caveat, I'm early into my testing and I've only been testing on the speaker selection prompting. Although this is critical to the multi-agent process, there are lots of other aspects of LLMs (quality responses, code generation, function calling, etc.) that I have not even touched.

So, my notes below are on early testing of LLMs choosing the correct next agent and returning its name. I'll put them in my order of preference.

Lastly, a lot of it is promping skills and I'm no expert :).

| LLM | Thoughts |
| --- | --- |
| Mixtral 8x7B v0.1 Instruct (Q4) | As the biggest model I expected this to handle direction better than the others. My experience has been that it provides consistent responses and with a few prompt changes you can wrangle it to get the outcome you need. It does have an odd quirk in that it responds in markdown format sometimes. |
| Mistral 7B v0.2 Instruct | Originally this provided the best responses, plain text outcomes and the ability to return a single agent name without going off course. Prompting showed that it was quite sensitive to prompt changes. It doesn't always understand the directions, though, well not as well as Mixtral | 
| Llama2 13B Chat | Hit and miss, when it was on point it was perfect, otherwise it just wasn't. More prompt tweaking could work here. |
| SOLAR 10.7B Instruct | As prompts were tweaked this became more and more consistent |
| Neural Chat 7B | Similar to Llama 13B, was excellent at times but anything but at others |
| OpenHermes 7B Mistral v2.5 (Q6) | In one test it was perfect, for all the rest it bombed. Found that it didn't follow directions well. |
| Orca 2 13B | Only completed one test well, didn't follow directions well for the rest |
| Qwen 14B Chat (Q6) | I had not used this model before and was hopefully, but it never passed a test and following directions wasn't its forte. |
| Phi-2 | Unfortunately the context length supported by this model quickly ran out. Additionally, it really didn't follow the directions precisely. |
| Yi-34B Chat (Q3) | This surprised me, it really was the worst of the bunch. I'm ranking it below Phi-2 as it is too large to be this bad at following directions. Perhaps an Instruct / Other version would be better. |

See more information in one of my [prompt findings](speaker_selection/PromptFindings.txt) documents that shows how I iterated through prompts and what the effect was on each of the LLMs' responses.

Have you used other models that do follow directions well, please let me know!