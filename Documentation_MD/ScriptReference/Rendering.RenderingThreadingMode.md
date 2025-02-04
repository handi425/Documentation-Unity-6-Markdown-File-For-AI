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

# RenderingThreadingMode

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

[ ]()

### Description

Options for the application's actual rendering threading mode.

The combination of Player Settings
[PlayerSettings.MTRendering](PlayerSettings.MTRendering.html),
[PlayerSettings.graphicsJobs](PlayerSettings-graphicsJobs.html) and
[PlayerSettings.graphicsJobMode](PlayerSettings-graphicsJobMode.html), as well
as the target platform capabilities decides the rendering threading mode
during the start of the Unity Editor or Standalone. After startup, you can use
the property [SystemInfo.renderingThreadingMode](SystemInfo-
renderingThreadingMode.html) to query the rendering threading mode.  
Refer to the [Multithreaded Rendering & Graphics Jobs
](https://unity3d.com/learn/tutorials/topics/best-practices/multithreaded-
rendering-graphics-jobs) tutorial for a comparison of different rendering
threading modes.  
To specify whether graphics jobs threading mode is allowed in the Editor, use
the **Allow Graphics Jobs in Editor** checkbox in the Jobs panel of the
[Preferences Window](../Manual/Preferences.html). Enabling this option lets
Unity use the graphics jobs threading mode in the Editor when graphics jobs is
enabled in Player Settings.

### Properties

[Direct](Rendering.RenderingThreadingMode.Direct.html)| Use the Direct enum to
directly render your application from the main thread.  
---|---  
[SingleThreaded](Rendering.RenderingThreadingMode.SingleThreaded.html)| Use
SingleThreaded for internal debugging. It uses only a single thread to
simulate RenderingThreadingMode.MultiThreaded.  
[MultiThreaded](Rendering.RenderingThreadingMode.MultiThreaded.html)|
Generates intermediate graphics commands via the main thread. The render
thread converts them into low-level platform API graphics commands.  
[LegacyJobified](Rendering.RenderingThreadingMode.LegacyJobified.html)|
Generates intermediate graphics commands via several worker threads. A single
render thread then converts them into low-level platform API graphics
commands.  
[NativeGraphicsJobs](Rendering.RenderingThreadingMode.NativeGraphicsJobs.html)|
Main thread generates intermediate graphics commands. Render thread converts
them into low-level platform API graphics commands. Render thread can also
dispatch graphics jobs to several worker threads.  
[NativeGraphicsJobsWithoutRenderThread](Rendering.RenderingThreadingMode.NativeGraphicsJobsWithoutRenderThread.html)|
Generates intermediate graphics commands via several worker threads and
converts them into low-level platform API graphics commands.  
[NativeGraphicsJobsSplitThreading](Rendering.RenderingThreadingMode.NativeGraphicsJobsSplitThreading.html)|
Generates intermediate graphics commands via several worker threads and render
thread dispatches several worker threads to convert them into low-level
platform API graphics commands.  
  
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

