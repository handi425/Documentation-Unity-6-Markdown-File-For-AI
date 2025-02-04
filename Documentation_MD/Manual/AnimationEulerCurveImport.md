[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimationEulerCurveImport.html)
  * [中文](/cn/current/Manual/AnimationEulerCurveImport.html)
  * [日本語](/ja/current/Manual/AnimationEulerCurveImport.html)
  * [한국어](/kr/current/Manual/AnimationEulerCurveImport.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimationEulerCurveImport.html)
  * [中文](/cn/current/Manual/AnimationEulerCurveImport.html)
  * [日本語](/ja/current/Manual/AnimationEulerCurveImport.html)
  * [한국어](/kr/current/Manual/AnimationEulerCurveImport.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * [Model Import Settings window](class-FBXImporter.html)
  * [Animation tab](class-AnimationClip.html)
  * Euler curve resampling

[](class-AnimationClip.html)

Animation tab

[](Splittinganimations.html)

Extracting animation clips

# Euler curve resampling

Rotations in 3D applications are usually represented as **Quaternions**
Unity’s standard way of representing rotations as data. When writing code that
deals with rotations, you should usually use the Quaternion class and its
methods. [More info](QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](Glossary.html#Quaternion) or Euler angles. For the most
part, Unity represents rotations as Quaternions internally; however, it’s
important to have a basic understanding of [rotation and orientation in
Unity](QuaternionAndEulerRotationsInUnity.html).

When you import files containing animation that come from external sources,
the imported files usually contain **keyframe** A frame that marks the start
or end point of a transition in an animation. Frames in between the keyframes
are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) animation in Euler format. Unity’s
default behavior is to resample these animations as Quaternion values and
generate a new Quaternion keyframe for every frame in the animation. This
minimizes the differences between the source animation and how it appears in
Unity.

There are still some situations where the quaternion representation of the
imported animation may not match the original closely enough, even with
resampling. For this reason, Unity provides the option to turn off animation
resampling. This means that you can use the original Euler animation keyframes
at run-time instead.

**Note:** You should only keep the Euler curves as a last resort, if the
default Quaternion interpolation between frames gives bad results and causes
issues.

## Keeping the original Euler curves on imported animations

To use the original Euler curve values in an animation file, uncheck the
**Resample Curves** option in the [Animation tab](class-AnimationClip.html):

![The Resample Curves option in the Animations
tab](../uploads/Main/AnimationImportResampleRotations.png) The Resample Curves
option in the Animations tab

When you disable this option, Unity keeps the rotation curve with its original
keyframes, in Euler or Quaternion mode as appropriate for the curve type.

**Note:** The FBX SDK automatically resamples any rotation curve on a
**joint** A physics component allowing a dynamic connection between Rigidbody
components, usually allowing some degree of movement such as a hinge. [More
info](Joints.html)  
See in [Glossary](Glossary.html#joint) that has pre- or post-rotations. This
means that Unity automatically imports them as Quaternion curves.

Unity supports such a wide variety of imported files and attempts to keep the
imported curves as close to the original as possible. In order to achieve
this, Unity supports all normal (non-repeating) Euler rotation orders, and
imports curves in their original rotation orders.

### Euler values and the Unity engine

When using original Euler (non-resampled) rotations, you can see very little
visual difference in the playback of animations. Under the hood, Unity stores
these curves in Euler representation even at run-time. However, Unity has to
convert rotation values to Quaternions eventually, since the engine only works
with Quaternions.

When you disable the **Resample Curves** option, Unity keeps the rotation
values as Euler values up until they are applied to a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). This means that the end result
should look as good as the original, but with an improvement in memory, since
rotation curves that have not been baked in the authoring software take up
less memory.

### Non-default Euler orders in the Transform Inspector

By default, Unity applies the Euler angles that appear in the Transform
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) in the Z,X,Y order.

When playing back or editing imported animations that feature Euler curves
with a rotation order different from Unity’s default, Unity displays an
indicator of the difference next to the rotation fields:

![The inspector showing that a non-default rotation order is being used for
the rotation animation on this
object](../uploads/Main/AnimationEulerAlternateRotationOrderInInspector.png)
The inspector showing that a non-default rotation order is being used for the
rotation animation on this object

When editing multiple transforms with differing rotation orders, Unity
displays a warning message that the same Euler rotation applied will give
different results on curves with different rotation orders:

![The inspector showing that a mixture of rotation orders are being used for
the rotation animation on the selected group of
objects](../uploads/Main/AnimationEulerMixedRotationOrderInInspector.png) The
inspector showing that a mixture of rotation orders are being used for the
rotation animation on the selected group of objects

[](class-AnimationClip.html)

Animation tab

[](Splittinganimations.html)

Extracting animation clips

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

