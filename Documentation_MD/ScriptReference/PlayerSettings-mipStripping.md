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

#  [PlayerSettings](PlayerSettings.html).mipStripping

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

public static bool mipStripping;

### Description

Enable mip stripping for all platforms.

If you enable this setting, Unity strips unused mips at build time.  
  
When Unity builds your game or application, it can strip unused mips from
textures in your Project. Stripping unused mips can make the resulting
executable smaller. The top mip for any mip chain contributes 75% of the size
on disk, so mip stripping can save disk space and improve download times.  
  
If you enable Mip Stripping, Unity examines the Quality Settings for the
current platform at build time. If a mip level is excluded from every Quality
Setting for the current platform, Unity strips those mips from the build.  
  
Mip Stripping depends on the
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html) and
[TextureMipmapLimitGroups](TextureMipmapLimitGroups.html) setup, and it will
only affect textures that are also affected by mipmap limits.  
  
For example, for any platform in a project, if you do the following:

  * Set **Global Mipmap Limit** (QualitySettings.globalTextureMipmapLimit) to **Half Resolution** (1) or lower resolution for every Quality level on that platform 
  * Enable **Texture Mipmap Stripping**

then every readonly Texture2D in the project will be built without mips higher
than the Global Mipmap Limit level. If
QualitySettings.globalTextureMipmapLimit is set to Full Resolution (0) for any
quality level, the Mip Stripping setting won't do anything.
![](../StaticFiles/ScriptRefImages/mipmap-stripping.png)  
  
At run time, if you use
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html) or
[QualitySettings.SetTextureMipmapLimitSettings](QualitySettings.SetTextureMipmapLimitSettings.html)
to set a mip level that has been stripped, Unity sets the value to the closest
mip level that has not been stripped.  
  
However, you need to be aware of the following:

  * Texture Mip Stripping is not compatible with crunch compressed textures, due to the non-constant compression ratio of this compression format. 
  * Use caution if you use functionality such as [the mipmap streaming API](../Manual/TextureStreaming-API.html), [Texture.width](Texture-width.html) or [Texture.mipmapCount](Texture-mipmapCount.html) as they do not reflect the texture's original state once mips have been stripped. For example, for a 1024x1024 texture, a [Texture2D.desiredMipmapLevel](Texture2D-desiredMipmapLevel.html) value of 0 in the Editor refers to a 1024x1024 mip. If we stripped 2 mips at build time from that same texture, a Texture2D.desiredMipmaplevel value of 0 refers to a 256x256 mip in the Player. 

  
  
For information on how to get Unity to ignore the Mipmap limit for a
particular texture, refer to
[TextureImporter.ignoreMipmapLimit](TextureImporter-ignoreMipmapLimit.html).

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

