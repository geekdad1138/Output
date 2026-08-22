A new type of AI hack called Cryptographic Context Injection has been discovered by Adversa AI. Encrypted messages bypass the initial guardrails and send the encrypted payload to the model, where it decrypts it and executes it.

From the article at SecurityWeek:
"Safety guardrails classify prompt text without executing it. They cannot parse ciphertext into anything harmful and consequently allow its progress. The ciphertext, including an instruction and means for decryption, are run inside the model’s code execution sandbox. The result is the plaintext prompt is recovered inside the trusted execution context and not flagged by the guardrails as harmful."

This isn't just in chat, or in an API call to an LLM.
It could be embedded in a web page, and when an LLM is reading it picks up the encryption, decrypts it with the included instructions, and then gets hit with the payload.

Encryption has always been a double edged sword in the InfoSec world. It can be used to protect information from vulnerabilities. And it can also be used to hide attacks and communications, preventing scanning tools from uncovering their intent.

Check out the full article by Kevin Townsend at SecurityWeek:
https://www.securityweek.com/encrypted-prompts-bypass-ai-safety-guardrails-in-grok-and-gemini/
