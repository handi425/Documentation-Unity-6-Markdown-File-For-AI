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

**Method group is Obsolete**  

#  [PrefabUtility](PrefabUtility.html).ConnectGameObjectToPrefab

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

**Obsolete** Use ConvertToPrefabInstance() or
ReplacePrefabAssetOfPrefabInstance() which has settings for better control.

## Declaration

public static [GameObject](GameObject.html)
ConnectGameObjectToPrefab([GameObject](GameObject.html) go,
[GameObject](GameObject.html) sourcePrefab);

### Parameters

go | The disconnected GameObject that you want to reconnect.  
---|---  
sourcePrefab | The source Prefab to connect to the GameObject.  
  
### Description

Connects the source Prefab to the game object.

This method allows you to reconnect a GameObject to its source Prefab, when it
has become disconnected. Prior to 2018.3 it was possible for Prefab instances
to become disconnected from their source Prefab. This method fixes that
connection. From 2018.3 onwards, Prefabs cannot become disconnected, so this
method exists only to correct problems that may exist in projects created in
earlier versions of Unity.

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

