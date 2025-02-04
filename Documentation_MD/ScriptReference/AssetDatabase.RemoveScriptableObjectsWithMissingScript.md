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

#
[AssetDatabase](AssetDatabase.html).RemoveScriptableObjectsWithMissingScript

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

public static int RemoveScriptableObjectsWithMissingScript(string assetPath);

### Parameters

assetPath | The path to the asset file to check.  
---|---  
  
### Returns

**int** The number of ScriptableObject-derived objects in the file which were
removed.

### Description

Removes any ScriptableObject instances from the given asset file which cannot
be loaded because their scripts could not be found.

If you delete the script which defines a type of ScriptableObject, all
instances of that ScriptableObject in your assets become unloadable. This also
happens if you move or rename the script outside of Unity without also moving
or renaming the script's .meta file accordingly. This method allows you to
remove any such unloadable ScriptableObject instances from an asset. You can
check whether there are unloadable ScriptableObject instances in your assets
without removing them, by using
[AssetDatabase.GetScriptableObjectsWithMissingScriptCount](AssetDatabase.GetScriptableObjectsWithMissingScriptCount.html).  
  
Note: This function can only be used with [native asset
files](AssetDatabase.IsNativeAsset.html). If you pass a non-native asset file,
it will throw an exception.  
  
You must call [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html) to
save the changes to your asset, after using this method.  
  
Additional resources:
[AssetDatabase.GetScriptableObjectsWithMissingScriptCount](AssetDatabase.GetScriptableObjectsWithMissingScriptCount.html),
[GameObjectUtility.RemoveMonoBehavioursWithMissingScript](GameObjectUtility.RemoveMonoBehavioursWithMissingScript.html).

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

