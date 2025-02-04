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

#  [TextureImporter](TextureImporter.html).SetPlatformTextureSettings

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

[Switch to Manual](../Manual/class-TextureImporter.html "Go to TextureImporter
Component in the Manual")

## Declaration

public void
SetPlatformTextureSettings([TextureImporterPlatformSettings](TextureImporterPlatformSettings.html)
platformSettings);

### Parameters

platformSettings | A [TextureImporterPlatformSettings](TextureImporterPlatformSettings.html) instance that contains the platform settings.  
---|---  
  
### Description

Sets specific target platform settings.

Setup the parameters for a specific platform as described in
[TextureImporterPlatformSettings](TextureImporterPlatformSettings.html).

* * *

**Obsolete** Use
UnityEditor.TextureImporter.SetPlatformTextureSettings(TextureImporterPlatformSettings)
instead.

## Declaration

public void SetPlatformTextureSettings(string platform, int maxTextureSize,
[TextureImporterFormat](TextureImporterFormat.html) textureFormat);

**Obsolete** Use
UnityEditor.TextureImporter.SetPlatformTextureSettings(TextureImporterPlatformSettings)
instead.

## Declaration

public void SetPlatformTextureSettings(string platform, int maxTextureSize,
[TextureImporterFormat](TextureImporterFormat.html) textureFormat, bool
allowsAlphaSplit = False);

**Obsolete** Use
UnityEditor.TextureImporter.SetPlatformTextureSettings(TextureImporterPlatformSettings)
instead.

## Declaration

public void SetPlatformTextureSettings(string platform, int maxTextureSize,
[TextureImporterFormat](TextureImporterFormat.html) textureFormat, int
compressionQuality, bool allowsAlphaSplit);

### Parameters

platform | The platforms whose settings are to be changed (see below).  
---|---  
maxTextureSize | Maximum texture width/height in pixels.  
textureFormat | Data format for the texture.  
allowsAlphaSplit | Allows splitting of imported texture into RGB+A so that ETC1 compression can be applied (Android only, and works only on textures that are a part of some atlas).  
compressionQuality | Value from 0..100, with 0, 50 and 100 being respectively Fast, Normal, Best quality options in the texture importer UI. For Crunch texture formats, this roughly corresponds to JPEG quality levels.  
  
### Description

Sets specific target platform settings.

The options for the `platform` string are as follows:

  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS

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

