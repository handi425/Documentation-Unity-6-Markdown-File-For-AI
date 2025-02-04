[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LoopingAnimationClips.html)
  * [中文](/cn/current/Manual/LoopingAnimationClips.html)
  * [日本語](/ja/current/Manual/LoopingAnimationClips.html)
  * [한국어](/kr/current/Manual/LoopingAnimationClips.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LoopingAnimationClips.html)
  * [中文](/cn/current/Manual/LoopingAnimationClips.html)
  * [日本語](/ja/current/Manual/LoopingAnimationClips.html)
  * [한국어](/kr/current/Manual/LoopingAnimationClips.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * [Model Import Settings window](class-FBXImporter.html)
  * [Animation tab](class-AnimationClip.html)
  * Loop optimization on Animation clips

[](Splittinganimations.html)

Extracting animation clips

[](AnimationCurvesOnImportedClips.html)

Curves

# Loop optimization on Animation clips

A common operation for people working with animations is to make sure they
loop properly. For example, if a character is walking down a path, the walking
motion comes from an **Animation clip** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). The motion might last for only
10 frames but that motion plays in a continuous loop. In order to make the
walking motion seamless, it must begin and end in a similar pose. This ensures
there is no foot sliding or strange jerky motions.

Animation clips can loop on pose, rotation, and position. Using the example of
the walk cycle, you want the start and end points for **Root Transform** The
Transform at the top of a hierarchy of Transforms. In a Prefab, the Root
Transform is the topmost Transform in the Prefab. In an animated humanoid
character, the Root Transform is a projection on the Y plane of the Body
Transform and is computed at run time. At every frame, a change in the Root
Transform is computed, and then this is applied to the GameObject to make it
move. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootTransform) Rotation and Root Transform
Position in Y to match. You don’t want to match the start and end points for
the Root Transform Position in XZ, because your character would never get
anywhere if its feet keep returning to their horizontal pose.

Unity provides match indicators and a set of special loop optimization graphs
under the clip-specific import settings on the Animation tab. These provide
visual cues to help you optimize where to clip the motion for each value.

To optimize whether the looping motion begins and ends optimally, you can view
and edit the looping match curves.

## Viewing loop optimization graphs

In this example, the looping motion displays bad matches for the clip ranges,
shown by the red and yellow indicators:

![Red and yellow indicators show bad matches for
looping](../uploads/Main/MecanimAnimClipRed.png) Red and yellow indicators
show bad matches for looping

To see the loop optimization graphs, click and hold either the start or end
indicator on the timeline. The **Based Upon** and **Offset** values disappear
and one curve for each loop basis appears:

![Looping graphs for bad
matches](../uploads/Main/MecanimAnimClipLoopingRed.png) Looping graphs for bad
matches

## Optimizing looping matches

Click and drag the start or end point of the Animation Clip until the point
appears on the graph where the property is green. Unity draws the graph in
green where it is more likely that the clip can loop properly.

![Position start and end points where the graph is
green](../uploads/Main/MecanimAnimClipLoopingGreen.png) Position start and end
points where the graph is green

When you let go of the mouse button, the graphs disappear but the indicators
remain:

![Green indicators show good matches for
looping](../uploads/Main/MecanimAnimClipGreen.png) Green indicators show good
matches for looping

[](Splittinganimations.html)

Extracting animation clips

[](AnimationCurvesOnImportedClips.html)

Curves

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

