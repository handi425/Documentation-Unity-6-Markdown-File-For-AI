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

#  [TextureMipmapLimitGroups](TextureMipmapLimitGroups.html).RemoveGroup

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

public static void RemoveGroup(string groupName);

### Parameters

groupName | Name of the texture mipmap limit group to remove.  
---|---  
  
### Description

(Editor Only) Attempts to remove a texture mipmap limit group with the
indicated `groupName`.

This operation fails and throws an exception if `groupName` is null or there
is no texture mipmap limit group named `groupName`. If Unity finds a matching
group, Unity removes it from all quality levels.  
  
Unity does not modify textures bound to the removed group. These textures
continue to point to the removed group as long as you do not update and re-
import them yourself. If you do not adjust the relevant textures, they
automatically fall back to the global texture mipmap limit.

    
    
    #if UNITY_EDITOR
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Attempts to remove the texture mipmap limit group "MyGroup", if it exists in the project.
        [[MenuItem](MenuItem.html)("MyMenu/Remove TextureMipmapLimitGroup")]
        static void RemoveMyGroup()
        {
            const string textureMipmapLimitGroupName = "MyGroup";
            if ([TextureMipmapLimitGroups.HasGroup](TextureMipmapLimitGroups.HasGroup.html)(textureMipmapLimitGroupName))
            {
                [TextureMipmapLimitGroups.RemoveGroup](TextureMipmapLimitGroups.RemoveGroup.html)(textureMipmapLimitGroupName);
            }
            else
            {
                [Debug.LogError](Debug.LogError.html)($"Cannot remove texture mipmap limit group '{textureMipmapLimitGroupName}' as it does not exist!");
            }
        }
    }
    #endif
    

Additional resources: [HasGroup](TextureMipmapLimitGroups.HasGroup.html),
[CreateGroup](TextureMipmapLimitGroups.CreateGroup.html).

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

