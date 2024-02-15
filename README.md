## Prompt Testing for AutoGen when using local LLMs

This repository is my playground for testing prompts that generate suitable responses from local LLMs. As it's a playground, it isn't structured well so feel free to ask any questions should you have them. The [AutoGen Discord](https://discord.gg/QKUXYrqD) is a great place for discussion, see the #alt-models channel within it.

I'm investigating points in the AutoGen workflow (from the code base to the agent descriptions) that need to be tailored to accommodate local LLMs that aren't as capable as large private models like AI's ChatGPT.

Currently testing with a "Group Chat" debating scenario (see [debate.py](speaker_selection/debate.py)) using Mixtral and various other local LLMs to get the LLM to return the name of the next agent/role consistently.

I'll put any findings in here.

Learnings to date:

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

### LLMs differ
Results differ significantly between LLMs, unsurprisingly, however tweaking prompts was changing the way they behaved independently - e.g. Changing a word or two in a prompt would mean that Mistral 7B, which had been producing the right outcome, would produce something unexpected. That same change would mean that Solar 10.7B, which wasn't producing what I wanted, would all of a sudden be generating the correct outcome.

So, at this stage I believe we'll need to tailor a lot of the prompts (both the ones we can control through agent descriptions and system messages, through to the underlying prompts such as the speaker selection) to suit the LLMs we are using. That is until a minimum standard can be achieved.

### Temperature
I learnt quickly that to get consistent outcomes, at least for the speaker selection prompt, I had to set the temperature to zero (may work with low numbers rather than just zero). Although, even at zero, the responses to vary at times they are generally consistent.

The ability to be able to set the temperature for models in AutoGen is important for these small LLMs.

### Context length
As the chat messages continue to grow in number, so too does the ability for models to continue to generate good responses. Some, like Phi-2 with a 2K context length, would stop generating outcomes less than halfway through my testing with the debate group chat. Others, including Mixtral 8x7B with 32K context window, showed improvement when context lengths were reduced (well before the content was that long).

At the moment there doesn't seem to be a mechanism for compressing the conversation history, however I think this could useful to keep the context of the full chat as more chatting occurs.

### Speaker Selection (Auto mode) in a Group Chat
I've been focusing on testing this as it's critical to having agents selected correctly. This task, which is largely done in the underlying AutoGen code, is tailored to Open AI's ChatGPT. The prompt it generates likely works with other very large models, too. However, controlling this prompt is necessary to provide the specific direction for our smaller local LLMs.

The default prompt is
```
You are in a role play game. The following roles are available:\n{self._participant_roles(agents)}.\n\nRead the following conversation.\nThen select the next role from {[agent.name for agent in agents]} to play. Only return the role.
```

For my testing on the debating workflow I'm continuously tailoring it and an example of what it looks like for Mixtral 8x7B is:
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

However, and painfully as it's the primary model I wanted to use, Mixtral appears to provide a response in Markdown (?) formats a lot of the time. So if an agent was named
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