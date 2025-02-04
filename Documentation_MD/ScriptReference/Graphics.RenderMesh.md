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

#  [Graphics](Graphics.html).RenderMesh

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

## Declaration

public static void RenderMesh(ref [RenderParams](RenderParams.html) rparams,
[Mesh](Mesh.html) mesh, int submeshIndex, [Matrix4x4](Matrix4x4.html)
objectToWorld, Nullable<Matrix4x4> prevObjectToWorld = null);

### Parameters

rparams | The parameters Unity uses to render the mesh.  
---|---  
mesh | The [Mesh](Mesh.html) to render.  
submeshIndex | The index of a submesh Unity renders when the Mesh contains multiple Materials (submeshes). For a Mesh with a single Material, use value 0.  
objectToWorld | The transformation matrix Unity uses to transform the mesh from object to world space.  
prevObjectToWorld | The previous frame transformation matrix Unity uses to calculate motion vectors for the mesh.  
  
### Description

Renders a mesh with given rendering parameters.

`RenderMesh` renders a Mesh for the current frame. This Mesh is affected by
Lights, can cast and receive shadows, and is affected by Projectors. This Mesh
can be rendered by all Cameras or by a specific Camera.  
  
Use `RenderMesh` to control Mesh rendering programmatically without the need
to create and manage GameObjects. `RenderMesh` submits the Mesh for rendering,
which means it does not render the Mesh immediately. Unity renders the Mesh as
part of normal rendering process. If you want to render a mesh immediately,
use [Graphics.DrawMeshNow](Graphics.DrawMeshNow.html).  
  
`RenderMesh` does not apply any changes you make to the Material properties of
a Mesh between calls. This is because it does not render the Mesh immediately.
If you want to render series of Meshes that have the same Material, but with
slightly different properties (for example, to change color of each mesh), use
[MaterialPropertyBlock](MaterialPropertyBlock.html) parameter.  
  
This call creates internal resources while the Mesh is in the render queue.
The allocation happens immediately and exists until the end of frame if the
object is in the render queue for all cameras. Otherwise, the allocation
exists until the specified Camera finishes rendering.  
  
Additional resources: [MaterialPropertyBlock](MaterialPropertyBlock.html).  
  
The following example renders 10 Meshes with a given Material:

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Material](Material.html) material;
        public [Mesh](Mesh.html) mesh;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [RenderParams](RenderParams.html) rp = new [RenderParams](RenderParams.html)(material);
            for(int i=0; i<10; ++i)
                [Graphics.RenderMesh](Graphics.RenderMesh.html)(rp, mesh, 0, [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(-4.5f+i, 0.0f, 5.0f)));
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

