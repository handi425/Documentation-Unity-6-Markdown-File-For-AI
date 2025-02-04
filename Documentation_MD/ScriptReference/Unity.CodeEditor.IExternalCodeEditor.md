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

# IExternalCodeEditor

interface in Unity.CodeEditor

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

Defines the responsibilities of handling external script editor integration
into UnityEditor.

### Properties

[Installations](Unity.CodeEditor.IExternalCodeEditor.Installations.html)|
Provide the editor with a list of known and supported editors that this
instance supports.  
---|---  
  
### Public Methods

[Initialize](Unity.CodeEditor.IExternalCodeEditor.Initialize.html)| Callback
to the IExternalCodeEditor when it has been chosen from the PreferenceWindow.  
---|---  
[OnGUI](Unity.CodeEditor.IExternalCodeEditor.OnGUI.html)| Unity calls this
method when it populates "Preferences/External Tools" in order to allow the
code editor to generate necessary GUI. For example, when creating an an
argument field for modifying the arguments sent to the code editor.  
[OpenProject](Unity.CodeEditor.IExternalCodeEditor.OpenProject.html)| The
external code editor needs to handle the request to open a file.  
[SyncAll](Unity.CodeEditor.IExternalCodeEditor.SyncAll.html)| Unity calls this
function during initialization in order to sync the Project. This is different
from SyncIfNeeded in that it does not get a list of changes.  
[SyncIfNeeded](Unity.CodeEditor.IExternalCodeEditor.SyncIfNeeded.html)| When
you change Assets in Unity, this method for the current chosen instance of
IExternalCodeEditor parses the new and changed Assets.  
[TryGetInstallationForPath](Unity.CodeEditor.IExternalCodeEditor.TryGetInstallationForPath.html)|
Unity stores the path of the chosen editor. An instance of IExternalCodeEditor
can take responsibility for this path, by returning true when this method is
being called. The out variable installation need to be constructed with the
path and the name that should be shown in the "External Tools" code editor
list.  
  
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

