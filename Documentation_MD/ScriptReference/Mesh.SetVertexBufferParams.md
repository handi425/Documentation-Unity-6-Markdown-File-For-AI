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

#  [Mesh](Mesh.html).SetVertexBufferParams

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
attributes | Layout of the vertex data -- which attributes are present, their data types and so on.  
  
### Description

Sets the vertex buffer size and layout.

Note: This method is designed for advanced users aiming for maximum
performance because it operates on the underlying mesh data structures that
primarily work on raw index buffers, vertex buffers and mesh subset data.
Using this method, Unity performs very little data validation, so you must
ensure your data is valid.  
  
In particular, you must ensure that the index buffer does not contain out-of-
bounds indices, and that the SubMesh index range and bounds are updated via
[SetSubMesh](Mesh.SetSubMesh.html).  
  
For information about the difference between the simpler and more advanced
methods of assigning data to a Mesh from script, see the notes on the
[Mesh](Mesh.html) page.  
  
For details on how to specify a mesh attribute layout, see
[VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html).

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var mesh = new [Mesh](Mesh.html)();
            // specify vertex layout with:
            // - floating point positions,
            // - half-precision (FP16) normals with two components,
            // - low precision (UNorm8) tangents
            var layout = new[]
            {
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Position](Rendering.VertexAttribute.Position.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 3),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html), [VertexAttributeFormat.Float16](Rendering.VertexAttributeFormat.Float16.html), 2),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Tangent](Rendering.VertexAttribute.Tangent.html), [VertexAttributeFormat.UNorm8](Rendering.VertexAttributeFormat.UNorm8.html), 4),
            };
            var vertexCount = 10;
            mesh.SetVertexBufferParams(vertexCount, layout);  
      
            // ...later on SetVertexBufferData would be used to set the actual vertex data
        }
    }
    

If the vertex buffer size exceeds the maximum buffer size that the device
supports, the method raises an exception. For more information, see
[SystemInfo.maxGraphicsBufferSize](SystemInfo-maxGraphicsBufferSize.html).  
  
Additional resources: [SetVertexBufferData](Mesh.SetVertexBufferData.html),
[VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html),
[GetVertexAttributes](Mesh.GetVertexAttributes.html).

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

