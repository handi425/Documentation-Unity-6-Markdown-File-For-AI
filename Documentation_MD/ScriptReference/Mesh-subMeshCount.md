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

#  [Mesh](Mesh.html).subMeshCount

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

public int subMeshCount;

### Description

The number of sub-meshes inside the Mesh object.

Each sub-mesh corresponds to a [Material](Material.html) in a
[Renderer](Renderer.html), such as [MeshRenderer](MeshRenderer.html) or
[SkinnedMeshRenderer](SkinnedMeshRenderer.html). A sub-mesh consists of a list
of triangles, which refer to a set of vertices. Vertices can be shared between
multiple sub-meshes.  
  
Additional resources: [GetTriangles](Mesh.GetTriangles.html),
[SetTriangles](Mesh.SetTriangles.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;
            [Debug.Log](Debug.Log.html)("Submeshes: " + mesh.subMeshCount);
        }
    }
    

For advanced lower-level sub-mesh and mesh data manipulation functions, see
[SubMeshDescriptor](Rendering.SubMeshDescriptor.html),
[SetSubMesh](Mesh.SetSubMesh.html),
[SetIndexBufferParams](Mesh.SetIndexBufferParams.html),
[SetIndexBufferData](Mesh.SetIndexBufferData.html).  
  
Note that changing `subMeshCount` to a smaller value than it was previously
resizes the Mesh index buffer to be smaller. The new index buffer size is set
to [SubMeshDescriptor.indexStart](Rendering.SubMeshDescriptor-indexStart.html)
of the first removed sub-mesh.

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

