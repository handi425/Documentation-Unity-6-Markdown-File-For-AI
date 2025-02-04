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

#  [PlayerSettings.WSA](PlayerSettings.WSA.html).supportStreamingInstall

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

public static bool supportStreamingInstall;

### Description

Indicates whether you can launch the Universal Windows Platform application
package before installation is complete.

In the Editor, Unity displays this under **Streaming Install** in [UWP Player
Settings](../Manual/class-PlayerSettingsWSA.html).  
If you enable Streaming Install, you must also set a
[lastRequiredScene](PlayerSettings.WSA-lastRequiredScene.html) value to
indicate which scenes the application requires to launch and which scenes are
streamable.  
  
Unity generates an AppxContentGroupMap.xml file which specifies the assets
that the application requires to launch and which the application can stream
in the background while the application is running.  
The application requires the assets from the scenes from the top of [the Build
list](../Manual/BuildSettings.html) through to the lastRequiredScene and does
not launch until it installs these assets. The application considers assets
from the remaining scenes as streamable which allows the application to launch
before installing these assets..  
  
For information on Streaming install, see [Microsoft's
documentation.](https://docs.microsoft.com/en-
us/windows/msix/package/streaming-install)

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

