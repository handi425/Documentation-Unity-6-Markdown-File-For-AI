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

# TextureGenerationSettings

struct in UnityEditor.AssetImporters

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

Represents how a texture should be generated from calling
[TextureGenerator.GenerateTexture](AssetImporters.TextureGenerator.GenerateTexture.html).

### Properties

[assetPath](AssetImporters.TextureGenerationSettings-assetPath.html)| Path
where the Asset will be placed.  
---|---  
[enablePostProcessor](AssetImporters.TextureGenerationSettings-
enablePostProcessor.html)| When set to true, the AssetPostprocessor hooks will
be called during texture generation. The following will hold for any
AssetPostprocessors triggered through TextureGenerator.GenerateTexture \- When
the postprocessor is invoked AssetPostprocessor.assetPath will be set to the
assetPath value in this structure. \- The value of AssetPostprocessor.context
will be set to null. \- Only OnPostprocessTexture, OnPostprocessCubemap, ...
is called. The OnPreprocessTexture functions are not called.  
[platformSettings](AssetImporters.TextureGenerationSettings-
platformSettings.html)| Platform settings for generating the texture.  
[qualifyForSpritePacking](AssetImporters.TextureGenerationSettings-
qualifyForSpritePacking.html)| Indicates if the Sprite generated can be used
for atlas packing.  
[secondarySpriteTextures](AssetImporters.TextureGenerationSettings-
secondarySpriteTextures.html)| Secondary textures for the generated Sprites.  
[sourceTextureInformation](AssetImporters.TextureGenerationSettings-
sourceTextureInformation.html)| Texture format for the image data.  
[spriteImportData](AssetImporters.TextureGenerationSettings-
spriteImportData.html)|  Sprite Asset generation data.  
[spritePackingTag](AssetImporters.TextureGenerationSettings-
spritePackingTag.html)| Tag used for Sprite packing.  
[textureImporterSettings](AssetImporters.TextureGenerationSettings-
textureImporterSettings.html)| Settings for generating texture.  
  
### Constructors

[TextureGenerationSettings](AssetImporters.TextureGenerationSettings-
ctor.html)| The Constructor initializes to most common value based on the
TetureImporterType you pass in.  
---|---  
  
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

