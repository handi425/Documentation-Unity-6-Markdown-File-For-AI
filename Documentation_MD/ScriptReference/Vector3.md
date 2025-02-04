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

# Vector3

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

[ ]()

### Description

Representation of 3D vectors and points.

This structure is used throughout Unity to pass 3D positions and directions
around. It also contains functions for doing common vector operations.  
  
Besides the functions listed below, other classes can be used to manipulate
vectors and points as well. For example the [Quaternion](Quaternion.html) and
the [Matrix4x4](Matrix4x4.html) classes are useful for rotating or
transforming vectors and points.

### Static Properties

[back](Vector3-back.html)| Shorthand for writing Vector3(0, 0, -1).  
---|---  
[down](Vector3-down.html)| Shorthand for writing Vector3(0, -1, 0).  
[forward](Vector3-forward.html)| Shorthand for writing Vector3(0, 0, 1).  
[left](Vector3-left.html)| Shorthand for writing Vector3(-1, 0, 0).  
[negativeInfinity](Vector3-negativeInfinity.html)| Shorthand for writing
Vector3(float.NegativeInfinity, float.NegativeInfinity,
float.NegativeInfinity).  
[one](Vector3-one.html)| Shorthand for writing Vector3(1, 1, 1).  
[positiveInfinity](Vector3-positiveInfinity.html)| Shorthand for writing
Vector3(float.PositiveInfinity, float.PositiveInfinity,
float.PositiveInfinity).  
[right](Vector3-right.html)| Shorthand for writing Vector3(1, 0, 0).  
[up](Vector3-up.html)| Shorthand for writing Vector3(0, 1, 0).  
[zero](Vector3-zero.html)| Shorthand for writing Vector3(0, 0, 0).  
  
### Properties

[magnitude](Vector3-magnitude.html)| Returns the length of this vector (Read
Only).  
---|---  
[normalized](Vector3-normalized.html)| Returns a normalized vector based on
the current vector. The normalized vector has a magnitude of 1 and is in the
same direction as the current vector. Returns a zero vector If the current
vector is too small to be normalized.  
[sqrMagnitude](Vector3-sqrMagnitude.html)| Returns the squared length of this
vector (Read Only).  
[this[int]](Vector3.Index_operator.html)| Access the x, y, z components using
[0], [1], [2] respectively.  
[x](Vector3-x.html)| X component of the vector.  
[y](Vector3-y.html)| Y component of the vector.  
[z](Vector3-z.html)| Z component of the vector.  
  
### Constructors

[Vector3](Vector3-ctor.html)| Creates a new vector with given x, y, z
components.  
---|---  
  
### Public Methods

[Equals](Vector3.Equals.html)| Returns true if the given vector is exactly
equal to this vector.  
---|---  
[Set](Vector3.Set.html)| Set x, y and z components of an existing Vector3.  
[ToString](Vector3.ToString.html)| Returns a formatted string for this vector.  
  
### Static Methods

[Angle](Vector3.Angle.html)| Calculates the angle between two vectors.  
---|---  
[ClampMagnitude](Vector3.ClampMagnitude.html)| Returns a copy of vector with
its magnitude clamped to maxLength.  
[Cross](Vector3.Cross.html)| Cross Product of two vectors.  
[Distance](Vector3.Distance.html)| Returns the distance between a and b.  
[Dot](Vector3.Dot.html)| Dot Product of two vectors.  
[Lerp](Vector3.Lerp.html)| Linearly interpolates between two points.  
[LerpUnclamped](Vector3.LerpUnclamped.html)| Linearly interpolates between two
vectors.  
[Max](Vector3.Max.html)| Returns a vector that is made from the largest
components of two vectors.  
[Min](Vector3.Min.html)| Returns a vector that is made from the smallest
components of two vectors.  
[MoveTowards](Vector3.MoveTowards.html)| Calculate a position between the
points specified by current and target, moving no farther than the distance
specified by maxDistanceDelta.  
[Normalize](Vector3.Normalize.html)| Makes this vector have a magnitude of 1.  
[OrthoNormalize](Vector3.OrthoNormalize.html)| Makes vectors normalized and
orthogonal to each other.  
[Project](Vector3.Project.html)| Projects a vector onto another vector.  
[ProjectOnPlane](Vector3.ProjectOnPlane.html)| Projects a vector onto a plane.  
[Reflect](Vector3.Reflect.html)| Reflects a vector off the plane defined by a
normal.  
[RotateTowards](Vector3.RotateTowards.html)| Rotates a vector current towards
target.  
[Scale](Vector3.Scale.html)| Multiplies two vectors component-wise.  
[SignedAngle](Vector3.SignedAngle.html)| Calculates the signed angle between
vectors from and to in relation to axis.  
[Slerp](Vector3.Slerp.html)| Spherically interpolates between two vectors.  
[SlerpUnclamped](Vector3.SlerpUnclamped.html)| Spherically interpolates
between two vectors.  
[SmoothDamp](Vector3.SmoothDamp.html)| Gradually changes a vector towards a
desired goal over time.  
  
### Operators

[operator -](Vector3-operator_subtract.html)| Subtracts one vector from
another.  
---|---  
[operator !=](Vector3-operator_ne.html)| Returns true if vectors are
different.  
[operator *](Vector3-operator_multiply.html)| Multiplies a vector by a number.  
[operator /](Vector3-operator_divide.html)| Divides a vector by a number.  
[operator +](Vector3-operator_add.html)| Adds two vectors.  
[operator ==](Vector3-operator_eq.html)| Returns true if two vectors are
approximately equal.  
  
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

