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

# Vector4

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

Representation of four-dimensional vectors.

This structure is used in some places to represent four component vectors
(e.g. mesh tangents, parameters for shaders). In the majority of other cases a
[Vector3](Vector3.html) is used.

### Static Properties

[negativeInfinity](Vector4-negativeInfinity.html)| Shorthand for writing
Vector4(float.NegativeInfinity, float.NegativeInfinity,
float.NegativeInfinity, float.NegativeInfinity).  
---|---  
[one](Vector4-one.html)| Shorthand for writing Vector4(1,1,1,1).  
[positiveInfinity](Vector4-positiveInfinity.html)| Shorthand for writing
Vector4(float.PositiveInfinity, float.PositiveInfinity,
float.PositiveInfinity, float.PositiveInfinity).  
[zero](Vector4-zero.html)| Shorthand for writing Vector4(0,0,0,0).  
  
### Properties

[magnitude](Vector4-magnitude.html)| Returns the length of this vector (Read
Only).  
---|---  
[normalized](Vector4-normalized.html)| Returns a normalized vector based on
the current vector. The normalized vector has a magnitude of 1 and is in the
same direction as the current vector. Returns a zero vector If the current
vector is too small to be normalized.  
[sqrMagnitude](Vector4-sqrMagnitude.html)| Returns the squared length of this
vector (Read Only).  
[this[int]](Vector4.Index_operator.html)| Access the x, y, z, w components
using [0], [1], [2], [3] respectively.  
[w](Vector4-w.html)| W component of the vector.  
[x](Vector4-x.html)| X component of the vector.  
[y](Vector4-y.html)| Y component of the vector.  
[z](Vector4-z.html)| Z component of the vector.  
  
### Constructors

[Vector4](Vector4-ctor.html)| Creates a new vector with given x, y, z, w
components.  
---|---  
  
### Public Methods

[Equals](Vector4.Equals.html)| Returns true if the given vector is exactly
equal to this vector.  
---|---  
[Set](Vector4.Set.html)| Set x, y, z and w components of an existing Vector4.  
[ToString](Vector4.ToString.html)| Returns a formatted string for this vector.  
  
### Static Methods

[Distance](Vector4.Distance.html)| Returns the distance between a and b.  
---|---  
[Dot](Vector4.Dot.html)| Dot Product of two vectors.  
[Lerp](Vector4.Lerp.html)| Linearly interpolates between two vectors.  
[LerpUnclamped](Vector4.LerpUnclamped.html)| Linearly interpolates between two
vectors.  
[Max](Vector4.Max.html)| Returns a vector that is made from the largest
components of two vectors.  
[Min](Vector4.Min.html)| Returns a vector that is made from the smallest
components of two vectors.  
[MoveTowards](Vector4.MoveTowards.html)| Moves a point current towards target.  
[Normalize](Vector4.Normalize.html)| Makes this vector have a magnitude of 1.  
[Project](Vector4.Project.html)| Projects a vector onto another vector.  
[Scale](Vector4.Scale.html)| Multiplies two vectors component-wise.  
  
### Operators

[operator -](Vector4-operator_subtract.html)| Subtracts one vector from
another.  
---|---  
[operator *](Vector4-operator_multiply.html)| Multiplies a vector by a number.  
[operator /](Vector4-operator_divide.html)| Divides a vector by a number.  
[operator +](Vector4-operator_add.html)| Adds two vectors.  
[operator ==](Vector4-operator_eq.html)| Returns true if two vectors are
approximately equal.  
[Vector2](Vector4-operator_Vector4.html)| Converts a Vector4 to a Vector2.  
[Vector3](Vector4-operator_Vector4.html)| Converts a Vector4 to a Vector3.  
[Vector4](Vector4-operator_Vector3.html)| Converts a Vector3 to a Vector4.  
[Vector4](Vector4-operator_Vector2.html)| Converts a Vector2 to a Vector4.  
  
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

