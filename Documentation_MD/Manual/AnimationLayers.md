[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimationLayers.html)
  * [中文](/cn/current/Manual/AnimationLayers.html)
  * [日本語](/ja/current/Manual/AnimationLayers.html)
  * [한국어](/kr/current/Manual/AnimationLayers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimationLayers.html)
  * [中文](/cn/current/Manual/AnimationLayers.html)
  * [日本語](/ja/current/Manual/AnimationLayers.html)
  * [한국어](/kr/current/Manual/AnimationLayers.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * Animation Layers

[](NestedStateMachines.html)

Sub-State Machines

[](AnimationSoloMute.html)

State Machine Solo and Mute

# Animation Layers

Unity uses **Animation Layers** for managing complex **state machines** The
set of states in an Animator Controller that a character or animated
GameObject can be in, along with a set of transitions between those states and
a variable to remember the current state. The states available will depend on
the type of gameplay, but typical states include things like idling, walking,
running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) for different body parts. An
example of this is if you have a lower-body layer for walking-jumping, and an
upper-body layer for throwing objects / shooting.

You can manage animation layers from the **Layers Widget** in the top-left
corner of the **Animator Controller** Controls animation through Animation
Layers with Animation State Machines and Animation Blend Trees, controlled by
Animation Parameters. The same Animator Controller can be referenced by
multiple models with Animator components. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController).

![](../uploads/Main/MecanimAnimationLayers.png)

Clicking the gear wheel on the right of the window shows you the settings for
this layer.

![](../uploads/Main/MecanimAnimationLayers2.png)

On each layer, you can specify the mask and the Blending type. The mask
specifies the body parts on which to apply the animation. The Blending type
specifies how the animation is applied.

  * Select **Override** to use the animation on this layer, replacing the animation on previous layers.
  * Select **Additive** to add the animation on this layer on top of the animation from previous layers.   
For additive blending to be successful, the animation on the additive layer
must contain the same properties as the previous layers.

Add a new layer by pressing the **+** above the widget.

The **Mask** property is there to [specify the mask used on this layer](class-
AvatarMask.html). For example if you wanted to play a throwing animation on
just the upper body of your model, while having your character also able to
walk, run or stand still at the same time, you would use a mask on the layer
which plays the throwing animation where the upper body sections are defined,
like this:

![](../uploads/Main/AnimatorMaskOnLayer.png)

An ‘M’ symbol in the Layers sidebar indicates that the layer has a mask
applied.

## Animation Layer syncing

Sometimes it is useful to be able to re-use the same state machine in
different layers. For example if you want to simulate “wounded” behavior, and
have “wounded” animations for walk / run / jump instead of the “healthy” ones.
You can click the **Sync** checkbox on one of your layers, and then select the
layer you want to sync with. The state machine structure will then be the
same, but the actual **animation clips** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) used by the states will be
distinct.

This means the Synced layer does not have its own state machine definition at
all - instead, it is an instance of the source of the synced layer. Any
changes you make to the layout or structure of the state machine in the synced
layer view (eg, adding/deleting states or transitions) is done to the source
of the synced layer. The only changes that are unique to the synced layer are
the selected animations used within each state.

The Timing checkbox allows the animator to adjust how long each animation in
synced layers takes, determined by the weight. If Timing is unselected then
animations on the synced layer will be adjusted. The adjustment will be
stretched to the length of the animation on the original layer. If the option
is selected the animation length will be a balance for both animations, based
on weight. In both cases (chosen and not chosen) the animator adjusts the
length of the animations. If not chosen then the original layer is the sole
master. If chosen, it is then a compromise.

![In this view, the Fatigued layer is synced with the base layer. The state
machine structure is the same as the base layer, and the individual animations
used within each state are swapped for different but appropriate equivalent
animations.](../uploads/Main/AnimatorSyncedLayer.png) In this view, the
“Fatigued” layer is synced with the base layer. The state machine structure is
the same as the base layer, and the individual animations used within each
state are swapped for different but appropriate equivalent animations.

An ‘S’ symbol in the Layers sidebar indicates that the layer is a synced
layer.

[](NestedStateMachines.html)

Sub-State Machines

[](AnimationSoloMute.html)

State Machine Solo and Mute

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

