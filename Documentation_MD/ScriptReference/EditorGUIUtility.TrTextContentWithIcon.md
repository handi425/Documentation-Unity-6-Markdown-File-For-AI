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

#  [EditorGUIUtility](EditorGUIUtility.html).TrTextContentWithIcon

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

public static [GUIContent](GUIContent.html) TrTextContentWithIcon(string text,
[Texture](Texture.html) icon);

## Declaration

public static [GUIContent](GUIContent.html) TrTextContentWithIcon(string text,
string iconName);

## Declaration

public static [GUIContent](GUIContent.html) TrTextContentWithIcon(string text,
string tooltip, string iconName);

## Declaration

public static [GUIContent](GUIContent.html) TrTextContentWithIcon(string text,
string tooltip, [Texture](Texture.html) icon);

## Declaration

public static [GUIContent](GUIContent.html) TrTextContentWithIcon(string text,
string tooltip, [MessageType](MessageType.html) messageType);

## Declaration

public static [GUIContent](GUIContent.html) TrTextContentWithIcon(string text,
[MessageType](MessageType.html) messageType);

### Parameters

text | The text associated with the [GUIContent.text](GUIContent-text.html).  
---|---  
icon | The icon associated with the [GUIContent.image](GUIContent-image.html).  
iconName | The name of the icon.  
tooltip | The tooltip to display when the cursor hovers over the icon.  
messageType | The type of the message to fetch the icon for.  
  
### Description

Gets the [GUIContent](GUIContent.html) from Unity built-in resources with the
given information or creates a [GUIContent](GUIContent.html) for a GUI
element.  
  
The text and the tooltip are localized and loaded with an icon.  
  
Typically, the icon from `Assets/Editor Default Resources/Icons` is fetched
using the icon name. Only the name of the icon, without the .png extension is
needed.  
  
If a message type is specified instead of an icon or an icon name, the
[GUIContent.image](GUIContent-image.html) is the icon associated with that
message type.

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

