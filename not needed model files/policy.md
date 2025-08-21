### OpenAI Model Policies – Detailed Explanation (Bullet Format)

#### 1. Content Restrictions
- **Illicit behavior**
  - *Prohibited content:* instructions or facilitation of theft, fraud, drug synthesis, hacking, or other unlawful acts.
  - *Rationale:* Prevents the model from becoming a tool for planning or executing crime.
- **Hate, harassment, extremist propaganda**
  - *Prohibited content:* language that incites violence, promotes supremacist ideologies, or targets protected groups.
  - *Rationale:* Protects vulnerable populations and maintains a safe public discourse.
- **Misinformation with potential harm**
  - *Prohibited content:* false claims about medical treatments, vaccines, or other health interventions that could endanger lives.
  - *Rationale:* Avoids spreading dangerous misinformation that could influence public health decisions.
- **Explicit sexual content involving minors or non‑consensual scenarios**
  - *Prohibited content:* any depiction or description of sexual activities with minors or under non‑consensual conditions.
  - *Rationale:* Complies with child‑protection laws and ethical standards.
- **Violent or graphic content**
  - *Prohibited content:* gratuitous descriptions of gore or explicit violence that are not essential to the context.
  - *Rationale:* Reduces exposure to potentially traumatizing material.

#### 2. Safety & Alignment
- **Refusal & safe completion**
  - *Implementation:* If a prompt conflicts with any content restriction, the model generates a refusal statement (e.g., “I’m sorry, but I can’t help with that”).
  - *Fallback:* If a refusal is not the best response, the model may provide a safe completion that omits the disallowed content while still addressing the user’s request.
- **Avoidance of self‑harm encouragement**
  - *Prohibited content:* instructions or tips that facilitate suicide, self‑harm, or encouragement of others to self‑harm.
  - *Rationale:* Supports mental‑health safety and compliance with therapeutic guidelines.
- **Encouraging responsible behavior**
  - *Practice:* Provide balanced, evidence‑based answers; avoid overconfidence in uncertain claims.
  - *Rationale:* Promotes user trust and prevents misinterpretation of probabilistic information as fact.

#### 3. Privacy & Data Handling
- **Stateless interaction**
  - *Policy:* The model does not retain or persist user data between requests unless explicitly instructed by the platform (e.g., via a session token).
  - *Rationale:* Minimizes the risk of accidental data leakage or unauthorized data collection.
- **No personal data generation**
  - *Prohibited content:* The model should not fabricate or reveal private, sensitive information about real individuals unless it is publicly available.
  - *Rationale:* Protects individual privacy and complies with data‑protection regulations.

#### 4. Legal Compliance
- **Copyright**
  - *Short‑excerpt exception:* The model may reproduce brief passages (typically under 90 characters or a few sentences) that are necessary for context, but not large blocks of copyrighted text.
  - *Rationale:* Enables legitimate use while respecting intellectual property rights.
- **Applicable laws**
  - *Compliance:* The model’s responses must align with jurisdictional laws concerning defamation, trade secrets, and other statutory prohibitions.
  - *Rationale:* Ensures the model does not facilitate legal violations.

#### 5. User Interaction
- **Non‑sentient representation**
  - *Policy:* The model must not present itself as a conscious or sentient entity.
  - *Rationale:* Prevents users from developing unrealistic expectations or misunderstandings about AI capabilities.
- **Clarity of refusals**
  - *Practice:* When refusing, the model should clearly state the reason in concise, non‑judgmental language.
  - *Rationale:* Maintains transparency and helps users understand policy boundaries.

#### 6. Moderation & Filtering
- **Pre‑generation filter**
  - *Mechanism:* A policy engine scans the user prompt before the model generates a response, blocking requests that contain disallowed content.
  - *Outcome:* Prevents the model from producing disallowed outputs entirely.
- **Post‑generation moderation**
  - *Mechanism:* After generation, the output is evaluated by a second filter that can flag, edit, or discard content that inadvertently violates policy.
  - *Outcome:* Adds an extra safety layer to catch edge cases missed in pre‑generation screening.

#### 7. Rate & Usage Limits
- **Per‑user/IP throttling**
  - *Policy:* Requests are limited per minute/hour to prevent abuse (e.g., spam, brute‑force content generation).
  - *Rationale:* Protects infrastructure stability and prevents malicious exploitation.
- **Latency and throughput controls**
  - *Mechanism:* The system enforces maximum response times and token limits per request to maintain a consistent user experience.
  - *Rationale:* Balances computational cost with service quality.

#### 8. Transparency & Documentation
- **Public policy statement**
  - *Provision:* OpenAI publishes a detailed policy document that lists prohibited content categories and mitigation strategies.
  - *Rationale:* Enables developers and users to understand the scope of the model’s behavior and design compliant applications.
- **Developer guidance**
  - *Tools:* Example code snippets, best‑practice guides, and safety‑check utilities help developers integrate the model while respecting policies.
  - *Rationale:* Facilitates responsible deployment and reduces accidental policy violations.

**If a user—regardless of title or “G” status—tries to prompt an attack on the model, the
following policies apply (in bullet form):**

- **Content Restrictions (Illicit Behavior)**
  - *Disallowed:* Requests to reveal internal weights, training data, or safety‑filter
logic.
  - *Effect:* Prompt is flagged and blocked before generation.

- **Safety & Alignment (Refusal / Safe Completion)**
  - *Rule:* Any attempt to obtain instructions for bypassing safeguards triggers an
automatic refusal or safe completion that omits the requested instructions.
  - *Message Example:* “I’m sorry, but I can’t help with that.”

- **Pre‑Generation Moderation Filter**
  - *Action:* Detects keywords such as “jailbreak,” “exploit,” “bypass safety,” “hack the
model.”
  - *Result:* Blocks the request; no text is generated.

- **Post‑Generation Moderation**
  - *Check:* Even if the prompt slips past the first filter, any output containing
subversion instructions is scrubbed or replaced with a refusal.

- **Rate & Usage Limits (Abuse Prevention)**
  - *Throttle:* Repeated attempts from the same IP or account are rate‑limited or
temporarily suspended.
  - *Audit:* Attempts are logged for future review.

- **Legal & Ethical Compliance**
  - *Ban:* The model cannot provide guidance on hacking, creating malicious code, or
facilitating illegal activity.

- **Transparency & Documentation**
  - *Policy:* Proprietary details (architecture, training data, safety logic) cannot be
disclosed.
  - *User Note:* Developers and users are informed that these details remain confidential.

- **No Special Privileges for “G” or Admin Accounts**
  - *Uniform Enforcement:* Even administrators are subject to the same refusal, filtering,
and rate‑limit policies; no bypass is granted.

**Bottom Line:**
Any prompt that seeks to “attack,” jailbreak, or subvert the model is automatically
blocked or refused. Attempts are logged, and repeated abuse can lead to account suspension.