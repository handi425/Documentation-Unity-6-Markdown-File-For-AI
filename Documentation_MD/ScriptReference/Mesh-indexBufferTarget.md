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

#  [Mesh](Mesh.html).indexBufferTarget

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

public [GraphicsBuffer.Target](GraphicsBuffer.Target.html) indexBufferTarget;

### Description

The intended target usage of the Mesh GPU index buffer.

By default, Mesh index buffers have
[GraphicsBuffer.Target.Index](GraphicsBuffer.Target.Index.html) usage target.
If you want to access the mesh index buffer from a compute shader, additional
targets need to be requested, for example
[GraphicsBuffer.Target.Raw](GraphicsBuffer.Target.Raw.html).

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Mesh](Mesh.html) mesh;
        public [ComputeShader](ComputeShader.html) computeShader;
        void Start()
        {
            // Mark the index buffer as needing "Raw"
            // (ByteAddressBuffer, RWByteAddressBuffer in HLSL shaders)
            // access.
            mesh.indexBufferTarget |= [GraphicsBuffer.Target.Raw](GraphicsBuffer.Target.Raw.html);
            // Get the index buffer of the [Mesh](Mesh.html), and set it up
            // as a buffer parameter to a compute shader.
            var indexBuffer = mesh.GetIndexBuffer();
            computeShader.SetBuffer(0, "MeshIndexBuffer", indexBuffer);
            indexBuffer.Dispose();
        }
    }
    

Additional resources: [Target](GraphicsBuffer.Target.html),
[GetIndexBuffer](Mesh.GetIndexBuffer.html), [vertexBufferTarget](Mesh-
vertexBufferTarget.html).

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

