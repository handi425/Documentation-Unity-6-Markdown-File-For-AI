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

#  [EditorStyles](EditorStyles.html).inspectorDefaultMargins

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

public static [GUIStyle](GUIStyle.html) inspectorDefaultMargins;

### Description

Wrap content in a vertical group with this style to get the default margins
used in the Inspector.

By default, content in the Inspector has a large left margin and a small right
margin. For a consistent look, these default margins should be used for most
GUI with regular controls.  
  
However, some special GUI elements may benefit from occupying the full width
of the Inspector, with only a small margin in both sides. To disable the
default margins, override the
[Editor.UseDefaultMargins](Editor.UseDefaultMargins.html) method in your
custom Editor. Then you can wrap your GUI content inside a vertical groups to
your liking. For example, you can wrap some of the GUI inside a vertical group
with the [EditorStyles.inspectorFullWidthMargins](EditorStyles-
inspectorFullWidthMargins.html) style and wrap other parts of the GUI inside a
vertical group with the [EditorStyles.inspectorDefaultMargins](EditorStyles-
inspectorDefaultMargins.html) style.  
  
Additional resources:
[EditorGUILayout.BeginVertical](EditorGUILayout.BeginVertical.html),
[EditorGUILayout.EndVertical](EditorGUILayout.EndVertical.html),
[Editor.UseDefaultMargins](Editor.UseDefaultMargins.html),
[EditorStyles.inspectorFullWidthMargins](EditorStyles-
inspectorFullWidthMargins.html).

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

