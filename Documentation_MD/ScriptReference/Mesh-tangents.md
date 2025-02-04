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

#  [Mesh](Mesh.html).tangents

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

public Vector4[] tangents;

### Description

The tangents of the Mesh.

Tangents are mostly used in bump-mapped Shaders. A tangent is a unit-length
vector that follows Mesh surface along horizontal (U) texture direction.
Tangents in Unity are represented as [Vector4](Vector4.html), with _x,y,z_
components defining the vector, and `w` used to flip the binormal if needed.  
  
Unity calculates the other surface vector (binormal) by taking a cross product
between the normal and the tangent, and multiplying the result by tangent.w.
Therefore, `w` should always be 1 or -1.  
  
You should calculate tangents yourself if you plan to use bump-mapped shaders
on the Mesh. Assign tangents after assigning [normals](Mesh-normals.html) or
using [RecalculateNormals](Mesh.RecalculateNormals.html).  
  
**Note:** To make changes to the [tangents](Mesh-tangents.html), it is
important to copy the tangents from the [Mesh](Mesh.html). Once the
[tangents](Mesh-tangents.html) have been copied and changed, the
[tangents](Mesh-tangents.html) can be reassigned back to the
[Mesh](Mesh.html).

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

