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

# Vector2

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

Representation of 2D vectors and points.

This structure is used in some places to represent 2D positions and vectors
(e.g. texture coordinates in a [Mesh](Mesh.html) or texture offsets in
[Material](Material.html)). In the majority of other cases a Vector3 is used.

### Static Properties

[down](Vector2-down.html)| Shorthand for writing Vector2(0, -1).  
---|---  
[left](Vector2-left.html)| Shorthand for writing Vector2(-1, 0).  
[negativeInfinity](Vector2-negativeInfinity.html)| Shorthand for writing
Vector2(float.NegativeInfinity, float.NegativeInfinity).  
[one](Vector2-one.html)| Shorthand for writing Vector2(1, 1).  
[positiveInfinity](Vector2-positiveInfinity.html)| Shorthand for writing
Vector2(float.PositiveInfinity, float.PositiveInfinity).  
[right](Vector2-right.html)| Shorthand for writing Vector2(1, 0).  
[up](Vector2-up.html)| Shorthand for writing Vector2(0, 1).  
[zero](Vector2-zero.html)| Shorthand for writing Vector2(0, 0).  
  
### Properties

[magnitude](Vector2-magnitude.html)| Returns the length of this vector (Read
Only).  
---|---  
[normalized](Vector2-normalized.html)| Returns a normalized vector based on
the current vector. The normalized vector has a magnitude of 1 and is in the
same direction as the current vector. Returns a zero vector If the current
vector is too small to be normalized.  
[sqrMagnitude](Vector2-sqrMagnitude.html)| Returns the squared length of this
vector (Read Only).  
[this[int]](Vector2.Index_operator.html)| Access the x or y component using
[0] or [1] respectively.  
[x](Vector2-x.html)| X component of the vector.  
[y](Vector2-y.html)| Y component of the vector.  
  
### Constructors

[Vector2](Vector2-ctor.html)| Constructs a new vector with given x, y
components.  
---|---  
  
### Public Methods

[Equals](Vector2.Equals.html)| Returns true if the given vector is exactly
equal to this vector.  
---|---  
[Normalize](Vector2.Normalize.html)| Makes this vector have a magnitude of 1.  
[Set](Vector2.Set.html)| Set x and y components of an existing Vector2.  
[ToString](Vector2.ToString.html)| Returns a formatted string for this vector.  
  
### Static Methods

[Angle](Vector2.Angle.html)| Gets the unsigned angle in degrees between from
and to.  
---|---  
[ClampMagnitude](Vector2.ClampMagnitude.html)| Returns a copy of vector with
its magnitude clamped to maxLength.  
[Distance](Vector2.Distance.html)| Returns the distance between a and b.  
[Dot](Vector2.Dot.html)| Dot Product of two vectors.  
[Lerp](Vector2.Lerp.html)| Linearly interpolates between vectors a and b by t.  
[LerpUnclamped](Vector2.LerpUnclamped.html)| Linearly interpolates between
vectors a and b by t.  
[Max](Vector2.Max.html)| Returns a vector that is made from the largest
components of two vectors.  
[Min](Vector2.Min.html)| Returns a vector that is made from the smallest
components of two vectors.  
[MoveTowards](Vector2.MoveTowards.html)| Moves a point current towards target.  
[Perpendicular](Vector2.Perpendicular.html)| Returns the 2D vector
perpendicular to this 2D vector. The result is always rotated 90-degrees in a
counter-clockwise direction for a 2D coordinate system where the positive Y
axis goes up.  
[Reflect](Vector2.Reflect.html)| Reflects a vector off the surface defined by
a normal.  
[Scale](Vector2.Scale.html)| Multiplies two vectors component-wise.  
[SignedAngle](Vector2.SignedAngle.html)| Gets the signed angle in degrees
between from and to.  
[SmoothDamp](Vector2.SmoothDamp.html)| Gradually changes a vector towards a
desired goal over time.  
  
### Operators

[operator -](Vector2-operator_subtract.html)| Subtracts one vector from
another.  
---|---  
[operator *](Vector2-operator_multiply.html)| Multiplies a vector by a number.  
[operator /](Vector2-operator_divide.html)| Divides a vector by a number.  
[operator +](Vector2-operator_add.html)| Adds two vectors.  
[operator ==](Vector2-operator_eq.html)| Returns true if two vectors are
approximately equal.  
[Vector2](Vector2-operator_Vector3.html)| Converts a Vector3 to a Vector2.  
[Vector3](Vector2-operator_Vector2.html)| Converts a Vector2 to a Vector3.  
  
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

