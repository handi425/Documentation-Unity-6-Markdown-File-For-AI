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

#  [TextureImporter](TextureImporter.html).ignoreMipmapLimit

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

public bool ignoreMipmapLimit;

### Description

Enable this flag for textures that should ignore mipmap limit settings.

This has no effect if the [textureShape](TextureImporter-textureShape.html) is
not `Texture2D` or `Texture2DArray`. Also, this has no effect on textures
without mipmaps. For additional information, see
[Texture2D.ignoreMipmapLimit](Texture2D-ignoreMipmapLimit.html) and
[Texture2DArray.ignoreMipmapLimit](Texture2DArray-ignoreMipmapLimit.html). By
default, an imported texture asset has mipmap limits enabled, and uses the
global mipmap limit. If you imported a Texture2DArray asset in Unity version
2023.1 or earlier, the asset will continue to ignore mipmap limits to ensure
consistent behavior when upgrading.  
  
Note that imported textures have mipmap limits enabled by default. This code
example demonstrates how to use an AssetPostprocessor to explicitly ignore the
mipmap limit.

    
    
    #if UNITY_EDITOR
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleImporter : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPreprocessTexture()
        {
            if (assetPath.Contains("_IgnoreMipmapLimit"))
            {
                [TextureImporter](TextureImporter.html) textureImporter = ([TextureImporter](TextureImporter.html))assetImporter;
                textureImporter.ignoreMipmapLimit = true;
            }
        }
    }
    #endif

Additional resources:
[Texture2D.ignoreMipmapLimit](Texture2D-ignoreMipmapLimit.html),
[Texture2DArray.ignoreMipmapLimit](Texture2DArray-ignoreMipmapLimit.html),
[mipmapEnabled](TextureImporter-mipmapEnabled.html).

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

