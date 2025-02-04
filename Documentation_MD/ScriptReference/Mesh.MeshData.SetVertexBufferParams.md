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

#  [Mesh.MeshData](Mesh.MeshData.html).SetVertexBufferParams

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

public void SetVertexBufferParams(int vertexCount, params
VertexAttributeDescriptor[] attributes);

## Declaration

public void SetVertexBufferParams(int vertexCount,
NativeArray<VertexAttributeDescriptor> attributes);

### Parameters

vertexCount | The number of vertices in the Mesh.  
---|---  
attributes | Layout of the vertex data: which attributes are present, their data types and so on.  
  
### Description

Sets the vertex buffer size and layout of the Mesh that Unity creates from the
`MeshData`.

Use this function to set vertex buffer size and layout for newly created Mesh
data (see
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html)). For
details, see [Mesh.SetVertexBufferParams](Mesh.SetVertexBufferParams.html).  
  
After you have set the vertex buffer parameters, you can write the vertices
into the array returned by
[Mesh.MeshData.GetVertexData](Mesh.MeshData.GetVertexData.html). If you call
this method on a read-only `MeshData`, Unity throws an exception.

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

