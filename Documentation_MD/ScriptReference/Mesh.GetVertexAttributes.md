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

#  [Mesh](Mesh.html).GetVertexAttributes

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

public VertexAttributeDescriptor[] GetVertexAttributes();

### Returns

**VertexAttributeDescriptor[]** Array of vertex attribute information.

### Description

Get information about vertex attributes of a Mesh.

Many of mesh vertex data attributes are optional, for example a mesh might
contain only vertex positions, normals and one UV coordinate. Each attribute
might use a different data type for storage. Use this function to query
information about all attributes that describe vertices of this Mesh.  
  
The returned array contains as many elements as there are vertex attributes.
For example, if a Mesh has [position](Mesh-vertices.html) and [normals](Mesh-
normals.html) set up, but no other attributes, then the returned array will
have two elements (one describing position, the other describing normal).  
  
Additional resources:
[VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html),
[HasVertexAttribute](Mesh.HasVertexAttribute.html),
[SetVertexBufferParams](Mesh.SetVertexBufferParams.html).

* * *

## Declaration

public int GetVertexAttributes(VertexAttributeDescriptor[] attributes);

## Declaration

public int GetVertexAttributes(List<VertexAttributeDescriptor> attributes);

### Parameters

attributes | Collection of vertex attributes to receive the results.  
---|---  
  
### Returns

**int** The number of vertex attributes returned in the attributes container.

### Description

Get information about vertex attributes of a Mesh, without memory allocations.

Use these overloads of the `GetVertexAttributes` function to avoid having to
allocate a new array each time the function is called. The `List` variant only
allocates memory if the list does not have enough capacity to hold all the
vertex attributes. The array variant never allocates memory; if the array is
too small then only a part of all the vertex attributes is returned.  
  
Alternative way to query vertex attributes that does not need any memory
allocations at all, is to use [vertexAttributeCount](Mesh-
vertexAttributeCount.html) and
[GetVertexAttribute](Mesh.GetVertexAttribute.html) functions.

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

