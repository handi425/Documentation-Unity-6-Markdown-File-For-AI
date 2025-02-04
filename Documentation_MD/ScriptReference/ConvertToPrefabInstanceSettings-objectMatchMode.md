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
[ConvertToPrefabInstanceSettings](ConvertToPrefabInstanceSettings.html).objectMatchMode

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

public [ObjectMatchMode](ObjectMatchMode.html) objectMatchMode;

### Description

Use this property to control how GameObjects and Components are matched up or
not when converting a plain GameObject to a Prefab instance.

The root GameObject and its components will always be matched up regardless of
the ObjectMatchMode so a reference to the root GameObject will always be
retained regardless of ObjectMatchMode. Use
[ObjectMatchMode.ByHierarchy](ObjectMatchMode.ByHierarchy.html) which will
retain references if GameObjects and Components are matched up using their
full hierarchy path. In this mode you can use
[componentsNotMatchedBecomesOverride](ConvertToPrefabInstanceSettings-
componentsNotMatchedBecomesOverride.html) and
[gameObjectsNotMatchedBecomesOverride](ConvertToPrefabInstanceSettings-
gameObjectsNotMatchedBecomesOverride.html) to control what happens with
objects that are not matched up. Alternatively use
[ObjectMatchMode.ByName](ObjectMatchMode.ByName.html) will retain references
if individual GameObject names matches up. Note that the hierarchy of
GameObjects are ignored and only the GameObject name is used for matching.
Only if a GameObject have the same name and same Transform type as in the used
Prefab Asset then they are matched up. Components have their GameObject name
prefixed to their type name for the final name matching. If the name is found
more than once in the Prefab Asset or in the instance then the match cannot be
performed; the name must be unique in each GameObject hierarchy.

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

