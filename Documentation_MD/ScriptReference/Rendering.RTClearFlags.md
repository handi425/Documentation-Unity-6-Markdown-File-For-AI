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

# RTClearFlags

enumeration

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

Flags that determine which render targets Unity clears when you use
[CommandBuffer.ClearRenderTarget](Rendering.CommandBuffer.ClearRenderTarget.html).

You can combine flags by using the bitwise OR operator.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    // Attach this script to a [Camera](Camera.html) and select a Clear [Mode](Scripting.GarbageCollector.Mode.html).
    // When you enter Play mode, a command buffer clears the screen with different clear parameters.
    [[RequireComponent](RequireComponent.html)(typeof([Camera](Camera.html)))]
    public class MyClearScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public enum ClearMode
        {
            All,
            ColorStencil
        }  
      
        public ClearMode m_ClearMode;  
      
        void Start()
        {
            var camera = GetComponent<[Camera](Camera.html)>();
            var buffer = new [CommandBuffer](Rendering.CommandBuffer.html)();  
      
            switch (m_ClearMode)
            {
                case ClearMode.All:
                    // Clear color, depth and stencil render targets. Stencil is cleared with value 0xF0.
                    buffer.ClearRenderTarget([RTClearFlags.All](Rendering.RTClearFlags.All.html), [Color.red](Color-red.html), 1.0f, 0xF0);
                    break;
                case ClearMode.ColorStencil:
                    // Clear only color and stencil render targets. Stencil is cleared with value 0xF0.
                    buffer.ClearRenderTarget(([RTClearFlags](Rendering.RTClearFlags.html))((int)[RTClearFlags.Color](Rendering.RTClearFlags.Color.html) | (int)[RTClearFlags.Stencil](Rendering.RTClearFlags.Stencil.html)), [Color.green](Color-green.html), 1.0f, 0xF0);
                    break;
            }  
      
            camera.AddCommandBuffer([CameraEvent.AfterSkybox](Rendering.CameraEvent.AfterSkybox.html), buffer);
        }
    }
    

### Properties

[None](Rendering.RTClearFlags.None.html)| Do not clear any render target.  
---|---  
[Color](Rendering.RTClearFlags.Color.html)| Clear all color render targets.  
[Depth](Rendering.RTClearFlags.Depth.html)| Clear the depth buffer.  
[Stencil](Rendering.RTClearFlags.Stencil.html)| Clear the stencil buffer.  
[All](Rendering.RTClearFlags.All.html)| Clear all color render targets, the
depth buffer, and the stencil buffer. This is equivalent to combining
RTClearFlags.Color, RTClearFlags.Depth and RTClearFlags.Stencil.  
[DepthStencil](Rendering.RTClearFlags.DepthStencil.html)| Clear both the depth
and the stencil buffer. This is equivalent to combining RTClearFlags.Depth and
RTClearFlags.Stencil.  
[ColorDepth](Rendering.RTClearFlags.ColorDepth.html)| Clear both the color and
the depth buffer. This is equivalent to combining RTClearFlags.Color and
RTClearFlags.Depth.  
[ColorStencil](Rendering.RTClearFlags.ColorStencil.html)| Clear both the color
and the stencil buffer. This is equivalent to combining RTClearFlags.Color and
RTClearFlags.Stencil.  
  
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

