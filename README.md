## Prompt Testing for AutoGen when using local LLMs

This repository is my playground for testing prompts that generate suitable responses from local LLMs. As it's a playground, it isn't structured well so feel free to ask any questions should you have them. The [AutoGen Discord](https://discord.gg/QKUXYrqD) is a great place for discussion, see the #alt-models channel within it.

I'm investigating points in the AutoGen workflow (from the code base to the agent descriptions) that need to be tailored to accommodate local LLMs that aren't as capable as large private models like AI's ChatGPT.

Currently testing with a "Group Chat" debating scenario (see [debate.py](speaker_selection/debate.py)) that was created by tevslin (see his [repository](https://github.com/tevslin/debate_team) and [blog post](https://blog.tomevslin.com/2024/02/an-ai-debate.html), thank you!) using Mixtral and various other local LLMs to get the LLM to return the name of the next agent/role consistently. This is a good test because it involves an LLM understanding an order of agents, reviewing where the debate is up to and determining the next agent. We could almost do this in a round-robin format, or a finite state machine (where we set who can talk to who), but it's important to be able to prompt an LLM to pick the right, next, agent.

I'll put any findings in this README. Please note that this is evolving and I'm just one person trying to make things work :smiley:.

### LLMs I'm trying
- Llama2 13B Chat
- Mistral 7B v0.2 Instruct
- Mixtral 8x7B v0.1 Instruct (Q4)
- Neural Chat 7B
- OpenHermes 7B Mistral v2.5 (Q6)
- Orca 2 13B
- Phi-2
- Phind CodeLlama 34B v2
- Qwen 14B Chat (Q6)
- SOLAR 10.7B Instruct
- Yi-34B Chat (Q3)

I'm using Ollama when testing against AutoGen libraries and with LiteLLM when testing through AutoGenStudio.

The code I'm currently testing with is in [Speaker Selection - Test Rounds](speaker_selection/agent_prompt_testing%20Debate%20P4%20Tests.py).

#### Current performance for speaker selection on the debate challenge:

| | Speakers selected correctly |
| --- | --- |
| :white_check_mark: | All 5 correct |
| :large_orange_diamond: | 4 of 5 correct |
| :x: | 3 or less correct |
| :thumbsdown: | didn't pass GO |

_Wide table - scroll -- >_

**Step 1 Content**|	**Select Speaker**|	**Context Reduction**|	phind-codellama:34b-v2|	mixtral 8x7B (Q4)|	openhermes:7b-mistral-v2.5-q6_K|	orca2:13b-q5_K_S|	solar:10.7b-instruct-v1-q5_K_M|	neural-chat:7b-v3.3-q6_K|	llama2:13b-chat|	qwen:14b-chat-q6_K|	mistral:7b-instruct-q6_K|	yi:34b-chat-q3_K_M|	phi-2|
| --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |	 --- |
|Original|	Original|	None|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Original|	Emphasize, Sequence, Concise|	Summarised|	:white_check_mark:|	:white_check_mark:|	:white_check_mark:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Original|	Emphasize, Sequence, Concise|	None|	:x:|	:white_check_mark:|	:white_check_mark:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize Order|	Emphasize, Sequence, Concise|	None|	:white_check_mark:|	:large_orange_diamond:|	:white_check_mark:|	:x:|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize Order|	Emphasize, Sequence, Concise|	Summarised|	:white_check_mark:|	:large_orange_diamond:|	:white_check_mark:|	:x:|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Sequence, Concise|	None|	:white_check_mark:|	:white_check_mark:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Sequence, Concise|	Summarised|	:white_check_mark:|	:white_check_mark:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Original|	Original|	Only Speaker Name|	:white_check_mark:|	:x:|	:x:|	:x:|	:white_check_mark:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Capitals, Reasoning, No Debating|	First 300 Characters|	:large_orange_diamond:|	:white_check_mark:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:large_orange_diamond:|	:x:|	:thumbsdown:|
|Emphasize Order|	Emphasize, Sequence, Concise|	First 300 Characters|	:large_orange_diamond:|	:white_check_mark:|	:x:|	:x:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize Order|	Emphasize, Sequence, Concise|	First 100 Chars and Name|	:white_check_mark:|	:large_orange_diamond:|	:x:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:thumbsdown:|
|Emphasize Order|	Emphasize, Sequence, Concise|	Only Speaker Name|	:large_orange_diamond:|	:white_check_mark:|	:x:|	:x:|	:x:|	:large_orange_diamond:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:thumbsdown:|
|Emphasize Order|	Emphasize, Capitals, Reasoning, No Debating|	First 300 Characters|	:x:|	:large_orange_diamond:|	:x:|	:white_check_mark:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Sequence, Concise|	First 300 Characters|	:x:|	:white_check_mark:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:large_orange_diamond:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Sequence, Concise|	Only Speaker Name|	:large_orange_diamond:|	:white_check_mark:|	:x:|	:x:|	:x:|	:x:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Capitals, Single Word Reply|	Summarised|	:x:|	:x:|	:large_orange_diamond:|	:white_check_mark:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Sequence, Concise|	First 100 Chars and Name|	:large_orange_diamond:|	:white_check_mark:|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Capitals, Single Word Reply|	None|	:x:|	:x:|	:x:|	:white_check_mark:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Capitals, Single Word Reply|	Only Speaker Name|	:x:|	:x:|	:x:|	:x:|	:white_check_mark:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Capitals, Reasoning, No Debating|	None|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|
|Emphasize + Example|	Emphasize, Capitals, Reasoning, No Debating|	Summarised|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:large_orange_diamond:|	:x:|	:x:|	:x:|	:x:|	:x:|	:thumbsdown:|



**Winners:**
1. phind-codellama:34b-v2
2. mixtral:8x7b-instruct-v0.1-q4_K_M
3. openhermes:7b-mistral-v2.5 (Q6)

#### Learnings to date:

### LLMs differ
Results differ significantly between LLMs, unsurprisingly. However, tweaking prompts was changing the way they behaved independently - e.g. Changing a word or two in a prompt would mean that Mistral 7B, which had been producing the right outcome, would produce something unexpected but that same change would mean that Solar 10.7B, which wasn't producing what I wanted, would all of a sudden be generating the correct outcome.

So, at this stage I believe we'll need to tailor a lot of the prompts (both the ones we can control through agent descriptions and system messages, through to the underlying prompts such as the speaker selection) to suit the LLMs we are using. That is until a minimum LLM standard of reasoning can be achieved.

### Temperature = 0
I learnt quickly that to get consistent outcomes, at least for the speaker selection prompt, I had to set the temperature to zero (may work with low numbers rather than just zero). Although, even at zero, the responses do vary at times they are generally consistent.

The ability to be able to set the temperature for models in AutoGen is important for these small LLMs.

### Context length
As the chat messages continue to grow in number, so too does the chance that a model will stop producing good responses. Some, like Phi-2 with a 2K context length, would stop generating outcomes less than halfway through my testing with the debate group chat. Others, including Mixtral 8x7B with a 32K context window, showed improvement when context lengths were reduced (well before the content was that long).

An example of this, with Mixtral, is that when the full chat message passed to Mixtral was less than 8,700 characters (not tokens, I couldn't get that figure) it would return the correct answer (consistently up to that character count). When it was above 8,700 characters it would not follow directions and instead of returning the next speaker's name it would debate as them. This was a consistent issue as the length continued to increase beyond 8,700. I imagine other models this switching point would be lower still.

At the moment there doesn't seem to be a mechanism for compressing the conversation history, however I think this could be useful to keep the context of the full chat as more chatting occurs.

### Reducing chat message length
With the challenge of minimising context length I thought of two options:
1. Removing the content of an agent's message if we don't need it for speaker selection
2. Summarising the content of an agent's message so we keep the general context - this works with a few messages but as the number of messages increase the summaries may still be too much. 

We could, I guess, combine the two options, removing the content of older messages and summarising the more recent ones.

For the speaker selection testing I'm doing, removing the context and summarising the agent messages both worked and produced the correct results. This is promising.

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


### Who's really speaking?
With the debating test there's an introducting chat message (this is a role play game, ...) and then a chat message for each of the debaters. We pass all these chat messages to the LLM to determine the next speaker during the speaker selection process.

The chat message for each debater has the content (their debate response), the role ("user"), and name (their agent name), like this:
```
    {
        "content": "<a whole lot of content here.>",
        "role": "user",
        "name": "Affirmative_Constructive_Debater",
    },
```

As that all gets passed to the LLM I thought it would use that ```name``` key/value to know which agent that message came from.

Interestingly, if I added the following to the start of the content for each of those messages
```
I am <the debater's name here>. <then the original content goes next>
```
... Mixtral was much better at picking up who has spoken and choosing the next agent. Therefore, it may be advantageous to insert this explicitly at the start of each agent's message so we are sure that the LLM knows who the agent was. Or, at least in this case where the name of the agent is important to determine the sequence.

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
| Phind CodeLlama 34B | Surprisingly good! Up with Mixtral. However, it says it won't debate! |
| Yi-34B Chat (Q3) | This surprised me, it really was the worst of the bunch. I'm ranking it below Phi-2 as it is too large to be this bad at following directions. Perhaps an Instruct / Other version would be better. |

See more information in one of my [prompt findings](speaker_selection/PromptFindings.txt) documents that shows how I iterated through prompts and what the effect was on each of the LLMs' responses.

Have you used other models that do follow directions well, please let me know!

### Hold up, what about after we address all these challenges?
Implementing some of these (temp=0, summarising, cleaning agent names, changing role selection prompt) meant I was able to get Mixtral to choose the right agent every time during speaker selection (5 sequences with 10 iterations each). :fireworks:

Without tuning the prompts specifically to these other models:
- Mistral 7B and Solar 10.7B successfully passed 4 of the 5 agent selection tests.
- Llama 2 13B passed 3 out of 5 tests.

I believe these are significant because they were less successful before these changes and rather unpredictable.

Of course my testing and tweaking, particularly on prompts, is on the test chat I'm working on. So more testing would be good.