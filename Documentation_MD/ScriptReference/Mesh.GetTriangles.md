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

#  [Mesh](Mesh.html).GetTriangles

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

public int[] GetTriangles(int submesh);

## Declaration

public int[] GetTriangles(int submesh, bool applyBaseVertex = true);

## Declaration

public void GetTriangles(List<int> triangles, int submesh, bool
applyBaseVertex = true);

## Declaration

public void GetTriangles(List<int> triangles, int submesh);

## Declaration

public void GetTriangles(List<ushort> triangles, int submesh, bool
applyBaseVertex);

### Parameters

triangles | A list of vertex indices to populate. Any existing items in the list are replaced.  
---|---  
submesh | The sub-mesh index. See [subMeshCount](Mesh-subMeshCount.html).  
applyBaseVertex | True (default value) will apply base vertex offset to returned indices.  
  
### Description

Fetches the triangle list for the specified sub-mesh on this object.

Each integer in the returned triangle list is a vertex index, which is used as
an offset into the Mesh's vertex arrays. See [vertices](Mesh-vertices.html)
and [GetVertices](Mesh.GetVertices.html). The triangle list contains a
multiple of three indices, one for each corner in each triangle.  
  
A sub-mesh represents a list of triangles that are rendered using a single
[Material](Material.html). When the Mesh is used with a
[Renderer](Renderer.html) that has multiple materials, you should ensure that
there is one sub-mesh per Material.  
  
Call the method overload with a `List<int>` parameter if you control the life
cycle of the index buffer and wish to avoid allocation of a new array with
every access.  
  
Additional resources: [subMeshCount](Mesh-subMeshCount.html).

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

