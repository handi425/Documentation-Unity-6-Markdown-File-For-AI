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

# EditorWindowTitleAttribute

class in UnityEditor

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

Use this class to set title text and icon for an Editor window.

Unity displays the text in the window's title bar. If the window is dockable,
Unity displays the text and icon in the window's tab. Icons must be .png
files. The recommended size is 16x16 pixels for regular icons, and 32x32
pixels for large variants used on HiDPI devices (see below). Icons can have
variants for different contexts. Variants must be in the same folder as the
default icon, and must have the same name, with specific text prepended or
appended. If a filename has `d_` prepended to its name (for example,
`d_MyWindowIcon.png`) Unity uses this icon instead of the default icon when
the Dark theme is enabled. If a variant has @2x appended to its name before
the file extension (for example, MyWindowIcon@2x.png), Unity uses this icon
when you run the Editor on HiDPI devices. Unity finds and uses variants
automatically. If it cannot find the variant it needs, it uses the next
closest variant. If no variants exist, Unity uses the default icon.

### Properties

[icon](EditorWindowTitleAttribute-icon.html)| Specifies the path to an Editor
window's default icon.  
---|---  
[title](EditorWindowTitleAttribute-title.html)| Specifies an Editor window's
title text.  
[useTypeNameAsIconName](EditorWindowTitleAttribute-
useTypeNameAsIconName.html)| When set to true Unity sets the window's icon
name to be the same as its type name.  
  
### Constructors

[EditorWindowTitleAttribute](EditorWindowTitleAttribute-ctor.html)| Creates
Editor window title content.  
---|---  
  
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

