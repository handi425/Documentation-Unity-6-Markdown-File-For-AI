[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimationSoloMute.html)
  * [中文](/cn/current/Manual/AnimationSoloMute.html)
  * [日本語](/ja/current/Manual/AnimationSoloMute.html)
  * [한국어](/kr/current/Manual/AnimationSoloMute.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimationSoloMute.html)
  * [中文](/cn/current/Manual/AnimationSoloMute.html)
  * [日本語](/ja/current/Manual/AnimationSoloMute.html)
  * [한국어](/kr/current/Manual/AnimationSoloMute.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * State Machine Solo and Mute

[](AnimationLayers.html)

Animation Layers

[](TargetMatching.html)

Target Matching

# State Machine Solo and Mute

In complex **state machines** The set of states in an Animator Controller that
a character or animated GameObject can be in, along with a set of transitions
between those states and a variable to remember the current state. The states
available will depend on the type of gameplay, but typical states include
things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine), it is useful to preview the
operation of some parts of the machine separately. For this, you can use the
**Mute** and **Solo** functionality:

  * **Mute** disables a transition.
  * **Solo** plays only that transition.

You can set up multiple **Solo** transitions to play only those that have Solo
enabled. If one transition has **Solo** enabled, Unity enables **Mute** on the
other transitions. If both **Solo** and **Mute** are enabled, then **Mute**
takes precedence.

You can set up **Mute** and **Solo** states either from the **Transition
Inspector** , or the **State Inspector** , which provides an overview of all
transitions from that state.

![](../uploads/Main/MecanimSoloMuteInspector.png)

Unity displays **Solo** transitions in green, and **Mute** transitions in red:

![](../uploads/Main/MecanimSoloMuteGraph.png)

In the example above, if you are in `State 0`, only transitions to `State A`
and `State B` are available.

Known issues:

  * The Controller graph doesn’t always reflect the internal Mute states of the engine.

[](AnimationLayers.html)

Animation Layers

[](TargetMatching.html)

Target Matching

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

