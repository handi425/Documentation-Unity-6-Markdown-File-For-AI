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

# ObjectIdRequest

class in UnityEngine.Rendering

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

ObjectId request that can be used to determine the object corresponding to
each pixel. Can be submitted using either
[Camera.SubmitRenderRequest](Camera.SubmitRenderRequest.html) or
[RenderPipeline.SubmitRenderRequest](Rendering.RenderPipeline.SubmitRenderRequest.html),
and the results can be used either on the CPU in C# or the GPU in a shader.

After submitting this render request, the ObjectIdRequest._result field will
be filled, and each pixel in ObjectIdRequest._destination will contain a
32-bit color that can be decoded to a 32-bit integer index using
[ObjectIdResult.DecodeIdFromColor](Rendering.ObjectIdResult.DecodeIdFromColor.html).
This 32-bit index can then be looked up in ObjectIdResult._idToObjectMapping
to determine the object corresponding to each pixel. The C# code example below
demonstrates how this render request can be used to determine the object
corresponding to each pixel.  
  
Although there is no built-in functionality for decoding the object ID (the
index into ObjectIdResult._idToObjectMapping) from a color on the GPU, the
following HLSL shader function can be used for this purpose: `int
decodeObjectIdInShader(float4 color) { return (int)(color.r * 255) +
((int)(color.g * 255) << 8) + ((int)(color.b * 255) << 16) + ((int)(color.a *
255) << 24); }`  
  
SRP Compatibility:

  * URP: Supported by falling back on the Built-In Render Pipeline implementation when called in the editor.
  * HDRP: Supported by falling back on the Built-In Render Pipeline implementation when called in the editor.

This render request is not currently supported outside of the editor.  
  
Additional resources:
[Camera.SubmitRenderRequest](Camera.SubmitRenderRequest.html),
[RenderPipeline.SubmitRenderRequest](Rendering.RenderPipeline.SubmitRenderRequest.html),
[ObjectIdResult](Rendering.ObjectIdResult.html).

    
    
    using UnityEngine;
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;
    using UnityEngine.Rendering;  
      
    // Snapshot containing the object at each pixel from the perspective of the camera.
    // The snapshot is taken when this class is constructed.
    class ObjectIdSnapshot
    {
        [Texture2D](Texture2D.html) m_ObjectIdTexture;
        Object[] m_IdToObjectMapping;  
      
        public ObjectIdSnapshot([Camera](Camera.html) camera)
        {
            var cameraTargetTexture = camera.targetTexture;
            var renderTexture = new [RenderTexture](RenderTexture.html)(
                width: cameraTargetTexture.width,
                height: cameraTargetTexture.height,
                colorFormat: [GraphicsFormat.R8G8B8A8_UNorm](Experimental.Rendering.GraphicsFormat.R8G8B8A8_UNorm.html),
                depthStencilFormat: [GraphicsFormat.D32_SFloat](Experimental.Rendering.GraphicsFormat.D32_SFloat.html));  
      
            var objectIdRequest = new [ObjectIdRequest](Rendering.ObjectIdRequest.html)(destination: renderTexture);
            camera.SubmitRenderRequest(objectIdRequest);
            m_ObjectIdTexture = ConvertTexture(objectIdRequest.destination);
            m_IdToObjectMapping = objectIdRequest.result.idToObjectMapping;
        }  
      
        public [GameObject](GameObject.html) GetGameObjectAtPixel(int x, int y)
        {
            var color = m_ObjectIdTexture.GetPixel(x, y);
            var id = [ObjectIdResult.DecodeIdFromColor](Rendering.ObjectIdResult.DecodeIdFromColor.html)(color);
            var obj = m_IdToObjectMapping[id];
            return GetParentGameObject(obj);
        }  
      
        static [GameObject](GameObject.html) GetParentGameObject(Object obj)
        {
            if (obj is null)
            {
                return null;
            }
            if (obj is [GameObject](GameObject.html) gameObject)
            {
                return gameObject;
            }
            if (obj is [MonoBehaviour](MonoBehaviour.html) component)
            {
                return component.gameObject;
            }
            return null;
        }  
      
        static [Texture2D](Texture2D.html) ConvertTexture([RenderTexture](RenderTexture.html) renderTexture)
        {
            var previousActiveRenderTexture = [RenderTexture.active](RenderTexture-active.html);
            [RenderTexture.active](RenderTexture-active.html) = renderTexture;
            var cpuTexture = new [Texture2D](Texture2D.html)(renderTexture.width, renderTexture.height, renderTexture.graphicsFormat, [TextureCreationFlags.None](Experimental.Rendering.TextureCreationFlags.None.html));
            cpuTexture.ReadPixels(new [Rect](Rect.html)(0, 0, renderTexture.width, renderTexture.height), 0, 0);
            cpuTexture.Apply();
            [RenderTexture.active](RenderTexture-active.html) = previousActiveRenderTexture;
            return cpuTexture;
        }
    }
    

### Properties

[destination](Rendering.ObjectIdRequest-destination.html)| RenderTexture to
store the rendering result of the request. The colors in this RenderTexture
can be decoded to determine the object that was rendered at each pixel, first
by decoding the color to an index using ObjectIdResult.DecodeIdFromColor and
then by looking this index up in ObjectIdResult._idToObjectMapping.  
---|---  
[face](Rendering.ObjectIdRequest-face.html)| Target Cubemap face to store the
rendering result.  
[mipLevel](Rendering.ObjectIdRequest-mipLevel.html)| Target mipLevel to store
the rendering output.  
[result](Rendering.ObjectIdRequest-result.html)| A result field that is filled
when the render request has been submitted and completed, containing the
ObjectIdResult._idToObjectMapping that is needed to interpret the color-
encoded object IDs that are rendered in the ObjectIdRequest._destination
RenderTexture.  
[slice](Rendering.ObjectIdRequest-slice.html)| Target slice to store the
rendering output.  
  
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

