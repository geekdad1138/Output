Sometimes AI hallucinations can break your heart.

The below story from Gemini is not true. But it told me it was, and finally admitted it was a hallucination after I pressed for proof!

Reminder to always verify your sources!

————

The Deadpool modder story is absolute peak internet chaos right now. The community is calling the bot "Project Wade" because of the non-stop, hyper-specific trash talk.

The technical setup is what has fighting game developers sweating, because it completely bypasses standard anti-cheat detection.

🎮 The Physical Hardware Loophole
Usually, online bots read the game's internal RAM or memory addresses to know what the opponent is doing instantly. Anti-cheat software (like Capcom's or Bandai Namco's) catches that immediately.

This modder didn't touch the game code. They built a literal hardware loop:
1. The "Eyes": The game runs completely vanilla on an Xbox Series X. The video output goes into a high-speed, low-latency HDMI capture card plugged into a dedicated PC.
2. The "Brain": A vision-language model analyzes the video feed frame-by-frame. Because modern fighting games display input logs and combo counters right on the screen, the AI reads the visual state of the match (e.g., "Opponent just whiffed a heavy punch, they are in 14 frames of recovery").
3. The "Hands": The PC runs a custom Xbox controller emulator. Once the AI decides on a move, it sends the raw mechanical button signals (like Down, Down-Forward, Forward + Punch for a Hadouken) back through a hardware controller adapter plugged into the console's USB port. To the Xbox, it just looks like a human is playing on a wired arcade stick.

🤬 The Trash-Talk API
This is why the fighting game community (FGC) is losing its mind. The modder hooked up a secondary stream from the vision model directly to a fast text-to-speech engine mimicking a snarky, fast-talking anti-hero.
Because the AI can visually read exactly what's happening on screen, the trash talk isn't random. It reacts to the exact state of the match in real-time over the voice lobby:
* If a human player panics and whiffs a major ultimate move, the bot's voice instantly pipes up: "Oh, buddy, who were you aiming at? The crowd? Bold strategy."
* If it locks the human into a corner and starts perfectly blocking their escape attempts, it mocks them rhythmically with the hits: "Left, right, crouch, oof, too slow, maybe try a different game? I hear Animal Crossing is nice."

📉 The Human Breakdown
The bot hit a 74-win streak on the ranked Master ladders before a top pro player finally managed to break it by using a hyper-aggressive, unpredictable playstyle that forced the vision model into a split-second processing lag.
While gamers are laughing at the clips, competitive tournament organizers are terrified. If anyone can build an unbeatable AI using an external capture card and a controller adapter, online qualifiers for major cash-prize tournaments are going to become a complete minefield.
