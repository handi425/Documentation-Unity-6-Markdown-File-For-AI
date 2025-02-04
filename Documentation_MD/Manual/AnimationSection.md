[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimationSection.html)
  * [中文](/cn/current/Manual/AnimationSection.html)
  * [日本語](/ja/current/Manual/AnimationSection.html)
  * [한국어](/kr/current/Manual/AnimationSection.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimationSection.html)
  * [中文](/cn/current/Manual/AnimationSection.html)
  * [日本語](/ja/current/Manual/AnimationSection.html)
  * [한국어](/kr/current/Manual/AnimationSection.html)

  * Animation

[](multiplayer-center.html)

Use the Multiplayer Center

[](AnimationOverview.html)

Mecanim Animation system

# Animation

Unity’s Animation system includes **retargeting** Applying animations created
for one model to another. [More info](Retargeting.html)  
See in [Glossary](Glossary.html#Retargeting) animation, controlling animation
weights at runtime, adding **animation events** Allows you to add data to an
imported clip which determines when certain actions should occur in time with
the animation. For example, for an animated character you might want to add
events to walk and run cycles to indicate when the footstep sounds should
play. [More info](AnimationEventsOnImportedClips.html)  
See in [Glossary](Glossary.html#AnimationEvent) to **animation clips**
Animation data that can be used for animated characters or simple animations.
It is a simple “unit” piece of motion, such as (one specific instance of)
“Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip), constructing **state machine**
The set of states in an Animator Controller that a character or animated
GameObject can be in, along with a set of transitions between those states and
a variable to remember the current state. The states available will depend on
the type of gameplay, but typical states include things like idling, walking,
running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) hierarchies and transitions,
importing blend shapes for facial animations, and much more.

![Animation in Unity](../uploads/Main/AnimationIntroPic.jpg) Animation in
Unity

Unity has two animation systems with different capabilities and performance
characteristics:

**Animation system** | **Description**  
---|---  
**[Mecanim Animation system](AnimationOverview.html)** | The Mecanim animation system (Mecanim) is a rich and sophisticated animation system that uses the [Animator component](class-Animator.html)A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent), the [Animation
window](AnimationEditorGuide.html), and the [Animator
window](AnimatorWindow.html)The window where the Animator Controller is
visualized and edited. [More info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow). Mecanim is the recommended
animation system for most situations. It provides better performance for
complex character animation with many [animation
curves](AnimationCurvesOnImportedClips.html)Allows you to add data to an
imported clip so you can animate the timings of other items based on the state
of an animator. For example, for a game set in icy conditions, you could use
an extra animation curve to control the emission rate of a particle system to
show the player’s condensing breath in the cold air. [More
info](AnimationCurvesOnImportedClips.html)  
See in [Glossary](Glossary.html#AnimationCurves) and [blending](class-
BlendTree.html).  
**[Legacy Animation system](Animations.html)** | Unity’s Legacy animation system (Legacy) has a limited **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset) that predates Mecanim. Legacy is
still available because it’s easier to use for simpler animations. Legacy is
also available for backwards compatibility with old Unity projects. Legacy
uses the [Animation component](class-Animation.html) and the special
**Legacy** import option when [importing legacy animation](animations.html).  
  
## Additional resources

  * [Related animation tutorials](http://unity3d.com/learn/tutorials/topics/animation)
  * [Knowledge Base Animation section](https://support.unity3d.com/hc/en-us/sections/201271005-Animation)

[](multiplayer-center.html)

Use the Multiplayer Center

[](AnimationOverview.html)

Mecanim Animation system

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

