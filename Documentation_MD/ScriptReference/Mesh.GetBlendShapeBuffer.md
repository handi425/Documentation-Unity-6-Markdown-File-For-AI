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

#  [Mesh](Mesh.html).GetBlendShapeBuffer

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

public [GraphicsBuffer](GraphicsBuffer.html)
GetBlendShapeBuffer([Rendering.BlendShapeBufferLayout](Rendering.BlendShapeBufferLayout.html)
layout);

## Declaration

public [GraphicsBuffer](GraphicsBuffer.html) GetBlendShapeBuffer();

### Parameters

layout | Which buffer to access. The default value is [BlendShapeBufferLayout.PerShape](Rendering.BlendShapeBufferLayout.PerShape.html).  
---|---  
  
### Returns

**GraphicsBuffer** The blend shape vertex data as a
[GraphicsBuffer](GraphicsBuffer.html).

### Description

Retrieves a [GraphicsBuffer](GraphicsBuffer.html) that provides direct read
and write access to GPU blend shape vertex data.

The buffer that this function returns is called the blend shape buffer. It
contains blend shape vertices, which the GPU uses to deform the mesh into
blend shapes.  
  
There are two blend shape buffers that you can access. They use different
layout patterns, and contain slightly different data. For more information,
see
[BlendShapeBufferLayout.PerShape](Rendering.BlendShapeBufferLayout.PerShape.html)
and
[BlendShapeBufferLayout.PerVertex](Rendering.BlendShapeBufferLayout.PerVertex.html).
Compute shader support is required to access this buffer.  
  
The version of this function that takes no parameter is equivalent to calling
it with
[BlendShapeBufferLayout.PerShape](Rendering.BlendShapeBufferLayout.PerShape.html)
as argument.  
  
[Mesh.isReadable](Mesh-isReadable.html) does not need to be `true` to access
this data.  
  
After using this buffer, you should dispose of it.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Mesh](Mesh.html) mesh;
        public [ComputeShader](ComputeShader.html) computeShader;  
      
        void Start()
        {
            // Fetch [GraphicsBuffer](GraphicsBuffer.html) with Blend Shape data, ordered per shape, from the mesh
            var perShapeBuffer = mesh.GetBlendShapeBuffer([BlendShapeBufferLayout.PerShape](Rendering.BlendShapeBufferLayout.PerShape.html));  
      
            // Fetch [GraphicsBuffer](GraphicsBuffer.html) with Blend Shape data, ordered per vertex, from the mesh
            var perVertexBuffer = mesh.GetBlendShapeBuffer([BlendShapeBufferLayout.PerVertex](Rendering.BlendShapeBufferLayout.PerVertex.html));  
      
            // Set Blend Shape data buffers to a compute shader
            computeShader.SetBuffer(0, "PerShape_BlendShapeBuffer", perShapeBuffer);
            computeShader.SetBuffer(0, "PerVertex_BlendShapeBuffer", perVertexBuffer);  
      
            // Dispatch compute shader and access Blend Shapes on the GPU, both per vertex and per shape
            computeShader.Dispatch(0, 64, 1, 1);  
      
            // Dispose buffers to avoid leaking memory
            perShapeBuffer.Dispose();
            perVertexBuffer.Dispose();
        }
    }
    

Additional resources: [Blend shapes](../Manual/AnatomyofaMesh.html#blend-
shapes.html), [BlendShapeBufferLayout](Rendering.BlendShapeBufferLayout.html),
[Mesh.GetBoneWeightBuffer](Mesh.GetBoneWeightBuffer.html).

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

