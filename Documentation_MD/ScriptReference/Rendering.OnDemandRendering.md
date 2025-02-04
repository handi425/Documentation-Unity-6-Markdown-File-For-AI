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

# OnDemandRendering

class in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Use the OnDemandRendering class to control and query information about your
application's rendering speed independent from all other subsystems (such as
physics, input, or animation).

If you use this with Optimized Frame Pacing on Android, and if you're also
using OpenGL ES, Optimized Frame Pacing is most effective when the frame rate
is either 20, 30, or 60 frames per second. To make sure that you render at one
of these frame rates, use OnDemandRendering.effectiveRenderframerate.  
  
Vulkan is less strict and allows a greater number of valid frame rates.  
  
If you request an incompatible frame rate, the application renders at the
highest frame rate possible. However, if the renderFrameInterval is too high,
the application might become unresponsive because the time between rendered
frames also becomes too high.  
  
Note about event execution:  
The diagram on the Manual page [Order of execution for event
functions](../Manual/execution-order.html) describes the execution order for
events in each frame. However, render-specific events, including those for
Scene rendering, Gizmo rendering, GUI rendering, and End of frame sections,
don't occur during frames that Unity doesn't render (when
[OnDemandRendering.willCurrentFrameRender](Rendering.OnDemandRendering-
willCurrentFrameRender.html) is false).

### Static Properties

[effectiveRenderFrameRate](Rendering.OnDemandRendering-
effectiveRenderFrameRate.html)| The current estimated rate of rendering in
frames per second rounded to the nearest integer.  
---|---  
[renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html)|
Get or set the current frame rate interval. To restore rendering back to the
value of Application.targetFrameRate or QualitySettings.vSyncCount set this to
0 or 1.  
[willCurrentFrameRender](Rendering.OnDemandRendering-
willCurrentFrameRender.html)|  True if the current frame will be rendered.  
  
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

