[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StateMachineBasics.html)
  * [中文](/cn/current/Manual/StateMachineBasics.html)
  * [日本語](/ja/current/Manual/StateMachineBasics.html)
  * [한국어](/kr/current/Manual/StateMachineBasics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StateMachineBasics.html)
  * [中文](/cn/current/Manual/StateMachineBasics.html)
  * [日本語](/ja/current/Manual/StateMachineBasics.html)
  * [한국어](/kr/current/Manual/StateMachineBasics.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * State Machine Basics

[](AnimationStateMachines.html)

Animation State Machine

[](class-State.html)

Animation States

# State Machine Basics

The basic idea is that a character is engaged in some particular kind of
action at any given time. The actions available will depend on the type of
gameplay but typical actions include things like idling, walking, running,
jumping, etc. These actions are referred to as **states** , in the sense that
the character is in a “state” where it is walking, idling or whatever. In
general, the character will have restrictions on the next state it can go to
rather than being able to switch immediately from any state to any other. For
example, a running jump can only be taken when the character is already
running and not when it is at a standstill, so it should never switch straight
from the idle state to the running jump state. The options for the next state
that a character can enter from its current state are referred to as **[state
transitions](class-Transition.html)**. Taken together, the set of states, the
set of transitions and the variable to remember the current state form a
**state machine**.

The states and transitions of a state machine can be represented using a graph
diagram, where the nodes represent the states and the arcs (arrows between
nodes) represent the transitions. You can think of the current state as being
a marker or highlight that is placed on one of the nodes and can then only
jump to another node along one of the arrows.

![](../uploads/Main/StateMachineDiagram.png)

The importance of state machines for animation is that they can be designed
and updated quite easily with relatively little coding. Each state has a
Motion associated with it that will play whenever the machine is in that
state. This enables an animator or designer to define the possible sequences
of character actions and animations without being concerned about how the code
will work.

## State Machines

Unity’s **Animation State Machines** A graph within an Animator Controller
that controls the interaction of Animation States. Each state references an
Animation Blend Tree or a single Animation Clip. [More
info](AnimationStateMachines.html)  
See in [Glossary](Glossary.html#AnimationStateMachine) provide a way to
overview all of the **animation clips** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) related to a particular
character and allow various events in the game (for example user input) to
trigger different animations.

Animation State Machines can be set up from the [Animator Controller
Window](Animator.html), and they look something like this:

![](../uploads/Main/MecanimStateMachine.png)

State Machines consist of **States** , **Transitions** The blend from one
state to another in a state machine, such as transitioning a character from a
walk to a jog animation. Transitions define how long the blend between states
should take, and the conditions that activate the blend. [More info](class-
Transition.html)  
See in [Glossary](Glossary.html#Transition) and **Events** and smaller Sub-
State Machines can be used as components in larger machines. See the reference
pages for [Animation States](class-State.html) and [Animation
Transitions](class-Transition.html)Allows a state machine to switch or blend
from one animation state to another. Transitions define how long a blend
between states should take, and the conditions that activate them. [More
info](StateMachineTransitions.html)  
See in [Glossary](Glossary.html#AnimationTransition) for further information.

[](AnimationStateMachines.html)

Animation State Machine

[](class-State.html)

Animation States

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

