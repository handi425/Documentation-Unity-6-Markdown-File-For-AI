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

#  [Mesh](Mesh.html).SetTangents

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

## Declaration

public void SetTangents(Vector4[] inTangents);

## Declaration

public void SetTangents(List<Vector4> inTangents);

## Declaration

public void SetTangents(NativeArray<T> inTangents);

### Parameters

inTangents | Per-vertex tangents.  
---|---  
  
### Description

Set the tangents of the Mesh.

Additional resources: [tangents](Mesh-tangents.html) property.

* * *

## Declaration

public void SetTangents(Vector4[] inTangents, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetTangents(List<Vector4> inTangents, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetTangents(NativeArray<T> inTangents, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

### Parameters

inTangents | Per-vertex tangents.  
---|---  
start | Index of the first element to take from the input array.  
length | Number of elements to take from the input array.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).  
  
### Description

Sets the tangents of the Mesh, using a part of the input array.

This method behaves as if you called SetTangents with an array that is a slice
of the whole array, starting at `start` index and being of a given `length`.
The resulting Mesh has `length` amount of vertices.

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

