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

# BlendShapeBufferRange

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Describes the location of blend shape vertex data in a
[GraphicsBuffer](GraphicsBuffer.html).

When you call [Mesh.GetBlendShapeBuffer](Mesh.GetBlendShapeBuffer.html) with
[BlendShapeBufferLayout.PerShape](Rendering.BlendShapeBufferLayout.PerShape.html),
Unity returns a [GraphicsBuffer](GraphicsBuffer.html) that contains blend
shape vertex data, ordered by blend shape.  
  
When you call
[Mesh.GetBlendShapeBufferRange](Mesh.GetBlendShapeBufferRange.html) for a
given blend shape, Unity returns this struct. Use this struct to locate the
data for that blend shape in the `GraphicsBuffer`.

    
    
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
      
            // Iterate over all Blend Shapes in a mesh
            for (int blendShapeIndex = 0; blendShapeIndex  < mesh.blendShapeCount; ++blendShapeIndex)
            {
                // Fetch which indices in the buffer that is part of this Blend Shape
                var blendShapeRange = mesh.GetBlendShapeBufferRange(blendShapeIndex);  
      
                // Set the start and end indices of the Blend Shape in the compute shader
                computeShader.SetInt("_StartIndex", (int)blendShapeRange.startIndex);
                computeShader.SetInt("_EndIndex", (int)blendShapeRange.endIndex);  
      
                // Dispatch compute shader and access data between start and end index for this Blend Shape
                computeShader.Dispatch(0, 64, 1, 1);
            }  
      
            // Dispose of [GraphicsBuffer](GraphicsBuffer.html) to avoid leak memory
            perShapeBuffer.Dispose();
        }
    }
    

Additional resources:
[Mesh.GetBlendShapeBuffer](Mesh.GetBlendShapeBuffer.html),
[Mesh.GetBlendShapeBufferRange](Mesh.GetBlendShapeBufferRange.html),
[BlendShapeBufferLayout.PerShape](Rendering.BlendShapeBufferLayout.PerShape.html).

### Properties

[endIndex](BlendShapeBufferRange-endIndex.html)| The index of the last blend
shape vertex for the requested blend shape.  
---|---  
[startIndex](BlendShapeBufferRange-startIndex.html)| The index of the first
blend shape vertex for the requested blend shape.  
  
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

