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

#  [Texture2D](Texture2D.html).mipmapLimitGroup

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

public string mipmapLimitGroup;

### Description

The name of the texture mipmap limit group that this texture is associated
with. (Read Only)

If this texture has a mipmap limit group assignment, this texture respects the
[TextureMipmapLimitSettings](TextureMipmapLimitSettings.html) of that group.
If this texture does not have a group assignment, or the indicated group does
not exist, this texture takes the
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html) instead. If you construct or import this
texture, assign it to a mipmap limit group that does not yet exist, then
create that mipmap limit group, this texture respects the
[TextureMipmapLimitSettings](TextureMipmapLimitSettings.html) of that new
group.  
  
Set this property in the constructor or in the texture importer, because you
cannot set this property after creating the texture. If the texture has no
mipmaps, this property has no effect.  
  
This code example demonstrates how to set this property in both the Texture2D
constructor and AssetPostprocessor.

    
    
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;
    #if UNITY_EDITOR
    using [UnityEditor](UnityEditor.html);
    #endif  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            const int size = 32;
            [Texture2D](Texture2D.html) scriptTexture = new [Texture2D](Texture2D.html)(size, size, [GraphicsFormat.R8G8B8A8_SRGB](Experimental.Rendering.GraphicsFormat.R8G8B8A8_SRGB.html), [Texture.GenerateAllMips](Texture.GenerateAllMips.html), "MyGroup", [TextureCreationFlags.MipChain](Experimental.Rendering.TextureCreationFlags.MipChain.html));
            [Debug.Log](Debug.Log.html)($"mipmapLimitGroup has been set to '{scriptTexture.mipmapLimitGroup}' on the script texture!");
        }
    }  
      
    #if UNITY_EDITOR
    public class ExampleImporter : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPreprocessTexture()
        {
            if (assetPath.Contains("_MyGroup"))
            {
                [TextureImporter](TextureImporter.html) textureImporter = ([TextureImporter](TextureImporter.html))assetImporter;
                textureImporter.mipmapLimitGroupName = "MyGroup";
            }
        }
    }
    #endif
    

Additional resources:
[TextureMipmapLimitGroups](TextureMipmapLimitGroups.html),
[TextureImporter.mipmapLimitGroupName](TextureImporter-
mipmapLimitGroupName.html).

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

