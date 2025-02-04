[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# Quaternion

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-Quaternion.html "Go to Quaternion Component
in the Manual")

### Description

Quaternions are used to represent rotations.

A quaternion is a four-tuple of real numbers {x,y,z,w}. A quaternion is a
mathematically convenient alternative to the euler angle representation. You
can interpolate a quaternion without experiencing gimbal lock. You can also
use a quaternion to concatenate a series of rotations into a single
representation.  
  
Unity internally uses Quaternions to represent all rotations.  
  
In most cases, you can use existing rotations from methods such as
[Transform.localRotation](Transform-localRotation.html) or
[Transform.rotation](Transform-rotation.html) to construct new rotations. For
example, use existing rotations to smoothly interpolate between two rotations.
The most used Quaternion functions are as follows:
[Quaternion.LookRotation](Quaternion.LookRotation.html),
[Quaternion.Angle](Quaternion.Angle.html),
[Quaternion.Euler](Quaternion.Euler.html),
[Quaternion.Slerp](Quaternion.Slerp.html),
[Quaternion.FromToRotation](Quaternion.FromToRotation.html), and
[Quaternion.identity](Quaternion-identity.html).  
  
You can use the Quaternion.operator * to rotate one rotation by another, or to
rotate a vector by a rotation.  
  
Note that Unity expects Quaternions to be normalized.

### Static Properties

[identity](Quaternion-identity.html)| The identity rotation (Read Only).  
---|---  
  
### Properties

[eulerAngles](Quaternion-eulerAngles.html)| Returns or sets the euler angle
representation of the rotation in degrees.  
---|---  
[normalized](Quaternion-normalized.html)| Returns this quaternion with a
magnitude of 1 (Read Only).  
[this[int]](Quaternion.Index_operator.html)| Access the x, y, z, w components
using [0], [1], [2], [3] respectively.  
[w](Quaternion-w.html)| W component of the Quaternion. Do not directly modify
quaternions.  
[x](Quaternion-x.html)| X component of the Quaternion. Don't modify this
directly unless you know quaternions inside out.  
[y](Quaternion-y.html)| Y component of the Quaternion. Don't modify this
directly unless you know quaternions inside out.  
[z](Quaternion-z.html)| Z component of the Quaternion. Don't modify this
directly unless you know quaternions inside out.  
  
### Constructors

[Quaternion](Quaternion-ctor.html)| Constructs new Quaternion with given
x,y,z,w components.  
---|---  
  
### Public Methods

[Set](Quaternion.Set.html)| Set x, y, z and w components of an existing
Quaternion.  
---|---  
[SetFromToRotation](Quaternion.SetFromToRotation.html)| Creates a rotation
which rotates from fromDirection to toDirection.  
[SetLookRotation](Quaternion.SetLookRotation.html)| Creates a rotation with
the specified forward and upwards directions.  
[ToAngleAxis](Quaternion.ToAngleAxis.html)| Converts a rotation to angle-axis
representation (angles in degrees).  
[ToString](Quaternion.ToString.html)| Returns a formatted string for this
quaternion.  
  
### Static Methods

[Angle](Quaternion.Angle.html)| Returns the angle in degrees between two
rotations a and b. The resulting angle ranges from 0 to 180.  
---|---  
[AngleAxis](Quaternion.AngleAxis.html)| Creates a rotation which rotates angle
degrees around axis.  
[Dot](Quaternion.Dot.html)| The dot product between two rotations.  
[Euler](Quaternion.Euler.html)| Returns a rotation that rotates z degrees
around the z axis, x degrees around the x axis, and y degrees around the y
axis; applied in that order.  
[FromToRotation](Quaternion.FromToRotation.html)| Creates a rotation from
fromDirection to toDirection.  
[Inverse](Quaternion.Inverse.html)| Returns the Inverse of rotation.  
[Lerp](Quaternion.Lerp.html)| Interpolates between a and b by t and normalizes
the result afterwards.  
[LerpUnclamped](Quaternion.LerpUnclamped.html)| Interpolates between a and b
by t and normalizes the result afterwards. The parameter t is not clamped.  
[LookRotation](Quaternion.LookRotation.html)| Creates a rotation with the
specified forward and upwards directions.  
[Normalize](Quaternion.Normalize.html)| Converts this quaternion to a
quaternion with the same orientation but with a magnitude of 1.0.  
[RotateTowards](Quaternion.RotateTowards.html)| Rotates a rotation from
towards to.  
[Slerp](Quaternion.Slerp.html)| Spherically linear interpolates between unit
quaternions a and b by a ratio of t.  
[SlerpUnclamped](Quaternion.SlerpUnclamped.html)| Spherically linear
interpolates between unit quaternions a and b by t.  
  
### Operators

[operator *](Quaternion-operator_multiply.html)| Combines rotations lhs and
rhs.  
---|---  
[operator ==](Quaternion-operator_eq.html)| Are two quaternions equal to each
other?  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

