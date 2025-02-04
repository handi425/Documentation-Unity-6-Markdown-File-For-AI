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
[IExternalCodeEditor](Unity.CodeEditor.IExternalCodeEditor.html).TryGetInstallationForPath

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

public bool TryGetInstallationForPath(string editorPath, out
[Unity.CodeEditor.CodeEditor.Installation](Unity.CodeEditor.CodeEditor.Installation.html)
installation);

### Parameters

editorPath | The absolute path of the chosen code editor.  
---|---  
installation | To store the resulting [Installation](Unity.CodeEditor.CodeEditor.Installation.html). If return value is false, this result is ignored.  
  
### Returns

**bool** Whether this
[IExternalCodeEditor](Unity.CodeEditor.IExternalCodeEditor.html) can support
the **editorPath** implementation.

### Description

Unity stores the path of the chosen editor. An instance of
[IExternalCodeEditor](Unity.CodeEditor.IExternalCodeEditor.html) can take
responsibility for this path, by returning true when this method is being
called. The `out` variable **installation** need to be constructed with the
path and the name that should be shown in the "External Tools" code editor
list.

For supported code editor paths, this function sets the output variable
**installation** to an instance of
[Installation](Unity.CodeEditor.CodeEditor.Installation.html) which describes
the name that appears in the Editor Preference > Editor Tool section.

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

