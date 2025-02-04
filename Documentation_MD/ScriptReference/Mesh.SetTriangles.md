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

#  [Mesh](Mesh.html).SetTriangles

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

public void SetTriangles(int[] triangles, int submesh, bool calculateBounds =
true, int baseVertex = 0);

## Declaration

public void SetTriangles(List<int> triangles, int submesh, bool
calculateBounds = true, int baseVertex = 0);

## Declaration

public void SetTriangles(ushort[] triangles, int submesh, bool
calculateBounds, int baseVertex);

## Declaration

public void SetTriangles(List<ushort> triangles, int submesh, bool
calculateBounds, int baseVertex);

### Parameters

triangles | The list of indices that define the triangles.  
---|---  
submesh | The sub-mesh to modify.  
calculateBounds | Calculate the bounding box of the Mesh after setting the triangles. This is done by default. Use false when you want to use the existing bounding box and reduce the CPU cost of setting the triangles.  
baseVertex | Optional vertex offset that is added to all triangle vertex indices.  
  
### Description

Sets the triangle list for the sub-mesh.

A sub-mesh represents a list of triangles that are rendered using a single
[Material](Material.html). When the Mesh is used with a
[Renderer](Renderer.html) that has multiple materials, you should ensure that
there is one sub-mesh per Material.  
  
It is recommended to assign the triangle array after assigning the vertex
array, in order to avoid out-of-bounds errors.  
  
The `baseVertex` argument can be used to achieve meshes that are larger than
65535 vertices while using 16 bit index buffers, as long as each sub-mesh fits
within its own 65535 vertex area. For example, if the index buffer that is
passed to SetTriangles contains indices 10,11,12 and `baseVertex` is set to
100000, then effectively vertices 100010, 100011 and 100012 will be used for
rendering.  
  
Note that meshes use 16-bit [indexFormat](Mesh-indexFormat.html) by default,
i.e. maximum value supported in the index buffer is 65535 (even when using
@int[]@ input data). In order to use larger index buffer values, you should
first set the [indexFormat](Mesh-indexFormat.html) to
[IndexFormat.UInt32](Rendering.IndexFormat.UInt32.html).  
  
Additional resources: [subMeshCount](Mesh-subMeshCount.html),
[SetIndices](Mesh.SetIndices.html), [indexFormat](Mesh-indexFormat.html).

* * *

## Declaration

public void SetTriangles(int[] triangles, int trianglesStart, int
trianglesLength, int submesh, bool calculateBounds, int baseVertex);

## Declaration

public void SetTriangles(List<int> triangles, int trianglesStart, int
trianglesLength, int submesh, bool calculateBounds, int baseVertex);

## Declaration

public void SetTriangles(ushort[] triangles, int trianglesStart, int
trianglesLength, int submesh, bool calculateBounds, int baseVertex);

## Declaration

public void SetTriangles(List<ushort> triangles, int trianglesStart, int
trianglesLength, int submesh, bool calculateBounds, int baseVertex);

### Parameters

triangles | The list of indices that define the triangles.  
---|---  
trianglesStart | Index of the first element to take from the input array.  
trianglesLength | Number of elements to take from the input array.  
submesh | The sub-mesh to modify.  
calculateBounds | Calculate the bounding box of the Mesh after setting the triangles. This is done by default. Use false when you want to use the existing bounding box and reduce the CPU cost of setting the triangles.  
baseVertex | Optional vertex offset that is added to all triangle vertex indices.  
  
### Description

Sets the triangle list of the Mesh, using a part of the input array.

This method behaves as if you called SetTriangles with an array that is a
slice of the whole array, starting at `trianglesStart` index and being of a
given `trianglesLength` length. The resulting Mesh has `trianglesLength`
amount of vertices. Resulting sub-mesh will have `trianglesLength/3` amount of
triangles.

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

