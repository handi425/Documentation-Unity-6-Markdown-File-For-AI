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

#  [CommandBuffer](Rendering.CommandBuffer.html).SetViewMatrix

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

public void SetViewMatrix([Matrix4x4](Matrix4x4.html) view);

### Parameters

view | View (world to camera space) matrix.  
---|---  
  
### Description

Add a command to set the view matrix.

The view matrix is the matrix that transforms from world space into camera
space.  
  
When setting both view and projection matrices, it is more efficient to use
[SetViewProjectionMatrices](Rendering.CommandBuffer.SetViewProjectionMatrices.html).  
  
Note: The camera space in Unity matches OpenGL convention, so the negative
z-axis is the camera's forward. This is different from usual Unity convention,
where the camera's forward is the positive z-axis. If you are manually
creating the view matrix, for example with an inverse of
[Matrix4x4.LookAt](Matrix4x4.LookAt.html), you need to scale it by -1 along
the z-axis to get a proper view matrix.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    // Attach this script to a [Camera](Camera.html) and pick a mesh to render.
    // When you enter Play mode, a command buffer renders a green mesh at
    // origin position.
    [[RequireComponent](RequireComponent.html)(typeof([Camera](Camera.html)))]
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Mesh](Mesh.html) mesh;  
      
        void Start()
        {
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Hidden/Internal-Colored"));
            material.SetColor("_Color", [Color.green](Color-green.html));  
      
            var tr = transform;
            var camera = GetComponent<[Camera](Camera.html)>();  
      
            // Code below does the same as what camera.worldToCameraMatrix would do. Doing
            // it "manually" here to illustrate how a view matrix is constructed.
            //
            // Matrix that looks from camera's position, along the forward axis.
            var lookMatrix = [Matrix4x4.LookAt](Matrix4x4.LookAt.html)(tr.position, tr.position + tr.forward, tr.up);
            // Matrix that mirrors along Z axis, to match the camera space convention.
            var scaleMatrix = [Matrix4x4.TRS](Matrix4x4.TRS.html)([Vector3.zero](Vector3-zero.html), [Quaternion.identity](Quaternion-identity.html), new [Vector3](Vector3.html)(1, 1, -1));
            // Final view matrix is inverse of the LookAt matrix, and then mirrored along Z.
            var viewMatrix = scaleMatrix * lookMatrix.inverse;  
      
            var buffer = new [CommandBuffer](Rendering.CommandBuffer.html)();
            buffer.SetViewMatrix(viewMatrix);
            buffer.SetProjectionMatrix(camera.projectionMatrix);
            buffer.DrawMesh(mesh, [Matrix4x4.identity](Matrix4x4-identity.html), material);  
      
            camera.AddCommandBuffer([CameraEvent.BeforeSkybox](Rendering.CameraEvent.BeforeSkybox.html), buffer);
        }
    }
    

Additional resources:
[SetProjectionMatrix](Rendering.CommandBuffer.SetProjectionMatrix.html),
[SetViewProjectionMatrices](Rendering.CommandBuffer.SetViewProjectionMatrices.html),
[Camera.worldToCameraMatrix](Camera-worldToCameraMatrix.html),
[Matrix4x4.LookAt](Matrix4x4.LookAt.html).

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

