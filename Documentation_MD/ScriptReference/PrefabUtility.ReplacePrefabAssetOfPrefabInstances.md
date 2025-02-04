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

#  [PrefabUtility](PrefabUtility.html).ReplacePrefabAssetOfPrefabInstances

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

public static void ReplacePrefabAssetOfPrefabInstances(GameObject[]
prefabInstanceRoots, [GameObject](GameObject.html) prefabAssetRoot,
[InteractionMode](InteractionMode.html) mode);

## Declaration

public static void ReplacePrefabAssetOfPrefabInstances(GameObject[]
prefabInstanceRoots, [GameObject](GameObject.html) prefabAssetRoot,
[PrefabReplacingSettings](PrefabReplacingSettings.html) settings,
[InteractionMode](InteractionMode.html) mode);

### Parameters

prefabInstanceRoots | The Prefab instance roots that will have their Prefab Asset replaced.  
---|---  
prefabAssetRoot | The new Prefab Asset used for the Prefab instances.  
mode | The interaction mode used.  
settings | The settings used to control the details of the replacements.  
  
### Description

Replace the Prefab Asset for an array of Prefab instances that exists in
Scenes or for nested Prefab instances inside another Prefab.

This function is similar to the
[ReplacePrefabAssetOfPrefabInstance](PrefabUtility.ReplacePrefabAssetOfPrefabInstance.html)
method, except it will perform the operation on each of the Prefab instances
in the input.

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

