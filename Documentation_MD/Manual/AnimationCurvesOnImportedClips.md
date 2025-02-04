[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimationCurvesOnImportedClips.html)
  * [中文](/cn/current/Manual/AnimationCurvesOnImportedClips.html)
  * [日本語](/ja/current/Manual/AnimationCurvesOnImportedClips.html)
  * [한국어](/kr/current/Manual/AnimationCurvesOnImportedClips.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimationCurvesOnImportedClips.html)
  * [中文](/cn/current/Manual/AnimationCurvesOnImportedClips.html)
  * [日本語](/ja/current/Manual/AnimationCurvesOnImportedClips.html)
  * [한국어](/kr/current/Manual/AnimationCurvesOnImportedClips.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * [Model Import Settings window](class-FBXImporter.html)
  * [Animation tab](class-AnimationClip.html)
  * Curves

[](LoopingAnimationClips.html)

Loop optimization on Animation clips

[](AnimationEventsOnImportedClips.html)

Events

# Curves

You can attach **animation curves** to imported **animation clips** Animation
data that can be used for animated characters or simple animations. It is a
simple “unit” piece of motion, such as (one specific instance of) “Idle”,
“Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) in the [Animation tab](class-
AnimationClip.html).

You can use these curves to add additional animated data to an imported clip.
You can use that data to animate the timings of other items based on the state
of an animator. For example, in a game set in icy conditions, an extra
animation curve could be used to control the emission rate of a **particle
system** A component that simulates fluid entities such as liquids, clouds and
flames by generating and animating large numbers of small 2D images in the
scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) to show the player’s
condensing breath in the cold air.

To add a curve to an imported animation, expand the **Curves** section at the
bottom of the [Animation tab](class-AnimationClip.html), and click the plus
icon to add a new curve to the current animation clip:

![The expanded Curves section on the Animation
tab](../uploads/Main/classAnimationClip-Curves.png) The expanded Curves
section on the Animation tab

If your imported animation file is split into multiple animation clips, each
clip can have its own custom curves.

![The curves on an imported animation clip](../uploads/Main/MecanimCurves.png)
The curves on an imported animation clip

The curve’s X-axis represents _normalized time_ and always ranges between 0.0
and 1.0 (corresponding to the beginning and the end of the animation clip
respectively, regardless of its duration).

![Unity Curve Editor](../uploads/Main/CurveEditorPopupDescr.png) Unity Curve
Editor

**(A)** Wrapping mode

**(B)** Curve Presets

Double-clicking an animation curve brings up the [standard Unity curve
editor](EditingCurves.html) which you can use to add **keys** to the curve.
Keys are points along the curve’s timeline where it has a value explicitly set
by the animator rather than just using an interpolated value. Keys are very
useful for marking important points along the timeline of the animation. For
example, with a walking animation, you might use keys to mark the points where
the left foot is on the ground, then both feet on the ground, right foot on
the ground, and so on. Once the keys are set up, you can move conveniently
between key frames by pressing the **Previous Key Frame** and **Next Key
Frame** buttons. This moves the vertical red line and shows the _normalized
time_ at the **keyframe** A frame that marks the start or end point of a
transition in an animation. Frames in between the keyframes are called
inbetweens.  
See in [Glossary](Glossary.html#keyframe). The value you enter in the text box
drives the value of the curve at that time.

## Animation curves and animator controller parameters

If you have a curve with the same name as one of the
[parameters](AnimationParameters.html) in the [Animator
Controller](Animator.html)Controls animation through Animation Layers with
Animation State Machines and Animation Blend Trees, controlled by Animation
Parameters. The same Animator Controller can be referenced by multiple models
with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), then that parameter takes
its value from the value of the curve at each point in the timeline. For
example, if you make a call to
[GetFloat](../ScriptReference/Animator.GetFloat.html) from a script, the
returned value is equal to the value of the curve at the time the call is
made. Note that at any given point in time, there might be multiple animation
clips attempting to set the same parameter from the same controller. In that
case, Unity blends the curve values from the multiple animation clips. If an
animation has no curve for a particular parameter, then Unity blends with the
default value for that parameter.

[](LoopingAnimationClips.html)

Loop optimization on Animation clips

[](AnimationEventsOnImportedClips.html)

Events

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

