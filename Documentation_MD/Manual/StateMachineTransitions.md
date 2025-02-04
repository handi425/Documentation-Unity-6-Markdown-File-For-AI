[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StateMachineTransitions.html)
  * [中文](/cn/current/Manual/StateMachineTransitions.html)
  * [日本語](/ja/current/Manual/StateMachineTransitions.html)
  * [한국어](/kr/current/Manual/StateMachineTransitions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StateMachineTransitions.html)
  * [中文](/cn/current/Manual/StateMachineTransitions.html)
  * [日本語](/ja/current/Manual/StateMachineTransitions.html)
  * [한국어](/kr/current/Manual/StateMachineTransitions.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * State Machine Transitions

[](AnimationParameters.html)

Animation Parameters

[](class-Transition.html)

Animation transitions

# State Machine Transitions

State Machine Transitions exist to help you simplify large or complex State
Machines. They allow you to have a higher level of abstraction over the
**state machine** The set of states in an Animator Controller that a character
or animated GameObject can be in, along with a set of transitions between
those states and a variable to remember the current state. The states
available will depend on the type of gameplay, but typical states include
things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) logic.

Each view in the **animator window** The window where the Animator Controller
is visualized and edited. [More info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow) has an Entry and Exit node.
These are used during State Machine Transitions.

The Entry node is used when transitioning into a state machine. The entry node
will be evaluated and will branch to the destination state according to the
conditions set. In this way the entry node can control which state the state
machine begins in, by evaluating the state of your parameters when the state
machine begins.

Because state machines always have a default state, there will always be a
default transition branching from the entry node to the default state.

![An entry node with a single default entry
transition](../uploads/Main/AnimatorEntryNodeSingleTransition.png) An entry
node with a single default entry transition

You can then add additional transitions from the Entry node to other states,
to control whether the state machine should begin in a different state.

![An entry node with a multiple entry
transitions](../uploads/Main/AnimatorEntryNodeMultipleTransitions.png) An
entry node with a multiple entry transitions

The Exit node is used to indicate that a state machine should exit.

Each sub-state within a state machine is considered a separate and complete
state machine, so by using these entry and exit nodes, you can control the
flow from a top-level state machine into its sub-state machines more
elegantly.

It is possible to mix state machine transitions with regular state
transitions, so it is possible to transition from state to state, from a state
to a statemachine, and from one statemachine directly to another statemachine.

[](AnimationParameters.html)

Animation Parameters

[](class-Transition.html)

Animation transitions

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

