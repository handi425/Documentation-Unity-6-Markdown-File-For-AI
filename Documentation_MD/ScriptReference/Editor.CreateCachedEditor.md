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

#  [Editor](Editor.html).CreateCachedEditor

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

public static void CreateCachedEditor([Object](Object.html) targetObject, Type
editorType, ref [Editor](Editor.html) previousEditor);

## Declaration

public static void CreateCachedEditor(Object[] targetObjects, Type editorType,
ref [Editor](Editor.html) previousEditor);

### Parameters

obj | The object the editor is tracking.  
---|---  
editorType | The requested editor type. Set to null for the default editor for the object.  
previousEditor | The previous editor for the object. After returning from CreateCachedEditor `previousEditor` is an editor for the `targetObject` or `targetObjects`.  
objects | The objects the editor is tracking.  
  
### Description

On return `previousEditor` is an editor for `targetObject` or `targetObjects`.
The function either returns if the editor is already tracking the objects, or
destroys the previous editor and creates a new one.

By default, the editor with a matching CustomEditor attribute is created. If
an editorType is specified, an editor of that type is created instead. Use
this if you have created multiple custom editors where each editor shows
different properties of the object. previousEditor will be NULL if `objects`
are of different types or if no approprate editor was found.

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

