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

#  [PrefabUtility](PrefabUtility.html).ConvertToPrefabInstance

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

public static void ConvertToPrefabInstance([GameObject](GameObject.html)
plainGameObject, [GameObject](GameObject.html) prefabAssetRoot,
[ConvertToPrefabInstanceSettings](ConvertToPrefabInstanceSettings.html)
settings, [InteractionMode](InteractionMode.html) mode);

### Parameters

plainGameObject | The GameObject that will be converted to a Prefab instance.  
---|---  
prefabAssetRoot | The Prefab Asset used to create the Prefab instance from.  
settings | Settings to control the conversion.  
mode | Using UserAction will record undo and show dialogs if needed.  
  
### Description

Convert the plain GameObject to a Prefab instance using the provided Prefab
Asset root object.

This function will keep the root GameObject position, rotation and scale in
the Scene but merge the contents from the new Prefab Asset. When using
[ObjectMatchMode.ByName](ObjectMatchMode.ByName.html) object matching is
performed. When a match is found references to this object will survive the
conversion. Note that matching cannot be performed for GameObjects with
duplicate names in each of the input GameObject hierarchies.  
  
Additional resources:
[ConvertToPrefabInstances](PrefabUtility.ConvertToPrefabInstances.html),
[ReplacePrefabAssetOfPrefabInstance](PrefabUtility.ReplacePrefabAssetOfPrefabInstance.html).

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

