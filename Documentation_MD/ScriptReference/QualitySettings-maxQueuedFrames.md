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

#  [QualitySettings](QualitySettings.html).maxQueuedFrames

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

[Switch to Manual](../Manual/class-QualitySettings.html "Go to QualitySettings
Component in the Manual")

public static int maxQueuedFrames;

### Description

Maximum number of frames queued up by graphics driver.

Graphics drivers queue up frames that are yet to be rendered, especially when
the CPU has lesser processes to execute than the graphics card, this queue can
grow large. In such scenarios, the user's input might lag behind the content
displayed on the screen.  
  
Use [QualitySettings.maxQueuedFrames](QualitySettings-maxQueuedFrames.html) to
limit maximum number of frames that are queued. On PC, the default value is 2,
which strikes a good balance between frame latency and framerate.  
  
**Note:** You can reduce input latency by using smaller `maxQueuedFrames`,
such that the CPU waits until the graphics card completes rendering previous
frames. However, doing this might result in a lower framerate.  
  
Currently, `maxQueuedFrames` is implemented in Direct3D 11, Direct3D 12, and
Vulkan graphics APIs only and ignored by other graphics APIs. For information
about other graphics APIs and where `maxQueuedFrames` is implemented, refer to
platform-specific documentation.

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

