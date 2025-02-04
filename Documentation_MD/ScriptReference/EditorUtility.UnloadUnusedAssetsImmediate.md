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

#  [EditorUtility](EditorUtility.html).UnloadUnusedAssetsImmediate

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

public static void UnloadUnusedAssetsImmediate();

## Declaration

public static void UnloadUnusedAssetsImmediate(bool
includeMonoReferencesAsRoots);

### Parameters

includeMonoReferencesAsRoots | When true, this method does not unload assets referenced by script properties and static variables.  
---|---  
  
### Description

Unloads assets that are not used.

An asset is deemed to be unused if it isn't reached after walking the whole
game object hierarchy, including script components. Static variables are also
examined.  
  
Set the `includeMonoReferencesAsRoots` parameter to false to ignore asset
references from script properties and static variables. The unloaded assets
load again on first use. This parameter is true by default.  
  
This method differs from
[Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html) in that it
will wait for asset garbage collection to finish before returning.  
  
Additional resources:
[Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html).

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

