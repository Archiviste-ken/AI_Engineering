🧠🚀 Lesson 2 Summary — Multi-Layer Networks & Forward Pass

"One neuron draws a line. Stack them, and you can draw anything." 🎯

🌍 The Big Problem

In Lesson 1, we built a Perceptron.

It was awesome... but it had one huge limitation.

A single perceptron can only create one straight decision boundary.

Single Perceptron

      /
     /
----/-------
   /
  /

That means it cannot solve problems like XOR because XOR needs a curved decision boundary.

🤯 Big Realization

One neuron = One straight line

That's the biggest limitation of the perceptron.

💡 The Solution

Instead of making one super neuron...

We stack many simple neurons together.

Input

↓

Neuron
Neuron
Neuron

↓

Neuron

↓

Prediction

This creates a Neural Network.

⭐ Biggest Realization #1

A Neural Network is NOT a new magical machine.

It is simply

Perceptron

+

Perceptron

+

Perceptron

+

Perceptron

+

...

Millions of simple neurons working together.

🧩 Layers

Every neural network has three kinds of layers.

🟢 Input Layer

Receives the data.

Example

Image

↓

Pixels

or

x₁

x₂

It does not learn anything.

It simply passes data forward.

❌ Input Layer does NOT have
Weights
Bias
Learning
Activation
Computation
🤯 Biggest Realization

The Input Layer is called a layer because it is a layer of data, not because it contains learning neurons.

It is simply the entry point of the network.

🔵 Hidden Layer

This is where the real work happens.

Every hidden neuron receives

✅ All outputs from the previous layer

Then performs

Weights × Inputs

↓

Add Bias

↓

Activation

↓

Output
🤯 Biggest Realization

Every neuron receives the same input vector.

Example

x₁
x₂
x₃
x₄

Neuron 1

↓

All 4 inputs

Neuron 2

↓

All 4 inputs

Neuron 3

↓

All 4 inputs

NOT

Neuron1 ← x₁

Neuron2 ← x₂

🚫 That's wrong.

🔴 Output Layer

Produces the final prediction.

Example

Cat

Dog

or

Spam

Not Spam
🧠 Hidden State

One of the most important concepts.

Suppose

Hidden Layer

○ ○ ○

Each neuron outputs

0.81

-0.24

0.55

The layer combines them into

[0.81, -0.24, 0.55]

This is called the

⭐ Hidden State
Biggest Realization

A Hidden State is simply

The collection (vector/list) of outputs from all neurons in a layer.

Nothing magical.

Just a list of numbers.

🧠 How Neurons Work Together

This completely changed your mental model.

Instead of thinking

Layer

↓

One neuron

Now you know

Layer

↓

Neuron 1

Neuron 2

Neuron 3

↓

Hidden State

Every neuron solves a tiny problem.

The layer combines all of their answers.

🧩 Representation Learning

Every layer creates a better representation.

Pixels

↓

Edges

↓

Shapes

↓

Eyes

↓

Face

↓

Person
Biggest Realization

The network never jumps directly from

Pixels

↓

Person

Instead,

every layer solves a slightly harder problem than the previous one.

🧮 Number of Weights

Golden Rule ⭐

Number of Inputs

=

Number of Weights

Always.

Example

4 Inputs

↓

Neuron

↓

4 Weights

If a layer has

4 Inputs

3 Neurons

then

Each neuron has

4 Weights

Total weights

4 × 3 = 12
Biggest Realization

Weights are NOT shared.

Every neuron owns its own private weights.

Neuron 1

[w₁ w₂ w₃ w₄]

Neuron 2

[w₅ w₆ w₇ w₈]

Neuron 3

[w₉ w₁₀ w₁₁ w₁₂]

That's why neurons learn different patterns.

🎲 Random Initialization

Every neuron starts with

random.uniform(-1,1)
Biggest Realization

Random weights are

❌ NOT learning.

They are simply

Initial guesses.

Learning comes later through Backpropagation.

Why Random?

Suppose every neuron started with

