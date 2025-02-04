[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/BlendTree-AdditionalOptions.html)
  * [中文](/cn/current/Manual/BlendTree-AdditionalOptions.html)
  * [日本語](/ja/current/Manual/BlendTree-AdditionalOptions.html)
  * [한국어](/kr/current/Manual/BlendTree-AdditionalOptions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/BlendTree-AdditionalOptions.html)
  * [中文](/cn/current/Manual/BlendTree-AdditionalOptions.html)
  * [日本語](/ja/current/Manual/BlendTree-AdditionalOptions.html)
  * [한국어](/kr/current/Manual/BlendTree-AdditionalOptions.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * [Animation Blend Trees](class-BlendTree.html)
  * Common Blend Tree Options

[](BlendTree-DirectBlending.html)

Direct blending

[](StateMachineBehaviours.html)

State Machine Behaviours

# Common Blend Tree Options

The options in this topic are common to both 1D and 2D blending.

## Time Scale

You can alter the “natural” speed of **animation clips** Animation data that
can be used for animated characters or simple animations. It is a simple
“unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or
“Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) with the animation speed number
fields (the columns with a clock icon). For example, to double the speed of a
walk clip, specify a value of `2.0`.

To rescale the speed of each clip in the motions list relative to the minimum
and maximum values, Select **Adjust Time Scale** > **Homogeneous Speed**. This
preserves the initial relative speed of each clip.

**Note** : The **Adjust Time Scale** is only available if all the clips are
animation clips and not child Blend Trees.

## Mirroring

Enable the Mirror checkbox to mirror any **humanoid Animation** An animation
using humanoid skeletons. Humanoid models generally have the same basic
structure, representing the major articulate parts of the body, head and
limbs. This makes it easy to map animations from one humanoid skeleton to
another, allowing retargeting and inverse kinematics. [More
info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Humanoidanimation) Clip in the motions list.
Mirroring uses the same animation as its unmirrored original without doubling
the memory and space.

However, mirroring an animation in a blend tree does not create a fully
symmetrical animation. Unity automatically adds offsets to ensure that run
cycles, walk cycles, and animations such as footsteps are blended correctly
with other animation clips and blend trees. For example, if your blend tree
has a humanoid running left, and you enable Mirror to switch the humanoid to
run right, the foot cycles need to match so that the left foot touches the
ground at the same time. This ensures that the mirrored Blend tree correctly
blends with surrounding clips and other blend trees that have not been
mirrored.

[](BlendTree-DirectBlending.html)

Direct blending

[](StateMachineBehaviours.html)

State Machine Behaviours

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

