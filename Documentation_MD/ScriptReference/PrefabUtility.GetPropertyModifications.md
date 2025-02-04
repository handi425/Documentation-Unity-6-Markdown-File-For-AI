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

#  [PrefabUtility](PrefabUtility.html).GetPropertyModifications

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

public static PropertyModification[]
GetPropertyModifications([Object](Object.html) targetPrefab);

### Parameters

targetPrefab | Can be a Prefab instance in the scene or a Prefab instance in an Prefab Asset (e.g a Variant asset).  
---|---  
  
### Description

Returns all modifications that have been applied to a particular Prefab
instance in a Scene or modifications for a Prefab instance in an Asset.  
  
See [SetPropertyModifications](PrefabUtility.SetPropertyModifications.html)
for details about the fields of the returned
[PropertyModification](PropertyModification.html) objects.  
  
An alternative approach to getting property overrides information for a Prefab
instance is to use the
[GetObjectOverrides](PrefabUtility.GetObjectOverrides.html) API which also has
Apply and Revert functionality.  
  
When using GetPropertyModifications bear in mind that:

  * it will return both default and non-default overrides
  * It can return overrides for all child GameObjects and their Components
  * it can return overrides that are no longer valid.

Additional resources:
[GetObjectOverrides](PrefabUtility.GetObjectOverrides.html)
[GetAddedComponents](PrefabUtility.GetAddedComponents.html)
[GetRemovedComponents](PrefabUtility.GetRemovedComponents.html)
[GetAddedGameObjects](PrefabUtility.GetAddedGameObjects.html)
[GetRemovedGameObjects](PrefabUtility.GetRemovedGameObjects.html).

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

