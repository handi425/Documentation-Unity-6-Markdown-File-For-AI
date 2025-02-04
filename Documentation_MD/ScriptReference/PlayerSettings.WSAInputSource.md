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

# WSAInputSource

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

### Description

Options for the input source from which a XAML application can receive pointer
input events.

To receive input, Universal Windows Platform applications subscribe to various
events, and with XAML builds you can register input events for alternative
sources via the SwapChainPanel API. This only applies to mouse, pen, and touch
events. Universal Windows Platform applications always take keyboard input
from CoreWindow.  
**Note** : These options are only applicable to XAML applications that use the
SwapChainPanel; XAML applications that use D3D only support the
[CoreWindow](PlayerSettings.WSAInputSource.CoreWindow.html) input source. For
more information, see [Microsoft's
documentation](https://docs.microsoft.com/en-
us/uwp/api/Windows.UI.Xaml.Controls.SwapChainPanel).

### Properties

[CoreWindow](PlayerSettings.WSAInputSource.CoreWindow.html)| Indicates that
pointer input comes from CoreWindow. This is the default option.  
---|---  
[IndependentInputSource](PlayerSettings.WSAInputSource.IndependentInputSource.html)|
Indicates that pointer input comes from SwapChainPanel's core input object.  
[SwapChainPanel](PlayerSettings.WSAInputSource.SwapChainPanel.html)| Indicates
that pointer input comes from the SwapChainPanel.  
  
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

