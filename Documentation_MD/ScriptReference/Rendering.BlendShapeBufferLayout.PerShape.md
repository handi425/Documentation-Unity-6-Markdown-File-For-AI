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

#  [BlendShapeBufferLayout](Rendering.BlendShapeBufferLayout.html).PerShape

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

### Description

Order the data by blend shape.

When you call [Mesh.GetBlendShapeBuffer](Mesh.GetBlendShapeBuffer.html) with
this option, it returns a [GraphicsBuffer](GraphicsBuffer.html) containing
blend shape vertex data ordered by blend shape.  
  
In this buffer, each blend shape vertex comprises:

  * An int that represents the index of the mesh vertex to which this data relates.
  * A [Vector3](Vector3.html) that represents the position delta.
  * A [Vector3](Vector3.html) that represents the normal delta.
  * A [Vector3](Vector3.html) that represents the tangent delta.

In this buffer, all the data for each blend shape vertex is contiguous. The
data layout is as follows:  
  
* All blend shape vertices that belong to a single blend shape are stored contiguously, followed by all blend shape vertices that belong to another blend shape, and so on  
  
The contiguous blend shape vertex data is stored as an array of 32-bit values.
You must manually convert the data to an appropriate type.  
  
To determine which data relates to which blend shape, use
[Mesh.GetBlendShapeBufferRange](Mesh.GetBlendShapeBufferRange.html).  
  
Unity creates this buffer when it creates the mesh. Accessing this buffer does
not result in additional memory allocations.

    
    
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
      
            // Set Blend Shape data buffer to a compute shader
            computeShader.SetBuffer(0, "PerShape_BlendShapeBuffer", perShapeBuffer);  
      
            // Dispatch compute shader and access Blend Shape [Data](Unity.Android.Gradle.Manifest.Data.html) on the GPU
            computeShader.Dispatch(0, 64, 1, 1);  
      
            // Dispose of [GraphicsBuffer](GraphicsBuffer.html) to avoid leaking memory
            perShapeBuffer.Dispose();
        }
    }
    

Additional resources: [Mesh data: blend
shapes](../Manual/AnatomyofaMesh.html#blend-shapes.html),
[Mesh.GetBlendShapeBuffer](Mesh.GetBlendShapeBuffer.html),
UnityEngine.BlendShapeBufferRange.

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

