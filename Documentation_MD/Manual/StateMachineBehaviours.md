[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StateMachineBehaviours.html)
  * [中文](/cn/current/Manual/StateMachineBehaviours.html)
  * [日本語](/ja/current/Manual/StateMachineBehaviours.html)
  * [한국어](/kr/current/Manual/StateMachineBehaviours.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StateMachineBehaviours.html)
  * [中文](/cn/current/Manual/StateMachineBehaviours.html)
  * [日本語](/ja/current/Manual/StateMachineBehaviours.html)
  * [한국어](/kr/current/Manual/StateMachineBehaviours.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * State Machine Behaviours

[](BlendTree-AdditionalOptions.html)

Common Blend Tree Options

[](NestedStateMachines.html)

Sub-State Machines

# State Machine Behaviours

A **State Machine** The set of states in an Animator Controller that a
character or animated GameObject can be in, along with a set of transitions
between those states and a variable to remember the current state. The states
available will depend on the type of gameplay, but typical states include
things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) Behaviour is a special class of
script. In a similar way to attaching regular Unity **scripts** A piece of
code that allows you to create your own Components, trigger game events,
modify Component properties over time and respond to user input in any way you
like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) (MonoBehaviours) to individual
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject), you can attach a
StateMachineBehaviour script to an individual state within a state machine.
This allows you to write code that will execute when the state machine enters,
exits or remains within a particular state. This means you do not have to
write your own logic to test for and detect changes in state.

A few examples for the use of this feature might be to:

  * Play sounds as states are entered or exited
  * Perform certain tests (eg, ground detection) only when in appropriate states
  * Activate and control special effects associated with specific states

State Machine Behaviours can be created and added to states in a very similar
way to the way you would create and add scripts to GameObjects. Select a state
in your state machine, and then in the **inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) use the “Add Behaviour” button to
select an existing StateMachineBehaviour or create a new one.

![A state machine with a behaviour attached to the Grounded
state](../uploads/Main/StateMachineBehaviourAttached.png) A state machine with
a behaviour attached to the “Grounded” state

State Machine Behaviour scripts have access to a number of events that are
called when the Animator enters, updates and exits different states (or sub-
state machines). There are also events which allow you to handle the **Root
motion** Motion of character’s root node, whether it’s controlled by the
animation itself or externally. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootMotion) and Inverse **Kinematics** The
geometry that describes the position and orientation of a character’s joints
and bodies. Used by inverse kinematics to control character movement.  
See in [Glossary](Glossary.html#kinematics) calls.

For more information see the [State Machine
Behaviour](../ScriptReference/StateMachineBehaviour.html) script reference.

[](BlendTree-AdditionalOptions.html)

Common Blend Tree Options

[](NestedStateMachines.html)

Sub-State Machines

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

