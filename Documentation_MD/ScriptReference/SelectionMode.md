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

# SelectionMode

enumeration

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

SelectionMode can be used to tweak the selection returned by
Selection.GetTransforms.

The default transform selection mode is: [SelectionMode.TopLevel](SelectionMode.TopLevel.html) | [SelectionMode.ExcludePrefab](SelectionMode.ExcludePrefab.html) | [SelectionMode.Editable](SelectionMode.Editable.html).

### Properties

[Unfiltered](SelectionMode.Unfiltered.html)| Return the whole selection.  
---|---  
[TopLevel](SelectionMode.TopLevel.html)| Only return the topmost selected
transform. A selected child of another selected transform will be filtered
out.  
[Deep](SelectionMode.Deep.html)| Return the selection and all child transforms
of the selection.  
[ExcludePrefab](SelectionMode.ExcludePrefab.html)| Excludes any Prefabs from
the selection.  
[Editable](SelectionMode.Editable.html)| Excludes any objects which shall not
be modified.  
[Assets](SelectionMode.Assets.html)| Only return objects that are assets in
the Asset directory.  
[DeepAssets](SelectionMode.DeepAssets.html)| If the selection contains
folders, also include all assets and subfolders within that folder in the file
hierarchy.  
  
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

