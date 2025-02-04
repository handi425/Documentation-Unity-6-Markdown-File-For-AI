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
[RenderingThreadingMode](Rendering.RenderingThreadingMode.html).NativeGraphicsJobs

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

Main thread generates intermediate graphics commands. Render thread converts
them into low-level platform API graphics commands. Render thread can also
dispatch graphics jobs to several worker threads.

In this mode, the main thread processes the application's high-level code and
issue an intermediate representation of the required graphics commands for
some of it.  
The main thread can also issue "Graphics Jobs" commands that describe bigger
chunks of the high-level code.  
  
The separate render thread reads the intermediate graphics commands and the
"graphics jobs" commands.  
Similarly to
[RenderingThreadingMode.MultiThreaded](Rendering.RenderingThreadingMode.MultiThreaded.html),
the render thread converts the intermediate graphics commands into the
platform's low-level graphics API commands.  
In addition, the render thread dispatches the "Graphics Jobs" commands to
several other worker threads. In parallel, the worker threads will convert the
graphics jobs into the platform's low-level graphics API commands.  
  
On some platforms this mode can be tested by passing command line argument
`-force-gfx-jobs native` to an application built with BuildSettings option
[BuildOptions.Development](BuildOptions.Development.html) .

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

