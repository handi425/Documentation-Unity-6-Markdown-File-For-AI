[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-State.html)
  * [中文](/cn/current/Manual/class-State.html)
  * [日本語](/ja/current/Manual/class-State.html)
  * [한국어](/kr/current/Manual/class-State.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-State.html)
  * [中文](/cn/current/Manual/class-State.html)
  * [日本語](/ja/current/Manual/class-State.html)
  * [한국어](/kr/current/Manual/class-State.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * Animation States

[](StateMachineBasics.html)

State Machine Basics

[](AnimationParameters.html)

Animation Parameters

# Animation States

**Animation States** are the basic building blocks of an **Animation**State
Machine** The set of states in an Animator Controller that a character or
animated GameObject can be in, along with a set of transitions between those
states and a variable to remember the current state. The states available will
depend on the type of gameplay, but typical states include things like idling,
walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine)**. Each state contains an
animation sequence (or [blend tree](class-BlendTree.html)) that plays when the
character is in that state. Select the state in the ****Animator Controller**
Controls animation through Animation Layers with Animation State Machines and
Animation Blend Trees, controlled by Animation Parameters. The same Animator
Controller can be referenced by multiple models with Animator components.
[More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController)**, to view the properties
for the state in the **Inspector** A Unity window that displays information
about the currently selected GameObject, asset or project settings, allowing
you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

![](../uploads/Main/anim-insp-state-properties.png) **_Property:_** | **_Description:_**  
---|---  
**Motion** | The **animation clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) or blend tree assigned to this
state.  
**Speed** | The default speed of the motion for this state. Enable Parameter to modify the speed with a custom value from a script. For example, you can multiply the speed with a custom value to decelerate or accelerate the play speed.  
**Motion Time** | The time used to play the motion for this state. Enable Parameter to control the motion time with a custom value from a script.  
**Mirror** | This property only applies to states with **humanoid animation** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Humanoidanimation). Enable to mirror the
animation for this state. Enable Parameter to enable or disable mirroring from
a script.  
**Cycle Offset** | The offset added to the state time of the motion. This offset does not affect the Motion Time. Enable Parameter to specify the Cycle Offset from a script.  
**Foot IK** | This property only applies to states with humanoid animation. Enable to respect Foot IK for this state.  
**Write Defaults** | Whether the AnimatorStates writes the default values for properties that are not animated by its motion.  
**Transitions** | The list of transitions originating from this state.  
  
The default state, displayed in brown, is the state that the machine will be
in when it is first activated. You can change the default state, if necessary,
by right-clicking on another state and selecting **Set As Default** from the
context menu. The **Solo** and **Mute** checkboxes on each transition are used
to control the behaviour of **animation previews**. Refer to [this
page](AnimationSoloMute.html) for further details.

A new state can be added by right-clicking on an empty space in the **Animator
Controller Window** and selecting **Create State- >Empty** from the context
menu. Alternatively, you can drag an animation into the Animator Controller
Window to create a state containing that animation. (Note that you can only
drag Mecanim animations into the Controller. Non-Mecanim animations will be
rejected.) States can also contain [Blend Trees](class-BlendTree.html).

## Any State

**Any State** is a special state which is always present. It exists for the
situation where you want to go to a specific state regardless of which state
you are currently in. This is a shorthand way of adding the same outward
transition to all states in your machine. Note that the special meaning of
**Any State** implies that it cannot be the end point of a transition (for
example, jumping to “any state” cannot be used as a way to pick a random state
to enter next).

![](../uploads/Main/AnyState.png)

[](StateMachineBasics.html)

State Machine Basics

[](AnimationParameters.html)

Animation Parameters

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

