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

#  [Mesh](Mesh.html).GetVertexAttributeStream

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

public int
GetVertexAttributeStream([Rendering.VertexAttribute](Rendering.VertexAttribute.html)
attr);

### Parameters

attr | The vertex data attribute to check for.  
---|---  
  
### Returns

**int** Stream index of the data attribute, or -1 if it is not present.

### Description

Gets the vertex buffer stream index of a specific vertex data attribute on
this Mesh.

Meshes usually use a single vertex buffer stream, but it is possible to set up
a vertex layout where attributes use different vertex buffers (see
[SetVertexBufferParams](Mesh.SetVertexBufferParams.html)). When you use such a
layout, use this function to query which vertex buffer stream a given
attribute is part of.  
  
Note that this function returns the index of the stream, without specifying
where the attribute is within the stream. To identify the location of a given
attribute in the stream, use
[GetVertexAttributeOffset](Mesh.GetVertexAttributeOffset.html).

    
    
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
      
            // Prints stream indices: 0, 0, 1
            [Debug.Log](Debug.Log.html)($"[Position](UIElements.Position.html) stream {mesh.GetVertexAttributeStream([VertexAttribute.Position](Rendering.VertexAttribute.Position.html))}");
            [Debug.Log](Debug.Log.html)($"Normal stream {mesh.GetVertexAttributeStream([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html))}");
            [Debug.Log](Debug.Log.html)($"[Color](Color.html) stream {mesh.GetVertexAttributeStream([VertexAttribute.Color](Rendering.VertexAttribute.Color.html))}");  
      
            // Cleanup
            [Object.DestroyImmediate](Object.DestroyImmediate.html)(mesh);
        }
    }
    

Additional resources: [VertexAttribute](Rendering.VertexAttribute.html),
[HasVertexAttribute](Mesh.HasVertexAttribute.html),
[GetVertexAttributeOffset](Mesh.GetVertexAttributeOffset.html),
[vertexBufferCount](Mesh-vertexBufferCount.html),
[GetVertexBufferStride](Mesh.GetVertexBufferStride.html).

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

