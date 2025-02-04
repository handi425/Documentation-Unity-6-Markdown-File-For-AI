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

#  [Mesh](Mesh.html).isReadable

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

public bool isReadable;

### Description

Returns true if the Mesh is read/write enabled, or false if it is not.

When a Mesh is read/write enabled, Unity uploads the Mesh data to GPU-
addressable memory, but also keeps it in CPU-addressable memory. When a Mesh
is not read/write enabled, Unity uploads the Mesh data to GPU-addressable
memory, and then removes it from CPU-addressable memory.  
  
You can set this value using the Read/Write Enabled checkbox when importing a
model to Unity. To set the value to false at run time, set the
`markNoLongerReadable` argument of
[Mesh.UploadMeshData](Mesh.UploadMeshData.html).  
  
In most cases, you should disable this option to save runtime memory usage.
You should only enable it under the following circumstances:

  * When you read from or write to the Mesh data in your code.
  * When you pass the Mesh to `StaticBatchingUtility.Combine()` to combine the Mesh at run time.
  * When you pass the mesh to [CanvasRenderer.SetMesh](CanvasRenderer.SetMesh.html).
  * When you use the Mesh to bake a NavMesh using the NavMesh building components at run time.
  * When the Mesh is convex, you use the Mesh with a Mesh Collider, and the Mesh Collider's Transform has negative scaling (for example, (–1, 1, 1)).
  * When you use the Mesh with a Mesh Collider, and the Mesh Collider's transform is skewed or sheared (for example, when a rotated Transform has a scaled parent Transform).
  * When you use the Mesh with a Mesh Collider, and the Mesh Collider's Cooking Options flags are set to any value other than the default.
  * When using a Mesh with a Particle System's Shape module or Renderer module when not using GPU instancing.

Note that the Particle System will automatically change Meshes to readable
when assigned through the inspector  
  
Notes: When Unity creates a Mesh from script, this value is initially set to
true. Meshes not marked readable will throw an error on accessing any data
arrays from script at runtime. Access is always allowed in the Unity Editor
outside of the game and rendering loop, regardless of this setting.  
  
Additional resources:
[StaticBatchingUtility.Combine](StaticBatchingUtility.Combine.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().sharedMesh;
            print(mesh.isReadable);
        }
    }
    

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

