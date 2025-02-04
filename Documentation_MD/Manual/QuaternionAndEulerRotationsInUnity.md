[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/QuaternionAndEulerRotationsInUnity.html)
  * [中文](/cn/current/Manual/QuaternionAndEulerRotationsInUnity.html)
  * [日本語](/ja/current/Manual/QuaternionAndEulerRotationsInUnity.html)
  * [한국어](/kr/current/Manual/QuaternionAndEulerRotationsInUnity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/QuaternionAndEulerRotationsInUnity.html)
  * [中文](/cn/current/Manual/QuaternionAndEulerRotationsInUnity.html)
  * [日本語](/ja/current/Manual/QuaternionAndEulerRotationsInUnity.html)
  * [한국어](/kr/current/Manual/QuaternionAndEulerRotationsInUnity.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [GameObject fundamentals](gameobject-fundamentals.html)
  * Rotation and orientation in Unity

[](class-Transform.html)

Transforms

[](StaticObjects.html)

Static GameObjects

# Rotation and orientation in Unity

Unity uses a left-handed coordinate system. In Unity, you can use both Euler
angles and **quaternions** to represent rotations and orientation. These
representations are equivalent but have different uses and limitations.

Typically, you rotate objects in your **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) using the **Transform component** A
Transform component determines the Position, Rotation, and Scale of each
object in the scene. Every GameObject has a Transform. [More info](class-
Transform.html)  
See in [Glossary](Glossary.html#TransformComponent), which displays
orientation as a Euler angle. However, Unity stores rotations and orientations
internally as quaternions, which can be useful for more complex motions that
might otherwise lead to gimbal lock.

## Left-handed coordinate system

![The axes of Unitys left-handed coordinate system, showing that the direction
of rotation from the positive x-axis to the positive y-axis is
counterclockwise when looking along the positive
z-axis.](../uploads/Main/unity-axis-with-rotation.png) The axes of Unity’s
left-handed coordinate system, showing that the direction of rotation from the
positive x-axis to the positive y-axis is counterclockwise when looking along
the positive z-axis.

A coordinate system describes the position of objects in a three-dimensional
space. Unity uses a left-handed coordinate system: the positive x-axis points
to the right, the positive y-axis points up, and the positive z-axis points
forward. Unity’s left-handed coordinate system means that the direction of
rotation from the positive x-axis to the positive y-axis is counterclockwise
when looking along the positive z-axis.

## Euler angles

In the Transform coordinate, Unity displays rotation with the vector property
[`Transform.eulerAngles`](https://docs.unity3d.com/ScriptReference/Transform-
eulerAngles.html) X, Y, and Z. Unlike a normal vector, these values actually
represent the angle (in degrees) of rotation about the X, Y, and Z axes.

Euler angle rotations perform three separate rotations around the three axes.
Unity performs the Euler rotations sequentially around the z-axis, the x-axis
and then the y-axis. This method of rotation is extrinsic rotation; the
original coordinate system doesn’t change while the rotations occur.

To rotate a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), you can enter angle values of how
far you want each axis to rotate into the Transform component. To rotate your
GameObjects with script, use `Transform.eulerAngles`. If you convert to Euler
angles to do calculations and rotations, you risk problems with gimbal lock.

### Gimbal lock

When an object in 3D space loses a degree of freedom and can only rotate
within two dimensions, it’s called gimbal lock. Gimbal lock can occur with
Euler angles if two axes become parallel. If you don’t convert the rotational
values to Euler angles in your script, the use of quaternions should prevent
gimbal lock.

If you do have problems with gimbal lock, you can avoid Euler angles if you
use `Transform.RotateAround` for rotations. You can also use
`Quaternion.AngleAxis` on each axis and multiply them together (quaternion
multiplication applies each rotation in turn).

## Quaternions

Quaternions provide mathematical notation for unique representations of
spatial orientation and rotation in 3D space. A quaternion uses four numbers
to encode the direction and angle of rotation around unit axes in 3D. These
four values are complex numbers rather than angles or degrees. You can look
into the [mathematics of
quaternions](https://www.semanticscholar.org/paper/Quaternions%2C-Interpolation-
and-Animation-Dam-Koch/89278a22076beb70c1e64a94c3f822eb1d6bfb13) for more
information.

Unity converts rotational values to quaternions to store them because
quaternion rotations are efficient and stable to compute. The Unity Editor
doesn’t display rotations as quaternions because a single quaternion can’t
represent a rotation greater than 360 degrees about any axis.

You can use quaternions directly if you use the [Quaternion class](class-
Quaternion.html). If you use script for your rotations, you can use the
Quaternion class and functions to create and change rotational values. You can
apply values to your rotation as Euler angles but you need to store them as
quaternions to avoid problems.

## Convert between Euler angles and quaternions

To convert between quaternions and Euler angles to view and edit your
rotations in your preferred way, you can use script:

  * To convert from Euler angles to quaternions, you can use the [`Quaternion.Euler`](https://docs.unity3d.com/ScriptReference/Quaternion.Euler.html) function.
  * To convert a quaternion to Euler angles, you can use the [`Quaternion.eulerAngles`](https://docs.unity3d.com/ScriptReference/Quaternion-eulerAngles.html) function.

## Additional resources

  * [Rotations in animations](AnimationRotate.html)
  * [Transforms](class-Transform.html)
  * [`Transform.rotate`](https://docs.unity3d.com/2021.2/Documentation/ScriptReference/Transform.Rotate.html)
  * [Important Classes - Quaternions](class-Quaternion.html)
  * [`Quaternion`](https://docs.unity3d.com/2021.2/Documentation/ScriptReference/Quaternion.html)

[](class-Transform.html)

Transforms

[](StaticObjects.html)

Static GameObjects

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

