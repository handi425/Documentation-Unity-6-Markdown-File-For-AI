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

#  [TextureMipmapLimitGroups](TextureMipmapLimitGroups.html).CreateGroup

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

public static void CreateGroup(string groupName);

### Parameters

groupName | Name of the new texture mipmap limit group.  
---|---  
  
### Description

(Editor Only) Attempts to create a texture mipmap limit group with the
indicated `groupName`.

This operation fails and throws an exception if `groupName` is null/empty or a
texture mipmap limit group with the same name already exists. If no other
group with the same name exists, Unity creates the new group across all
quality levels. By default, the new group mirrors the global texture mipmap
limit.  
  
If Unity creates the new group successfully, textures previously bound to
`groupName` stop using
[QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html) as a fallback and begin respecting the new
group's [TextureMipmapLimitSettings](TextureMipmapLimitSettings.html) instead.

    
    
    #if UNITY_EDITOR
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Attempts to create a texture mipmap limit group with the name "MyGroup", as long as it doesn't exist already.
        [[MenuItem](MenuItem.html)("MyMenu/Create MipmapLimitGroup")]
        static void CreateMyGroup()
        {
            const string textureMipmapLimitGroup = "MyGroup";
            if (![TextureMipmapLimitGroups.HasGroup](TextureMipmapLimitGroups.HasGroup.html)(textureMipmapLimitGroup))
            {
                [TextureMipmapLimitGroups.CreateGroup](TextureMipmapLimitGroups.CreateGroup.html)(textureMipmapLimitGroup);
            }
            else
            {
                [Debug.LogError](Debug.LogError.html)($"Cannot create new texture mipmap limit group '{textureMipmapLimitGroup}', it already exists!");
            }
        }
    }
    #endif
    

Additional resources: [HasGroup](TextureMipmapLimitGroups.HasGroup.html),
[RemoveGroup](TextureMipmapLimitGroups.RemoveGroup.html).

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

