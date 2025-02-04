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

#  [CommandBuffer](Rendering.CommandBuffer.html).SetShadowSamplingMode

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

public void
SetShadowSamplingMode([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
shadowmap, [Rendering.ShadowSamplingMode](Rendering.ShadowSamplingMode.html)
mode);

### Parameters

shadowmap | Shadowmap render target to change the sampling mode on.  
---|---  
mode | New sampling mode.  
  
### Description

Add a "set shadow sampling mode" command.

Shadowmap render textures are normally set up to be sampled with a comparison
filter - the sampler gets a shadow-space depth value of the screen pixel and
returns 0 or 1, depending on if the depth value in the shadowmap is smaller or
larger. That's the default
[ShadowSamplingMode.CompareDepths](Rendering.ShadowSamplingMode.CompareDepths.html)
mode and is used for rendering shadows.  
  
If you'd like to access the shadowmap values as in a regular texture, set the
sampling mode to
[ShadowSamplingMode.RawDepth](Rendering.ShadowSamplingMode.RawDepth.html).  
  
Shadowmap's sampling mode will be reverted to default after the the last
command in the current CommandBuffer.  
  
Check [SystemInfo.supportsRawShadowDepthSampling](SystemInfo-
supportsRawShadowDepthSampling.html) to verify if current runtime platform
supports sampling shadows this way. Notably, DirectX9 does not.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    [[RequireComponent](RequireComponent.html)(typeof([Camera](Camera.html)))]
    public class RawShadowmapDepth : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Light](Light.html) m_Light;
        [RenderTexture](RenderTexture.html) m_ShadowmapCopy;  
      
        void Start()
        {
            [RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html) shadowmap = [BuiltinRenderTextureType.CurrentActive](Rendering.BuiltinRenderTextureType.CurrentActive.html);
            m_ShadowmapCopy = new [RenderTexture](RenderTexture.html)(1024, 1024, 0);
            [CommandBuffer](Rendering.CommandBuffer.html) cb = new [CommandBuffer](Rendering.CommandBuffer.html)();  
      
            // Change shadow sampling mode for m_Light's shadowmap.
            cb.SetShadowSamplingMode(shadowmap, [ShadowSamplingMode.RawDepth](Rendering.ShadowSamplingMode.RawDepth.html));  
      
            // The shadowmap values can now be sampled normally - copy it to a different render texture.
            cb.Blit(shadowmap, new [RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)(m_ShadowmapCopy));  
      
            // Execute after the shadowmap has been filled.
            m_Light.AddCommandBuffer([LightEvent.AfterShadowMap](Rendering.LightEvent.AfterShadowMap.html), cb);  
      
            // Sampling mode is restored automatically after this command buffer completes, so shadows will render normally.
        }  
      
        void OnRenderImage([RenderTexture](RenderTexture.html) src, [RenderTexture](RenderTexture.html) dest)
        {
            // [Display](Display.html) the shadowmap in the corner.
            Camera.main.rect = new [Rect](Rect.html)(0, 0, 0.5f, 0.5f);
            [Graphics.Blit](Graphics.Blit.html)(m_ShadowmapCopy, dest);
            Camera.main.rect = new [Rect](Rect.html)(0, 0, 1, 1);
        }
    }
    

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

