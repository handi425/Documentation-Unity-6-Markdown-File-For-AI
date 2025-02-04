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

#  [TextureImporter](TextureImporter.html).IsPlatformTextureFormatValid

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

public static bool
IsPlatformTextureFormatValid([TextureImporterType](TextureImporterType.html)
textureType, [BuildTarget](BuildTarget.html) target,
[TextureImporterFormat](TextureImporterFormat.html) currentFormat);

### Parameters

textureType | The TextureImporterType that the importer uses.  
---|---  
target | The platform that the setting targets, referred to as the BuilTarget.  
currentFormat | The TextureImporterFormat to validate.  
  
### Returns

**bool** Returns true if [TextureImporterFormat](TextureImporterFormat.html)
is valid and can be set. Returns false otherwise.

### Description

Validates [TextureImporterFormat](TextureImporterFormat.html) based on a
specified import type ([TextureImporterType](TextureImporterType.html)) and a
specified build target ([BuildTarget](BuildTarget.html).).

[TextureImporterFormat](TextureImporterFormat.html) is not available for all
platforms based on the [TextureImporterType](TextureImporterType.html) of a
given Texture. Use this method to check that the format set with
SetPlatformTextureSettings is a valid format.

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

