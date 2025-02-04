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

#  [Texture2D](Texture2D.html).activeMipmapLimit

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

public int activeMipmapLimit;

### Description

The number of high resolution mipmap levels from the texture that Unity
doesn't upload to the GPU. (Read Only)

Unity takes a texture's mipmap limit settings into account to determine its
active mipmap limit that affects how many texture mipmap levels are uploaded
to the GPU. This property provides the active number of texture mipmap levels
that Unity didn't upload to the GPU. This number is relative to the number of
texture mipmap levels included in the build.  
  
Unity ensures that a certain platform-dependent number of mipmap levels are
always uploaded regardless of the texture's mipmap limit. `activeMipmapLimit`
can therefore be smaller than expected in certain cases.  
  
When [PlayerSettings.mipStripping](PlayerSettings-mipStripping.html) is
enabled, which strips mipmap levels from textures, `activeMipmapLimit` returns
a limit that accounts for the number of mipmap levels stripped. For example, a
texture with 3 stripped mipmap levels and an applicable
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html) value of 3 has a `activeMipmapLimit` value of
0. This value is because the number of mipmap levels that Unity uploads to the
GPU is the same as the number of mipmap levels included in the build.  
  
`activeMipmapLimit` also reflects any downscale fallbacks applied by
EditorUserBuildSettings.androidETC2Fallback or
[AndroidETC2FallbackOverride](AndroidETC2FallbackOverride.html).  
  
The following code example demonstrates how you can use `activeMipmapLimit` to
perform a [Graphics.CopyTexture](Graphics.CopyTexture.html) operation on the
GPU to copy the highest resolution mipmap level of a texture that uses mipmap
limits to a new texture that does not use mipmap limits.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using UnityEngine.Experimental.Rendering;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)] [Texture2D](Texture2D.html) m_SourceTexture;  
      
        public void ExecuteCopyTexture()
        {
            if (([SystemInfo.copyTextureSupport](SystemInfo-copyTextureSupport.html) & [CopyTextureSupport.Basic](Rendering.CopyTextureSupport.Basic.html)) == 0)
            {
                [Debug.LogError](Debug.LogError.html)("Cannot perform CopyTexture, there is no support on this platform.");
                return;
            }  
      
            if (![SystemInfo.IsFormatSupported](SystemInfo.IsFormatSupported.html)(m_SourceTexture.graphicsFormat, [GraphicsFormatUsage.Sample](Experimental.Rendering.GraphicsFormatUsage.Sample.html)))
            {
                [Debug.LogError](Debug.LogError.html)("Cannot perform CopyTexture, the source texture's [GraphicsFormat](Experimental.Rendering.GraphicsFormat.html) is not supported on this platform.");
                return;
            }  
      
            // The width and height of the texture in the build need to be halved for each mipmap level that wasn't uploaded to the GPU
            int width = m_SourceTexture.width >> m_SourceTexture.activeMipmapLimit;
            int height = m_SourceTexture.height >> m_SourceTexture.activeMipmapLimit;  
      
            // No mipmap limit applies because the texture doesn't have mipmaps.
            [Texture2D](Texture2D.html) destinationTexture = new [Texture2D](Texture2D.html)(width, height, m_SourceTexture.format, false);  
      
            // GPU copy of the mipmap level 0 to the mipmap level 0 of the destination texture.
            // The mipmap level 0 on the GPU is smaller than the mipmap level 0 of the texture in the build when m_SourceTexture.activeMipmapLimit is greater than 0.
            [Graphics.CopyTexture](Graphics.CopyTexture.html)(m_SourceTexture, 0, 0, 0, 0, m_SourceTexture.width, m_SourceTexture.height, destinationTexture, 0, 0, 0, 0);
        }
    }
    

Additional resources:
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html),
[mipmapLimitGroup](Texture2D-mipmapLimitGroup.html),
[ignoreMipmapLimit](Texture2D-ignoreMipmapLimit.html).

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

