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

#  [GenericDropdownMenu](UIElements.GenericDropdownMenu.html).DropDown

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

public void DropDown([Rect](Rect.html) position,
[UIElements.VisualElement](UIElements.VisualElement.html) targetElement, bool
anchored);

### Parameters

position | The position in the coordinate space of the panel.  
---|---  
targetElement | The element determines which root to use as the menu's parent.  
anchored | If true, the menu's width matches the width of the `position`; otherwise, the menu expands to the container's full width.  
  
### Description

Displays the menu at the specified position.

The parent element that displays the menu:

  * For Editor UI, the parent element is [EditorWindow.rootVisualElement](EditorWindow-rootVisualElement.html).
  * For runtime UI, the parent element is [UIDocument.rootVisualElement](UIElements.UIDocument-rootVisualElement.html).

The `anchored` parameter determines the width of the menu. Refer to
[GenericDropdownMenu](UIElements.GenericDropdownMenu.html) for example usages.

* * *

## Declaration

public void DropDown([Rect](Rect.html) position,
[UIElements.VisualElement](UIElements.VisualElement.html) targetElement, bool
anchored, bool fitContentWidthIfAnchored);

### Parameters

position | The position in the coordinate space of the panel.  
---|---  
targetElement | The element determines which root to use as the menu's parent.  
anchored | If true, the menu's width matches the width of the `position`; otherwise, the menu expands to the container's full width.  
fitContentWidthIfAnchored | If true and the menu is anchored, the menu's width matches its content's width; otherwise, the menu's width matches the width of the `position`. If the menu is unanchored, this parameter is ignored.  
  
### Description

Displays the menu at the specified position.

The parent element that displays the menu:

  * For Editor UI, the parent element is [EditorWindow.rootVisualElement](EditorWindow-rootVisualElement.html).
  * For runtime UI, the parent element is [UIDocument.rootVisualElement](UIElements.UIDocument-rootVisualElement.html).

The `anchored` and `fitContentWidthIfAnchored` parameters determine the width
of the menu. Refer to
[GenericDropdownMenu](UIElements.GenericDropdownMenu.html) for example usages.

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

