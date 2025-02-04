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

# CodeEditor

class in Unity.CodeEditor

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

Handles interaction with the code editor.

### Static Properties

[CurrentEditorPath](Unity.CodeEditor.CodeEditor.CurrentEditorPath.html)| The
path to the external code editor that Unity uses used to open script assets.  
---|---  
[Editor](Unity.CodeEditor.CodeEditor.Editor.html)| A singleton instance of
CodeEditor. The Unity Editor references this instance to handle code editor
callbacks.  
  
### Properties

[CurrentCodeEditor](Unity.CodeEditor.CodeEditor.CurrentCodeEditor.html)|
Returns the current IExternalCodeEditor instance for the code editor.  
---|---  
[CurrentInstallation](Unity.CodeEditor.CodeEditor.CurrentInstallation.html)|
Returns the current CodeEditor.Installation instance for the code editor.  
  
### Public Methods

[GetCodeEditorForPath](Unity.CodeEditor.CodeEditor.GetCodeEditorForPath.html)|
Each registered code editor package has an instance of IExternalCodeEditor.
This method invokes IExternalCodeEditor.TryGetInstallationForPath on that
instance. It returns the first instance that returns a valid installation.  
---|---  
[GetFoundScriptEditorPaths](Unity.CodeEditor.CodeEditor.GetFoundScriptEditorPaths.html)|
Collects all installations from registered instances of IExternalCodeEditor.
This is done using IExternalCodeEditor.Installations.  
[GetInstallationForPath](Unity.CodeEditor.CodeEditor.GetInstallationForPath.html)|
Each registered code editor package has an instance of IExternalCodeEditor.
This method invokes IExternalCodeEditor.TryGetInstallationForPath on that
instance. It finds the first instance that returns a valid installation, and
returns the installation.  
[SetCodeEditor](Unity.CodeEditor.CodeEditor.SetCodeEditor.html)| Sets the path
to the code editor that Unity uses to open script assets.  
  
### Static Methods

[OSOpenFile](Unity.CodeEditor.CodeEditor.OSOpenFile.html)| Open an application
with a quoted string of arguments.  
---|---  
[ParseArgument](Unity.CodeEditor.CodeEditor.ParseArgument.html)| Parse a
string using the rules defined under External Tools.  
[QuoteForProcessStart](Unity.CodeEditor.CodeEditor.QuoteForProcessStart.html)|
Quotes a string to pass to Process.Start as a single argument, and appends it
to this string builder.  
[Register](Unity.CodeEditor.CodeEditor.Register.html)| Register an instance of
IExternalCodeEditor to use when populating Preferences/External Tools menu.
Calls ref::Initialize if you select the instance.  
[Unregister](Unity.CodeEditor.CodeEditor.Unregister.html)| Remove an instance
of IExternalCodeEditor from the list of registered code editors. Calls
ref::Initialize if you select the instance.  
  
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

