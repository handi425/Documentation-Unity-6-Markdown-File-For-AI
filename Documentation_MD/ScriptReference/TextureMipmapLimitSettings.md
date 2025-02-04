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

# TextureMipmapLimitSettings

struct in UnityEngine

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

Structure that represents texture mipmap limit settings.

This code example illustrates how to modify
[TextureMipmapLimitSettings](TextureMipmapLimitSettings.html) from script.

    
    
    #if UNITY_EDITOR
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("MyMenu/Modify MyGroup")]
        static void ModifyMyGroup()
        {
            const string textureMipmapLimitGroupName = "MyGroup";
            if ([TextureMipmapLimitGroups.HasGroup](TextureMipmapLimitGroups.HasGroup.html)(textureMipmapLimitGroupName))
            {
                [TextureMipmapLimitSettings](TextureMipmapLimitSettings.html) settings = [QualitySettings.GetTextureMipmapLimitSettings](QualitySettings.GetTextureMipmapLimitSettings.html)(textureMipmapLimitGroupName);  
      
                // For the currently active quality level, this group will now offset the Global [Texture](Texture.html) Mipmap Limit. (default behavior)
                settings.limitBiasMode = [TextureMipmapLimitBiasMode.OffsetGlobalLimit](TextureMipmapLimitBiasMode.OffsetGlobalLimit.html);  
      
                // Drop 1 extra mip. Assuming that the limitBias is now 1 and that the Global [Texture](Texture.html) Mipmap Limit is 1 as well (for example), then textures assigned to 'MyGroup' drop 2 mips in total.
                settings.limitBias++;  
      
                [QualitySettings.SetTextureMipmapLimitSettings](QualitySettings.SetTextureMipmapLimitSettings.html)(textureMipmapLimitGroupName, settings);
            }
            else
            {
                [Debug.LogError](Debug.LogError.html)($"Failed to modify settings, could not find texture mipmap limit group '{textureMipmapLimitGroupName}'!");
            }
        }
    }
    #endif
    

Additional resources:
[TextureMipmapLimitGroups](TextureMipmapLimitGroups.html),
[QualitySettings.GetTextureMipmapLimitSettings](QualitySettings.GetTextureMipmapLimitSettings.html),
[QualitySettings.SetTextureMipmapLimitSettings](QualitySettings.SetTextureMipmapLimitSettings.html).

### Properties

[limitBias](TextureMipmapLimitSettings-limitBias.html)| The new value to apply
on top of the global texture mipmap limit. Can act as an offset (default) or
an override to it.  
---|---  
[limitBiasMode](TextureMipmapLimitSettings-limitBiasMode.html)| Indicates
whether the limitBias functions as an offset to the global texture mipmap
limit or, instead, acts as an override to it.  
  
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

