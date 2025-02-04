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

# IApplyRevertPropertyContextMenuItemProvider

interface in UnityEditor

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

### Description

Used to identify a [MonoBehaviour](MonoBehaviour.html) that provides a hook
into the apply/revert context menu for Prefabs open in Prefab Mode and non
Prefabs.

Any prefab instance with overrides displays Apply/Revert context menu items
when a user right clicks on a prefab override property in the inspector.  
  
This interface provides an extension hook to that prefab override builtin
behaviour for prefabs in edit mode.

### Public Methods

[GetSourceName](IApplyRevertPropertyContextMenuItemProvider.GetSourceName.html)|
Returns the component specific name to be used in the apply menu item.  
---|---  
[GetSourceTerm](IApplyRevertPropertyContextMenuItemProvider.GetSourceTerm.html)|
Returns the name of the source term to be used in the apply/revert menu item.  
[TryGetApplyMethodForFieldName](IApplyRevertPropertyContextMenuItemProvider.TryGetApplyMethodForFieldName.html)|
Extension hook for an optional property apply menu item.  
[TryGetRevertMethodForFieldName](IApplyRevertPropertyContextMenuItemProvider.TryGetRevertMethodForFieldName.html)|
Extension hook for an optional property revert menu item.  
  
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

