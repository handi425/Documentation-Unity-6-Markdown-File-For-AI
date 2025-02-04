[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimationStateMachines.html)
  * [中文](/cn/current/Manual/AnimationStateMachines.html)
  * [日本語](/ja/current/Manual/AnimationStateMachines.html)
  * [한국어](/kr/current/Manual/AnimationStateMachines.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimationStateMachines.html)
  * [中文](/cn/current/Manual/AnimationStateMachines.html)
  * [日本語](/ja/current/Manual/AnimationStateMachines.html)
  * [한국어](/kr/current/Manual/AnimationStateMachines.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * Animation State Machine

[](AnimatorWindow.html)

Animator Window

[](StateMachineBasics.html)

State Machine Basics

# Animation State Machine

It is common for a character or a **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to have several different
animations for the different actions it performs in a game. For example, a
character breathes and sways slightly when idle, walks when commanded, and
raises their arms when they fall from a platform. A door has animations for
when it opens, closes, jams, and when it gets broken open.

Mecanim uses a visual layout system, similar to a flowchart, to represent a
**state machine** The set of states in an Animator Controller that a character
or animated GameObject can be in, along with a set of transitions between
those states and a variable to remember the current state. The states
available will depend on the type of gameplay, but typical states include
things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine). You use this visual layout
system to control and arrange when to play the **animation clips** Animation
data that can be used for animated characters or simple animations. It is a
simple “unit” piece of motion, such as (one specific instance of) “Idle”,
“Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) for your character or
GameObject.

The following topics provide more details on Mecanim’s state machine:

  * [State Machine Basics](StateMachineBasics.html)
  * [Animation States](class-State.html)
  * [Animation Parameters](AnimationParameters.html)Used to communicate between scripting and the Animator Controller. Some parameters can be set in scripting and used by the controller, while other parameters are based on Custom Curves in Animation Clips and can be sampled using the scripting API. [More info](AnimationParameters.html)  
See in [Glossary](Glossary.html#AnimationParameters)

  * [State Machine Transitions](StateMachineTransitions.html)
  * [Animation Transitions](class-Transition.html)Allows a state machine to switch or blend from one animation state to another. Transitions define how long a blend between states should take, and the conditions that activate them. [More info](StateMachineTransitions.html)  
See in [Glossary](Glossary.html#AnimationTransition)

  * [Animation Blend Trees](class-BlendTree.html)Used for continuous blending between similar Animation Clips based on float Animation Parameters. [More info](class-BlendTree.html)  
See in [Glossary](Glossary.html#AnimationBlendTree)

  * [State Machine Behaviours](StateMachineBehaviours.html)A script that attaches to a state within a state machine to control what happens when the state machine enters, exits or remains within a state, such as play sounds as states are entered. [More info](StateMachineBehaviours.html)  
See in [Glossary](Glossary.html#StateMachineBehaviour)

  * [Sub-State Machines](NestedStateMachines.html)
  * [Animation Layers](AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](AnimationLayers.html)  
See in [Glossary](Glossary.html#AnimationLayer)

  * [State Machine Solo and Mute](AnimationSoloMute.html)
  * [Target Matching](TargetMatching.html)A scripting function that allows you to move characters in such a way that a hand or foot lands in a certain place at a certain time. For example, the character may need to jump across stepping stones or jump and grab an overhead beam. [More info](TargetMatching.html)  
See in [Glossary](Glossary.html#Targetmatching)

[](AnimatorWindow.html)

Animator Window

[](StateMachineBasics.html)

State Machine Basics

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

