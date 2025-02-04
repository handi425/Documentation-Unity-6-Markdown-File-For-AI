[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Splittinganimations.html)
  * [中文](/cn/current/Manual/Splittinganimations.html)
  * [日本語](/ja/current/Manual/Splittinganimations.html)
  * [한국어](/kr/current/Manual/Splittinganimations.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Splittinganimations.html)
  * [中文](/cn/current/Manual/Splittinganimations.html)
  * [日本語](/ja/current/Manual/Splittinganimations.html)
  * [한국어](/kr/current/Manual/Splittinganimations.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * [Model Import Settings window](class-FBXImporter.html)
  * [Animation tab](class-AnimationClip.html)
  * Extracting animation clips

[](AnimationEulerCurveImport.html)

Euler curve resampling

[](LoopingAnimationClips.html)

Loop optimization on Animation clips

# Extracting animation clips

An animated character typically has a number of different movements that are
activated in the game in different circumstances, called [Animation
Clips](class-AnimationClip.html)Animation data that can be used for animated
characters or simple animations. It is a simple “unit” piece of motion, such
as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-
AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). For example, we might have
separate animation clips for walking, running, jumping, throwing, and dying.
Depending on how the artist set up the animation in the 3D modeling
application, these separate movements might be imported as distinct animation
clips or as one single clip where each movement simply follows on from the
previous one. In cases where there is only one long clip, you can extract
component animation clips inside Unity, which adds a few extra steps to your
workflow.

If your model has multiple animations that you already defined as individual
clips, the [Animations tab](class-AnimationClip.html) looks like this:

![Model file with several animation clips
defined](../uploads/Main/MecanimImportPreSplitAnimation.png) Model file with
several animation clips defined

You can preview any of the clips that appear in the list. If you need to, you
can edit the time ranges of the clips.

If your model has multiple animations supplied as one continuous take, the
**Animation** tab looks like this:

![Model file with one long continous animation
clip](../uploads/Main/MecanimImportAnimationNoSplit.png) Model file with one
long continous animation clip

In this case, you can define the time ranges (frames or seconds) that
correspond to each of the separate animation sequences (walking, jumping,
running, and idling). You can create a new animation clip by following these
steps:

  1. Click the add (`+`) button.
  2. Select the range of frames or seconds that it includes.
  3. You can also change the name of the clip.

For example, you could define the following:

  * walk forward animation during frames 71–77
  * idle during frames 170–200
  * hit animation during frames 250–280

For further information, see the [Animation tab](class-AnimationClip.html).

## Importing animations using multiple model files

Another way to import animations is to follow a naming scheme that Unity
allows for the animation files. You can create separate **model files** A file
containing a 3D data, which may include definitions for meshes, bones,
animation, materials and textures. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#Modelfile) and name them with the convention
`modelName@animationName.fbx`. For example, for a model called `goober`, you
could import separate idle, walk, jump and walljump animations using files
named `goober@idle.fbx`, `goober@walk.fbx`, `goober@jump.fbx` and
`goober@walljump.fbx`. When exporting animation like this, it is unnecessary
to include the **Mesh** The main graphics primitive of Unity. Meshes make up a
large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) in these files, but in that case you
should enable the [Preserve Hierarchy Model import option](FBXImporter-
Model.html).

![An example of four animation files for an animated
character](../uploads/Main/animation_at_naming.png) An example of four
animation files for an animated character

Unity automatically imports all four files and collects all animations to the
file without the @ sign in. In the example above, Unity imports the
`goober.mb` file with references to the `idle`, `jump`, `walk` and `wallJump`
animations automatically.

For FBX files, you can export the Mesh in a Model file without its animation.
Then export the four clips as `goober@_animname_.fbx` by exporting the desired
**keyframes** A frame that marks the start or end point of a transition in an
animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) for each (enable animation in the
FBX dialog).

[](AnimationEulerCurveImport.html)

Euler curve resampling

[](LoopingAnimationClips.html)

Loop optimization on Animation clips

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