[0,0,0]

Every neuron would

produce the same output
receive the same error
update identically

They become clones.

😂

Random initialization breaks this symmetry.

🧠 Activation Functions

We learned an important distinction.

Many beginners think

Step Function

=

Activation Function

🚫 Wrong.

Correct view

Activation Functions

├── Step Function
├── Sigmoid
├── ReLU
├── Tanh
├── GELU

The Step Function is just one member of the activation family.

Biggest Realization

We intentionally postponed implementing activation functions.

Why?

Because the question

"Why sigmoid?"

is answered properly in the Backpropagation lesson.

We don't memorize.

We understand.

🧩 Forward Pass

This is the heart of Lesson 2.

Forward Pass means

Pushing data through the network to get a prediction.

No learning happens here.

Just computation.

Flow

Input

↓

Layer 1

↓

Hidden State

↓

Layer 2

↓

Prediction
Biggest Realization

The output of one layer becomes the input to the next layer.

This sentence is one of the golden rules of deep learning.

🧠 Variable Transformation

Initially

inputs = [1,0]

After Hidden Layer

inputs = [0.81,-0.25,1.10]

After Output Layer

inputs = [0.67]

Same variable.

Different representation.

🤯

🏗️ Software Architecture

We built everything ourselves.

🟢 Neuron

Responsibility

Compute

Weights × Inputs

+

Bias

Nothing else.

🔵 Layer

Responsibility

Create Neurons

↓

Ask every neuron to compute

↓

Collect outputs

↓

Return Hidden State

The Layer is the manager.

The neurons are the workers.

🔴 Network

Responsibility

Layer 1

↓

Layer 2

↓

Layer 3

↓

Prediction

The Network simply coordinates the layers.

🤯 Biggest Software Engineering Realization

Every class has one responsibility.

Neuron

↓

Computes
Layer

↓

Organizes Neurons
Network

↓

Organizes Layers

This is called Composition.

Small objects combine to build larger systems.

🏗️ Files We Built

📄 neuron.py

✅ Random Weights

✅ Bias

✅ Forward computation

📄 layer.py

✅ Creates multiple neurons

✅ Calls every neuron's forward()

✅ Returns the Hidden State

📄 network.py

✅ Stores layers

✅ Chains the forward pass

📄 playground.py

✅ Creates the network

✅ Runs the forward pass

✅ Lets us observe how data flows

🎯 Complete Forward Pass

When we execute

prediction = network.forward([1,0])

The computer thinks like this:

Network receives

[1,0]

↓

Hidden Layer

↓

Neuron 1 computes

↓

Neuron 2 computes

↓

Neuron 3 computes

↓

Hidden State

↓

Output Layer

↓

Output Neuron computes

↓

Prediction

↓

Return prediction

Nothing magical.

Just many tiny computations chained together.

💎 Biggest Realizations of Lesson 2 ⭐⭐⭐⭐⭐

🌟 A Neural Network is just many perceptrons working together.

🌟 One neuron = one output.

🌟 One layer = many neuron outputs = Hidden State.

🌟 The output of one layer becomes the input to the next layer.

🌟 Every neuron receives ALL outputs from the previous layer.

🌟 Number of Inputs = Number of Weights (Always).

🌟 Every neuron owns its own weights. They are never shared.

🌟 Random weights are just starting guesses, not learned knowledge.

🌟 The Input Layer doesn't learn—it only passes data into the network.

🌟 Forward Pass is pure computation. No learning happens here.

🌟 The Step Function is only one type of activation function.

🌟 Good software design separates responsibilities:

🧠 Neuron → Computes
🧩 Layer → Organizes neurons
🌐 Network → Organizes layers

🌟 Deep learning is simply a chain of small calculations, not one giant magical calculation.

🏆 Lesson 2 in One Sentence

A neural network is a collection of simple neurons organized into layers, where each layer transforms its input into a richer hidden representation, and the output of one layer becomes the input to the next until a final prediction is produced through the forward pass. 🚀