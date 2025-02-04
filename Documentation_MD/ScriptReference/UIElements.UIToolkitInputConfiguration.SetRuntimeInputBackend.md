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
[UIToolkitInputConfiguration](UIElements.UIToolkitInputConfiguration.html).SetRuntimeInputBackend

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

public static void
SetRuntimeInputBackend([UIElements.UIToolkitInputBackendOption](UIElements.UIToolkitInputBackendOption.html)
backend);

### Parameters

backend |  The input backend to be used as the source of input for UI Toolkit events at runtime.   
---|---  
  
### Description

Use this method to activate one of the two input backends available for
UIToolkit events at runtime. The new Input System compatible backend allows
the Input System package to send its input to UI Toolkit directly, removing
the need for an UnityEngine.EventSystems.EventSystem in the user scene, and
will automatically fall back to Input Manager input if the Input System
package input isn't enabled in the Player Settings active input handling.
Alternatively, use the legacy backend to always rely on Input Manager input
only. In that case, if the Input Manager is not enabled as an active input
handler, UI Toolkit runtime events will not work.

The Input System compatible backend is enabled by default. Call this method to
disable it or to enable it again if it was otherwise disabled.  
  
Setting the runtime input backend has no impact on Editor-only content such as
EditorWindows or custom inspectors.  
  
This method has no effect if there is an UnityEngine.EventSystems.EventSystem
in the user scene. In that case, UI Toolkit runtime events will be provided by
that EventSystem for as long as it remains enabled.

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

