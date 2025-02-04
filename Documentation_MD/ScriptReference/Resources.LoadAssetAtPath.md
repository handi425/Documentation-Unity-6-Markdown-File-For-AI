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

**Removed**  

#  [Resources](Resources.html).LoadAssetAtPath

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

**Obsolete** Use AssetDatabase.LoadAssetAtPath instead.  
**Upgrade to[LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)**

## Declaration

public static Object LoadAssetAtPath(string assetPath, Type type);

### Parameters

assetPath | Pathname of the target asset.  
---|---  
type | Type filter for objects returned.  
  
### Description

Returns a resource at an asset path (Editor Only).

This function always return null in the standalone player or web player. This
is useful for quickly accessing an asset for use in the editor only.  
  
**Note:** All asset names and paths in Unity use forward slashes, paths using
backslashes will **not** work.  
This returns only asset object that is visible in the Project view.  
  
Resources.LoadAssetAtPath is deprecated. Use
[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html) instead.  
  
Note that web player is not supported from 5.4.0 onwards.

* * *

**Obsolete** Use AssetDatabase.LoadAssetAtPath<T>() instead.  
**Upgrade to[LoadAssetAtPath<T>](AssetDatabase.LoadAssetAtPath<T>.html)**

## Declaration

public static T LoadAssetAtPath(string assetPath);

### Parameters

assetPath | Pathname of the target asset.  
---|---  
  
### Description

Returns a resource at an asset path (Editor Only).

This function always return null in the standalone player or web player. This
is useful for quickly accessing an asset for use in the editor only.  
  
**Note:** All asset names and paths in Unity use forward slashes, paths using
backslashes will **not** work.  
This returns only asset object that is visible in the Project view.  
  
Note that web player is not supported from 5.4.0 onwards.

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

