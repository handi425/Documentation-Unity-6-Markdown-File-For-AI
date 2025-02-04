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

#  [Mesh](Mesh.html).GetVertexBufferStride

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

public int GetVertexBufferStride(int stream);

### Parameters

stream | Vertex data stream index to check for.  
---|---  
  
### Returns

**int** Vertex data size in bytes in this stream, or zero if the stream is not
present.

### Description

Get vertex buffer stream stride in bytes.

Meshes usually use a single vertex buffer stream. But it is possible to setup
a vertex layout where some attributes use different vertex buffers (see
[SetVertexBufferParams](Mesh.SetVertexBufferParams.html),
[VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)). You
can use this function to query vertex data size in bytes within the given
stream.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a [Mesh](Mesh.html) with custom vertex data layout:
            // position and normal go into stream 0,
            // color goes into stream 1.
            var mesh = new [Mesh](Mesh.html)();
            mesh.SetVertexBufferParams(10,
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Position](Rendering.VertexAttribute.Position.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 3, stream:0),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 3, stream:0),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Color](Rendering.VertexAttribute.Color.html), [VertexAttributeFormat.UNorm8](Rendering.VertexAttributeFormat.UNorm8.html), 4, stream:1));  
      
            // Prints 2 (two vertex streams)
            [Debug.Log](Debug.Log.html)($"[Vertex](UIElements.Vertex.html) stream count: {mesh.vertexBufferCount}");
            // Next two lines print: 24 (12 bytes position + 12 bytes normal), 4 (4 bytes color)
            [Debug.Log](Debug.Log.html)($"Steam 0 stride {mesh.GetVertexBufferStride(0)}");
            [Debug.Log](Debug.Log.html)($"Steam 1 stride {mesh.GetVertexBufferStride(1)}");  
      
            // Cleanup
            [Object.DestroyImmediate](Object.DestroyImmediate.html)(mesh);
        }
    }
    

Additional resources: [vertexBufferCount](Mesh-vertexBufferCount.html),
[GetVertexAttributeOffset](Mesh.GetVertexAttributeOffset.html),
[SetVertexBufferParams](Mesh.SetVertexBufferParams.html).

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

